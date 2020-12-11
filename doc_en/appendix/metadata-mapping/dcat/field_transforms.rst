Dataset Level
-------------

.. list-table::
   :widths: 10 15 20 15 20 20
   :header-rows: 1

   * - Field
     - Identifier Type / Scheme
     - URI Prefix
     - Example (Original)
     - Example (Transformed)
     - Comments

   * - Data Type
     - :ref:`parse-insight-content-types`
     - http://registry.it.csiro.au/def/re3data/contentType/_
     - Standard office documents (internal value: doc)
     - http://registry.it.csiro.au/def/re3data/contentType/_doc
     - For internal values, please refer to the notation field in :ref:`parse-insight-content-types`.

   * - Wikidata Keywords
     - `Wikidata items <https://www.wikidata.org/wiki/Help:Items>`_
     - http://www.wikidata.org/entity/
     - unmanned aerial vehicle (internal value: Q484000)
     - http://www.wikidata.org/entity/Q484000
     - Internal value is the Wikidata QID.

   * - Language
     - `ISO 639-3 <https://zh.wikipedia.org/wiki/ISO_639-3>`_
     - http://www.lexvo.org/page/iso639-3/
     - Chinese (zho)
     - http://www.lexvo.org/page/iso639-3/zho
     - See the `related discussion <https://github.com/dcmi/usage/issues/22>`_.

   * - Temporal Resolution
     - (N/A)
     - (N/A)
     - | Yearly
       | Monthly
       | Daily
     - | P1Y
       | P1M
       | P1D
     - According to `DCAT 2 <https://www.w3.org/TR/vocab-dcat-2/#temporal-properties>`_.

   * - | X.min
       | X.max
       | Y.min
       | Y.max
     - (N/A)
     - (N/A)
     - | (X.min, X.max, Y.min, Y.max) =
       | (116.658, 122.134, 20.653, 26.407)
     - 20.653 116.658 26.407 122.134
     - According to the `discussion thread <https://lists.w3.org/Archives/Public/public-vocabs/2012Jun/0116.html>`_ from public-vocabs@w3.org.

   * - License
     - (N/A)
     - (N/A)
     - CC-BY 4.0
     - https://creativecommons.org/licenses/by/4.0/
     - For licenses and their urls, please refer to the url field in this :site_url:`JSON file <license_list.json>`.

Resource Level
--------------

.. list-table::
   :widths: 10 15 20 15 20 20
   :header-rows: 1

   * - Field
     - Identifier Type / Scheme
     - URI Prefix
     - Example (Original)
     - Example (Transformed)
     - Comments

   * - Coordinate Systems
     - `EPSG code <https://en.wikipedia.org/wiki/EPSG_Geodetic_Parameter_Dataset>`_
     - http://www.opengis.net/def/crs/EPSG/0/
     - 3826
     - http://www.opengis.net/def/crs/EPSG/0/3826
     - According to `GeoDCAT-AP <https://joinup.ec.europa.eu/sites/default/files/distribution/2016-08/geodcat-ap_v1.0.1.pdf#page=73>`_.

   * - Format
     - `Media type <https://en.wikipedia.org/wiki/Media_type>`_
     - https://www.iana.org/assignments/media-types/
     - text/csv
     - https://www.iana.org/assignments/media-types/text/csv
     - The original value is generated automatically against each resource as it is uploaded. External resources are not supported at the moment.
