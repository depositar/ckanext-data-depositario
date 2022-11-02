.. This tocdepth stops Sphinx from putting every subsection title in this file
   into the master table of contents.

:tocdepth: 1

---------
Changelog
---------

v6.5.6 2022-11-03
=================

Changes:
 * Update: CKAN core version `2.9.7 <https://docs.ckan.org/en/2.9/changelog.html#v-2-9-7-2022-10-26>`_.
 * Update: ckanext-xloader 0.11.0.

v6.5.5 2022-10-14
=================

Notice:
 * This version requires the latest `ckanext-depositar_theme <https://github.com/depositar/ckanext-depositar_theme>`_.

Changes:
 * Update: CKAN core version `2.9.6 <https://docs.ckan.org/en/2.9/changelog.html#v-2-9-6-2022-09-28>`_.
 * Improvement: performance and design tweaks for the homepage.

v6.5.4 2022-09-23
=================

Notice:
 * This version requires the latest `ckanext-depositar_theme <https://github.com/depositar/ckanext-depositar_theme>`_.

Changes:
 * Update: New design of the homepage.

v6.5.3 2022-07-08
=================

Notice:
 * This version requires the latest `ckanext-citation <https://github.com/depositar/ckanext-citation>`_ and `ckanext-ark <https://github.com/depositar/ckanext-ark>`_.

Changes:
 * Add: :ref:`ark-identifier` which assigns ARKs as persistent identifiers (PID) to datasets.
 * Update: Rename the ``Author`` field to ``Creator``.
 * Other improvements and UI adjustments.

v6.5.2 2022-05-06
=================

Notice:
 * This version requires the latest `ckanext-citation <https://github.com/depositar/ckanext-citation>`_.

Changes:
 * Improvement: Fix an issue where the month is wrongly displayed in the BibTeX generic citation style.
 * Improvement: Fix an issue where the citation-key in the BibTeX generic citation may not be valid.
 * Improvement: Load the ``ckanext.data_depositario.demo.enabled`` config correctly.
 * Update: Correct some errors in documentation.

v6.5.1 2022-03-25
=================

Notice:
 * This version requires the latest `ckanext-wikidatakeyword <https://github.com/depositar/ckanext-wikidatakeyword>`_.
 * This version requires Solr 8. Run the commands below to upgrade Solr to 8.11.1:

   ::

     sudo service solr stop
     sudo rm /etc/default/solr.in.sh
     sudo bash ./install_solr_service.sh solr-8.11.1.tgz -f
     sudo -u solr /opt/solr/bin/solr delete -c ckan
     sudo -u solr /opt/solr/bin/solr create -c ckan
     sudo ln -sf /usr/lib/ckan/default/src/ckanext-data-depositario/solr/schema.xml /var/solr/data/ckan/conf/managed-schema
     wget https://repo1.maven.org/maven2/com/github/magese/ik-analyzer/8.5.0/ik-analyzer-8.5.0.jar
     wget https://repo1.maven.org/maven2/org/locationtech/jts/jts-core/1.18.2/jts-core-1.18.2.jar
     sudo cp ik-analyzer-8.5.0.jar /opt/solr/server/solr-webapp/webapp/WEB-INF/lib/.
     sudo cp jts-core-1.18.2.jar /opt/solr/server/solr-webapp/webapp/WEB-INF/lib/.
     sudo mkdir /opt/solr/server/solr-webapp/webapp/WEB-INF/classes
     sudo ln -s /usr/lib/ckan/default/src/ckanext-data-depositario/solr/IKAnalyzer.cfg.xml /opt/solr/server/solr-webapp/webapp/WEB-INF/classes/.
     sudo ln -s /usr/lib/ckan/default/src/ckanext-data-depositario/solr/words.dic /var/solr/data/ckan/conf/words.dic
     . /usr/lib/ckan/default/bin/activate
     ckan -c /etc/ckan/default/ckan.ini search-index rebuild

Changes:
 * Update: CKAN core version `2.9.5 <http://docs.ckan.org/en/2.9/changelog.html#v-2-9-5-2022-01-19>`_.
 * Improvement: Fix an issue where some fields disappear when displaying the form with errors.

v6.5.0 2022-02-18
=================

Notice:
 * Since this version, |site_name| only supports Python 3.6 or greater.
   |site_name| now supports Python 3.6, 3.7 and 3.8.
 * Please rebuild the Python virtual environment and update the CKAN config file
   according to the :doc:`maintaining/installing/install-from-source` section.
   Then run the commands below:

   ::

     . /usr/lib/ckan/default/bin/activate
     ckan -c /etc/ckan/default/ckan.ini db upgrade
     ckan -c /etc/ckan/default/ckan.ini search-index rebuild
     python /usr/lib/ckan/default/src/ckan/migration/migrate_package_activity.py -c /etc/ckan/default/ckan.ini

Changes:
 * Update: CKAN core version `2.9.4 <http://docs.ckan.org/en/2.9/changelog.html#v-2-9-4-2021-09-22>`_. Changes from CKAN 2.8 and 2.9:

    - New interface based on Bootstrap 3.
    - Video (MP4, WebM, and Ogg) and audio (MP3, WAV, and Ogg) preview.
    - :ref:`dataset_collaborators` which allows users with appropriate permissions to give permissions to other users over individual datasets.
    - API Tokens: Tokens can be created and removed on demand and there is no restriction on the maximum number of tokens per user. Check the documentation on :ref:`data_api`.
    - Users can now upload or link to custom profile pictures.
    - History of a dataset is now in the Activity Stream.

   (The above changelog is adapted from `Changelog — CKAN 2.9.5 documentation <http://docs.ckan.org/en/2.9/changelog.html>`_ by `Open Knowledge Foundation <https://okfn.org/>`_ and `contributors <https://github.com/ckan/ckan/graphs/contributors>`_ licensed under `Creative Commons Attribution-ShareAlike 3.0 Unported <https://creativecommons.org/licenses/by-sa/3.0/>`_.)

 * Other improvements and UI adjustments.

v6.4.6 2021-09-10
=================

Notice:
 * This version requires a requirements upgrade::

    pip install -r /usr/lib/ckan/default/src/ckanext-data-depositario/requirements.txt
    pip install -r /usr/lib/ckan/default/src/ckanext-spatial/pip-requirements-py2.txt
    pip install -r https://raw.githubusercontent.com/ckan/ckanext-xloader/master/requirements.txt
    pip install -r /usr/lib/ckan/default/src/ckanext-dcat/requirements.txt

 * This version does require a database upgrade::

    wget -O- https://github.com/ckan/ckanext-xloader/raw/master/full_text_function.sql | sudo -u postgres psql datastore_default

 * This version requires changes to the configuration file. You will have to manually
   change the following settings according to the 5-c. section in the :doc:`maintaining/installing/install-from-source`:

    - Plugins Settings
    - Schema Settings

 * This version requires changes to the deployment configurations. You will have to
   set the startup script for XLoader according to the section 2 (XLoader Settings) and the section 5 in the :doc:`maintaining/installing/deployment`.
 * The following Python modules can be safely removed:

    - ckanext-repeating
    - DataPusher

Changes:
 * Add: (User guide) Citing a Dataset.
 * Update: (Metadata at the dataset level) Description of Data Type (:ref:`parse-insight-content-types`).

    - Plain text: Remove CSV
    - Structured text: Add CSV and JSON

 * Improvement: CSS refactoring and simplified.
 * Improvement: Replace DataPusher with XLoader for uploading data to the DataStore to prevent from failures due to wrong field type guessing (#11).
 * Upgrade Python dependencies ahead of upcoming updates of CKAN core.
 * Other improvements and UI adjustments.

v6.4.5 2021-07-30
=================

Notice:
 * This version requires the latest `ckanext-wikidatakeyword <https://github.com/depositar/ckanext-wikidatakeyword>`_ and `ckanext-depositar_theme <https://github.com/depositar/ckanext-depositar_theme>`_.

Changes:
 * Improvement: Fix the HTTP 500 error when uploading datasets via the Action API without keywords.
 * Improvement: Fix overflow with long url in WebKit browsers.
 * Other improvements and UI adjustments.

v6.4.4 2021-06-18
=================

Notice:
 * This version requires the latest `ckanext-citation <https://github.com/depositar/ckanext-citation>`_ and `ckanext-depositar_theme <https://github.com/depositar/ckanext-depositar_theme>`_.

Changes:
 * Add: Terms of Use and Privacy Policy.
 * Update: CKAN core version `2.7.11 <https://docs.ckan.org/en/2.7/changelog.html#v-2-7-11-2021-05-19>`_.
 * Other improvements and UI adjustments.

v6.4.3 2021-04-01
=================

Changes:
 * Update: CKAN core version `2.7.10 <https://docs.ckan.org/en/latest/changelog.html#v-2-7-10-2021-02-10>`_.

v6.4.2 2020-12-17
=================

Notice:
 * This version requires the latest `ckanext-spatial <https://github.com/depositar/ckanext-spatial>`_ and `ckanext-depositar_theme <https://github.com/depositar/ckanext-depositar_theme>`_.

Changes:
 * Add: :ref:`rdf_serializations` (experimental).
 * Other improvements and UI adjustments.

v6.4.1 2020-08-20
=================

Notice:
 * This version requires the latest `ckanext-wikidatakeyword <https://github.com/depositar/ckanext-wikidatakeyword>`_, `ckanext-spatial <https://github.com/depositar/ckanext-spatial>`_, and `ckanext-depositar_theme <https://github.com/depositar/ckanext-depositar_theme>`_.

Changes:
 * Improvement: Add links to manual, icons, and help texts on dataset and resource form.
 * Update: Correct some errors in documentation.
 * Update: CKAN core version `2.7.8 <https://docs.ckan.org/en/latest/changelog.html#v-2-7-8-2020-08-05>`_.
 * Remove: Google+ share button.
 * Other improvements and UI adjustments.

v6.4.0 2020-06-10
=================

Notice:
 * This version requires `ckanext-scheming 1.2.0 <https://github.com/ckan/ckanext-scheming/releases/tag/release-1.2.0>`_ and the latest `ckanext-wikidatakeyword <https://github.com/depositar/ckanext-wikidatakeyword>`_.

Changes:
 * Improvement: Simplify metadata. Merge ``Descriptive Information`` into ``Basic Information``, and add the ``Spatio-temporal Information`` section. Please refer to the following table for details. You can also find new metadata standard at the :doc:`appendix/fields/index` section.

 .. list-table::
    :widths: 25 40 35
    :header-rows: 1

    * - Original Field Name
      - Changes
      - Remarks

    * - Language
      - Provide all ISO 639-3 languages. Accept multiple values.
      -

    * - Keywords
      - Rename as "Wikidata Keywords"
      -

    * - Data Type
      - Adopt the :ref:`parse-insight-content-types` used by `Registry of Research Data Repositories (re3data) <https://www.re3data.org/>`_. Accept multiple values.

        The comparison of the old and new options:

        | Statistics → Scientific and statistical data formats
        | Books → Standard office documents
        | Pictures (Non spatial) → Images
        | Pictures (Spatial) → Images
        | Vector → Scientific and statistical data formats
        | 3D Model → Structured graphics
        | Multimedia → Audiovisual data

      -

    * - Time Period Shortcut
      - Removed
      - This field is just a tool for inputing for filling temporal information of the dataset and not part of metadata.

    * - Temporal Resolution
      - Remove the "Decade" and "Century" options. Rename "Year", "Month", and "Date" as "Yearly", "Monthly", and "Daily", respectively.
      - The definitions of decade and century are controversial and seldom used by datasets in depositar.

    * - Start Time
      - Does not restricted to the "Temporal Resolution" field anymore.
      -

    * - End Time
      - Does not restricted to the "Temporal Resolution" field anymore.
      - Add a validator to check whether end time is greater than or equal to start time.

    * - Prompted fields when "Books" is selected in the "Data Type" field
      - Remove the following fields:

        | ISBN-13
        | ISSN
        | Journal
        | Volume
        | Proceeding
        | Location
        | Publisher
        | Publication Year
        | Book Query
        | URL
        | Historical Material
        | Village of Research Area
        | Religion of Research Area
        | Family of Research Area
        | Reservoir of Research Area
        | Industry of Research Area
        | Notes

      - The values of removed fields are merged into the "Remarks" field.

    * - Prompted fields when "Pictures" is selected in the "Data Type" field
      - Remove the following fields:

        | Original Source
        | Scan Size
        | Scanning Resolution
        | Scale Denominator

        The following fields remain but are moved to another place:

        | Spatial Resolution
        | Preprocessing

      - The values of removed fields are merged into the "Remarks" field.

    * - Spatial Resolution
      - Moved to the Spatio-temporal Information section.
      - Formerly used to describe "Pictures" type datasets.

    * - Preprocessing
      - Rename as "Process Step". Moved to the Management Information section.
      - Formerly used to describe "Pictures" type datasets.

    * - Created Time
      -
      - Support the YYYY and YYYY-MM format without converting missing month and day to "01."

    * - Maintainer
      - Rename as "Contact Person"
      - Renaming to meet the practical requirements of data management.

    * - Maintainer Email
      - Rename as "Contact Person Email"
      - Renaming to meet the practical requirements of data management. Add an email validation.

    * - Maintainer Phone
      - Removed
      - Removal due to privacy concerns.

    * - Identifier
      - Removed
      - The value of this field is merged into the "Remarks" field.

    * - Encoding
      - Rename as "Character Encodings"
      - This is a field in the resource level.

 * Other improvements and UI adjustments.

v6.3.6 2019-08-26
=================

 * Add: Citation widget on dataset page.
 * Update: Correct some errors in documentation.
 * Update: CKAN core version 2.7.6.

v6.3.5 2019-03-29
=================

 * Improvement: Fix an issue where newly created user cannot add datasets to
   existed topics (#6).
 * Other improvements.

v6.3.4 2018-12-18
=================

 * Improvement: Fix the scrollable when showing facets on mobile devices.
 * Update: CKAN core version 2.7.5.

v6.3.3 2018-12-07
=================

 * Improvement: Fix an issue where search filters and pills in results cannot be
   displayed correctly.
 * Other improvements and UI adjustments.

v6.3.2 2018-10-25
=================

 * Update: UI hotfix.

v6.3.1 2018-10-25
=================

 * Update: Miscellaneous UI improvements.

v6.3.0 2018-10-23
=================

 * Update: Revamped look.

And, registration is open to the public as of today.

v6.2.1 2018-08-24
=================

 * Update: Email confirmation required to create an account.
 * Update: Correct some errors in documentation.
 * Update: Update licenses to match https://licenses.opendefinition.org/.
   Add CC-BY-NC-SA 4.0 license.
 * Remove: News block in the home page.

v6.2.0 2018-07-20
=================

 * Improvement: Add a "License Details" tool beside all Licenses filters.
 * Update: CKAN core version 2.7.4.
 * Other improvements and UI adjustments.

v6.1.3 2018-07-06
=================

 * Add: English documentation in footer.
 * Improvement: Move the language selector to the top-right corner.
 * Improvement: Fix an issue where the ``Preprocessing`` dataset level field cannot be
   displayed correctly (#2).
 * Improvement: Correct some errors in Chinese documentation.

v6.1.2 2018-05-10
=================

 * Update: CKAN core version 2.6.6.

v6.1.1 2018-04-23
=================

 * Add: Documentation in footer (Chinese only at present).

v6.1.0 2018-03-23
=================

 * Add: Site status in footer.
 * Improvement: Fix the wrong positive_float_validator validator.
 * Improvement: Apply the suitable validators to schema fields.
 * Improvement: Add LineString support to map for filling spatial extent.
 * Improvement: Add edit and delete tools to map for filling spatial extent.
 * Update: Leaflet.draw 0.4.1.
 * Update: CKAN core version 2.6.5.
 * Move the Wikidata-powered keyword function to an extension: https://github.com/depositar-io/ckanext-wikidatakeyword.
 * Other improvements and UI adjustments.

v6.0 2017-11-03
===============

 * Add: A Keywords field, which integrates wikidata entries, replaces the old theme and spatial keywords.
 * Add: System will generate a hash if the new dataset's title can not be slugfied.
 * Update: CKAN core version 2.6.4.
 * Other improvements and UI adjustments.

v5.0.x 2017-09-05
=================

 * Improvement: Simplified metadata with three categories – basic information, descriptive Information, and management information. Add Remarks to replace Reference and Sub Project. Move Encoding to resource level. Remove some fields which are not often used.
 * Improvement: After a user fills in Spatial field using a map, system will generate geojson value and parcel corner and lock those fields.
 * Improvement: Maintainer and Maintainer Email can be filled in with logged-in account information.
 * Improvement: Add a checkbox to open a dataset for organization members only.
 * Improvement: Separate translations for our custom extension from CKAN core thanks to CKAN 2.5's translation capabilities for extensions.
 * Update: ckanext-pages verison with zh_TW language.
 * Update: CKAN core version 2.6.3.
 * Other improvements and UI adjustments.
