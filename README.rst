=================
data.depositar.io
=================

The https://data.depositar.io is a research data repository for the humanities and areas studies.


Prerequirements
----------------

- **Data.depositar.io CKAN.** The code powering the data.depositar.io instance of CKAN.

  - `release-data-depositar-io <https://github.com/depositar-io/ckan>`_ - The main development branch used for the current data.depositar.io.

- **Extensions.** We have developed several CKAN extensions. The `full list of installed extensions can be seen via the CKAN API <https://data.depositar.io/api/util/status>`_. Custom extensions include:

  - `depositar-io/ckanext-data-depositario <https://github.com/depositar-io/ckanext-data-depositario>`_ - Most data.depositar.io specific CKAN customizations are contained within this extension.
  - `depositar-io/ckanext-spatial <https://github.com/depositar-io/ckanext-spatial>`_ - Geospatial extension for CKAN.
  - `depositar-io/ckanext-geoview <https://github.com/depositar-io/ckanext-geoview>`_ - CKAN Geospatial ResourceView.
  - `depositar-io/data-depositario-translations <https://github.com/depositar-io/data-depositario-translations>`_ - Translations for data.depositar.io.
  - `depositar-io/ckanext-dga-stats <https://github.com/depositar-io/ckanext-dga-stats>`_ - CKAN's built-in Statistics plugin modified for data.depositar.io.


Install
--------

With your virtualenv activated:

::

   cd src
   git clone https://github.com/depositar-io/ckanext-data-depositario.git
   cd ckanext-data-depositario
   python setup.py develop
   pip install -r requirements.txt

Add the following plugin and the Google Maps API key to your CKAN ini file:

::

   ckan.plugins = ... data_depositario_datasets
   ckanext.data_depositario.gmap.api_key = YOUR_GOOGLE_MAPS_API_KEY

Then restart your server.
