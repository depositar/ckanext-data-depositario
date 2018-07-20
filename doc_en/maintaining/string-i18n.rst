=======================
Translating |site_name|
=======================

---------------------------
String internationalization
---------------------------

Our customized extension can be internationalized. This guide shows
how to internationalize strings.

.. note::

   This is the simplified version. For details please refer to `String internationalization`_
   in CKAN's documentation.

#. Internationalizing strings in Jinja2 templates

   To internationalize a string put it inside a ``_()`` function:

   .. code-block:: jinja

      {% set hello = _('Hello World!') %}

#. Internationalizing strings in Python code

   To internationalize a string put it inside a ``_()`` function:

   .. code-block:: python

      my_string = _("This paragraph is translatable.")

#. Internationalizing strings in JavaScript code

   To internationalize a string put it inside a ``this._()`` function:

   .. code-block:: javascript

      this._('Something that should be translated')

-------------------------------------
Extract strings and edit translations
-------------------------------------

Before editing translations, you should extract strings from the customized extension.

.. important::

   The virtualenv has to remain active for the rest of the installation and deployment process,
   or commands will fail. You can tell when the virtualenv is active because
   its name appears in front of your shell prompt, something like this::

     (default) $ _

   For example, if you logout and login again, or if you close your terminal
   window and open it again, your virtualenv will no longer be activated. You
   can always reactivate the virtualenv with this command::

     . /usr/lib/ckan/default/bin/activate

.. important::

   Please run all the commands below under the directory where
   the customized extension is installed.

   .. parsed-literal::

      cd /usr/lib/ckan/default/src/ckanext-data-depositario

a. Extract strings to be translated:

   .. parsed-literal::

      python setup.py extract_messages

b. Create translation files for a locale:

   .. note::

      We will create translation files for the ``zh_TW`` locale.

      Since the ``zh_TW`` locale already exists, we run the ``update_catalog`` command 
      to keep the translated strings. If you want to create a new locale, please use 
      ``init_catalog`` instead.

   .. parsed-literal::

      python setup.py update_catalog -l zh_TW

c. Open the generated translation file and add translations for it
   by editing the ``msgstr`` section:

   .. parsed-literal::

      vi ckanext/data_depositario/i18n/zh_TW/LC_MESSAGES/ckanext-data_depositario.po

d. Compiling the catalog:

   .. parsed-literal::

      python setup.py compile_catalog

e. Restart CKAN:

   .. note::

      In this tutorial we are assuming that you have finished :doc:`installing/deployment`.

   .. parsed-literal::

      sudo stop ckan && sudo start ckan
