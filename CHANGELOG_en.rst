.. This tocdepth stops Sphinx from putting every subsection title in this file
   into the master table of contents.

:tocdepth: 1

---------
Changelog
---------

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
