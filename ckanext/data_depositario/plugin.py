from logging import getLogger

import ckan.plugins as p
from ckan.common import json
from datetime import datetime
from ckanext.data_depositario import helpers
from ckanext.data_depositario import validators

log = getLogger(__name__)
ignore_empty = p.toolkit.get_validator('ignore_empty')


class DataDepositarioDatasets(p.SingletonPlugin):

    p.implements(p.ITemplateHelpers)
    p.implements(p.IConfigurer)
    p.implements(p.IPackageController, inherit=True)
    p.implements(p.IFacets)
    p.implements(p.IValidators)
    p.implements(p.IRoutes, inherit=True)

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
        data_dict.update({'data_type_facet': '', 'proj_facet': '', 'language_facet': '',
                'encoding_facet': '', 'theme_keyword_facets': [], 'loc_keyword_facet': []})
        fields = helpers.get_field_choices('dataset')
        for field_name in ['data_type', 'proj', 'language', 'encoding']:
            value = data_dict.get(field_name)
            if value:
                data_dict[field_name+'_facet'] = fields[field_name][value]
        if data_dict.get('theme_keyword'):
            data_dict['theme_keyword_facets'] = json.loads(data_dict.get('theme_keyword'))
        #For old schema definition
        for i in range(5):
            field_name = 'theme_keyword_' + str(i+1)
            if isinstance(data_dict.get(field_name), unicode):
	        data_dict['theme_keyword_facets'].append(fields['theme_keyword'].get(data_dict[field_name]))
        if data_dict.get('loc_keyword'):
            data_dict['loc_keyword_facet'] = json.loads(data_dict.get('loc_keyword'))
            if isinstance(data_dict['loc_keyword_facet'], list):
                data_dict['loc_keyword_facet'] = [fields['loc_keyword'][loc_keyword] for loc_keyword in filter(None, data_dict['loc_keyword_facet'])]
            #For old schema definition
	    elif isinstance(data_dict['loc_keyword_facet'], int):
                data_dict['loc_keyword_facet'] = fields['loc_keyword'][str(data_dict['loc_keyword'])]
        return data_dict

    ## IFacets
    def dataset_facets(self, facets_dict, package_type):
        facets_dict['date_facet'] = p.toolkit._('Date of Dataset')
        facets_dict['data_type_facet'] = p.toolkit._('Data Type')
        facets_dict['proj_facet'] = p.toolkit._('Project')
        facets_dict['language_facet'] = p.toolkit._('Language')
        facets_dict['encoding_facet'] = p.toolkit._('Encoding')
        facets_dict['theme_keyword_facets'] = p.toolkit._('Theme Keyword')
        facets_dict['loc_keyword_facet'] = p.toolkit._('Spatial Keyword')

        return facets_dict

    def group_facets(self, facets_dict, group_type, package_type):
        return facets_dict

    def organization_facets(self, facets_dict, organization_type, package_type):
        facets_dict['data_type_facet'] = p.toolkit._('Data Type')
        facets_dict['proj_facet'] = p.toolkit._('Project')
        facets_dict['language_facet'] = p.toolkit._('Language')
        facets_dict['encoding_facet'] = p.toolkit._('Encoding')
        facets_dict['theme_keyword_facets'] = p.toolkit._('Theme Keyword')
        facets_dict['loc_keyword_facet'] = p.toolkit._('Spatial Keyword')

        return facets_dict

    ## IValidators
    def get_validators(self):
        function_names = (
            'positive_integer_validator',
            'long_validator',
            'lat_validator',
            'positive_float_validator',
            'json_validator',
            'temp_res_validator',
            'append_time_period',
            'date_validator',
            'duplicate_validator',
            'remove_blank_wrap',
        )
        return _get_module_functions(validators, function_names)

    ## ITemplateHelpers
    def get_helpers(self):
        function_names = (
            'extras_to_dict',
	    'geojson_to_wkt',
            'latest_news',
            'date_to_iso',
            'get_default_slider_values',
            'get_date_url_param',
            'get_field_choices',
            'get_time_period',
            'string_to_list',
            'get_gmap_config'
        )
        return _get_module_functions(helpers, function_names)

    ## IRoutes
    def after_map(self, map):
        map.connect('help', '/help',
            controller='ckanext.data_depositario.controller:HelpController',
            action='index')
        return map

def _get_module_functions(module, function_names):
    functions = {}
    for f in function_names:
        functions[f] = module.__dict__[f]

    return functions
