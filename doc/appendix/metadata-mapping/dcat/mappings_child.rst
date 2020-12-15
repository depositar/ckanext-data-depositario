.. list-table::
   :widths: 15 25 15 15 15 15
   :header-rows: 1

   * - 類型
     - 欄位
     - 值域
     - 對應語彙
     - 範圍
     - 備註

   * - 時間資訊
     - 起始時間
     - dct:PeriodOfTime
     - schema:startDate
     - ISO8601 date format
     -

   * - 時間資訊
     - 結束時間
     - dct:PeriodOfTime
     - schema:endDate
     - ISO8601 date format
     -

   * - 空間範圍
     - 空間範圍
     - dct:Location
     - locn:geometry
     - locn:Geometry
     -

   * - 空間範圍
     - | 空間範圍.X.min
       | 空間範圍.X.max
       | 空間範圍.Y.min
       | 空間範圍.Y.max
     - dct:Location
     - locn:geometry
     - locn:Geometry
     - 使用 locn:Geometry 所建議之 `RDF (schema.org) 格式 <https://www.w3.org/ns/locn#locn:geometry>`_

   * - 專案
     - 名稱
     - foaf:Agent
     - foaf:name
     - rdfs:Literal
     -

   * - 專案
     - 描述
     - foaf:Agent
     - org:purpose
     - rdfs:Literal
     -

   * - 聯絡資訊
     - 聯絡人
     - vcard:Kind
     - vcard:fn
     - xsd:string
     -

   * - 聯絡資訊
     - 聯絡人的電子郵件
     - vcard:Kind
     - vcard:hasEmail
     - vcard:Email
     -
