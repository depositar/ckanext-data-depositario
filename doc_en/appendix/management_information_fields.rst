.. list-table::
   :widths: 14 14 14 14 14 14
   :header-rows: 1

   * - Field Name
     - Description
     - Mandatory (M)/Optional (O)
     - Maximum Occurrence
     - Data Type
     - Validators and Converters

   * - License [#]_
     - It is important to include license information so that people know how they can use the data.
     - M
     - 1
     - License_code
     -

   * - Author
     - The name of the person or organization responsible for producing the data.
     - M
     - 1
     - gco:CharacterString
     -

   * - Created Time
     - The time when the resources in the dataset were created.
     - O
     - 1
     - gco:Date
     - :ref:`ignore_empty <external_validators>` :ref:`date_validator <internal_validators>`

   * - Organization [#]_ [#]_
     - If you are a member of any organizations, this drop-down will enable you to choose
       which one should own the dataset.
     - O
     - 1
     - gco:CharacterString
     - :ref:`owner_org_validator <external_validators>` :ref:`unicode <external_validators>`

   * - Maintainer
     - If necessary, the name for a second person responsible for the data.
     - O
     - 1
     - gco:CharacterString
     -

   * - Maintainer Email
     - If necessary, the email for a second person responsible for the data.
     - O
     - 1
     - gco:CharacterString
     -

   * - Maintainer Phone
     - If necessary, the phone number for a second person responsible for the data.
     - O
     - 1
     - gco:CharacterString
     - 

   * - Identifier
     - The unique identifier of this dataset in its source.
     - O
     - 1
     - gco:CharacterString
     -

.. [#] If you need to use a license not on the list, please select the "Other Licenses"
       and mark the license in the ``Remarks`` field above.
.. [#] If you select "No organization", this dataset will not be owned by any organization and
       will be opened to the public.
.. [#] If you check the "Open for organization members only" box below this field,
       this dataset will only be seen by members of the organization owning
       the dataset and will not show up in searches by other users.
       Otherwise, the dataset will be public and can be seen by any user of the site.
.. image:: /images/add_dataset_3.png
