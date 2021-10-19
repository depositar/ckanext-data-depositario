import pycountry
import ckan.plugins as p
from ckan.plugins.toolkit import config
from ckan.common import json
import re
import json
import logging
from ckanext import data_depositario

log = logging.getLogger(__name__)


def get_default_slider_values():
   data_dict = {
      'sort': 'start_time_t asc',
      'rows': 1,
      'q': 'start_time_t:[* TO *]',
   }
   result = p.toolkit.get_action('package_search')({}, data_dict)['results']
   if not result: return
   start_time = result[0].get('start_time')

   data_dict = {
      'sort': 'end_time_t desc',
      'rows': 1,
      'q': 'end_time_t:[* TO *]',
   }
   result = p.toolkit.get_action('package_search')({}, data_dict)['results']
   if not result: return
   end_time = result[0].get('end_time')

   if start_time == end_time: return

   return start_time, end_time

def get_date_url_param():
   params = ['', '']
   for k, v in p.toolkit.request.params.items():
      if k == 'ext_begin':
         params[0] = v
      elif k == 'ext_end':
         params[1] = v
      else:
         continue
   return params

def get_gmap_config():
    '''
        Returns a dict with all configuration options related to the
        Google Maps API (ie those starting with 'ckanext.data_depositario.gmap')
    '''
    namespace = 'ckanext.data_depositario.gmap.'

    gmap_configs = dict([(k.replace(namespace, ''), v) for k, v in config.iteritems()
            if k.startswith(namespace)])

    if not gmap_configs.get('api_key'):
        log.critical('''Please specify a ckanext.data_depositario.gmap.api_key
                     in your config for the Google Maps layer''')

    return dict([(k.replace(namespace, ''), v) for k, v in config.iteritems()
                 if k.startswith(namespace)])

def get_pkg_version():
    """
    Obtain the extension version for documentation
    Borrowed from CKAN core
    """
    pkg_version = data_depositario.__version__
    pkg_base_version = re.sub('[^0-9\.]', '', pkg_version)
    if pkg_base_version == pkg_version:
       pkg_version = pkg_version[:5]
    else:
       pkg_version = 'latest'
    return pkg_version

def googleanalytics_header():
    """
    Render the googleanalytics_header snippet for CKAN 2.0 templates.
    Borrowed from ckanext-googleanalytics.
    """
    googleanalytics_id = config.get('ckanext.data_depositario.googleanalytics.id')

    data = {
        'googleanalytics_id': googleanalytics_id
    }

    return p.toolkit.render_snippet(
            'snippets/googleanalytics_header.html', data)

def is_demo():
    """
    Tell whether or not this site is a demo.
    """
    return config.get('ckanext.data_depositario.demo.enabled', False)

def schema_license_choices(field):
    """
    License choices helper.
    """
    license_list = p.toolkit.get_action('license_list')({}, {})
    licenses = [{'value': license['id'], 'label': {'en': license['title'],
            'zh_Hant_TW': license['title_zh']}} for license in license_list]

    return licenses

def schema_language_choices(field):
    """
    Language choices helper.
    """
    major_lang_alpha_3 = ['zho', 'jpn', 'eng',
            'fra', 'spa', 'ara', 'por', 'rus', 'deu']
    major_lang = [{'value': lang_alpha_3,
            'label': p.toolkit._(pycountry.languages. \
            get(alpha_3=lang_alpha_3).name) + \
            ' (%s)' % lang_alpha_3} \
            for lang_alpha_3 in major_lang_alpha_3]
    other_lang = [{'value': lang.alpha_3, 'label': p.toolkit._(lang.name) + \
            ' (%s)' % lang.alpha_3} \
            for lang in pycountry.languages \
            if lang.alpha_3 not in major_lang_alpha_3]

    return major_lang + other_lang
