資料集層級
----------

.. list-table::
   :widths: 10 15 20 15 20 20
   :header-rows: 1

   * - 欄位
     - 識別碼類型 / 綱要
     - URI 前綴
     - 原始值範例
     - 轉換值範例
     - 備註

   * - 資料類型
     - :ref:`parse-insight-content-types`
     - http://registry.it.csiro.au/def/re3data/contentType/_
     - 辦公軟體文件 (內部值：doc)
     - http://registry.it.csiro.au/def/re3data/contentType/_doc
     - 內部值請參考 :ref:`parse-insight-content-types` 表格之「標記」欄位

   * - Wikidata 關鍵字
     - `Wikidata 項目 <https://www.wikidata.org/wiki/Help:Items>`_
     - http://www.wikidata.org/entity/
     - 無人航空載具 (內部值：Q484000)
     - http://www.wikidata.org/entity/Q484000
     - 內部值即 Wikidata QID

   * - 語言
     - `ISO 639-3 <https://zh.wikipedia.org/wiki/ISO_639-3>`_
     - http://www.lexvo.org/page/iso639-3/
     - 中文 (zho)
     - http://www.lexvo.org/page/iso639-3/zho
     - 參見 `相關討論 <https://github.com/dcmi/usage/issues/22>`_

   * - 時間解析度
     - (不適用)
     - (不適用)
     - | 年
       | 月
       | 日
     - | P1Y
       | P1M
       | P1D
     - 參考 `DCAT 2 <https://www.w3.org/TR/vocab-dcat-2/#temporal-properties>`_

   * - | 空間範圍.X.min
       | 空間範圍.X.max
       | 空間範圍.Y.min
       | 空間範圍.Y.max
     - (不適用)
     - (不適用)
     - | (X.min, X.max, Y.min, Y.max) =
       | (116.658, 122.134, 20.653, 26.407)
     - 20.653 116.658 26.407 122.134
     - 參考 public-vocabs@w3.org 郵件群組之 `討論 <https://lists.w3.org/Archives/Public/public-vocabs/2012Jun/0116.html>`_

   * - 授權
     - (不適用)
     - (不適用)
     - 創用 CC 姓名標示 4.0
     - https://creativecommons.org/licenses/by/4.0/
     - 授權與對應網址請參考此 :site_url:`JSON 檔案 <license_list.json>` 之 url 欄位

資源層級
--------

.. list-table::
   :widths: 10 15 20 15 20 20
   :header-rows: 1

   * - 欄位
     - 識別碼類型 / 綱要
     - URI 前綴
     - 原始值範例
     - 轉換值範例
     - 備註

   * - 座標參考系統
     - `EPSG 代號 <https://en.wikipedia.org/wiki/EPSG_Geodetic_Parameter_Dataset>`_
     - http://www.opengis.net/def/crs/EPSG/0/
     - 3826
     - http://www.opengis.net/def/crs/EPSG/0/3826
     - 參考 `GeoDCAT-AP <https://joinup.ec.europa.eu/sites/default/files/distribution/2016-08/geodcat-ap_v1.0.1.pdf#page=73>`_

   * - 格式
     - `網際網路媒體類型 <https://zh.wikipedia.org/wiki/%E4%BA%92%E8%81%94%E7%BD%91%E5%AA%92%E4%BD%93%E7%B1%BB%E5%9E%8B>`_
     - https://www.iana.org/assignments/media-types/
     - text/csv
     - https://www.iana.org/assignments/media-types/text/csv
     - 原始值將於上傳檔案至本平台後自動產生 (暫不支援外部連結)
