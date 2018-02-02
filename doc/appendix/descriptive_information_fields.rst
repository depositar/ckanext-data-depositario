.. list-table::
   :widths: 14 14 14 14 14 14
   :header-rows: 1

   * - 欄位名稱
     - 說明
     - 必填 M / 選填 O
     - 最多發生次數
     - 資料型別
     - 校驗（轉換）器/值域定義

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

.. [#] 本平台之關鍵字來自 Wikidata （維基資料）條目，並支援該平台之多語系名稱，意即無論在中文或英文語系下新增關鍵字，瀏覽時均會根據網站語系設定顯示對應之翻譯。您並可快速自 Wikidata 找尋符合條件之條目作為關鍵字，如下圖所示。
.. image:: /images/keyword_wikidata.png
.. [#] 當無法自 Wikidata 尋得合適條目作為關鍵字時使用時，請將該關鍵字填寫於「標籤」欄位。
.. [#] 當資料集之「資料類型」欄位為「文獻書籍」類時，系統介面將進一步顯示對應之細節描述項目。
.. [#] 當資料集之「資料類型」欄位為「圖像」類時，系統介面將進一步顯示對應之細節描述項目。
