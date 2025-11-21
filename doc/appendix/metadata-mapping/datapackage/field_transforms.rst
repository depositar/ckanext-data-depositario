資料集層級
----------

.. list-table::
   :header-rows: 1

   * - 本平台欄位
     - 欄位值範例
     - 對應 Data Package 屬性
     - 屬性值範例
     - 備註

   * - Wikidata 關鍵字
     - Q484000
     - wd_keywords
     - http://www.wikidata.org/entity/Q484000
     - Wikidata QID

   * - metadata_created（內部欄位）
     - 2000-01-01T11:00:00.123456
     - created
     - 2000-01-01T11:00:00.123456+08:00（加入時區）
     - 資料集建立時間；匯入 Data Package 時，不匯入此欄位

   * - （無）
     - （無）
     - id
     - ``https://n2t.net/ark:37281/<blade>`` （ARK 網址）
     - 新增屬性（僅於下載 Data Package 時且資料集獲得 :doc:`../../../user-guide/ark-identifier` 時）

   * - （無）
     - （無）
     - sources
     - JSON: ``[{"email": "data.contact@depositar.io", "path": "<資料集網址或 ARK 網址>", "title": "研究資料寄存所 | depositar"}]``
     - 新增屬性（僅於下載 Data Package 時）

資源層級
--------

.. list-table::
   :widths: 20 15 30 20 15
   :header-rows: 1

   * - 本平台欄位
     - 欄位值範例
     - 對應 Data Package 屬性
     - 屬性值範例
     - 備註

   * - （無）
     - （無）
     - name
     - resource_N，N 為自 1 開始之編號 (1, 2, …)
     - 新增屬性（僅於下載 Data Package 時）

   * - 格式
     - PDF
     - format
     - pdf
     - 下載 Data Package 時，將轉為小寫；匯入 Data Package 時，將轉為大寫
