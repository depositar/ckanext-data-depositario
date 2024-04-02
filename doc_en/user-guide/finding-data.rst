Finding data
============

Searching the site
------------------

To find datasets in CKAN, type any combination of search words (e.g. "health",
"transport", etc) in the search box on any page. CKAN displays the first page
of results for your search. You can:

* View more pages of results

* Repeat the search, altering some terms

* Restrict the search to datasets with particular tags, data formats, etc using
  the filters in the left-hand column

If there are a large number of results, the filters can be very helpful, since
you can combine filters, selectively adding and removing them, and modify and
repeat the search with existing filters still in place.

.. image:: /images/search_the_site.png

Extended feature — Temporal search
----------------------------------

|site_name| has temporal search function. You can search for the datasets within a given time range.

You can find the temporal search widget from the left sidebar of the home page of datasets.
You can use a slider to set the time range.

.. image:: /images/temporal_search.png

.. _spatial_search:

Extended feature — Spatial search
---------------------------------

If datasets are tagged by geographical area in the ``Spatial Coverage`` field (please refer to
:ref:`Spatial Fields  <UI_editing_extend_spatial>` for details), it is also possible to run CKAN
with an extension which allows searching and filtering of datasets by selecting
an area on a map.

You can find the spatial search widget from the left sidebar of the home page of datasets.
You can do spatial search through the following steps:

#. Select the pencil icon in the upper-right corner:

   .. image:: /images/spatial_search_1.png

#. Then you can draw a rectangle in the expanded map to specify a geographical area you are interested in:

   .. image:: /images/spatial_search_2.jpg

#. The matched datasets will be shown up.

#. If you want to respecify a geographical area, please repeat step 1 and 2.


Searching within a project
--------------------------

If you want to look for data owned by a particular project, you can search
within that project from its home page in CKAN.

#. Select the "Projects" link at the top of any page.

#. Select the project you are interested in. CKAN will display your
   project's home page.

#. Type your search query in the main search box on the page.

CKAN will return search results as normal, but restricted to datasets from the
project.

If the project is of interest, you can opt to be notified of changes to it
(such as new datasets and modifications to datasets) by using the "Follow"
button on the project page. See the section :ref:`managing_your_news_feed`
below. You must have a user account and be logged in to use this feature.


Exploring datasets
------------------

When you have found a dataset you are interested and selected it, CKAN will
display the dataset page. This includes

* The name, description, and other information about the dataset

* Links to and brief descriptions of each of the resources

.. image:: /images/exploring_datasets.png

The resource descriptions link to a dedicated page for each resource. This
resource page includes information about the resource, and enables it to be
downloaded. Many types of resource can also be previewed directly on the
resource page. .CSV and .XLS spreadsheets are previewed in a grid view, with
map and graph views also available if the data is suitable. The resource page
will also preview resources if they are common image types, PDF, or HTML.

The dataset page also has two other tabs:

* *Activity stream* -- see the history of recent changes to the dataset

* *Topics* -- see any topic associated with this dataset.

If the dataset is of interest, you can opt to be notified of changes to it by
using the "Follow" button on the dataset page. See the section
:ref:`managing_your_news_feed` below. You must have a user account and be
logged in to use this feature.

Extended feature — Citing a Dataset
-----------------------------------

You can get the citation for the dataset using the **Cite as** widget in the bottom left corner of the dataset page:

.. image:: /images/citation.png

We provide the following major citation styles:

* American Psychological Association 6th edition (APA)
* Modern Language Association 8th edition (MLA)
* Chicago Manual of Style 17th edition (note)
* Chicago Manual of Style 17th edition (author-date)
* IEEE
* Council of Science Editors, Citation-Sequence (numeric) (CSE C-S)
* American Medical Association (AMA)
* American Chemical Society (ACS)
* American Institute of Physics (AIP)
* American Society of Civil Engineers (ASCE)

You can also find the other citation styles using the search box on the top of the dropdown.

To get the complete list of citation styles,
please visit the `CSL Style Repository <https://github.com/citation-style-language/styles/tree/f5a731144d4b0a838e66ce60cd62a92f7a9e66df>`_.
To search the styles in the style repository by file name, press “t” and start typing.

.. note::

   If the dataset is assigned an :ref:`ark-identifier`, the ARK URL will be used as the URL
   in the citation; if not, the dataset URL will be used instead.

.. _data_preview:

Extended feature — Data preview and visualization
-------------------------------------------------

CKAN's data preview allows you learn the data without the need to download the entire file first:

#. Go to the dataset’s page. You can find it by entering the title in the search box on any page.

#. Select the "Preview" button inside the "Explore" button beside a resource in
   the "Data and Resources" section:

   .. image:: /images/data_preview_1.png

#. Then you can preview the resource:

   .. image:: /images/data_preview_2.png

The data preview function will check the `Format` field to specify a proper ``resource view``.
Please refer to step 5 of :ref:`adding_a_new_dataset`. |site_name| can preview the following formats:

* Text: txt, html, xml, json, and geojson

* Image: png, jpg, jpeg, and gif

* Video: MP4, WebM, and Ogg

* Audio: MP3, WAV, and Ogg

* Table: csv and xls(x)

* Spatial data: WMTS, WMS, and Shapefile (Please specify the shapefile as "shp" in the ``Format`` field
  when filling out resource information, otherwise it can not be visualized.)

* Others: PDF and web page

.. image:: /images/data_preview_3.png

One resource can have multiple views of the same data (for example a grid and some graphs
for tabular data).

You can add a new resource view through the following steps:

#. Go to the resource's page.

#. Select the "Manage" button (You must have the right to edit the resource).

   .. image:: /images/new_preview_1.png

#. Select the "Views" tab in the next page. From here you can create new views,
   update or delete existing ones and reorder them. Available view plugins are:

   * Data Explorer: It allows querying, filtering, graphing and mapping data.

   * Grid: Displays a filterable, sortable, table view of structured data.

   * Map: Shows data stored on the DataStore in an interactive map.
     It supports plotting markers from a pair of latitude / longitude fields or
     from a field containing a GeoJSON representation of the geometries.

   * Image: If the resource format is a common image format like PNG, JPEG or GIF,
     it adds an ``<img>`` tag pointing to the resource URL.

   * Web page: Adds an ``<iframe>`` tag to embed the resource URL.

   .. image:: /images/new_preview_2.png

#. Select the "Add" button to save the new view. You can also take a sneak peek at
   the view by clicking the "Preview" button.
