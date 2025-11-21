============
Data Package
============

`Data Package`_ is a standard to describe datasets and data files, developed by Open Knowledge Foundation.
Via the `ckanext-datapackager`_ extension, |site_name| allows users to download and upload a ``Data Package``, which is a zip archive consisting of the following files:

* A ``datapackage.json`` descriptor that describes the dataset and resources. The descriptor is defined in the :doc:`../appendix/datapackage/index`.
* One or more data resources

.. note::

    This feature is a work in process. If you have any comment or feedback, please `contact us`_.

Features
--------

Download the dataset as a Data Package
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can obtain the latest version of the Data Package for the dataset from the “Download Data Package” in the upper right corner of the dataset page:

.. image:: /images/datapackage/datapackage_1.png
    :width: 700

Import the Data Package as a dataset
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

----------------------
Prepare a Data Package
----------------------

#. Write a ``datapackage.json`` descriptor according to the :doc:`Metadata Mapping <../appendix/metadata-mapping/datapackage/index>` and the following example:

.. dropdown:: Example: A complete ``datapackage.json`` including all properties (click to expand)
    :color: primary
    :icon: file-code

    .. code-block:: json

        {
          "resources": [
            {
              "name": "resource_1",
              "path": "http://example.com",
              "title": "Resource 1",
              "description": "A longer description of the resource.",
              "encoding": "utf-8",
              "resource_crs": "4326",
              "format": "HTML"
            }
          ],
          "title": "Sample Dataset",
          "name": "sample-dataset",
          "description": "A longer description of the dataset.",
          "data_type": [
            "other"
          ],
          "wd_keywords": [
            "http://www.wikidata.org/entity/Q484000"
          ],
          "keywords": [
            "free_keyword_1",
            "free_keyword_2"
          ],
          "language": ["eng"],
          "remarks": "Some supplementary information for the dataset.",
          "temp_res": "daily",
          "start_time": "2024-01-01",
          "end_time": "2025-01-01",
          "spatial": {"type": "Polygon", "coordinates": [[[120.01,22.96], [120.01,23.12], [120.23,23.12], [120.23,22.96], [120.01,22.96]]]},
          "x_min": "120.01",
          "x_max": "120.23",
          "y_min": "22.96",
          "y_max": "23.12",
          "spatial_res": "1.0",
          "licenses": [
            {
              "name": "notspecified"
            }
          ],
          "contributors": [
            {
              "title": "Creator Name",
              "roles": [
                "author"
              ]
            }
          ],
          "process_step": "Steps of data generating process.",
          "contact_person": "Joe Bloggs",
          "contact_email": "joe@example.com"
        }

.. dropdown:: Example: A simple ``datapackage.json`` for import (click to expand)
    :color: primary
    :icon: file-code

    .. code-block:: json

        {
          "resources": [
            {
              "name": "resource_1",
              "path": "http://example.com"
            }
          ],
          "name": "sample-dataset",
          "title": "Sample Dataset",
          "licenses": [
            {
              "name": "notspecified"
            }
          ],
          "contributors": [
            {
              "title": "Creator Name",
              "roles": [
                "author"
              ]
            }
          ],
          "data_type": [
            "other"
          ]
        }

2. If you want to upload the data file(s) to |site_name|,
   please compress the data file(s) and ``datapackage.json`` into a single zip file.
   Note that the data file(s) must still adhere to the :doc:`limitation`.

.. note::
    * The ``datapackage.json`` must be placed in the top-level directory of the zip file.
    * The ``datapackage.json`` is a JSON file; you can author it using any text editor (e.g., Visual Studio Code) or an online tool like `JSON Editor Online`_.
    * If you want to upload the data file(s) to |site_name|, please specify the path
      of each data file relative to the top-level directory within the ``path`` attribute
      of each resource found in the ``resources`` property of ``datapackage.json``.
    * Required properties: ``resources``, ``name``, ``licenses``, ``contributors``, and ``data_type``

-----------------------
Import the Data Package
-----------------------

#. You can access the “Import Data Package” page in two ways:

.. grid:: 2

    .. grid-item-card:: Select the “Datasets” link at the top of any page

        From this, above the search box, select the “Import Data Package” button.

    .. grid-item-card:: Select the “Projects” link at the top of any page

        Then select the page for the project that should own your new dataset.
        Provided that you are a member of this project,
        you can now select the “Import Data Package” button above the search box.

2. Select the project that should own your new dataset, decide the visibility (Private/Public) of the dataset, then upload the Data Package:

.. grid:: 2

    .. grid-item-card:: If the Data Package contains no data files

        Upload the ``datapackage.json`` in the “Import Data Package” page.

    .. grid-item-card:: If the Data Package contains data file(s)

        Upload the zip file in the “Import Data Package” page.

.. image:: /images/datapackage/datapackage_2.png
    :width: 700

.. note::

    If the fields converted from the Data Package properties exceed the ranges
    listed in the :doc:`../appendix/fields/index`, the import will be terminated
    and an error will displayed.

Automatic Data Package Generation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When a dataset is created or edited, and the total size of the resources in the dataset
is 50 MB or less, a Data Package will be generated automatically and uploaded as a resource for the dataset:

* The file name of the Data Package is fixed as ``datapackage.zip``
* The Data Package resource is **NOT LISTED** in the resource list on the dataset page and the edit dataset page
* The Data Package resource is **LISTED** in the API results, :doc:`rdf-serializations`, and :doc:`binder`. You need to exclude the Data Package resource when calculating the resource count via the API.
* The Data Package resource only includes data files uploaded to |site_name|. External URLs will only be listed in the ``datapackage.json``, and any resource without a URL will not be included.
* The Data Package resource will not be updated (and the existing one will be deleted)
  if the dataset's total resource size exceeds 50 MB after editing,
  or if all resources lack a URL.

.. note::

    Automatic Data Package generation is a background task.
    If the “Download Data Package” button does not appear,
    please ensure the above conditions are met and refresh the dataset page.

API Methods
~~~~~~~~~~~

-----------------------
Update the Data Package
-----------------------

To update the Data Package, run the command below:

.. code-block:: bash

    curl -X POST \
         -H 'Authorization: YOUR_API_TOKEN' \
         -d '{"id": "DATASET_ID"}' \
         https://data.depositar.io/api/action/datapackage_update

.. note::

    * The Data Package will be generated automatically when the dataset is created or edited, and generally does not require manual updating.
    * The dataset must include at least one resource with URL, and the dataset's total resource size must be 50 MB or less.
    * Please refer to the :doc:`data-api` to get an API token.

-----------------------
Import the Data Package
-----------------------

To import a Data Package as a |site_name| dataset, run the commands below:

For uploading a local Data Package:

.. code-block:: bash

    curl -X POST \
         -H 'Authorization: YOUR_API_TOKEN' \
         -F 'owner_org=project_id' \
         -F 'upload=@/path/to/datapackage.json/or/file.zip' \
         https://data.depositar.io/api/action/package_create_from_datapackage

For uploading a remote Data Package:

.. code-block:: bash

    curl -X POST \
         -H 'Authorization: YOUR_API_TOKEN' \
         -d '{"url": "https://link.to/datapackage.json", "owner_org": project_id}' \
         https://data.depositar.io/api/action/package_create_from_datapackage

.. _Data Package: https://datapackage.org/
.. _ckanext-datapackager: https://github.com/depositar/ckanext-datapackager
.. _JSON Schema: https://json-schema.org/
.. _JSON Editor Online: https://jsoneditoronline.org/
