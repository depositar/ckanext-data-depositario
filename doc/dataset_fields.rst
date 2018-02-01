.. list-table::
   :widths: 14 14 14 14 14 14
   :header-rows: 1

   * - 欄位名稱
     - 說明
     - 必填M/選填O
     - 最多發生次數
     - 資料型別 [#]_
     - 校驗（轉換）器/值域定義 [#]_

   * - **基本資訊**
     -
     -
     -
     -
     -

   * - 標題
     - 建議以簡單扼要的方式描述，如「英國各區域之人口密度」較「人口統計圖表」來的具識別性
     - O
     - 1
     - gco:CharacterString
     - :ref:`if_empty_same_as(name) <external_validators>` :ref:`unicode <external_validators>` 

   * - 網址 [#]_
     - 網址為CKAN資料集唯一的識別碼，僅能為英數字及部分符號
     - M
     - 1
     - gco:CharacterString
     - :ref:`not_empty <external_validators>` :ref:`unicode <external_validators>` :ref:`package_name_validator <external_validators>`

   * - 摘要
     - 記錄關於此資料集的細節內容，或是任何其他使用者可以進一步了解本資料集的資訊
     - O
     - 1
     - gco:CharacterString
     -

   * - 資料類型
     - 資料集所屬之類型，依據不同類型將顯示不同詮釋資料填寫項目
     - M
     - 1
     - Data_type
     - :ref:`scheming_required <external_validators>` :ref:`scheming_choices <external_validators>`

   * - 標籤 [#]_
     - 標籤欄位可協助使用者更容易找到該筆資料集，例如您可加上「人口」、「犯罪」標籤
     - O
     - N
     - gco:CharacterString
     - :ref:`ignore_missing <external_validators>` :ref:`tag_string_convert <external_validators>`

   * - 備註
     - 描述資料集的額外資訊
     - O
     - 1
     - gco:CharacterString
     -

   * - **描述資訊**
     -
     -
     -
     -
     -

   * - 語言
     - 本項目說明資料集內容所使用之語言，如歷史文獻可能為華語、日語、西班牙語系等
     - O
     - 1
     - Language_type
     - :ref:`scheming_required <external_validators>` :ref:`scheming_choices <external_validators>`

   * - 時間解析度
     - 請參考 :ref:`時間資訊填寫輔助功能 <UI_editing_extend_time>`
     - O
     - 1
     - Temp_res_type
     - :ref:`scheming_required <external_validators>` :ref:`scheming_choices <external_validators>`

   * - 起始時間
     - 請參考 :ref:`時間資訊填寫輔助功能 <UI_editing_extend_time>`
     - O
     - 1
     - gco:Date
     - :ref:`ignore_empty <external_validators>` :ref:`temp_res_validator <internal_validators>`

   * - 結束時間
     - 請參考 :ref:`時間資訊填寫輔助功能 <UI_editing_extend_time>`
     - O
     - 1
     - gco:Date
     - :ref:`ignore_empty <external_validators>` :ref:`temp_res_validator <internal_validators>`

   * - 空間範圍
     - 請參考 :ref:`空間範圍填寫輔助功能 <UI_editing_extend_spatial>`
     - O
     - 1
     - GeoJSON
     - :ref:`ignore_empty <external_validators>` :ref:`json_validator <internal_validators>` :ref:`remove_blank_wrap <internal_validators>`

   * - 空間範圍.X.min
     - 請參考 :ref:`空間範圍填寫輔助功能 <UI_editing_extend_spatial>`
     - O
     - 1
     - gco:Decimal
     - :ref:`ignore_empty <external_validators>` :ref:`long_validator <internal_validators>`

   * - 空間範圍.X.max
     - 請參考 :ref:`空間範圍填寫輔助功能 <UI_editing_extend_spatial>`
     - O
     - 1
     - gco:Decimal
     - :ref:`ignore_empty <external_validators>` :ref:`long_validator <internal_validators>`

   * - 空間範圍.Y.min
     - 請參考 :ref:`空間範圍填寫輔助功能 <UI_editing_extend_spatial>`
     - O
     - 1
     - gco:Decimal
     - :ref:`ignore_empty <external_validators>` :ref:`lat_validator <internal_validators>`

   * - 空間範圍.Y.max
     - 請參考 :ref:`空間範圍填寫輔助功能 <UI_editing_extend_spatial>`
     - O
     - 1
     - gco:Decimal
     - :ref:`ignore_empty <external_validators>` :ref:`lat_validator <internal_validators>`

   * - 關鍵字 [#]_ [#]_
     - 用以描述資料集內容的簡短詞語
     - O
     - N
     - gco:CharacterString
     - :ref:`wikidata_keyword <external_validators>`

   * - **文獻書籍** [#]_
     -
     -
     -
     -
     -

   * - ISBN-13
     -
     - O
     - 1
     - gco:CharacterString
     -

   * - ISSN
     -
     - O
     - 1
     - gco:CharacterString
     -

   * - 期刊
     -
     - O
     - 1
     - gco:CharacterString
     -

   * - 卷期
     -
     - O
     - 1
     - gco:CharacterString
     -

   * - 論文集名稱
     -
     - O
     - 1
     - gco:CharacterString
     -

   * - 出版地
     -
     - O
     - 1
     - gco:CharacterString
     -

   * - 出版單位
     -
     - O
     - 1
     - gco:CharacterString
     -

   * - 出版年
     -
     - O
     - 1
     - gco:CharacterString
     -

   * - 書目查詢
     -
     - O
     - 1
     - gco:CharacterString
     -

   * - 網址
     -
     - O
     - 1
     - gco:CharacterString
     -

   * - 使用史料
     -
     - O
     - N
     - Hist_material_type
     - :ref:`scheming_multiple_choice <external_validators>`

   * - 研究區的聚落名
     -
     - O
     - 1
     - gco:CharacterString
     -

   * - 研究區的宗教
     -
     - O
     - 1
     - gco:CharacterString
     -

   * - 研究區的家族
     -
     - O
     - 1
     - gco:CharacterString
     -

   * - 研究區的埤圳
     -
     - O
     - 1
     - gco:CharacterString
     -

   * - 研究區的特殊產業
     -
     - O
     - 1
     - gco:CharacterString
     -

   * - 備註
     -
     - O
     - 1
     - gco:CharacterString
     -

   * - **圖像** [#]_
     -
     -
     -
     -
     -

   * - 掃描原件來源
     -
     - O
     - 1
     - gco:CharacterString
     -

   * - 掃描原件尺寸
     - 填寫原件尺寸大小，單位為公分，如 60x72
     - O
     - 1
     - gco:CharacterString
     -

   * - 掃描解析度
     - 填寫掃描解析度數值，單位為 DPI，如 300
     - O
     - 1
     - gco:Integer
     - :ref:`ignore_empty <external_validators>` :ref:`is_positive_integer <external_validators>`

   * - 空間解析度
     - 填寫資料空間解析度數值，以公尺為單位
     - O
     - 1
     - gco:CharacterString
     - :ref:`ignore_empty <external_validators>` :ref:`positive_float_validator <internal_validators>`

   * - 比例尺
     - 填寫資料比例尺之分母
     - O
     - 1
     - gco:Integer
     - :ref:`ignore_empty <external_validators>` :ref:`is_positive_integer <external_validators>`

   * - 資料處理歷程
     - 以文字描述資料形成所經過之處理過程，建議以各階段或步驟為導向進行填寫
     - O
     - 1
     - gco:CharacterString
     -

   * - **管理資訊**
     -
     -
     -
     -
     -

   * - 授權 [#]_
     - 宣告資料集之使用授權方式，提供後續使用者應用該筆資料之參考
     - M
     - 1
     - License_code
     -

   * - 產製者
     - 資料生產者或單位的名稱
     - M
     - 1
     - gco:CharacterString
     -

   * - 資料產置時間
     - 資料集檔案產出時間
     - O
     - 1
     - gco:Date
     - :ref:`ignore_empty <external_validators>` :ref:`date_validator <internal_validators>`

   * - 組織 [#]_ [#]_
     - 若您屬於任一組織內之成員，則您可於組織欄位之下拉選單內找到您所屬的組織清單
     - O
     - 1
     - gco:CharacterString
     - :ref:`owner_org_validator <external_validators>` :ref:`unicode <external_validators>`

   * - 維護者
     - 負責維護資料集檔案之人員或單位
     - O
     - 1
     - gco:CharacterString
     -

   * - 維護者的電子郵件
     - 資料權責者（單位）之電子郵件信箱
     - O
     - 1
     - gco:CharacterString
     -

   * - 維護者的聯絡電話
     - 資料權責者（單位）之聯絡電話
     - O
     - 1
     - gco:CharacterString
     - 

   * - 識別碼
     - 資料集位於來源資料庫時所帶有之唯一識別碼
     - O
     - 1
     - gco:CharacterString
     -

.. [#] 關於個別資料型別的說明請見附錄 :doc:`appendix/data_type`。
.. [#] CKAN具有校驗器（validator）機制，用以檢查欄位是否符合規定，故亦可視為值域。另有轉換器（converter），用以轉換欄位值俾符合規定。
.. [#] 網址會在您輸入資料集標題時自動產生。若標題內含有英數字（及部分符號），則產生之網址為該英數字（同時去除所有非英數字之文字）；若標題不含英數字，則系統會為您產生一組隨機英數字。您可隨時修改自動產生之網址。
.. [#] 請僅於無法自Wikidata尋得合適條目填入「關鍵字」欄位時使用此欄位。
.. [#] 類似「標籤」欄位，不同之處在於本平台之關鍵字來自維基數據（Wikidata）條目，並支援該平台之多語系名稱，意即無論在中文或英文語系下新增關鍵字，瀏覽時均會根據網站語系設定顯示對應之翻譯。 您並可快速自Wikidata找尋符合條件之條目作為關鍵字，如下圖所示。
.. image:: /images/keyword_wikidata.png
.. [#] 當無法自Wikidata尋得合適條目作為關鍵字時使用時，請將該關鍵字填寫於「標籤」欄位。
.. [#] 當資料集之「資料類型」欄位為「文獻書籍」類時，系統介面將進一步顯示對應之細節描述項目。
.. [#] 當資料集之「資料類型」欄位為「圖像」類時，系統介面將進一步顯示對應之細節描述項目。
.. [#] 若資料集釋出之授權不在候選清單內，請選擇「Other Licenses」，並於「備註」欄位註明授權條款。
.. [#] 若選擇「沒有此組織」選項，此資料集將不屬於任何組織，且將會被強制設定為「公開」資料集。
.. [#] 欄位下方之「只對組織內成員公開」核取方塊（如下圖）被選中時，非屬於選定組織之成員即無法瀏覽該資料集（即「非公開」狀態），反之則對任何使用者公開該資料集。
.. image:: /images/add_dataset_3.png
