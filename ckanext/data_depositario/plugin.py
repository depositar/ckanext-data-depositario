from logging import getLogger

import ckan.plugins as p
from ckan.common import json
from ckan.lib.plugins import DefaultTranslation
from datetime import datetime
from ckanext.data_depositario import helpers
from ckanext.data_depositario import validators

log = getLogger(__name__)
ignore_empty = p.toolkit.get_validator('ignore_empty')


class DataDepositarioDatasets(p.SingletonPlugin, DefaultTranslation):

    p.implements(p.ITranslation)
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
        for field_name in ['data_type', 'language']:
            value = data_dict.get(field_name, '')
            data_dict[field_name+'_facet'] = value
        schema = helpers.get_schema('dataset')
        for field_name in ['theme_keyword', 'loc_keyword', 'book_hist_materials']:
            field = helpers.get_field_by_name(schema['dataset_fields'], field_name)
            value = data_dict.get(field_name, [])
            if value:
                keywords = json.loads(value)
                #Get the value for the old Chinese label of theme_keyword
                value = [helpers.get_choices_value(field['choices'], k) for k in keywords]
            data_dict[field_name+'_facet'] = value
        #But we still need the labels for text search
        for field_name in ['theme_keyword', 'loc_keyword']:
            field = helpers.get_field_by_name(schema['dataset_fields'], field_name)
            data_dict[field_name+'_en_label'] = \
                    [helpers.get_choices_label(field['choices'], v, 'en') \
		        for v in data_dict[field_name+'_facet']]
            data_dict[field_name+'_zh_TW_label'] = \
                    [helpers.get_choices_label(field['choices'], v, 'zh_TW') \
                        for v in data_dict[field_name+'_facet']]

        return data_dict

    ## IFacets
    def dataset_facets(self, facets_dict, package_type):
        facets_dict['date_facet'] = ''
        facets_dict['data_type_facet'] = p.toolkit._('Data Type')
        facets_dict['language_facet'] = p.toolkit._('Language')
        facets_dict['theme_keyword_facet'] = p.toolkit._('Theme Keyword')
        facets_dict['loc_keyword_facet'] = p.toolkit._('Spatial Keyword')
        facets_dict['book_hist_materials_facet'] = p.toolkit._('Historical Material')

        return facets_dict

    def group_facets(self, facets_dict, group_type, package_type):
        return facets_dict

    def organization_facets(self, facets_dict, organization_type, package_type):
        facets_dict['data_type_facet'] = p.toolkit._('Data Type')
        facets_dict['language_facet'] = p.toolkit._('Language')
        facets_dict['theme_keyword_facet'] = p.toolkit._('Theme Keyword')
        facets_dict['loc_keyword_facet'] = p.toolkit._('Spatial Keyword')
        facets_dict['book_hist_materials_facet'] = p.toolkit._('Historical Material')

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
            'get_time_period',
            'get_time_period_for_facet_slider',
            'get_gmap_config',
            'get_license_list',
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
