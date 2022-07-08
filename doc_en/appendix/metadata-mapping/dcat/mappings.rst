Dataset Level
-------------

.. list-table::
   :widths: 10 20 20 20 30
   :header-rows: 1

   * - Field
     - Mappings
     - Range
     - Specification
     - Comments

   * - Title
     - dct:title
     - rdfs:Literal
     - :dcat_2:`DCAT 2 <Property:resource_title>`
     -

   * - URL
     - dct:identifier
     - rdfs:Literal
     - :dcat_2:`DCAT 2 <Property:resource_identifier>`
     - 

   * - Description
     - dct:description
     - rdfs:Literal
     - :dcat_2:`DCAT 2 <Property:resource_description>`
     - Markdown syntax removed

   * - Data Type
     - dct:type
     - rdfs:Class
     - :dcat_2:`DCAT 2 <Property:resource_type>`
     - See :ref:`field_transforms`

   * - Wikidata Keywords
     - dcat:theme
     - skos:Concept
     - :dcat_2:`DCAT 2 <Property:resource_theme>`
     - See :ref:`field_transforms`

   * - Tags
     - dcat:keyword
     - rdfs:Literal
     - :dcat_2:`DCAT 2 <Property:resource_keyword>`
     -

   * - Language
     - dct:language
     - dct:LinguisticSystem
     - :dcat_2:`DCAT 2 <Property:resource_language>`
     - See :ref:`field_transforms`

   * - Remarks
     - (No Mapping)
     - (N/A)
     - (N/A)
     - (N/A)

   * - Temporal Resolution
     - dcat:temporalResolution
     - xsd:duration
     - :dcat_2:`DCAT 2 <Property:dataset_temporal_resolution>`
     - See :ref:`field_transforms`

   * - (Field Type: Temporal Information)
     - dct:temporal
     - dct:PeriodOfTime
     - :dcat_2:`DCAT 2 <Property:dataset_temporal>`
     - See :ref:`mappings_child`

       Includes the following fields:

       | Start Time
       | End Time

   * - (Field Type: Spatial Coverage)
     - dct:spatial
     - dct:Location
     - :dcat_2:`DCAT 2 <Property:dataset_spatial>`
     - See :ref:`mappings_child`

       See :ref:`field_transforms`

       Includes the following fields:

       | Spatial Coverage
       | X.min
       | X.max
       | Y.min
       | Y.max

   * - Spatial Resolution
     - dcat:spatialResolutionInMeters
     - xsd:decimal
     - :dcat_2:`DCAT 2 <Property:dataset_spatial_resolution>`
     -

   * - License
     - dct:license
     - dct:LicenseDocument
     - :dcat_2:`DCAT 2 <Property:distribution_license>`
     - See :ref:`field_transforms`

   * - Creator
     - dc:creator
     - rdfs:Literal
     - :dcat_ap_jrc:`DCAT-AP-JRC <dataset-contributor-as-literal>`
     -

   * - Created Time
     - dct:issued
     - rdfs:Literal
     - :dcat_2:`DCAT 2 <Property:resource_release_date>`
     -

   * - Process Step
     - dct:provenance
     - dct:ProvenanceStatement
     - :dcat_ap_jrc:`DCAT-AP-JRC <dataset-lineage>`
     - Markdown syntax removed

   * - (Field Type: Project)
     - dct:publisher
     - foaf:Agent
     - :dcat_2:`DCAT 2 <Property:resource_publisher>`
     - See :ref:`mappings_child`

       Includes the following fields:

       | Name
       | Description

   * - (Field Type: Contact Information)
     - dcat:contactPoint
     - vcard:Kind
     - :dcat_2:`DCAT 2 <Property:resource_contact_point>`
     - See :ref:`mappings_child`

       Includes the following fields:

       | Contact Person
       | Contact Person Ema

   * - Topic
     - dcat:theme
     - skos:Concept
     - :dcat_2:`DCAT 2 <Property:resource_theme>`
     - You should complete the upload process of the dataset before adding a dataset to a topic. See :ref:`adding_a_dataset_to_topic`.

Resource Level
--------------

.. list-table::
   :widths: 10 20 20 20 30
   :header-rows: 1

   * - Field
     - Mappings
     - Range
     - Specification
     - Comments

   * - URL
     - dcat:downloadURL
     - rdfs:Resource
     - :dcat_2:`DCAT 2 <Property:distribution_download_url>`
     -

   * - Name
     - dct:title
     - rdfs:Literal
     - :dcat_2:`DCAT 2 <Property:distribution_title>`
     -

   * - Description
     - dct:description
     - rdfs:Literal
     - :dcat_2:`DCAT 2 <Property:distribution_description>`
     - Markdown syntax removed

   * - Character Encoding
     - cnt:characterEncoding
     - rdfs:Literal
     - :geodcat_ap:`GeoDCAT-AP <page=76>`
     -

   * - Coordinate Systems
     - dct:conformsTo
     - dct:Standard
     - :geodcat_ap:`GeoDCAT-AP <page=73>`
     - See :ref:`field_transforms`

   * - Format
     - dcat:mediaType
     - dct:MediaTypeOrExtent
     - :dcat_2:`DCAT 2 <Property:distribution_media_type>`
     - See :ref:`field_transforms`
