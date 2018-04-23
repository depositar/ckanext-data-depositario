.. list-table::
   :widths: 14 14 14 14 14 14
   :header-rows: 1

   * - 欄位名稱
     - 說明
     - 必填 M / 選填 O
     - 最多發生次數
     - 資料型別 [#]_
     - 校驗（轉換）器/值域定義 [#]_

   * - 標題
     - 建議以簡單扼要的方式描述，如「台灣各縣市之人口密度」較「人口統計圖表」來的具識別性
     - O
     - 1
     - gco:CharacterString
     - :ref:`if_empty_same_as(name) <external_validators>` :ref:`unicode <external_validators>` 

   * - 網址 [#]_
     - 網址為本平台上資料集唯一的識別碼，僅能為英數字及部分符號
     - M
     - 1
     - gco:CharacterString
     - :ref:`not_empty <external_validators>` :ref:`unicode <external_validators>` :ref:`package_name_validator <external_validators>`

   * - 摘要
     - 記錄關於此資料集的細節內容，或是任何其他使用者可以進一步了解此資料集的資訊
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
     - 標籤欄位可協助使用者更容易找到該筆資料集，例如您可加上「人口」、「犯罪」等標籤
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

.. [#] 關於個別資料型別的說明請見附錄 :doc:`data_type`。
.. [#] CKAN 軟體套件具有校驗器 (validator) 機制，用以檢查欄位是否符合規定，故亦可視為值域。另有轉換器(converter)，用以轉換欄位值俾符合規定。
.. [#] 網址會在您輸入資料集標題時自動產生。若標題內含有英數字（及部分符號），則產生之網址為該英數字（同時去除所有非英數字之文字）；若標題不含英數字，則系統會為您產生一組隨機英數字。您可隨時修改自動產生之網址。
.. [#] 若無法自 Wikidata 尋得合適條目填入「關鍵字」欄位時，始建議使用此「標籤」欄位。
