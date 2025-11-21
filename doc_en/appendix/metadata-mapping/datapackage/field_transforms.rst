Dataset Level
-------------

.. list-table::
   :header-rows: 1

   * - Field
     - Example
     - Data Package Property
     - Example
     - Comments

   * - Wikidata Keywords
     - Q484000
     - wd_keywords
     - http://www.wikidata.org/entity/Q484000
     - Wikidata QID

   * - metadata_created (internal field)
     - 2000-01-01T11:00:00.123456
     - created
     - 2000-01-01T11:00:00.123456+08:00 (timezone added)
     - The time when the dataset is created. Excluded when importing the Data Package as a dataset.

   * - (N/A)
     - (N/A)
     - id
     - ``https://n2t.net/ark:37281/<blade>`` (ARK URL)
     - Included when downloading the dataset (with :doc:`../../../user-guide/ark-identifier` issued) as a Data Package

   * - (N/A)
     - (N/A)
     - sources
     - JSON: ``[{"email": "data.contact@depositar.io", "path": "<dataset URL or ARK URL>", "title": "研究資料寄存所 | depositar"}]``
     - Included when downloading the dataset as a Data Package

Resource Level
--------------

.. list-table::
   :widths: 20 15 30 20 15
   :header-rows: 1

   * - Field
     - Example
     - Data Package Property
     - Example
     - Comments

   * - (N/A)
     - (N/A)
     - name
     - resource_N, where N is a sequential number starting from 1 (1, 2, …)
     - Included when downloading the dataset as a Data Package

   * - Format
     - PDF
     - format
     - pdf
     - Included and lowercased when downloading the dataset as a Data Package. Included and uppercased when importing the Data Package as a dataset.
