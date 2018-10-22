.. list-table::
   :widths: 14 14 14 14 14 14
   :header-rows: 1

   * - 欄位名稱
     - 說明
     - 必填 M / 選填 O
     - 最多發生次數
     - 資料型別
     - 校驗（轉換）器/值域定義

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

   * - 專案 [#]_ [#]_
     - 若您屬於任一專案內之成員，則您可於專案欄位之下拉選單內找到您所屬的專案清單
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

.. [#] 若資料集釋出之授權不在候選清單內，請選擇 "Other Licenses" ，並於「備註」欄位註明授權條款。
.. [#] 若選擇「沒有此專案」選項，此資料集將不屬於任何專案，且將會被強制設定為「公開」資料集。
.. [#] 欄位下方之「只對專案內成員公開」核取方塊（如下圖）被選中時，非屬於選定專案之成員即無法瀏覽該資料集（即「非公開」狀態），反之則對任何使用者公開該資料集。
.. image:: /images/add_dataset_3.png
