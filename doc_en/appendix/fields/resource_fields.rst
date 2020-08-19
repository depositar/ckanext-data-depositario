.. list-table::
   :widths: 20 5 45 30
   :header-rows: 1

   * - Field Name
     - Required
     - Description
     - Range

   * - URL
     - No
     - The url of the resource.
     - Must be a valid unicode string.

   * - Name
     - No
     - The title of the resource.
     - Must be a valid unicode string.

   * - Description
     - No
     - You can add a longer description of the resource here.
     - Markdown

   * - Character Encoding
     - No
     - The character encoding of the resource (e.g., UTF-8 or Big5). Applied only to shapefile resources for now.
     - `IANA Character Sets <https://www.iana.org/assignments/character-sets/character-sets.xhtml>`_:

       | Big5
       | UTF-8
       | ISO-8859-1
       | GB2312
       | GB18030
       | Shift_JIS
       | EUC-JP

   * - Coordinate Systems
     - No
     - This field is required when the resource is in shapefile format with no projection (.prj file), otherwise the shapefile can not be previewed. The EPSG (European Petroleum Survey Group) system has been used.
     - Must be a postive integer.

   * - Format
     - No
     - The file format of the resource (e.g., CSV, XLS, JSON, or PDF). The data preview function will check this field to specify a proper resource view. Please refer to :ref:`data_preview`.
     - Must be a valid unicode string.
