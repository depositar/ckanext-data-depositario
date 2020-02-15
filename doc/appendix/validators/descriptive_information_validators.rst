.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - 名稱
     - 校驗（轉換）器

   * - 資料類型
     - :ref:`scheming_required <external_validators>` :ref:`scheming_choices <external_validators>`

   * - 時間解析度
     - :ref:`scheming_required <external_validators>` :ref:`scheming_choices <external_validators>`

   * - 起始時間
     - :ref:`ignore_empty <external_validators>` :ref:`temp_res_validator <internal_validators>`

   * - 結束時間
     - :ref:`ignore_empty <external_validators>` :ref:`temp_res_validator <internal_validators>`

   * - 空間範圍
     - :ref:`ignore_empty <external_validators>` :ref:`json_validator <internal_validators>` :ref:`remove_blank_wrap <internal_validators>`

   * - 空間範圍.X.min
     - :ref:`ignore_empty <external_validators>` :ref:`long_validator <internal_validators>`

   * - 空間範圍.X.max
     - :ref:`ignore_empty <external_validators>` :ref:`long_validator <internal_validators>`

   * - 空間範圍.Y.min
     - :ref:`ignore_empty <external_validators>` :ref:`lat_validator <internal_validators>`

   * - 空間範圍.Y.max
     - :ref:`ignore_empty <external_validators>` :ref:`lat_validator <internal_validators>`

   * - 空間解析度
     - :ref:`ignore_empty <external_validators>` :ref:`positive_float_validator <internal_validators>`
