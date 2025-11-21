資料集層級
----------

.. list-table::
   :widths: 25 30 45
   :header-rows: 1

   * - 本平台欄位
     - 對應 Data Package 屬性
     - 備註

   * - 標題
     - title
     -

   * - 網址
     - name
     - 匯入 Data Package 時，屬性值僅能為小寫英數字與「-」、「_」符號

   * - 摘要
     - description
     -

   * - 資料類型
     - data_type
     - Data Package 屬性值請參見 :ref:`parse-insight-content-types` 列表之「標記」欄位

   * - Wikidata 關鍵字
     - wd_keywords
     - 參見 :ref:`dp_field_transforms`

   * - 標籤
     - keywords
     -

   * - 語言
     - language
     - `ISO 639-3`_ 語言編碼（三個字母代號）

   * - 備註
     - remarks
     -

   * - 時間解析度
     - temp_res
     - Data Package 屬性值參見以下列表：

       | 年：yearly
       | 月：monthly
       | 日：daily

   * - 起始時間
     - start_time
     -

   * - 結束時間
     - end_time
     -

   * - 空間範圍
     - spatial
     -

   * - 空間範圍.X.min
     - x_min
     -

   * - 空間範圍.X.max
     - x_max
     -

   * - 空間範圍.Y.min
     - y_min
     -

   * - 空間範圍.Y.max
     - y_max
     -

   * - 空間解析度
     - spatial_res
     -

   * - 授權
     - licenses
     - 下載 Data Package 時：將輸出為 ``"licenses": [{"name": "<license_id>", "title": "<license_title>", "path": "<license_url>"}]``

       | 匯入 Data Package 時：請填寫 ``"licenses": [{"name": "<LICNESE_NAME>"}]`` ，LICNESE_NAME 參見以下列表：

       | 授權條款未指定：notspecified
       | `公眾領域 <https://creativecommons.org/publicdomain/mark/1.0/>`_：pd
       | `公眾領域貢獻宣告 1.0 <https://creativecommons.org/publicdomain/zero/1.0/>`_：cc-zero
       | `創用 CC 姓名標示 4.0 <https://creativecommons.org/licenses/by/4.0/>`_：cc-by
       | `創用 CC 姓名標示-相同方式分享 4.0 <https://creativecommons.org/licenses/by-sa/4.0 />`_：cc-by-sa
       | `創用 CC 姓名標示-非商業性-相同方式分享 4.0 <https://creativecommons.org/licenses/ by-nc-sa/4.0/>`_：cc-by-nc-sa
       | `ODC 開放資料庫授權條款 1.0 <https://www.opendefinition.org/licenses/odc-odbl>`_：odc-odbl
       | `GNU 自由文檔許可證 <https://www.opendefinition.org/licenses/gfdl>`_：gfdl
       | `(台灣) 政府資料開放授權條款 <https://data.gov.tw/license>`_：twogd
       | 其他授權：other

   * - 產製者
     - contributors
     - 下載 Data Package 時：將輸出為 ``"contributors": [{"title": "<author>", "roles": ["author"]}]``

       | 匯入 Data Package 時：請填寫 ``"contributors": [{"title": "<CREATOR_NAME>", "roles": ["author"]}]``

   * - 資料產製時間
     - created_time
     -

   * - 資料處理歷程
     - process_step
     -

   * - 專案
     - （無對應）
     - 下載 Data Package 時，不輸出此欄位；匯入 Data Package 時，請於頁面選擇欲匯入專案

   * - 聯絡人
     - contact_person
     -

   * - 聯絡人的電子郵件
     - contact_email
     -

   * - 主題
     - （無對應）
     - 下載 Data Package 時，不輸出此欄位；匯入 Data Package 時，不匯入此欄位

   * - id（內部欄位）
     - ckan:id
     - 資料集 UUID；匯入 Data Package 時，不匯入此欄位

資源層級
--------

.. list-table::
   :widths: 30 30 40
   :header-rows: 1

   * - 本平台欄位
     - 對應 Data Package 屬性
     - 備註

   * - 網址
     - path
     -

   * - 名稱
     - title
     -

   * - 摘要
     - description
     -

   * - 字元編碼
     - encoding
     - Data Package 屬性值參見以下列表：

       | Big5 (繁體中文大五碼)：big5
       | UTF-8：utf-8
       | ISO-8859-1 (西歐字元)：latin1
       | GB2312 (簡體中文)：gb2312
       | GB18030 (簡體中文)：gb18030
       | Shift_JIS (日文)：shift_jis
       | EUC-JP (日文)：euc-jp

   * - 座標參考系統
     - resource_crs
     -

   * - 格式
     - format
     - 參見 :ref:`dp_field_transforms`

   * - id（內部欄位）
     - ckan:id
     - 資源 UUID；匯入 Data Package 時，不匯入此欄位

   * - mediatype（內部欄位）
     - mediatype
     - 媒體型式；匯入 Data Package 時，不匯入此欄位

   * - size（內部欄位）
     - bytes
     - 資源大小；匯入 Data Package 時，不匯入此欄位

.. _ISO 639-3: https://en.wikipedia.org/wiki/List_of_ISO_639-3_codes
