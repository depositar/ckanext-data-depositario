.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Field Name
     - Validators and Converters

   * - Temporal Resolution
     - :ref:`scheming_required <external_validators>` :ref:`scheming_choices <external_validators>`

   * - Start Time
     - :ref:`ignore_empty <external_validators>`

   * - End Time
     - :ref:`ignore_empty <external_validators>` :ref:`end_time_validator <internal_validators>`

   * - Spatial
     - :ref:`ignore_empty <external_validators>` :ref:`json_validator <internal_validators>` :ref:`remove_blank_wrap <internal_validators>`

   * - X.min
     - :ref:`ignore_empty <external_validators>` :ref:`long_validator <internal_validators>`

   * - X.max
     - :ref:`ignore_empty <external_validators>` :ref:`long_validator <internal_validators>`

   * - Y.min
     - :ref:`ignore_empty <external_validators>` :ref:`lat_validator <internal_validators>`

   * - Y.max
     - :ref:`ignore_empty <external_validators>` :ref:`lat_validator <internal_validators>`

   * - Spatial Resolution
     - :ref:`ignore_empty <external_validators>` :ref:`positive_float_validator <internal_validators>`
