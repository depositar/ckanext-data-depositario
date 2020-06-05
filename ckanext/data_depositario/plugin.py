from logging import getLogger

from calendar import monthrange
from datetime import date
from datetime import datetime
from dateutil.parser import parse
import ckan.plugins as p
import ckan.logic as logic
from ckan.logic.action.create import user_create as ckan_user_create
import ckan.model as model
from ckan.common import json
from ckan.common import OrderedDict
import ckan.lib.mailer as mailer
from ckan.lib.plugins import DefaultTranslation
from ckanext.scheming import helpers as scheming_helpers
from ckanext.data_depositario import helpers
from ckanext.data_depositario import validators
from ckanext.data_depositario import converters

log = getLogger(__name__)

_check_access = logic.check_access


class DepositarISO639(p.SingletonPlugin, DefaultTranslation):

    p.implements(p.ITranslation)

    ## ITranslation
    def i18n_domain(self):
        return 'iso_639-3'

class DataDepositarioDatasets(p.SingletonPlugin, DefaultTranslation):

    p.implements(p.ITranslation)
    p.implements(p.ITemplateHelpers)
    p.implements(p.IConfigurer)
    p.implements(p.IPackageController, inherit=True)
    p.implements(p.IFacets)
    p.implements(p.IValidators)
    p.implements(p.IRoutes, inherit=True)
    p.implements(p.IActions)

    ## IConfigurer
    def update_config(self, config):
        p.toolkit.add_template_directory(config, 'templates')
        p.toolkit.add_public_directory(config, 'public')
        p.toolkit.add_resource('fanstatic', 'ckanext-data-depositario')

    ## IPackageController
    def before_search(self, search_params):
        if (search_params.get('extras', None) and 'ext_begin' in
                search_params['extras'] and 'ext_end' in
                search_params['extras']):
            try:
                begin = search_params['extras']['ext_begin']
                end = search_params['extras']['ext_end']
            except ValueError:
                return search_params
            query = ("((start_time: [* TO {0}] AND "
                     "end_time: [{0} TO *]) OR "
                     "(start_time: [{0} TO {1}] AND "
                     "end_time: [{0} TO *]))")
            query = query.format(begin, end)

            q = search_params.get('q', '').strip() or '""'
            new_q = '%s AND %s' % (q if q else '', query)

            search_params['q'] = new_q

        return search_params

    def before_index(self, data_dict):
        for field_name in ['data_type', 'language']:
            value = data_dict.get(field_name)
            try:
                data_dict[field_name+'_facet'] = json.loads(value)
            except ValueError:
                # For old datasets with single data_type and language.
                data_dict[field_name+'_facet'] = value
        # Index start_time and end_time in TrieDateField because
        # DateRangeField is not sortable.
        if data_dict.get('start_time'):
            data_dict['start_time_t'] = parse( \
                    data_dict['start_time'],
                    default=datetime(1, 1, 1)).isoformat() + 'Z'
        if data_dict.get('end_time'):
            end_time_t = parse(data_dict['end_time'],
                    default=datetime(date.today().year, 12, 1))
            if len(data_dict['end_time']) == 7:
                # If the day of month is missing
                end_time_t = end_time_t.replace( \
                        day=monthrange(end_time_t.year, end_time_t.month)[1])
            data_dict['end_time_t'] = end_time_t.isoformat() + 'Z'

        return data_dict

    def after_search(self, search_results, search_params):
        facets = search_results.get('search_facets')
        results = search_results.get('results')
        if not facets or not results:
            return search_results
        schema = scheming_helpers.scheming_get_dataset_schema(results[0]['type'])
        for facet in facets.values():
            for item in facet['items']:
                field_name = facet['title'].replace('_facet', '')
                field = scheming_helpers.scheming_field_by_name( \
                        schema['dataset_fields'], field_name)
                if field and (field.get('choices') or \
                        field.get('choices_helper')):
                    choices = scheming_helpers.scheming_field_choices(field)
                    item['display_name'] = scheming_helpers. \
                            scheming_choices_label(choices, item['name'])

        return search_results

    ## IFacets
    def dataset_facets(self, facets_dict, package_type):
        return _add_facets(facets_dict)

    def group_facets(self, facets_dict, group_type, package_type):
        return _add_facets(facets_dict, group=True)

    def organization_facets(self, facets_dict, organization_type, package_type):
        return _add_facets(facets_dict, group=True)

    ## IValidators
    def get_validators(self):
        validator_names = (
            'long_validator',
            'lat_validator',
            'positive_float_validator',
            'json_validator',
            'date_validator',
            'end_time_validator',
        )
        converter_names = (
            'remove_blank_wrap',
            'value_string_convert',
        )
        field_validators = _get_module_functions(validators, validator_names)
        field_validators.update(_get_module_functions(converters, converter_names))
        return field_validators

    ## ITemplateHelpers
    def get_helpers(self):
        function_names = (
            'extras_to_dict',
	    'geojson_to_wkt',
            'get_default_slider_values',
            'get_date_url_param',
            'get_gmap_config',
            'get_pkg_version',
            'googleanalytics_header',
            'schema_license_choices',
            'schema_language_choices',
        )
        return _get_module_functions(helpers, function_names)

    ## IRoutes
    def before_map(self, map):
        map.connect('/user/register',
            controller='ckanext.data_depositario.controller:CustomUserController',
            action='register')
        return map

    def after_map(self, map):
        map.connect('help', '/help',
            controller='ckanext.data_depositario.controller:HelpController',
            action='index')
        return map

    ## IActions
    def get_actions(self):
        return {'license_list': license_list, 'user_create': user_create}

def _get_module_functions(module, function_names):
    functions = {}
    for f in function_names:
        functions[f] = module.__dict__[f]

    return functions

def _add_facets(facets_dict, group=False):
    new_facets_dict = OrderedDict([
        ('keywords_facet', ''),
        facets_dict.items()[2],
        ('data_type_facet', p.toolkit._('Data Type')),
        ('organization', p.toolkit._('Projects')),
        ('groups', p.toolkit._('Topics')),
        ('language_facet', p.toolkit._('Language'))
    ] + facets_dict.items()[3:])

    if not group:
        new_facets_dict['date_facet'] = ''

    return new_facets_dict

def license_list(context, data_dict):
    '''Return the list of licenses available for datasets on the site.

    Adapted from original CKAN using a nondeprecated method.

    :rtype: list of dictionaries
    '''
    model = context["model"]

    _check_access('license_list', context, data_dict)

    license_register = model.Package.get_license_register()
    licenses = license_register.values()
    licenses = [l._data for l in licenses]
    return licenses

def user_create(context, data_dict):
    user_dict = ckan_user_create(context, data_dict)

    group_context = context.get('group')
    # We don't do this when inviting new user to a group
    if not group_context or group_context.type != 'group':
        # Add the created user to existed groups
        groups = p.toolkit.get_action('group_list')({}, {})
        context['ignore_auth'] = True
        for group in groups:
            group_dict = {
                'id': group,
                'username': user_dict['id'],
                'role': 'member'
            }
            p.toolkit.get_action('group_member_create')(context, group_dict)

    # We don't need these when inviting new users
    if not context['auth_user_obj']:
        user = model.User.get(user_dict['id'])

        # Set the user as pending before changing his/her password.
        user.set_pending()

        # Reset the created user's password immediately
        try:
            mailer.send_reset_link(user)
        except mailer.MailerException, e:
            log.debug('Could not send reset link: %s' % unicode(e))

    return user_dict
