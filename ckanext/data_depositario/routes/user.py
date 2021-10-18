from flask import Blueprint

import ckan.lib.base as base
import ckan.lib.captcha as captcha
import ckan.lib.helpers as h
import ckan.lib.navl.dictization_functions as dictization_functions
import ckan.logic as logic
import ckan.logic.schema as schema
import ckan.model as model
from ckan import authz
from ckan.common import _, g, request
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
        context = {
            u'model': model,
            u'session': model.Session,
            u'user': g.user,
            u'auth_user_obj': g.userobj,
            u'schema': user_schema,
            u'save': u'save' in request.form
        }
        try:
            logic.check_access(u'user_create', context)
        except logic.NotAuthorized:
            base.abort(403, _(u'Unauthorized to register as a user.'))
        return context

    def post(self):
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

        context[u'message'] = data_dict.get(u'log_message', u'')
        try:
            captcha.check_recaptcha(request)
        except captcha.CaptchaError:
            error_msg = _(u'Bad Captcha. Please try again.')
            h.flash_error(error_msg)
            return self.get(data_dict)

        try:
            logic.get_action(u'user_create')(context, data_dict)
        except logic.NotAuthorized:
            base.abort(403, _(u'Unauthorized to create user %s') % u'')
        except logic.NotFound:
            base.abort(404, _(u'User not found'))
        except logic.ValidationError as e:
            errors = e.error_dict
            error_summary = e.error_summary
            return self.get(data_dict, errors, error_summary)

        if g.user:
            # #1799 User has managed to register whilst logged in - warn user
            # they are not re-logged in as new user.
            h.flash_success(
                _(u'User "%s" is now registered but you are still '
                  u'logged in as "%s" from before') % (data_dict[u'name'],
                                                       g.user))
            if authz.is_sysadmin(g.user):
                # the sysadmin created a new user. We redirect him to the
                # activity page for the newly created user
                return h.redirect_to(u'user.activity', id=data_dict[u'name'])
            else:
                return base.render(u'user/logout_first.html')

        # return to home page
        h.flash_success(_('Please check your inbox to '
                'set your password.'))
        return h.redirect_to('/')


blueprint.add_url_rule(
    u'/register', view_func=CustomRegisterView.as_view(str(u'register')))
