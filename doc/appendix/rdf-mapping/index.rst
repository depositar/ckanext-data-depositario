=========================
後設資料與 RDF 語彙之對應
=========================

RDF 輸出用。

經由 ckanext-dcat 提供支援。

實作參考：(GitHub custom profile 網址)

------------
使用命名空間
------------

.. list-table::
   :widths: 15 65 20
   :header-rows: 1

   * - 前綴
     - 命名空間 URI
     - 文件連結

   * - dct
     - http://purl.org/dc/terms/
     - [DCTERMS_]

   * - foaf
     - http://xmlns.com/foaf/0.1/
     - [FOAF_]

.. _DCTERMS: http://dublincore.org/documents/dcmi-terms/
.. _FOAF: http://xmlns.com/foaf/spec

--------
欄位對應
--------

.. include:: mapping_table.rst

----------
子欄位對應
----------

.. include:: mapping_table_child.rst

--------
格式轉換
--------

.. list-table::
   :widths: 5 45 5 45
   :header-rows: 1

   * - 欄位
     - URI 前綴
     - 原始值範例
     - 轉換值範例

   * - 空間範圍.(X.min, X.max, Y.min, Y.max)
     -
     - (116.658, 122.134, 20.653, 26.407)
     - 20.653 116.658 26.407 122.134

   * - 座標參考系統
     - http://www.opengis.net/def/crs/EPSG/0/
     - 3826
     - http://www.opengis.net/def/crs/EPSG/0/3826

   * - 格式
     - https://www.iana.org/assignments/media-types/
     - text/csv
     - https://www.iana.org/assignments/media-types/text/csv
