資料集層級
----------

.. list-table::
   :widths: 10 20 20 20 30
   :header-rows: 1

   * - 欄位
     - 對應語彙
     - 範圍
     - 規範
     - 備註

   * - 標題
     - dct:title
     - rdfs:Literal
     - :dcat_2:`DCAT 2 <Property:resource_title>`
     -

   * - 網址
     - dct:identifier
     - rdfs:Literal
     - :dcat_2:`DCAT 2 <Property:resource_identifier>`
     - 

   * - 摘要
     - dct:description
     - rdfs:Literal
     - :dcat_2:`DCAT 2 <Property:resource_description>`
     - 將去除 Markdown 標記

   * - 資料類型
     - dct:type
     - rdfs:Class
     - :dcat_2:`DCAT 2 <Property:resource_type>`
     - 參見 :ref:`field_transforms`

   * - Wikidata 關鍵字
     - dcat:theme
     - skos:Concept
     - :dcat_2:`DCAT 2 <Property:resource_theme>`
     - 參見 :ref:`field_transforms`

   * - 標籤
     - dcat:keyword
     - rdfs:Literal
     - :dcat_2:`DCAT 2 <Property:resource_keyword>`
     -

   * - 語言
     - dct:language
     - dct:LinguisticSystem
     - :dcat_2:`DCAT 2 <Property:resource_language>`
     - 參見 :ref:`field_transforms`

   * - 備註
     - (無對應)
     - (不適用)
     - (不適用)
     - (不適用)

   * - 時間解析度
     - dcat:temporalResolution
     - xsd:duration
     - :dcat_2:`DCAT 2 <Property:dataset_temporal_resolution>`
     - 參見 :ref:`field_transforms`

   * - (時間資訊類型)
     - dct:temporal
     - dct:PeriodOfTime
     - :dcat_2:`DCAT 2 <Property:dataset_temporal>`
     - 參見 :ref:`mappings_child`

       包括以下欄位：

       | 起始時間
       | 結束時間

   * - (空間範圍類型)
     - dct:spatial
     - dct:Location
     - :dcat_2:`DCAT 2 <Property:dataset_spatial>`
     - 參見 :ref:`mappings_child`

       參見 :ref:`field_transforms`

       包括以下欄位：

       | 空間範圍
       | 空間範圍.X.min
       | 空間範圍.X.max
       | 空間範圍.Y.min
       | 空間範圍.Y.max

   * - 空間解析度
     - dcat:spatialResolutionInMeters
     - xsd:decimal
     - :dcat_2:`DCAT 2 <Property:dataset_spatial_resolution>`
     -

   * - 授權
     - dct:license
     - dct:LicenseDocument
     - :dcat_2:`DCAT 2 <Property:distribution_license>`
     - 參見 :ref:`field_transforms`

   * - 產製者
     - dc:creator
     - rdfs:Literal
     - :dcat_ap_jrc:`DCAT-AP-JRC <dataset-contributor-as-literal>`
     -

   * - 資料產製時間
     - dct:issued
     - rdfs:Literal
     - :dcat_2:`DCAT 2 <Property:resource_release_date>`
     -

   * - 資料處理歷程
     - dct:provenance
     - dct:ProvenanceStatement
     - :dcat_ap_jrc:`DCAT-AP-JRC <dataset-lineage>`
     - 將去除 Markdown 標記

   * - (專案類型)
     - dct:publisher
     - foaf:Agent
     - :dcat_2:`DCAT 2 <Property:resource_publisher>`
     - 參見 :ref:`mappings_child`

       包括以下欄位：

       | 名稱
       | 描述

   * - (聯絡資訊類型)
     - dcat:contactPoint
     - vcard:Kind
     - :dcat_2:`DCAT 2 <Property:resource_contact_point>`
     - 參見 :ref:`mappings_child`

       包括以下欄位：

       | 聯絡人
       | 聯絡人的電子郵件

   * - 主題
     - dcat:theme
     - skos:Concept
     - :dcat_2:`DCAT 2 <Property:resource_theme>`
     - 需於建立資料集後進行編輯，參見 :ref:`adding_a_dataset_to_topic`

資源層級
--------

.. list-table::
   :widths: 10 20 20 20 30
   :header-rows: 1

   * - 欄位
     - 對應語彙
     - 範圍
     - 規範
     - 備註

   * - 網址 
     - dcat:downloadURL
     - rdfs:Resource
     - :dcat_2:`DCAT 2 <Property:distribution_download_url>`
     -

   * - 名稱
     - dct:title
     - rdfs:Literal
     - :dcat_2:`DCAT 2 <Property:distribution_title>`
     -

   * - 摘要
     - dct:description
     - rdfs:Literal
     - :dcat_2:`DCAT 2 <Property:distribution_description>`
     - 將去除 Markdown 標記

   * - 字元編碼
     - cnt:characterEncoding
     - rdfs:Literal
     - :geodcat_ap:`GeoDCAT-AP <page=76>`
     -

   * - 座標參考系統
     - dct:conformsTo
     - dct:Standard
     - :geodcat_ap:`GeoDCAT-AP <page=73>`
     - 參見 :ref:`field_transforms`

   * - 格式
     - dcat:mediaType
     - dct:MediaTypeOrExtent
     - :dcat_2:`DCAT 2 <Property:distribution_media_type>`
     - 參見 :ref:`field_transforms`
