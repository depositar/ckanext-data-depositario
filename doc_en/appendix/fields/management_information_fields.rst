.. list-table::
   :widths: 20 5 45 30
   :header-rows: 1

   * - Field Name
     - Required
     - Description
     - Range

   * - License
     - Yes
     - Declare the license for the dataset so that people know how they can use the data. If you need to use a license not on the list, please select the "Other Licenses" and mark the license in the ``Remarks`` field above.
     - Must be one of the following licenses:

       | License Not Specified
       | `Public Domain <https://creativecommons.org/publicdomain/mark/1.0/>`_
       | `CC0 1.0 <https://creativecommons.org/publicdomain/zero/1.0/>`_
       | `CC-BY 4.0 <https://creativecommons.org/licenses/by/4.0/>`_
       | `CC-BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0/>`_
       | `CC-BY-NC-SA 4.0 <https://creativecommons.org/licenses/by-nc-sa/4.0/>`_
       | `ODbL 1.0 <https://www.opendefinition.org/licenses/odc-odbl>`_
       | `GFDL <https://www.opendefinition.org/licenses/gfdl>`_
       | `TWOGDL <https://data.gov.tw/license>`_
       | Other Licenses

   * - Author
     - Yes
     - The name of the person or project responsible for producing the data.
     -

   * - Created Time
     - No
     - The time when the resources in the dataset were created.
     - Must be in one of the following format:

       | YYYY
       | YYYY-MM
       | YYYY-MM-DD

   * - Process Step
     - No
     - Steps of data generating process.
     - Markdown

   * - Project
     - No
     - If you are a member of any projects, this drop-down will enable you to choose
       which one should own the dataset. If you select "No project", this dataset will
       not be owned by any project and will be opened to the public. If you check the
       "Open for project members only" box below this field [#]_, this dataset will only
       be seen by members of the project owning the dataset and will not show up in
       searches by other users. Otherwise, the dataset will be public and can be seen
       by any user of the site.
     -

   * - Contact Person
     - No
     - The person responsible for maintaining the dataset.
     -

   * - Contact Person Email
     - No
     - The email of the person responsible for maintaining the dataset.
     - `Email format <https://html.spec.whatwg.org/#e-mail-state-(type=email)>`_

.. [#] .. image:: /images/add_dataset_3.png
