ARK Persistent Identifier
=========================

`Archival Resource Key <https://arks.org/about/>`_ (ARK) is a multi-purpose, general identifier which can be used as references for information objects.
|site_name| assigns ARKs as persistent identifiers (PID) to datasets via the `ckanext-ark <https://github.com/depositar/ckanext-ark>`_ extension,
just like the Digital Object Identifier (DOI).

.. note::

   This feature is a work in process.
   If you have any comment or feedback, please `contact us`_.

|site_name| assigns ARKs followed by ``ark:`` (e.g. ``ark:37281/k5c8w2q9c``)
using the following rules:

* ``37281``: The `NAAN <https://arks.org/about/ark-naans-and-systems/>`_ (Name Assigning Authority Number) registered on `N2T.net <https://n2t.net/ark:37281/>`__ to identify the organization that assigns ARKs.
* ``k5``: The fixed and dedicated sub-namespace (`shoulder <https://www.ietf.org/archive/id/draft-kunze-ark-34.html#name-optional-shoulders>`_ in the ARK) for datasets on the |site_name|.
* A unique identifier (blade in the ARK): The identifier is seven characters long and coded
  using the ``redededk`` `template <https://metacpan.org/dist/Noid/view/noid#TEMPLATES>`_:

  * ``r`` means that the seven-character-long identifier is quasi-randomly generated.
  * ``e`` means that the character is one of the extended digits ``{0123456789bcdfghjkmnpqrstvwxz}``.
  * ``d`` means that the character is one of the pure digits ``{0123456789}``.
  * ``k`` is the final check character.

For the technical specification of the ARK, please refer to the `IETF Internet Draft <https://datatracker.ietf.org/doc/draft-kunze-ark/>`_.

The Criteria for Assigning ARKs
-------------------------------

To ensure that the ARKs are shared broadly and fulfill the metadata requirements,
a public dataset will acquire an ARK identifier if it has the following fields:

* Title
* Start Time and/or End Time
* Creator

.. note::

   * Please refer to :ref:`Metadata <dataset_fields>`.
   * Please also refer to :ref:`editing-a-dataset` to learn more about public and private datasets.
     Make a private dataset public will acquire an ARK identifier, too.
   * If the above fields are removed after an ARK identifier is assigned,
     the ARK identifier will still be active, and its metadata (ERC) will contain the above fields.

Linking to Dataset via ARK
--------------------------

You can get the ARK identifier followed by ``ark:`` and its URL using the ARK Identifier widget in the bottom left corner of the dataset page:

.. image:: /images/ark_1.png
  :width: 300

The ARK URL will lead you to the target dataset.

The Name Mapping Authority (NMA) of |site_name| is https://pid.depositar.io/.
You can also use the NMA provided by `N2T.net <https://n2t.net/>`__,
just replace the https://pid.depositar.io/ part in the URL with https://n2t.net/.

.. note::

   The NMA of the demo system (https://demo.depositar.io/) is https://demo.depositar.io/.
   And there is neither N2T.net support nor a commitment about the persistent access of ARKs for the demo system.

ARK Identifier Metadata (ERC)
-----------------------------

With the ``?info`` inflection appended to the ARK URL, you can get the simple metadata of the identifier.

.. note::

   The metadata is called `Electronic Resource Citation (ERC) <https://n2t.net/ark:/13030/c7sn0141m>`_. |site_name| uses ERC to briefly describe dataset.

The ERC record is a JSON file with the ``erc`` attribute including the following information:

====== ==================== ==============================================
Field  Description          From :ref:`Metadata <dataset_fields>`
====== ==================== ==============================================
what   Title                Title
when   Temporal Information Start Time and End Time (in YYYYMMDD-YYYYMMDD)
where  URL of ARK           N/A (generated automatically)
who    Creator              Creator
====== ==================== ==============================================

Defunct ARK Identifier
----------------------

The ARK identifier will be defunct under the following circumstances:

* Make a public dataset private, then access the ARK URL without read permission of the dataset.
* Remove a dataset, then access the ARK URL without logging in as the creator of the dataset.
* Purge a dataset, then access the ARK URL (only sysadmin has the right to purge a dataset).

You will see the Defunct ARK page as follows:

.. image:: /images/ark_2.png
  :width: 400

For the first two cases aforementioned, the defunct ARK identifier still partially works as follows:

* Make a public dataset private, then access the ARK URL with logging in as user with read permission of the dataset.
* Remove a dataset, then access the ARK URL with logging in as the creator of the dataset.

.. note::

   * If you make the private dataset public or restore the deleted dataset, the defunct ARK identifier will be active again.
   * The metadata (ERC) of the defunct ARK identifier remains available.
