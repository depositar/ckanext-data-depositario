==============================
Metadata at the resource level
==============================

.. list-table::
   :widths: 14 14 14 14 14 14
   :header-rows: 1

   * - Field Name
     - Description
     - Mandatory (M)/Optional (O)
     - Maximum Occurrence
     - Data Type [#]_
     - Validators and Converters [#]_

   * - URL
     - The url of the resource.
     - O
     - 1
     - gco:CharacterString
     - :ref:`ignore_missing <external_validators>` :ref:`unicode <external_validators>` :ref:`remove_whitespace <external_validators>`

   * - Name
     - The title of the resource.
     - O
     - 1
     - gco:CharacterString
     -

   * - Description
     - You can add a longer description of the resource here.
     - O
     - 1
     - gco:CharacterString
     -

   * - Encoding
     - The character encoding of the resource (e.g., UTF-8 or Big5).
     - O
     - 1
     - Encoding_type
     - :ref:`scheming_required <external_validators>` :ref:`scheming_choices <external_validators>`

   * - Coordinate Systems [#]_
     - The coordinate systems of the spatial resource.
     - O
     - 1
     - gco:Integer
     - :ref:`ignore_empty <external_validators>` :ref:`is_positive_integer <external_validators>`

   * - Format [#]_
     - The file format of the resource (e.g., CSV [#]_, XLS, JSON, or PDF).
     - O
     - 1
     - gco:CharacterString
     - :ref:`if_empty_guess_format <external_validators>` :ref:`ignore_missing <external_validators>` :ref:`clean_format <external_validators>` :ref:`unicode <external_validators>`

.. [#] For details please refer to appendix: :doc:`data_type`.
.. [#] CKAN has the validator mechanism to check if the given value is valid.
       CKAN also comes with converters to transform the given value into a valid value.
.. [#] The EPSG (European Petroleum Survey Group) system has been used.
.. [#] The data preview function will check this field to specify a proper resource view.
       Please refer to :ref:`data_preview`.
.. [#] Comma-separated values
