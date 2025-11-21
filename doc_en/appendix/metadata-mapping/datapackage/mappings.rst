Dataset Level
-------------

.. list-table::
   :widths: 25 30 45
   :header-rows: 1

   * - Field
     - Data Package Property
     - Comments

   * - Title
     - title
     -

   * - URL
     - name
     - Only lowercase English alphanumeric characters plus ``-`` and ``_`` characters are accepted when importing the Data Package.

   * - Description
     - description
     -

   * - Data Type
     - data_type
     - Refer to the ``Value`` column in :ref:`parse-insight-content-types` for the property value.

   * - Wikidata Keywords
     - wd_keywords
     - See :ref:`field_transforms`

   * - Tags
     - keywords
     -

   * - Language
     - language
     - `ISO 639-3`_ languages (three-letter codes)

   * - Remarks
     - remarks
     -

   * - Temporal Resolution
     - temp_res
     - Accepted value:

       | Yearly: yearly
       | Monthly: monthly
       | Daily: daily

   * - Start Time
     - start_time
     -

   * - End Time
     - end_time
     -

   * - Spatial Coverage
     - spatial
     -

   * - X.min
     - x_min
     -

   * - X.max
     - x_max
     -

   * - Y.min
     - y_min
     -

   * - Y.max
     - y_max
     -

   * - Spatial Resolution
     - spatial_res
     -

   * - License
     - licenses
     - Included when downloading the dataset as a Data Package: ``"licenses": [{"name": "<license_id>", "title": "<license_title>", "path": "<license_url>"}]``

       | Insert ``"licenses": [{"name": "<LICNESE_NAME>"}]`` when importing the Data Package as a dataset. Accepted LICNESE_NAME:

       | License Not Specified: notspecified
       | `Public Domain <https://creativecommons.org/publicdomain/mark/1.0/>`_: pd
       | `CC0 1.0 <https://creativecommons.org/publicdomain/zero/1.0/>`_: cc-zero
       | `CC-BY 4.0 <https://creativecommons.org/licenses/by/4.0/>`_: cc-by
       | `CC-BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0/>`_: cc-by-sa 
       | `CC-BY-NC-SA 4.0 <https://creativecommons.org/licenses/by-nc-sa/4.0/>`_: cc-by-nc-sa
       | `ODbL 1.0 <https://www.opendefinition.org/licenses/odc-odbl>`_: odc-odbl
       | `GFDL <https://www.opendefinition.org/licenses/gfdl>`_: gfdl
       | `TWOGDL <https://data.gov.tw/license>`_: twogd
       | Other Licenses: other

   * - Creator
     - contributors
     - Included when downloading the dataset as a Data Package: ``"contributors": [{"title": "<author>", "roles": ["author"]}]``.

       | Insert ``"contributors": [{"title": "<CREATOR_NAME>", "roles": ["author"]}]`` when importing the Data Package as a dataset.

   * - Created Time
     - created_time
     -

   * - Process Step
     - process_step
     -

   * - Project
     - (N/A)
     - Excluded when downloading the dataset as a Data Package. Select the project when importing the Data Package as a dataset.

   * - Contact Person
     - contact_person
     -

   * - Contact Person Email
     - contact_email
     -

   * - Topic
     - (N/A)
     - Excluded when downloading and importing the Data Package.

   * - id (internal field)
     - ckan:id
     - Dataset UUID, excluded when importing the Data Package as a dataset.

Resource Level
--------------

.. list-table::
   :widths: 30 30 40
   :header-rows: 1

   * - Field
     - Data Package Property
     - Comments

   * - URL
     - path
     -

   * - Name
     - title
     -

   * - Description
     - description
     -

   * - Character Encoding
     - encoding
     - Accepted value:

       | Big5: big5
       | UTF-8: utf-8
       | ISO-8859-1: latin1
       | GB2312: gb2312
       | GB18030: gb18030
       | Shift_JIS: shift_jis
       | EUC-JP: euc-jp

   * - Coordinate Systems
     - resource_crs
     -

   * - Format
     - format
     - See :ref:`field_transforms`

   * - id (internal field)
     - ckan:id
     - Resource UUID, excluded when importing the Data Package as a dataset.

   * - mediatype (internal field)
     - mediatype
     - The mediatype/mimetype of the resource. Excluded when importing the Data Package as a dataset.

   * - size (internal field)
     - bytes
     - The size of the file in bytes. Excluded when importing the Data Package as a dataset.

.. _ISO 639-3: https://en.wikipedia.org/wiki/List_of_ISO_639-3_codes
