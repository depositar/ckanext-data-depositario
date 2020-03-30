from logging import getLogger

from datetime import datetime
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
        def parse_date(date_string):
            '''
            Parse a date string or throw a nice error into the log. Re-raises
            the error for the plugin to catch.
            '''
            try:
                return datetime.strptime(date_string, '%Y-%m-%d')
            except ValueError as e:
                log.debug('Date {0} not in the right format. Needs to be YYYY'
                        '-MM-DD'.format(date_string))
                raise e

        if (search_params.get('extras', None) and 'ext_begin_date' in
                search_params['extras'] and 'ext_end_date' in
                search_params['extras']):
            try:
                begin = parse_date(search_params['extras']['ext_begin_date'])
                end = parse_date(search_params['extras']['ext_end_date'])
            except ValueError:
                return search_params
            # Adding 'Z' manually here is evil, but we do this in core too.
            query = ("((start_time: [* TO {0}Z] AND "
                     "end_time: [{0}Z TO *]) OR "
                     "(start_time: [{0}Z TO {1}Z] AND "
                     "end_time: [{0}Z TO *]))")
            query = query.format(begin.isoformat(), end.isoformat())

            q = search_params.get('q', '').strip() or '""'
            new_q = '%s AND %s' % (q if q else '', query)

            search_params['q'] = new_q

        return search_params

    def before_index(self, data_dict):
        for field_name in ['data_type', 'language']:
            value = data_dict.get(field_name, '')
            data_dict[field_name+'_facet'] = value

        return data_dict

    def after_search(self, search_results, search_params):
        facets = search_results.get('search_facets')
        if not facets:
            return search_results
        dataset_type = search_results['results'][0]['type']
        schema = scheming_helpers.scheming_get_dataset_schema(dataset_type)
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
            'temp_res_validator',
            'date_validator',
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
            'date_to_iso',
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
    new_facets_dict = OrderedDict(facets_dict.items()[:2])
    new_facets_dict['organization'] = p.toolkit._('Projects')
    new_facets_dict['groups'] = p.toolkit._('Topics')
    new_facets_dict['keywords_facet'] = p.toolkit._('Keywords')
    new_facets_dict = OrderedDict(new_facets_dict.items() + facets_dict.items()[2:])
    if not group:
        new_facets_dict['date_facet'] = ''
    new_facets_dict['data_type_facet'] = p.toolkit._('Data Type')
    new_facets_dict['language_facet'] = p.toolkit._('Language')

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
