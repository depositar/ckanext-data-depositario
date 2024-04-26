from typing import Union, cast

from flask import Blueprint

import ckan.lib.base as base
import ckan.lib.captcha as captcha
from ckan.lib.helpers import helper_functions as h
import ckan.lib.navl.dictization_functions as dictization_functions
import ckan.logic as logic
import ckan.logic.schema as schema
import ckan.model as model
from ckan import authz
from ckan.common import _, g, request, current_user
from ckan.types import Context, Response
from ckan.views.user import RegisterView

blueprint = Blueprint(u'custom_user', __name__, url_prefix=u'/user')


class CustomRegisterView(RegisterView):
    """
    Adapted from original CKAN's RegisterView to prompt new user to
    set a password immediately.
    """

    def _prepare(self):
        user_schema = schema.user_new_form_schema()
        user_schema.pop('password')
        user_schema.pop('password1')
        user_schema.pop('password2')
        context = cast(Context, {
            u'model': model,
            u'session': model.Session,
            u'user': current_user.name,
            u'auth_user_obj': current_user,
            u'schema': user_schema,
            u'save': u'save' in request.form
        })
        try:
            logic.check_access(u'user_create', context)
        except logic.NotAuthorized:
            base.abort(403, _(u'Unauthorized to register as a user.'))
        return context

    def post(self) -> Union[Response, str]:
        context = self._prepare()
        try:
            data_dict = logic.clean_dict(
                dictization_functions.unflatten(
                    logic.tuplize_dict(logic.parse_params(request.form))))
            data_dict.update(logic.clean_dict(
                dictization_functions.unflatten(
                    logic.tuplize_dict(logic.parse_params(request.files)))
            ))

        except dictization_functions.DataError:
            base.abort(400, _(u'Integrity Error'))

        try:
            captcha.check_recaptcha(request)
        except captcha.CaptchaError:
            error_msg = _(u'Bad Captcha. Please try again.')
            h.flash_error(error_msg)
            return self.get(data_dict)

        try:
            user_dict = logic.get_action(u'user_create')(context, data_dict)
        except logic.NotAuthorized:
            base.abort(403, _(u'Unauthorized to create user %s') % u'')
        except logic.NotFound:
            base.abort(404, _(u'User not found'))
        except logic.ValidationError as e:
            errors = e.error_dict
            error_summary = e.error_summary
            return self.get(data_dict, errors, error_summary)

        user = current_user.name
        if user:
            # #1799 User has managed to register whilst logged in - warn user
            # they are not re-logged in as new user.
            h.flash_success(
                _(u'User "%s" is now registered but you are still '
                  u'logged in as "%s" from before') % (data_dict[u'name'],
                                                       user))
            if authz.is_sysadmin(user):
                # the sysadmin created a new user. We redirect him to the
                # activity page for the newly created user
                if "activity" in g.plugins:
                    return h.redirect_to(
                        u'activity.user_activity', id=data_dict[u'name'])
                return h.redirect_to(u'user.read', id=data_dict[u'name'])
            else:
                return base.render(u'user/logout_first.html')

        # return to home page
        h.flash_success(_('Please check your inbox to '
                'set your password.'))
        return h.redirect_to('/')


blueprint.add_url_rule(
    u'/register', view_func=CustomRegisterView.as_view(str(u'register')))
