.. list-table::
   :widths: 20 5 45 30
   :header-rows: 1

   * - Field Name
     - Required
     - Description
     - Range

   * - Temporal Resolution
     - No
     - Please refer to :ref:`Fill-in snippet for temporal information <UI_editing_extend_time>`.
     - Must be one of the following resolution:

       | Yearly
       | Monthly
       | Daily

   * - Start Time
     - No
     - Same as above
     - Must be in one of the following format:

       | YYYY
       | YYYY-MM
       | YYYY-MM-DD

   * - End Time
     - No
     - Same as above
     - Same as above

   * - Spatial Coverage
     - No
     - Please refer to :ref:`Fill-in snippet for spatial fields <UI_editing_extend_spatial>`.
     - GeoJSON format

   * - X.min
     - No
     - Same as above
     - Must be a float between -180 and 180, and X.max must be greater than X.min.

   * - X.max
     - No
     - Same as above
     - Same as above

   * - Y.min
     - No
     - Same as above
     - Must be a float between -90 and 90, and Y.max must be greater than Y.min.

   * - Y.max
     - No
     - Same as above
     - Same as above

   * - Spatial Resolution
     - No
     - Spatial resolution (in meter) of source.
     - Must be a positive float.
