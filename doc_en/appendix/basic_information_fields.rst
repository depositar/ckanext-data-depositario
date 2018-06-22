.. list-table::
   :widths: 14 14 14 14 14 14
   :header-rows: 1

   * - Field Name
     - Description
     - Mandatory (M)/Optional (O)
     - Maximum Occurrence
     - Data Type [#]_
     - Validators and Converters [#]_

   * - Title
     - It is recommended to make it brief but specific.
       E.g. “Taiwan population density by region” is better than “Population figures”.
     - O
     - 1
     - gco:CharacterString
     - :ref:`if_empty_same_as(name) <external_validators>` :ref:`unicode <external_validators>` 

   * - URL [#]_
     - This URL will be unique across CKAN.
       Only letters, numbers, - and _ characters are accepted.
     - M
     - 1
     - gco:CharacterString
     - :ref:`not_empty <external_validators>` :ref:`unicode <external_validators>` :ref:`package_name_validator <external_validators>`

   * - Description
     - You can add a longer description of the dataset here, including
       information such as where the data is from and any information that people will
       need to know when using the data.
     - O
     - 1
     - gco:CharacterString
     -

   * - Data Type
     - The type of the dataset. Fields will be changed according to the data type.
     - M
     - 1
     - Data_type
     - :ref:`scheming_required <external_validators>` :ref:`scheming_choices <external_validators>`

   * - Tags [#]_
     - Here you may add tags that will help people find the data and link it
       with other related data.
     - O
     - N
     - gco:CharacterString
     - :ref:`ignore_missing <external_validators>` :ref:`tag_string_convert <external_validators>`

   * - Remarks
     - You can put some supplementary information for the dataset here.
     - O
     - 1
     - gco:CharacterString
     -

.. [#] For details please refer to appendix: :doc:`data_type`.
.. [#] CKAN has the validator mechanism to check if the given value is valid.
       CKAN also comes with converters to transform the given value into a valid value.
.. [#] The URL will be generated automatically when you input the title of the dataset.
       If there is no letter or number in the title, a random hash will be generated.
       You can modify the generated URL afterwards.
.. [#] Please only use this field when there is no proper entry in the Wikidata to
       describe the dataset. Otherwise, use the ``Keywords`` field below instead.
