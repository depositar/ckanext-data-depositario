.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - 名稱
     - 校驗（轉換）器

   * - 授權
     - *必填欄位基本校驗器*

   * - 產製者
     - *必填欄位基本校驗器*

   * - 資料產製時間
     - :ref:`ignore_empty <external_validators>` :ref:`date_validator <internal_validators>`

   * - 資料處理歷程
     - *選填欄位基本校驗器*

   * - 專案
     - :ref:`owner_org_validator <external_validators>` :ref:`unicode <external_validators>`

   * - 聯絡人
     - *選填欄位基本校驗器*

   * - 聯絡人的電子郵件
     - :ref:`ignore_missing <external_validators>` :ref:`unicode <external_validators>` :ref:`email_validator <external_validators>`
