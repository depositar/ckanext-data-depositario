.. This tocdepth stops Sphinx from putting every subsection title in this file
   into the master table of contents.

:tocdepth: 1

---------
Changelog
---------

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
