=====================
Writing documentation
=====================

.. note::

   For details please refer to `Writing documentation`_.

---------------
Getting started
---------------

Install documentation into a Python virtual environment
=======================================================

Create a Python virtual environment (virtualenv) to install documentation into, and activate it:

::

    sudo apt install python3-dev python3-pip python3-venv git
    python3 -m venv pyenv
    . pyenv/bin/activate
    pip install wheel
    pip install -e 'git+https://github.com/depositar/ckan.git#egg=ckan[requirements]'
    pip install -e 'git+https://github.com/depositar/ckanext-data-depositario.git#egg=ckanext-data-depositario'
    pip install -r pyenv/src/ckanext-data-depositario/requirements-docs.txt

Edit the reStructuredText files
===============================

|site_name|'s documentation is created using `Sphinx <http://sphinx-doc.org/>`_.
To make changes to the documentation, use a text editor to edit the ``.rst`` files in
``pyenv/src/ckanext-data-depositario/doc``. Some useful links to bookmark:

* `Sphinx's reStructuredText Primer <http://sphinx-doc.org/rest.html>`_
* `reStructuredText cheat sheet <http://docutils.sourceforge.net/docs/user/rst/cheatsheet.txt>`_
* `reStructuredText quick reference <http://docutils.sourceforge.net/docs/user/rst/quickref.html>`_
* `Sphinx Markup Constructs <http://sphinx-doc.org/markup/index.html>`_ is a full list of the markup that Sphinx adds on top of Docutils.

--------------
Build the docs
--------------

You should now be able to build the CKAN documentation locally. Make sure your
virtual environment is activated, and then run the these commands::

    cd pyenv/src/ckanext-data-depositario
    python setup.py build_sphinx

Now you can open the built HTML files in
``build/sphinx/html``.

.. important::

   When you build the docs, Sphinx prints out warnings about any broken
   cross-references, syntax errors, etc. We aim not to have any of these warnings,
   so when adding to or editing the docs make sure your changes don't introduce
   any new ones.

   It's best to delete the ``build`` directory and completely rebuild the docs, to
   check for any warnings::

       rm -rf build; python setup.py build_sphinx

----------------
Publish the docs
----------------

|site_name|'s documentation is published using `ReadTheDocs <https://readthedocs.org/>`_. 
ReadTheDocs will detect each change to the ``ckanext-data-depositario`` repository
and build a new version.
