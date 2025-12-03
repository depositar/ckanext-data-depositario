import ckan.authz as authz
import ckan.logic.auth as logic_auth
from ckan.common import _

from ckan.logic.auth.create import _check_group_auth
from ckan.types import Context, DataDict, AuthResult


# Override the ckan.logic.auth.update.package_update
def package_update(context: Context, data_dict: DataDict) -> AuthResult:
    model = context['model']
    user = context.get('user')

    package = logic_auth.get_package_object(context, data_dict)
    if package.owner_org:
        # if there is an owner org then we must have update_dataset
        # permission for that organization
        check1 = authz.has_user_permission_for_group_or_org(
            package.owner_org, user, 'update_dataset'
        )
    else:
        # If dataset is not owned then we can edit if config permissions allow
        if authz.auth_is_anon_user(context):
            check1 = all(authz.check_config_permission(p) for p in (
                'anon_create_dataset',
                'create_dataset_if_not_in_organization',
                'create_unowned_dataset',
                ))
        else:
            if context['auth_user_obj'].id == package.creator_user_id:
                # A package creator has the authority to edit it regardless
                check1 = True
            else:
                check1 = False

    if not check1:
        success = False
        if authz.check_config_permission('allow_dataset_collaborators'):
            # if org-level auth failed, check dataset-level auth
            # (ie if user is a collaborator)
            user_obj = model.User.get(user)
            if user_obj:
                success = authz.user_is_collaborator_on_dataset(
                    user_obj.id, package.id, ['admin', 'editor'])
        if not success:
            return {'success': False,
                    'msg': _('User %s not authorized to edit package %s') %
                            (str(user), package.id)}
    else:
        check2 = _check_group_auth(context, data_dict)
        if not check2:
            return {'success': False,
                    'msg': _('User %s not authorized to edit these groups') %
                            (str(user))}

    return {'success': True}
