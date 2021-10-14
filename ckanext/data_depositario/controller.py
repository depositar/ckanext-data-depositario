import ckan.plugins as p
from ckan.lib.base import BaseController
import ckan.authz as authz
import ckan.logic as logic
from ckan.logic.validators import user_password_validator
import ckan.lib.base as base
import ckan.lib.helpers as h
import ckan.lib.captcha as captcha
from ckan.lib.navl.validators import ignore_missing
import ckan.lib.navl.dictization_functions as dictization_functions
from ckan.common import _, c, request
from ckan.controllers.user import UserController


abort = base.abort
render = base.render

get_action = logic.get_action
NotFound = logic.NotFound
NotAuthorized = logic.NotAuthorized
ValidationError = logic.ValidationError

DataError = dictization_functions.DataError
unflatten = dictization_functions.unflatten


class CustomUserController(UserController):
    """
    Adapted from original CKAN's UserController to prompt new user to
    set a password immediately.
    """
    def _remove_requires_password_from_schema(self, schema):
        """
        Helper function that modifies the password validation on
        an existing schema
        """
        schema.pop('password1')
        schema.pop('password2')
        schema['password'] = [user_password_validator, ignore_missing, unicode]

    def _new_form_to_db_schema(self):
        """
        Defines a custom schema that does not require a password to
        be supplied

        This method is a hook that the base class calls for the validation
        schema to use when creating a new user.
        """
        schema = super(CustomUserController, self)._new_form_to_db_schema()
        self._remove_requires_password_from_schema(schema)
        return schema

    def _save_new(self, context):
        try:
            data_dict = logic.clean_dict(unflatten(
                logic.tuplize_dict(logic.parse_params(request.params))))
            context['message'] = data_dict.get('log_message', '')
            captcha.check_recaptcha(request)
            user = get_action('user_create')(context, data_dict)
        except NotAuthorized:
            abort(403, _('Unauthorized to create user %s') % '')
        except NotFound, e:
            abort(404, _('User not found'))
        except DataError:
            abort(400, _(u'Integrity Error'))
        except captcha.CaptchaError:
            error_msg = _(u'Bad Captcha. Please try again.')
            h.flash_error(error_msg)
            return self.new(data_dict)
        except ValidationError, e:
            errors = e.error_dict
            error_summary = e.error_summary
            return self.new(data_dict, errors, error_summary)
        if not c.user:
            h.flash_success(_('Please check your inbox to '
                            'set your password.'))
            h.redirect_to('/')
        else:
            # #1799 User has managed to register whilst logged in - warn user
            # they are not re-logged in as new user.
            h.flash_success(_('User "%s" is now registered but you are still '
                            'logged in as "%s" from before') %
                            (data_dict['name'], c.user))
            if authz.is_sysadmin(c.user):
                # the sysadmin created a new user. We redirect him to the
                # activity page for the newly created user
                h.redirect_to(controller='user',
                              action='activity',
                              id=data_dict['name'])
            else:
                return render('user/logout_first.html')
