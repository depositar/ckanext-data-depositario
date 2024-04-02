RDF Serializations
==================

|site_name| uses `RDF serializer <https://github.com/ckan/ckanext-dcat/tree/v1.1.0#rdf-dcat-serializer>`_ provided by ckanext-dcat to expose RDF graph.

For the alignments of the metadata of |site_name| and RDF vocabularies, please refer to :doc:`../appendix/metadata-mapping/dcat/index`.

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
