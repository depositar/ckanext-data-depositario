============
DCAT Profile
============

Adapted from `DCAT 2 (Version 20200204) <https://www.w3.org/TR/2020/REC-vocab-dcat-2-20200204/>`__.

.. _namespaces:

----------
Namespaces
----------

The table below indicates the full list of namespaces and prefixes of the vocabularies and specifications used in this profile.

.. include:: namespaces.rst

--------
Mappings
--------

This section describes the alignments of the metadata of |site_name| and RDF vocabularies defined in this profile.

Fields:

* **Field:** The name of the field.
* **Mappings:** The mapped RDF vocabularies in prefixed name [1]_.
* **Range:** The instance used to state that the values of a property (mapped RDF vocabulary) are instances of one or more classes. See rdfs:range_.
* **Specification:** The specification and its document of the mapping.

.. include:: mappings.rst

.. _mappings_child:

---------------------------
Mappings for Child Elements
---------------------------

This section describes the alignments of the metadata of |site_name| and RDF vocabularies used by fields with child elements defined in this profile.

Fields:

* **Type:** The type of the field.
* **Field:** The name of the field.
* **Domain:** The instance used to state that any child element that has a given property (mapped RDF vocabulary) is an instance of one or more classes. See rdfs:domain_.
* **Mappings:** The mapped RDF vocabularies in prefixed name [1]_.
* **Range:** The instance used to state that the values of a property (mapped RDF vocabulary) are instances of one or more classes. See rdfs:range_.

.. include:: mappings_child.rst

.. _field_transforms:

----------------
Field Transforms
----------------

This section describes transforms of values of some fields to fit the range of mapped RDF vocabularies.

Fields:

* **Field:** The name of the field.
* **Identifier Type / Scheme:** The specification and its document of the transformed value.
* **URI Prefix:** URI prefix used in transformed value.
* **Example (Original):** The original value of the field.
* **Example (Transformed):** The transformed value to expose.

.. include:: field_transforms.rst

.. [1] `prefix label:local part format <https://www.w3.org/TR/turtle/#prefixed-name>`_。For prefix labels and their corresponding IRIs, please refer to the ``Prefix`` and ``Namespace URI``, respectively, in the :ref:`namespaces`.

.. _rdfs:range: https://www.w3.org/TR/rdf-schema/#ch_range
.. _rdfs:domain: https://www.w3.org/TR/rdf-schema/#ch_domain
