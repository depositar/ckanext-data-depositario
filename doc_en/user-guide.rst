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

   This manual is translated and adapted from `User guide — CKAN 2.7.6 documentation`_ by `Open Knowledge International <https://okfn.org/>`_ and `contributors <https://github.com/ckan/ckan/graphs/contributors>`_ licensed under `Creative Commons Attribution-ShareAlike 3.0 Unported <https://creativecommons.org/licenses/by-sa/3.0/>`_.

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

-----------------
Using |site_name|
-----------------

Registering and logging in
==========================

.. note::

    Registration is needed for most publishing features and for personalization
    features, such as "following" datasets. It is not needed to search for and
    download data.

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

.. image:: /images/register_account.png

If there are problems with any of the fields, CKAN will tell you the problem
and enable you to correct it. When the fields are filled in correctly, we will receive an
email to set your password as follows.
Then you can use the "Log in" link at the top of any page to log in.

.. parsed-literal::

   Dear OOO,

   You have requested your password on depositar to be reset.

   Please click the following link to confirm this request:

      :site_url:`user/reset/[token]`

   Have a nice day.

   --
   Message sent by depositar (https://data.depositar.io)

Features for publishers
=======================

.. _adding_a_new_dataset:

Adding a new dataset
--------------------

.. note::

   You may need an user account in order to add and edit datasets.

**Step 1**. You can access CKAN's "Create dataset" screen in two ways.

a) Select the "Datasets" link at the top of any page. From this, above the
   search box, select the "Add Dataset" button.

b) Alternatively, select the "projects" link at the top of a page. Now
   select the page for the project that should own your new dataset. Provided
   that you are a member of this project, you can now select the "Add
   Dataset" button above the search box.

**Step 2**. CKAN will ask for the information about your data (See :ref:`dataset_fields`).

.. image:: /images/add_dataset_1.png

.. note::

    By default, the only required field on this page is the title. However, it
    is good practice to include, at the minimum, a short description and, if
    possible, the license information. You should ensure that you choose the
    correct project for the dataset, since at present, this cannot be changed
    later. You can edit or add to the other fields later.

**Step 3**. When you have filled in the information on this page, select the "Next: Add
Data" button. (Alternatively select "Cancel" to discard the information filled
in.)

.. _add_resource:

**Step 4**. CKAN will display the "Add data" screen.

  .. image:: /images/add_dataset_2.png

This is where you will add one or more "resources" which contain the data for
this dataset. Choose a file or link for your data resource and select the
appropriate choice at the top of the screen:

* If you are giving CKAN a link to the data, like
  ``http://example.com/mydata.csv``, then select "Link to a file" or "Link to an
  API". (If you don't know what an API is, you don't need to worry about this
  option - select "Link to a file".)

* If the data to be added to CKAN is in a file on your computer, select "Upload
  a file". CKAN will give you a file browser to select it.

**Step 5**. Add the other information on the page. (Please refer to :ref:`resource_fields`)
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

.. _adding_a_dataset_to_topic:

Extended feature — Add a dataset to an existing topic
-----------------------------------------------------

The topic is different from "Projects" feature as the latter is the way to control the visibility of datasets in CKAN and each dataset can belong to ONLY ONE project.

We refer to the `Wikipedia's categories <https://en.wikipedia.org/wiki/Portal:Contents/Categories>`_
to define the following topics:

* General reference
* Culture and the arts
* Geography and places
* Health and fitness
* History and events
* Human activities
* Mathematics and logic
* Natural and physical sciences
* People and self
* Philosophy and thinking
* Religion and belief systems
* Society and social sciences
* Technology and applied sciences

You can also use the following topics, which are based on `ISO19115 <https://www2.usgs.gov/science/about/thesaurus-full.php?thcode=15>`_ standard:

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

* Select the "Topics" tab in the dataset's page.

    .. image:: /images/add_topic_1.png

+ Select an existing topic and select the "Add to topic" button.

    .. image:: /images/add_topic_2.png

.. _UI_editing_extend:

Extended feature — Fill-in snippet
----------------------------------

.. _UI_editing_extend_time:

* **Temporal Information (Time Period of Dataset)**

The "temporal information" here means the time to events related to the dataset, not the time when
the resources in the dataset were created.

  * *Temporal Resolution* -- This refers to the precision of a measurement with respect to time.
    It can be the minimal time interval between subsequent examinations, or the maximum time error
    when the time period is uncertain.

  * *Start and End Time* -- This refers the beginning and end time of the time period.
    Acceptable formats: "YYYY", "YYYY-MM", or "YYYY-MM-DD".
  
.. image:: /images/temporal_info.png

.. _UI_editing_extend_spatial:

* **Spatial Information**

Here you can specify the spatial extent of the dataset for indexing, then the dataset can
be found through `spatial search <Extended feature — Spatial search_>`_.

You can use the following two methods to generate a valid spatial extent in GeoJSON format:

  * *Using a Map* -- You can also add the spatial extent through digitizing process.
    Select the "Use a map to fill in spatial coverage" button and draw a polyline, polygon,
    rectangle, or marker on the expanded map to generate the spatial extent.

  * *Convert from Parcel Corner* -- If you already have the longitude and latitude of the corners
    for the parcel to describe the dataset, you can fill in the X.min, X.max, Y.mim, and Y.max
    fields, then select the "Use parcel corners to fill in spatial coverage" button to generate
    the spatial extent.

You can also fill in the spatial resolution of the dataset here.

.. image:: /images/spatial_info.png

* **Auto-completion of management metadata**

You can use the "Use your account information to fill in contact person's name and email" button
to automatically fill in the contact person's information (``Contact Person`` and ``Contact Person Email``)
using your account information (for account information, please refer to :ref:`managing_profile`).

.. image:: /images/profile_input.png

.. _editing-a-dataset:

Editing a dataset
-----------------

You can edit the dataset you have created, or any dataset owned by an
project that you are a member of. (If a dataset is not owned by any
project, then any registered user can edit it.)

#. Go to the dataset's page. You can find it by entering the title in the search box on any page.

#. Select the "Edit" button, which you should see above the dataset title.

#. CKAN displays the "Edit dataset" screen. You can edit any of the fields
   (Title, Description, Dataset, etc), change the visibility (Private/Public), and
   add or delete tags or custom fields. For details of these fields, see
   :ref:`adding_a_new_dataset`.

#. When you have finished, select the "Update dataset" button to save your changes.

.. image:: /images/edit_dataset.png

.. _dataset_collaborators:

Dataset collaborators
---------------------

In addition to traditional project-based permissions, CKAN instances can also enable
the dataset collaborators feature, which allows dataset-level authorization. This provides
more granular control over who can access and modify datasets that belong to a project,
or allows authorization setups not based on projects.

You can manage dataset collaborators through the "Collaborators" tab in the "Edit dataset" page.

By default, only Administrators of the project a dataset belongs to can add collaborators
to a dataset. When adding them, they can choose between two roles: member and editor.

A **member** can:

* View the dataset if it is private.

An **editor** can do everything a **member** can plus:

* Make the dataset public or private.
* Edit or delete the dataset (including assigning it to a project)

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


.. _creating_an_project:

Creating a project
------------------

In general, each dataset is owned by one project. Each project
includes certain users, who can modify its datasets and create new ones.
Different levels of access privileges within a project can be given to
users, e.g. some users might be able to edit datasets but not create new ones,
or to create datasets but not publish them. Each project has a home page,
where users can find some information about the project and search within
its datasets. This allows different data publishing departments, bodies, etc to
control their own publishing policies.

To create a project:

#. Select the "Projects" link at the top of any page.

#. Select the "Add Project" button below the search box.

#. CKAN displays the "Create a Project" page.

#. Enter a name for the project, and, optionally, a description and image
   URL for the project's home page.

#. Select the "Create Project" button. CKAN creates your project and
   displays its home page. Initially, of course, the project has no datasets.

.. image:: /images/create_project.png

You can now change the access privileges to the project for other users -
see :ref:`managing_an_project` below. You can also create datasets owned by the
project; see :ref:`adding_a_new_dataset` above.

.. note::

    You can learn how to fill in the information above by referring to
    :site_url:`existing projects <organization>`.
    And, depending on how CKAN is set up, you may not be authorized to create new
    projects. In this case, if you need a new project, you will need to
    contact your site administrator.


.. _managing_an_project:

Managing a project
------------------

When you create a project, CKAN automatically makes you its "Admin".
From the project's page you should see an "Admin" button above the search
box. When you select this, CKAN displays the project admin page. This page
has two tabs:

* *Info* -- Here you can edit the information supplied when the project
  was created (title, description and image).

* *Members* -- Here you can add, remove and change access roles for different
  users in the project. Note: you will need to know their username on CKAN.

.. image:: /images/manage_project.png

By default CKAN allows members of projects with three roles:

* *Member* -- can see the project's private datasets

* *Editor* -- can edit and publish datasets

* *Admin* -- can add, remove and change roles for project members

Inviting others to project
--------------------------

If you want to invite others to collaborate on datasets, you can invite them to your project.
From the project’s page you should see an “Admin” button above the search box.
When you select this, CKAN displays the project admin page.

Select the "Members" tab, and you will see the project members page.
Then select the "Add Member" button.

.. image:: /images/invite_user.png

You can invite an user to your project by his/her username in the "Existing User" section.
Or you can invite a new user via email.

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

.. image:: /images/search_the_site.png

Extended feature — Temporal search
----------------------------------

|site_name| has temporal search function. You can search for the datasets within a given time range.

You can find the temporal search widget from the left sidebar of the home page of datasets.
You can use a slider to set the time range.

.. image:: /images/temporal_search.png
  
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

   .. image:: /images/data_api_1.png

   .. image:: /images/data_api_2.png
  
#. Some API functions require an API key. You can get your key from the user profile page using the "User" link at the top of any page. You can also get a key from the API Tokens function located at the top of the user page:

    .. image:: /images/data_api_3.png

.. _rdf_serializations:

RDF Serializations
==================

|site_name| uses `RDF serializer <https://github.com/ckan/ckanext-dcat/tree/v1.1.0#rdf-dcat-serializer>`_ provided by ckanext-dcat to expose RDF graph.

For the alignments of the metadata of |site_name| and RDF vocabularies, please refer to :doc:`appendix/metadata-mapping/dcat/index`.

.. note::

   This feature is a work in process.
   If you have any comment or feedback, please `contact us`_.

.. note::

   The currently supported formats are:

   ========= ========= ===================
   Format    Extension Media Type
   ========= ========= ===================
   RDF/XML   xml       application/rdf+xml
   Turtle    ttl       text/turtle
   Notation3 n3        text/n3
   JSON-LD   jsonld    application/ld+json
   ========= ========= ===================

.. hint::

   About the ``{}`` in the following sections：

   * For the ``dataset-id``, please fill in the dataset's **URL**.
   * For the ``format``, please fill in the **Extension** in the above table.
   * For the ``media_type``, please fill in the **Media Type** in the above table.

Method 1: RDF Endpoints
-----------------------

.. parsed-literal::

   Catalog endpoint:

   :site_url:`catalog.{format}`

   Dataset endpoints:

   :site_url:`dataset/{dataset-id}.{format}`

You can also access the serialization using the **Other Access** widget in the bottom left corner of the dataset page:

.. image:: /images/rdf_serializations.png

Method 2: Content Negotiation
-----------------------------

Please run the command below:

.. parsed-literal::

   curl :site_url:`dataset/{dataset-id}` -H Accept:{media_type}

Example
-------

To get the RDF/XML format of the :site_url:`Example dataset <dataset/place-names-in-west-central-district-of-tainan>`:

Method 1:

.. parsed-literal::

   :site_url:`dataset/place-names-in-west-central-district-of-tainan.xml`

Method 2:

Run the command below:

.. parsed-literal::

   curl :site_url:`dataset/place-names-in-west-central-district-of-tainan` -H Accept:application/rdf+xml

.. _ark-identifier:

ARK Persistent Identifier
=========================

`Archival Resource Key <https://arks.org/about/>`_ (ARK) is a multi-purpose, general identifier which can be used as references for information objects.
|site_name| assigns ARKs as persistent identifiers (PID) to datasets via the `ckanext-ark <https://github.com/depositar/ckanext-ark>`_ extension,
just like the Digital Object Identifier (DOI).

.. note::

   This feature is a work in process.
   If you have any comment or feedback, please `contact us`_.

|site_name| assigns ARKs followed by ``ark:`` (e.g. ``ark:37281/k5c8w2q9c``)
using the following rules:

* ``37281``: The `NAAN <https://arks.org/about/ark-naans-and-systems/>`_ (Name Assigning Authority Number) registered on `N2T.net <https://n2t.net/ark:37281/>`__ to identify the organization that assigns ARKs.
* ``k5``: The fixed and dedicated sub-namespace (`shoulder <https://www.ietf.org/archive/id/draft-kunze-ark-34.html#name-optional-shoulders>`_ in the ARK) for datasets on the |site_name|.
* A unique identifier (blade in the ARK): The identifier is seven characters long and coded
  using the ``redededk`` `template <https://metacpan.org/dist/Noid/view/noid#TEMPLATES>`_:

  * ``r`` means that the seven-character-long identifier is quasi-randomly generated.
  * ``e`` means that the character is one of the extended digits ``{0123456789bcdfghjkmnpqrstvwxz}``.
  * ``d`` means that the character is one of the pure digits ``{0123456789}``.
  * ``k`` is the final check character.

For the technical specification of the ARK, please refer to the `IETF Internet Draft <https://datatracker.ietf.org/doc/draft-kunze-ark/>`_.

The Criteria for Assigning ARKs
-------------------------------

To ensure that the ARKs are shared broadly and fulfill the metadata requirements,
a public dataset will acquire an ARK identifier if it has the following fields:

* Title
* Start Time and/or End Time
* Creator

.. note::

   * Please refer to :ref:`Metadata <dataset_fields>`.
   * Please also refer to :ref:`editing-a-dataset` to learn more about public and private datasets.
     Make a private dataset public will acquire an ARK identifier, too.
   * If the above fields are removed after an ARK identifier is assigned,
     the ARK identifier will still be active, and its metadata (ERC) will contain the above fields.

Linking to Dataset via ARK
--------------------------

You can get the ARK identifier followed by ``ark:`` and its URL using the ARK Identifier widget in the bottom left corner of the dataset page:

.. image:: /images/ark_1.png
  :width: 300

The ARK URL will lead you to the target dataset.

The Name Mapping Authority (NMA) of |site_name| is https://pid.depositar.io/.
You can also use the NMA provided by `N2T.net <https://n2t.net/>`__,
just replace the https://pid.depositar.io/ part in the URL with https://n2t.net/.

.. note::

   The NMA of the demo system (https://demo.depositar.io/) is https://demo.depositar.io/.
   And there is neither N2T.net support nor a commitment about the persistent access of ARKs for the demo system.

ARK Identifier Metadata (ERC)
-----------------------------

With the ``?info`` inflection appended to the ARK URL, you can get the simple metadata of the identifier.

.. note::

   The metadata is called `Electronic Resource Citation (ERC) <https://n2t.net/ark:/13030/c7sn0141m>`_. |site_name| uses ERC to briefly describe dataset.

The ERC record is a JSON file with the ``erc`` attribute including the following information:

====== ==================== ==============================================
Field  Description          From :ref:`Metadata <dataset_fields>`
====== ==================== ==============================================
what   Title                Title
when   Temporal Information Start Time and End Time (in YYYYMMDD-YYYYMMDD)
where  URL of ARK           N/A (generated automatically)
who    Creator              Creator
====== ==================== ==============================================

Defunct ARK Identifier
----------------------

The ARK identifier will be defunct under the following circumstances:

* Make a public dataset private, then access the ARK URL without read permission of the dataset.
* Remove a dataset, then access the ARK URL without logging in as the creator of the dataset.
* Purge a dataset, then access the ARK URL (only sysadmin has the right to purge a dataset).

You will see the Defunct ARK page as follows:

.. image:: /images/ark_2.png
  :width: 400

For the first two cases aforementioned, the defunct ARK identifier still partially works as follows:

* Make a public dataset private, then access the ARK URL with logging in as user with read permission of the dataset.
* Remove a dataset, then access the ARK URL with logging in as the creator of the dataset.

.. note::

   * If you make the private dataset public or restore the deleted dataset, the defunct ARK identifier will be active again.
   * The metadata (ERC) of the defunct ARK identifier remains available.

Personalization
===============

CKAN provides features to personalize the experience of both searching for and
publishing data. You must be logged in to use these features.

.. _managing_your_news_feed:

Managing your news feed
-----------------------

At the top of any page, select the dashboard symbol (next to your name). CKAN
displays your News feed. This shows changes to datasets that you follow, and
any changed or new datasets in projects that you follow. The number by the
dashboard symbol shows the number of new notifications in your News feed since
you last looked at it. As well as datasets and projects, it is possible to
follow individual users (to be notified of changes that they make to datasets).

.. image:: /images/manage_news_feed.png

If you want to stop following a dataset (or project or user), go to the
dataset's page (e.g. by selecting a link to it in your News feed) and select
the "Unfollow" button.

.. _managing_profile:

Managing your user profile
--------------------------

You can change the information that CKAN holds about you, including what other
users see about you by editing your user profile. (Users are most likely to see
your profile when you edit a dataset or upload data to a project that
they are following.) To do this, select the gearwheel symbol at the top of any
page.

.. image:: /images/manage_user_profile.png

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

* Limitations of XLS/XLSX/CSV files: the field name length must be less than
  or equal to 63 characters (or 21 Chinese characters).
  Merged cells and multiple sheets are not supported.
