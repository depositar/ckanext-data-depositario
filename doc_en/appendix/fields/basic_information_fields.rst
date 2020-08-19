.. list-table::
   :widths: 15 5 55 25
   :header-rows: 1

   * - Field Name
     - Required
     - Description
     - Range

   * - Title
     - No
     - It is recommended to make it brief but specific.
       E.g. “Taiwan population density by region” is better than “Population figures”.
     - Must be a valid unicode string. The value will be the same as the ``URL``
       field if the provided value is empty.

   * - URL
     - Yes
     - This URL will be unique across CKAN. Only letters, numbers, - and _ characters
       are accepted. The URL will be generated automatically when you input the title
       of the dataset. If there is no letter or number in the title, a random hash will
       be generated. You can modify the generated URL afterwards.
     - Must not be empty. Must be a valid unicode string. There can not be a dataset
       with the given name already exists. The length limit for the URL is from
       2 characters to 100 characters.

   * - Description
     - No
     - You can add a longer description of the dataset here, including
       information such as where the data is from and any information that people will
       need to know when using the data.
     - Markdown

   * - Data Type
     - Yes
     - The type of the dataset. Fields will be changed according to the data type.
     - Accept multiple values. Use the :ref:`parse-insight-content-types`.

   * - Wikidata Keywords
     - No
     - Search Wikidata items for keywords to describe the dataset as shown below [#]_.
       For labels that are specific to your projects or datasets (eg. grant no.),
       use Tags instead.
       The language of keywords may align with the site language setting.
     - Accept multiple values.

   * - Tags
     - No
     - Here you may add tags that will help people find the data and link it with other
       related data.
       Tags should be used as labels that are specific to your projects or datasets.
     - Accept multiple values. Must be a valid unicode string, -, _, or . characters.
       The length limit for the tag is from 1 characters to 100 characters.

   * - Language
     - No
     - The language of the dataset (e.g., Chinese or Japanese). Main language (according
       to Wikipedia: `World language`_) will be listed first,
       followed by other ISO 639-3 languages in alphabetical order.
     - Accept multiple values. Must be a language defined in ISO 639-3.

   * - Remarks
     - No
     - You can put some supplementary information for the dataset here.
     - Markdown

.. [#] .. image:: /images/keyword_wikidata.png
.. _World language: https://en.wikipedia.org/wiki/World_language#Living_world_languages
