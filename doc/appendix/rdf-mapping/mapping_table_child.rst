.. list-table::
   :widths: 25 30 15 15 15
   :header-rows: 1

   * - 主欄位
     - 子欄位
     - 主欄位資料範圍
     - 子欄位對應語彙
     - 子欄位資料範圍

   * - 時間
     - 起始時間
     - dct:PeriodOfTime
     - schema:startDate
     - ISO8601 date format

   * - 時間
     - 結束時間
     - dct:PeriodOfTime
     - schema:endDate
     - ISO8601 date format

   * - 空間範圍
     - 

       | 空間範圍（GeoJson）
       | 空間範圍.X.min
       | 空間範圍.X.max
       | 空間範圍.Y.min
       | 空間範圍.Y.max

     - dct:Location
     - locn:geometry
     - locn:Geometry

   * - 專案
     - 名稱
     - foaf:Agent
     - foaf:name
     - rdfs:Literal

   * - 專案
     - 描述
     - foaf:Agent 
     - org:purpose
     - rdfs:Literal
