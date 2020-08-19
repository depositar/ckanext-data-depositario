.. list-table::
   :widths: 20 5 45 30
   :header-rows: 1

   * - 名稱
     - 必填
     - 說明
     - 資料範圍

   * - 時間解析度
     - 否
     - 請參考 :ref:`時間資訊填寫輔助功能 <UI_editing_extend_time>`。
     - 限以下時間之一：

       | 年
       | 月
       | 日

   * - 起始時間
     - 否
     - 同上
     - 限制以下時間格式：

       | YYYY
       | YYYY-MM
       | YYYY-MM-DD

   * - 結束時間
     - 否
     - 同上
     - 同上

   * - 空間範圍
     - 否
     - 請參考 :ref:`空間範圍填寫輔助功能 <UI_editing_extend_spatial>`。
     - 需為 GeoJSON 格式。

   * - 空間範圍.X.min
     - 否
     - 同上
     - 必須為 -180 至 180 之浮點數，且 X.max > X.min。

   * - 空間範圍.X.max
     - 否
     - 同上
     - 同上

   * - 空間範圍.Y.min
     - 否
     - 同上
     - 必須為 -90 至 90 之浮點數，且 Y.max > Y.min。

   * - 空間範圍.Y.max
     - 否
     - 同上
     - 同上

   * - 空間解析度
     - 否
     - 資料的空間解析度數值，以公尺為單位。
     - 必須為正浮點數。
