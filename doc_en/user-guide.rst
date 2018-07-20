==========
User guide
==========

"|site_name|" is a public platform for storing, preserving, managing, and exploring research data. |site_name| is built with `CKAN <http://ckan.org>`_, which is an open source data management system, and extended with many useful features. The site is located at https://data.depositar.io.

This user guide covers using CKAN's web interface to organize, publish and find
data. CKAN also has a powerful API (machine interface), which makes it easy to
develop extensions and links with other information systems. The API is
documented in http://docs.ckan.org/en/2.7/api/index.html.

Some web UI features relating to site administration are available only to
users with sysadmin status, and are documented in http://docs.ckan.org/en/2.7/sysadmin-guide.html.

.. note::

   This manual is translated and adapted from `User guide — CKAN 2.7.4 documentation`_ by `Open Knowledge International <https://okfn.org/>`_ and `contributors <https://github.com/ckan/ckan/graphs/contributors>`_ licensed under `Creative Commons Attribution-ShareAlike 3.0 Unported <https://creativecommons.org/licenses/by-sa/3.0/>`_.

-------------
What is CKAN?
-------------

CKAN is a tool for making open data websites. (Think of a content management
system like WordPress - but for data, instead of pages and blog posts.) It
helps you manage and publish collections of data. It is used by national and
local governments, research institutions, and other organizations who collect a
lot of data. |site_name| is built with CKAN.

Once your data is published, users can use its faceted search features to
browse and find the data they need, and preview it using maps, graphs and
tables - whether they are developers, journalists, researchers, NGOs, citizens,
or even your own staff.

Datasets and resources
======================

For CKAN purposes, data is published in units called "datasets". A dataset is a
parcel of data - for example, it could be the crime statistics for a region,
the spending figures for a government department, or temperature readings from
various weather stations. When users search for data, the search results they
see will be individual datasets.

A dataset contains two things:

* Information or "metadata" about the data. For example, the title and
  publisher, date, what formats it is available in, what license it is released
  under, etc.

* A number of "resources", which hold the data itself. CKAN does not mind what
  format the data is in. A resource can be a CSV or Excel spreadsheet, XML file,
  PDF document, image file, linked data in RDF format, etc. CKAN can store the
  resource internally, or store it simply as a link, the resource itself being
  elsewhere on the web. A dataset can contain any number of resources. For
  example, different resources might contain the data for different years, or
  they might contain the same data in different formats.

Users, organizations and authorization
======================================

CKAN users can register user accounts and log in. Normally (depending on the
site setup), login is not needed to search for and find data, but is needed for
all publishing functions: datasets can be created, edited, etc by users with
the appropriate permissions.

Normally, each dataset is owned by an "organization". A CKAN instance can have
any number of organizations. For example, if CKAN is being used as a data
portal by a national government, the organizations might be different
government departments, each of which publishes data. Each organization can
have its own workflow and authorizations, allowing it to manage its own
publishing process.

An organization's administrators can add individual users to it, with
different roles depending on the level of authorization needed. A user in an
organization can create a dataset owned by that organization. In the default
setup, this dataset is initially private, and visible only to other users in
the same organization. When it is ready for publication, it can be published at
the press of a button. This may require a higher authorization level within the
organization.

Datasets cannot normally be created except within organizations. It is
possible, however, to set up CKAN to allow datasets not owned by any
organization. Such datasets can be edited by any logged-in user, creating the
possibility of a wiki-like datahub.

.. note::

    The user guide covers all the main features of the web user interface (UI).
    In practice, depending on how the site is configured, some of these functions
    may be slightly different or unavailable. For example, in an official CKAN
    instance in a production setting, the site administrator will probably have
    made it impossible for users to create new organizations via the UI. You can
    try out all the features described at http://demo.ckan.org. We also provide
    a demo system at https://demo.depositar.io with the same features
    as |site_name| for evaluation purposes.

-----------------
Using |site_name|
-----------------

Registering and logging in
==========================

.. note::

    Registration is needed for most publishing features and for personalization
    features, such as "following" datasets. It is not needed to search for and
    download data.

.. note::

   You can not directly register on |site_name| currently. If you want to create
   a new account, please refer to :doc:`join-guide` and apply one. Therefore, the information
   as below is for reference only.

.. hint::

   We provide a demo system at https://demo.depositar.io with the same features
   as |site_name| for evaluation purposes. You can create an account and try
   any functions provided by |site_name|. Please note that all data in this instance
   will be deleted occasionally.

To create a user ID, use the "Register" link at the top of any page. CKAN will
ask for the following:

* *Username* -- choose a username using only letters, numbers, - and _ characters.
  For example, "jbloggs" or "joe_bloggs93".

* *Full name* -- to be displayed on your user profile

* *E-mail address* -- this will not be visible to other users

* *Password* -- enter the same password in both boxes

.. image:: /images/register_account.jpg

If there are problems with any of the fields, CKAN will tell you the problem
and enable you to correct it. When the fields are filled in correctly, CKAN
will create your user account and automatically log you in.

Features for publishers
=======================

.. _adding_a_new_dataset:

Adding a new dataset
--------------------

.. note::

   You may need to be a member of an organization in order to add and edit
   datsets. If you want to create a new account, please refer to :doc:`join-guide`
   and apply one.

**Step 1**. You can access CKAN's "Create dataset" screen in two ways.

a) Select the "Datasets" link at the top of any page. From this, above the
   search box, select the "Add Dataset" button.

b) Alternatively, select the "organizations" link at the top of a page. Now
   select the page for the organization that should own your new dataset. Provided
   that you are a member of this organization, you can now select the "Add
   Dataset" button above the search box.

**Step 2**. CKAN will ask for the information about your data (See :doc:`appendix/dataset_fields`).

.. image:: /images/add_dataset_1.jpg

.. note::

    By default, the only required field on this page is the title. However, it
    is good practice to include, at the minimum, a short description and, if
    possible, the license information. You should ensure that you choose the
    correct organization for the dataset, since at present, this cannot be changed
    later. You can edit or add to the other fields later.

**Step 3**. When you have filled in the information on this page, select the "Next: Add
Data" button. (Alternatively select "Cancel" to discard the information filled
in.)

.. _add_resource:

**Step 4**. CKAN will display the "Add data" screen.

  .. image:: /images/add_dataset_2.jpg

This is where you will add one or more "resources" which contain the data for
this dataset. Choose a file or link for your data resource and select the
appropriate choice at the top of the screen:

* If you are giving CKAN a link to the data, like
  ``http://example.com/mydata.csv``, then select "Link to a file" or "Link to an
  API". (If you don't know what an API is, you don't need to worry about this
  option - select "Link to a file".)

* If the data to be added to CKAN is in a file on your computer, select "Upload
  a file". CKAN will give you a file browser to select it.

**Step 5**. Add the other information on the page. (Please refer to :doc:`appendix/resource_fields`)
CKAN does not require this information, but it is good practice to add it.

**Step 6**. If you have more resources (files or links) to add to the dataset, select
the "Save & add another" button. When you have finished adding resources,
select "Next: Additional Info".

**Step 7**. Select the 'Finish' button. CKAN creates the dataset and shows you
the result. You have finished!

You should be able to find your dataset by typing the title, or some relevant
words from the description, into the search box on any page in your CKAN
instance. For more information about finding data, see the section
:ref:`finding_data`.


Extended feature — Add a dataset to an existing group
-----------------------------------------------------

|site_name| uses the "Group" feature built in CKAN to label a dataset as one or several themes. The group is different from "Organization" feature as the latter is the way to control the visibility of datasets in CKAN and each dataset can belong to ONLY ONE organization.

We refer the `ISO19115 <https://www2.usgs.gov/science/about/thesaurus-full.php?thcode=15>`_ standard to define the following themes:

* **farming**: Rearing of animals or cultivation of plants, for example agriculture, irrigation, aquaculture, plantations, herding, pests and diseases affecting crops and livestock
* **biota**: Flora or fauna in natural environment, for example wildlife, vegetation, biological sciences, ecology, wilderness, sea life, wetlands, habitat, biological resources
* **boundaries**: Legal land descriptions, for example political and administrative boundaries, governmental units, marine boundaries, voting districts, school districts, international boundaries
* **climatologyMeteorologyAtmosphere**: Processes and phenomena of the atmosphere, for example cloud cover, weather, climate, atmospheric conditions, climate change, precipitation
* **economy** Economic activities, conditions, and employment, for example production, labor, revenue, business, commerce, industry, tourism and ecotourism, forestry, fisheries, commercial or subsistence hunting, exploration and exploitation of resources such as minerals, oil and gas
* **elevation** Height above or below seal level, for example altitude, bathymetry, digital elevation models, slope, derived products, DEMs, TINs
* **environment** Environmental resources, protection and conservation, for example environmental pollution, waste storage and treatment, environmental impact assessment, monitoring environmental risk, nature reserves, landscape, water quality, air quality, environmental modeling
* **geoscientificInformation** Information pertaining to earth sciences, for example geophysical features and processes, geology, minerals, sciences dealing with the composition, structure and origin of the earth's rocks, risks of earthquakes, volcanic activity, landslides, gravity information, soils, permafrost, hydrogeology, groundwater, erosion
* **health** Health, health services, human ecology, and safety, for example disease and illness, factors affecting health, hygiene, substance abuse, mental and physical health, health services, health care providers, public health
* **imageryBaseMapsEarthCover** Base maps, for example land/earth cover, topographic maps, imagery, unclassified images, annotations, digital ortho imagery
* **intelligenceMilitary** Military bases, structures, activities, for example barracks, training grounds, military transportation, information collection
* **inlandWaters** Inland water features, drainage systems and characteristics, for example rivers and glaciers, salt lakes, water utilization plans, dams, currents, floods and flood hazards, water quality, hydrographic charts, watersheds, wetlands, hydrography
* **location** Positional information and services, for example addresses, geodetic networks, geodetic control points, postal zones and services, place names, geographic names
* **oceans** Features and characteristics of salt water bodies (excluding inland waters), for example tides, tidal waves, coastal information, reefs, maritime, outer continental shelf submerged lands, shoreline
* **planningCadastre** Information used for appropriate actions for future use of the land, for example land use maps, zoning maps, cadastral surveys, land ownership, parcels, easements, tax maps, federal land ownership status, public land conveyance records
* **society** Characteristics of society and culture, for example settlements, housing, anthropology, archaeology, education, traditional beliefs, manners and customs, demographic data, tourism, recreational areas and activities, parks, recreational trails, historical sites, cultural resources, social impact assessments, crime and justice, law enforcement, census information, immigration, ethnicity
* **structure** Man-made construction, for example buildings, museums, churches, factories, housing, monuments, shops, towers, building footprints, architectural and structural plans
* **transportation** Means and aids for conveying persons or goods, for example roads, airports/airstrips, shipping routes, tunnels nautical charts, vehicle or vessel location, aeronautical charts, railways
* **utilitiesCommunication** Energy, water and waste systems and communications infrastructure and services, for example hydroelectricity, geothermal, solar and nuclear sources of energy, water purification and distribution, sewage collection and disposal, electricity and gas distribution, data communication, telecommunication, radio, communication networks

Before adding a dataset to a theme, you should complete the upload process of the dataset (listed on the :ref:`adding_a_new_dataset`). Then do the following steps:

* Go to the dataset's page. You can find it by entering the title in the search box on any page.

* Select the "Groups" tab in the dataset's page.

    .. image:: /images/addGroup1.jpg

+ Select an existing group and select the "Add to group" button.

    .. image:: /images/addGroup2.jpg

.. _UI_editing_extend:

Extended feature — Fill-in snippet
----------------------------------

.. _UI_editing_extend_time:

* **Temporal Information**

The "temporal information" here means the time to events related to the dataset, not the time when
the resources in the dataset were created.

  * *Time Period Shortcut* -- This shortcut provides some historical periods for filling temporal
    information of the dataset.

  * *Temporal Resolution* [#]_ -- This refers to the precision of a measurement with respect to time.
    
  * *Start and End Time* -- It depends on the temporal resolution setting.
    Acceptable formats: "YYYY", "YYYY-MM", or "YYYY-MM-DD".
  
.. image:: /images/timeInfo.jpg

.. _UI_editing_extend_spatial:

* **Spatial Fields**

Here you can specify the spatial extent of the dataset for indexing, then the dataset can
be found through `spatial search <Extended feature — Spatial search_>`_.

You can use the following two methods to generate a valid spatial extent in GeoJSON format:

  * *Convert from Parcel Corner* -- If you already have the longitude and latitude of the corners
    for the parcel to describe the dataset, you can fill in the X.min, X.max, Y.mim, and Y.max
    fields, then select the "Convert from Parcel Corner" button to generate the spatial extent.

  * *Using a Map* -- You can also add the spatial extent through digitizing process.
    Select the "Using a Map" button and draw a polyline, polygon, rectangle, or marker
    on the expanded map to generate the spatial extent.

.. image:: /images/spatialInfo.jpg

* **Auto-completion of management metadata**

You can use the "Use your account information to fill in maintainer's name and email" button
to automatically fill in the maintainer's information (``Maintainer`` and ``Maintainer Email``)
using your account information (for account information, please refer to :ref:`managing_profile`).

.. image:: /images/profileInput.jpg


Editing a dataset
-----------------

You can edit the dataset you have created, or any dataset owned by an
organization that you are a member of. (If a dataset is not owned by any
organization, then any registered user can edit it.)

#. Go to the dataset's page. You can find it by entering the title in the search box on any page.

#. Select the "Edit" button, which you should see above the dataset title.

#. CKAN displays the "Edit dataset" screen. You can edit any of the fields
   (Title, Description, Dataset, etc), change the visibility (Private/Public), and
   add or delete tags or custom fields. For details of these fields, see
   :ref:`adding_a_new_dataset`.

#. When you have finished, select the "Update dataset" button to save your changes.

.. image:: /images/edit_dataset.jpg


Adding, deleting and editing resources
--------------------------------------

#. Go to the dataset's "Edit dataset" page (steps 1-2 above).

#. In the left sidebar, there are options for editing resources. You can select
   an existing resource (to edit or delete it), or select "Add new resource".

#. You can edit the information about the resource or change the linked or
   uploaded file. For details, see steps 4-5 of "Adding a new resource", above.

#. When you have finished editing, select the button marked "Update resource"
   (or "Add", for a new resource) to save your changes. Alternatively, to delete
   the resource, select the "Delete resource" button.


Deleting a dataset
------------------

#. Go to the dataset's "Edit dataset" page (see "Editing a dataset", above).

#. Select the "Delete" button.

#. CKAN displays a confirmation dialog box. To complete deletion of the
   dataset, select "Confirm".

.. note::

    The "Deleted" dataset is not completely deleted. It is hidden, so it does
    not show up in any searches, etc. However, by visiting the URL for the
    dataset's page, it can still be seen (by users with appropriate authorization),
    and "undeleted" if necessary. If it is important to completely delete the
    dataset, contact your site administrator.


.. _creating_an_organization:

Creating an organization
------------------------

In general, each dataset is owned by one organization. Each organization
includes certain users, who can modify its datasets and create new ones.
Different levels of access privileges within an organization can be given to
users, e.g. some users might be able to edit datasets but not create new ones,
or to create datasets but not publish them. Each organization has a home page,
where users can find some information about the organization and search within
its datasets. This allows different data publishing departments, bodies, etc to
control their own publishing policies.

To create an organization:

#. Select the "Organizations" link at the top of any page.

#. Select the "Add Organization" button below the search box.

#. CKAN displays the "Create an Organization" page.

#. Enter a name for the organization, and, optionally, a description and image
   URL for the organization's home page.

#. Select the "Create Organization" button. CKAN creates your organization and
   displays its home page. Initially, of course, the organization has no datasets.

.. image:: /images/create_organization.jpg

You can now change the access privileges to the organization for other users -
see :ref:`managing_an_organization` below. You can also create datasets owned by the
organization; see :ref:`adding_a_new_dataset` above.

.. note::

    Depending on how CKAN is set up, you may not be authorized to create new
    organizations. In this case, if you need a new organization, you will need to
    contact your site administrator.


.. _managing_an_organization:

Managing an organization
------------------------

When you create an organization, CKAN automatically makes you its "Admin".
From the organization's page you should see an "Admin" button above the search
box. When you select this, CKAN displays the organization admin page. This page
has two tabs:

* *Info* -- Here you can edit the information supplied when the organization
  was created (title, description and image).

* *Members* -- Here you can add, remove and change access roles for different
  users in the organization. Note: you will need to know their username on CKAN.

.. image:: /images/manage_organization.jpg

By default CKAN allows members of organizations with three roles:

* *Member* -- can see the organization's private datasets

* *Editor* -- can edit and publish datasets

* *Admin* -- can add, remove and change roles for organization members

.. _finding_data:

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

.. image:: /images/search_the_site.jpg

Extended feature — Temporal search
----------------------------------

|site_name| has temporal search function. You can search for the datasets within a given date range.

You can find the temporal search widget from the left sidebar of the home page of datasets.
You can do temporal search in two ways:

#. Use a range slider.

#. Use a time period shortcut which contains some historical periods.

.. image:: /images/time_search.jpg
  
Extended feature — Spatial search
---------------------------------

If datasets are tagged by geographical area in the ``spatial`` field (please refer to
:ref:`Spatial Fields  <UI_editing_extend_spatial>` for details), it is also possible to run CKAN
with an extension which allows searching and filtering of datasets by selecting
an area on a map.

You can find the spatial search widget from the left sidebar of the home page of datasets.
You can do spatial search through the following steps:

#. Select the pencil icon in the upper-right corner:

   .. image:: /images/spatial_search1.jpg
      
#. Then you can draw a rectangle in the expanded map to specify a geographical area you are interested in:

   .. image:: /images/spatial_search2.jpg
      
#. The matched datasets will be shown up.

   .. image:: /images/spatial_search3.jpg

#. If you want to respecify a geographical area, please repeat step 1 and 2.


Searching within an organization
--------------------------------

If you want to look for data owned by a particular organization, you can search
within that organization from its home page in CKAN.

#. Select the "Organizations" link at the top of any page.

#. Select the organization you are interested in. CKAN will display your
   organization's home page.

#. Type your search query in the main search box on the page.

CKAN will return search results as normal, but restricted to datasets from the
organization.

If the organization is of interest, you can opt to be notified of changes to it
(such as new datasets and modifications to datasets) by using the "Follow"
button on the organization page. See the section :ref:`managing_your_news_feed`
below. You must have a user account and be logged in to use this feature.


Exploring datasets
------------------

When you have found a dataset you are interested and selected it, CKAN will
display the dataset page. This includes

* The name, description, and other information about the dataset

* Links to and brief descriptions of each of the resources

.. image:: /images/exploring_datasets.jpg

The resource descriptions link to a dedicated page for each resource. This
resource page includes information about the resource, and enables it to be
downloaded. Many types of resource can also be previewed directly on the
resource page. .CSV and .XLS spreadsheets are previewed in a grid view, with
map and graph views also available if the data is suitable. The resource page
will also preview resources if they are common image types, PDF, or HTML.

The dataset page also has two other tabs:

* *Activity stream* -- see the history of recent changes to the dataset

* *Groups* -- see any group associated with this dataset.

If the dataset is of interest, you can opt to be notified of changes to it by
using the "Follow" button on the dataset page. See the section
:ref:`managing_your_news_feed` below. You must have a user account and be
logged in to use this feature.

.. _data_preview:

Extended feature — Data preview and visualization
-------------------------------------------------

CKAN's data preview allows you learn the data without the need to download the entire file first:

#. Go to the dataset’s page. You can find it by entering the title in the search box on any page.

#. Select the "Preview" button inside the "Explore" button beside a resource in
   the "Data and Resources" section:

   .. image:: /images/data_preview.jpg
    
#. Then you can preview the resource:

   .. image:: /images/data_preview2.jpg

The data preview function will check the `Format` field to specify a proper ``resource view``.
Please refer to step 5 of :ref:`adding_a_new_dataset`. |site_name| can preview the following formats:

* Text: txt, html, xml, json, and geojson

* Image: png, jpg, jpeg, and gif

* Table: csv and xls(x)

* Spatial data: WMTS, WMS, and Shapefile [#]_

* Others: PDF and web page

One resource can have multiple views of the same data (for example a grid and some graphs
for tabular data): 

.. image:: /images/data_preview3.jpg

.. image:: /images/data_preview4.jpg

You can add a new resource view through the following steps:

#. Go to the resource's page.

#. Select the "Manage" button (You must have the right to edit the resource).

   .. image:: /images/new_preview.jpg
    
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

   .. image:: /images/new_preview2.jpg

#. Select the "Add" button to save the new view. You can also take a sneak peek at
   the view by clicking the "Preview" button.

.. _data_api:

DataStore API
=============

The CKAN DataStore extension provides an ad hoc database for storage of structured data
from CKAN resources. It also offers an API for reading, searching and filtering data without
the need to download the entire file first.

You can get access to DataStore API through the following steps:

#. Go to the resource's page.

#. Select the "Data API" button, a pop-up window will show how to use the API and provide
   some examples.

   .. image:: /images/data_api.jpg

   .. image:: /images/data_api2.jpg
  
#. Some API functions require an API key. You can get your key from the user profile page:

    .. image:: /images/data_api3.jpg

Personalization
===============

CKAN provides features to personalize the experience of both searching for and
publishing data. You must be logged in to use these features.

.. _managing_your_news_feed:

Managing your news feed
-----------------------

At the top of any page, select the dashboard symbol (next to your name). CKAN
displays your News feed. This shows changes to datasets that you follow, and
any changed or new datasets in organizations that you follow. The number by the
dashboard symbol shows the number of new notifications in your News feed since
you last looked at it. As well as datasets and organizations, it is possible to
follow individual users (to be notified of changes that they make to datasets).

.. image:: /images/manage_news_feed.jpg

If you want to stop following a dataset (or organization or user), go to the
dataset's page (e.g. by selecting a link to it in your News feed) and select
the "Unfollow" button.

.. _managing_profile:

Managing your user profile
--------------------------

You can change the information that CKAN holds about you, including what other
users see about you by editing your user profile. (Users are most likely to see
your profile when you edit a dataset or upload data to an organization that
they are following.) To do this, select the gearwheel symbol at the top of any
page.

.. image:: /images/manage_user_profile.jpg

CKAN displays the user settings page. Here you can change:

* Your username

* Your full name

* Your e-mail address (note: this is not displayed to other users)

* Your profile text - an optional short paragraph about yourself

* Your password

Make the changes you require and then select the "Update Profile" button.

.. note::

    If you change your username, CKAN will log you out. You will need to log
    back in using your new username.

.. _limitation:

System Limitation
=================

* File size limit: up to around 1 GB.

* File size limit for data preview: up to around 20 MB for general format.
  Up to dozens of MB for PDFs.

* Filename length: 3 to 100 characters (including the filename extension).

.. [#] This section uses material from the Wikipedia article
       `Temporal resolution <https://en.wikipedia.org/wiki/Temporal_resolution>`_,
       which is released under the `Creative Commons Attribution-Share-Alike License 3.0
       <https://creativecommons.org/licenses/by-sa/3.0/>`_.
.. [#] Please specify the shapefile as "shp" in the ``Format`` field when filling out its information,
       otherwise it can not be visualized (Please refer to :doc:`appendix/resource_fields`).
