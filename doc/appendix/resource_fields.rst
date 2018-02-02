======================
資源層級之詮釋資料項目
======================

.. list-table::
   :widths: 14 14 14 14 14 14
   :header-rows: 1

   * - 欄位名稱
     - 說明
     - 必填 M / 選填 O
     - 最多發生次數
     - 資料型別 [#]_
     - 校驗（轉換）器/值域定義 [#]_

   * - 網址
     - 線上資源的連結位址
     - O
     - 1
     - gco:CharacterString
     - :ref:`ignore_missing <external_validators>` :ref:`unicode <external_validators>` :ref:`remove_whitespace <external_validators>`

   * - 名稱
     - 本筆資源的名稱。資料集內不同的資源應用不同的名稱區別
     - O
     - 1
     - gco:CharacterString
     -

   * - 摘要
     - 關於資源的簡短描述
     - O
     - 1
     - gco:CharacterString
     -

   * - 編碼
     - 此檔案所使用之編碼系統，如 UTF-8、Big5 等
     - O
     - 1
     - Encoding_type
     - :ref:`scheming_required <external_validators>` :ref:`scheming_choices <external_validators>`

   * - 座標參考系統 [#]_
     - 當您所新增之資源屬於空間資料時，則需另外填寫該空間資料所參考之坐標系統
     - O
     - 1
     - gco:Integer
     - :ref:`ignore_empty <external_validators>` :ref:`is_positive_integer <external_validators>`

   * - 格式 [#]_
     - 資源的檔案格式，例如：CSV [#]_、XLS、JSON、PDF 等
     - O
     - 1
     - gco:CharacterString
     - :ref:`if_empty_guess_format <external_validators>` :ref:`ignore_missing <external_validators>` :ref:`clean_format <external_validators>` :ref:`unicode <external_validators>`

.. [#] 關於個別資料型別的說明請見附錄 :doc:`data_type`。
.. [#] CKAN 軟體套件具有校驗器 (validator) 機制，用以檢查欄位是否符合規定，故亦可視為值域。另有轉換器 (converter)，用以轉換欄位值俾符合規定。
.. [#] 本平台所採用之記錄方式為 EPSG （歐洲石油測量組織）編碼。
.. [#] 格式填寫內容將會影響本平台所設定的資源預覽的預設畫面。請參考 :ref:`data_preview`。
.. [#] comma-separated values
