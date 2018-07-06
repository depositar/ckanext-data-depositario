Manual for Validators and Converters
====================================

CKAN has the validator mechanism to check if the given value is valid.
CKAN also comes with converters to transform the given value into a valid value.

.. _internal_validators:

----------------------------------
Internal Validators and Converters
----------------------------------

.. automodule:: ckanext.data_depositario.validators
   :members:
   :undoc-members:

.. automodule:: ckanext.data_depositario.converters
   :members:
   :undoc-members:

.. _external_validators:

----------------------------------
External Validators and Converters
----------------------------------

if_empty_same_as(name)
  Return the value in the ``name`` field if the provided value is empty.

unicode
  Checks that the provided value (if it is present) is a valid unicode string.

not_empty
  Only check if the provided value is empty.

package_name_validator
  Check that no package with the given name already exists and
  limit the length of the name from 2 characters to 100 characters.

scheming_required
  If the field is required, apply the ``not_empty`` validator.
  Otherwise, apply the ``ignore_missing`` validator.

scheming_choices
  Must be empty or one of the field choices values.

ignore_missing
  By putting ``ignore_missing`` at the start of the schema list for a field,
  you can allow users to post a dataset or resource without the field and
  the dataset or resource will pass validation. But if they post a dataset or
  resource that does contain the field, then any validators after ignore_missing in
  the dataset's or resource's schema list will be applied.

tag_string_convert
  Check that if the tag is a valid unicode string, -, _, or . characters.
  And limit the length of the tag from 1 characters to 100 characters.

ignore_empty
  Accept the empty string.

wikidata_keyword
  Must be in the form of Python list (e.g., ``["Q1", "Q2"]``) or string (e.g., ``"Q1, Q2"``).

scheming_multiple_choice
  Must be in the form of Python list (e.g., ``["Q1", "Q2"]``) or string (e.g., ``"Q1, Q2"``).
  And the values must be in the field choices values.

is_positive_integer
  Must be a postive integer.

owner_org_validator
  Must be "no organization" or an existing organization.

remove_whitespace
  Remove the leading and trailing whitespace characters in the string.

if_empty_guess_format
  Guess file format if it is empty.

clean_format
  Convert the filename extension to lower case.
