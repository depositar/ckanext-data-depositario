.. list-table::
   :widths: 15 25 15 15 15 15
   :header-rows: 1

   * - Type
     - Field
     - Domain
     - Mappings
     - Range
     - Comments

   * - Temporal Information
     - Start Time
     - dct:PeriodOfTime
     - schema:startDate
     - ISO8601 date format
     -

   * - Temporal Information
     - End Time
     - dct:PeriodOfTime
     - schema:endDate
     - ISO8601 date format
     -

   * - Spatial Coverage
     - Spatial Coverage
     - dct:Location
     - locn:geometry
     - locn:Geometry
     -

   * - Spatial Coverage
     - | X.min
       | X.max
       | Y.min
       | Y.max
     - dct:Location
     - locn:geometry
     - locn:Geometry
     - Use `RDF (schema.org) format <https://www.w3.org/ns/locn#locn:geometry>`_ recommended by locn:Geometry.

   * - Project
     - Name
     - foaf:Agent
     - foaf:name
     - rdfs:Literal
     -

   * - Project
     - Description
     - foaf:Agent
     - org:purpose
     - rdfs:Literal
     -

   * - Contact Information
     - Contact Person
     - vcard:Kind
     - vcard:fn
     - xsd:string
     -

   * - Contact Information
     - Contact Person Email
     - vcard:Kind
     - vcard:hasEmail
     - vcard:Email
     -
