.. list-table::
   :widths: 14 14 14 14 14 14
   :header-rows: 1

   * - Field Name
     - Description
     - Mandatory (M)/Optional (O)
     - Maximum Occurrence
     - Data Type
     - Validators and Converters

   * - Language
     - The language of the dataset (e.g., Chinese or Japanese).
     - O
     - 1
     - Language_type
     - :ref:`scheming_required <external_validators>` :ref:`scheming_choices <external_validators>`

   * - Temporal Resolution
     - Please refer to :ref:`Fill-in snippet for temporal information <UI_editing_extend_time>`
     - O
     - 1
     - Temp_res_type
     - :ref:`scheming_required <external_validators>` :ref:`scheming_choices <external_validators>`

   * - Start Time
     - Please refer to :ref:`Fill-in snippet for temporal information <UI_editing_extend_time>`
     - O
     - 1
     - gco:Date
     - :ref:`ignore_empty <external_validators>` :ref:`temp_res_validator <internal_validators>`

   * - End Time
     - Please refer to :ref:`Fill-in snippet for temporal information <UI_editing_extend_time>`
     - O
     - 1
     - gco:Date
     - :ref:`ignore_empty <external_validators>` :ref:`temp_res_validator <internal_validators>`

   * - Spatial
     - Please refer to :ref:`Fill-in snippet for spatial fields <UI_editing_extend_spatial>`
     - O
     - 1
     - GeoJSON
     - :ref:`ignore_empty <external_validators>` :ref:`json_validator <internal_validators>` :ref:`remove_blank_wrap <internal_validators>`

   * - X.min
     - Please refer to :ref:`Fill-in snippet for spatial fields <UI_editing_extend_spatial>`
     - O
     - 1
     - gco:Decimal
     - :ref:`ignore_empty <external_validators>` :ref:`long_validator <internal_validators>`

   * - X.max
     - Please refer to :ref:`Fill-in snippet for spatial fields <UI_editing_extend_spatial>`
     - O
     - 1
     - gco:Decimal
     - :ref:`ignore_empty <external_validators>` :ref:`long_validator <internal_validators>`

   * - Y.min
     - Please refer to :ref:`Fill-in snippet for spatial fields <UI_editing_extend_spatial>`
     - O
     - 1
     - gco:Decimal
     - :ref:`ignore_empty <external_validators>` :ref:`lat_validator <internal_validators>`

   * - Y.max
     - Please refer to :ref:`Fill-in snippet for spatial fields <UI_editing_extend_spatial>`
     - O
     - 1
     - gco:Decimal
     - :ref:`ignore_empty <external_validators>` :ref:`lat_validator <internal_validators>`

   * - Keywords [#]_ [#]_
     - The short term to describe the contents of the dataset.
     - O
     - N
     - gco:CharacterString
     - :ref:`wikidata_keyword <external_validators>`

   * - **Books** [#]_
     -
     -
     -
     -
     -

   * - ISBN-13
     -
     - O
     - 1
     - gco:CharacterString
     -

   * - ISSN
     -
     - O
     - 1
     - gco:CharacterString
     -

   * - Journal
     -
     - O
     - 1
     - gco:CharacterString
     -

   * - Volume
     -
     - O
     - 1
     - gco:CharacterString
     -

   * - Proceeding
     -
     - O
     - 1
     - gco:CharacterString
     -

   * - Location
     -
     - O
     - 1
     - gco:CharacterString
     -

   * - Publisher
     -
     - O
     - 1
     - gco:CharacterString
     -

   * - Publication Year
     -
     - O
     - 1
     - gco:CharacterString
     -

   * - Book Query
     -
     - O
     - 1
     - gco:CharacterString
     -

   * - URL
     -
     - O
     - 1
     - gco:CharacterString
     -

   * - Historical Material
     -
     - O
     - N
     - Hist_material_type
     - :ref:`scheming_multiple_choice <external_validators>`

   * - Village of Research Area
     -
     - O
     - 1
     - gco:CharacterString
     -

   * - Religion of Research Area
     -
     - O
     - 1
     - gco:CharacterString
     -

   * - Family of Research Area
     -
     - O
     - 1
     - gco:CharacterString
     -

   * - Reservoir of Research Area
     -
     - O
     - 1
     - gco:CharacterString
     -

   * - Industry of Research Area
     -
     - O
     - 1
     - gco:CharacterString
     -

   * - Notes
     -
     - O
     - 1
     - gco:CharacterString
     -

   * - **Pictures** [#]_
     -
     -
     -
     -
     -

   * - Original Source
     -
     - O
     - 1
     - gco:CharacterString
     -

   * - Scan Size
     - Size (cm) of source (e.g., 60x72)
     - O
     - 1
     - gco:CharacterString
     -

   * - Scanning Resolution
     - Resolution (DPI) of source (e.g., 300)
     - O
     - 1
     - gco:Integer
     - :ref:`ignore_empty <external_validators>` :ref:`is_positive_integer <external_validators>`

   * - Spatial Resolution
     - Spatial resolution (m) of source
     - O
     - 1
     - gco:CharacterString
     - :ref:`ignore_empty <external_validators>` :ref:`positive_float_validator <internal_validators>`

   * - Scale Denominator
     - Scale denominator of data
     - O
     - 1
     - gco:Integer
     - :ref:`ignore_empty <external_validators>` :ref:`is_positive_integer <external_validators>`

   * - Preprocessing
     - Steps of data generating process
     - O
     - 1
     - gco:CharacterString
     -

.. [#] We use Wikidata entries as the source for keywords.
       Wikidata entries are multilingual, which means the language of keywords may align with
       the site language setting.

       You can also search and select keywords by an autocomplete dropdown list as shown below:
.. image:: /images/keyword_wikidata.png
.. [#] Use the ``Tags`` field above when there is no proper entry in the Wikidata to describe the dataset.
.. [#] The corresponding fields for the ``Books`` data type (See the "Basic Information" above).
.. [#] The corresponding fields for the ``Pictures`` data type (See the "Basic Information" above).
