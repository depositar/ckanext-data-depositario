===========================
Installing CKAN from source
===========================

This section describes how to install CKAN used by |site_name| from source on an Ubuntu 18.04 server.

--------------------------------
1. Install the required packages
--------------------------------

.. parsed-literal::

   sudo apt install python3-dev postgresql libpq-dev python3-pip python3-venv git openjdk-8-jdk redis-server

-------------------------------------------------
2. Install CKAN into a Python virtual environment
-------------------------------------------------

a. Create a Python virtual environment (virtualenv) to install CKAN into, and activate it:

   .. parsed-literal::

      sudo mkdir -p /usr/lib/ckan/default
      sudo chown \`whoami\` /usr/lib/ckan/default
      python3 -m venv /usr/lib/ckan/default
      . /usr/lib/ckan/default/bin/activate

   .. important::

      The final command above activates your virtualenv. The virtualenv has to
      remain active for the rest of the installation and deployment process,
      or commands will fail. You can tell when the virtualenv is active because
      its name appears in front of your shell prompt, something like this::

        (default) $ _

      For example, if you logout and login again, or if you close your terminal
      window and open it again, your virtualenv will no longer be activated. You
      can always reactivate the virtualenv with this command::

        . /usr/lib/ckan/default/bin/activate

b. Install the recommended setuptools version:

   .. important::

      Please run all the commands below under the `ckan` directory:

      .. parsed-literal::

         cd /usr/lib/ckan/default/

   .. parsed-literal::

      pip install setuptools==44.1.0
      pip install --upgrade pip

c. Install CKAN into your virtualenv:

   .. parsed-literal::

      pip install -e 'git+git://github.com/depositar/ckan.git#egg=ckan[requirements]'

d. Install customized extesion into your virtualenv:

   .. parsed-literal::

      pip install -e 'git+https://github.com/depositar/ckanext-data-depositario.git#egg=ckanext-data-depositario'

e. Install the Python modules that customized extesion requires into your virtualenv:

   .. parsed-literal::

      pip install -r /usr/lib/ckan/default/src/ckanext-data-depositario/requirements.txt

f. Install other required Python modules into your virtualenv:

   .. parsed-literal::

      pip install -r /usr/lib/ckan/default/src/ckanext-spatial/pip-requirements.txt
      pip install -r https://raw.githubusercontent.com/ckan/ckanext-xloader/master/requirements.txt
      pip install -r /usr/lib/ckan/default/src/ckanext-dcat/requirements.txt
      pip install -r /usr/lib/ckan/default/src/ckanext-harvest/pip-requirements.txt

---------------------------------
3. Create the FireStore directory
---------------------------------

.. note::

   When enabled, CKAN’s FileStore allows users to upload data files to CKAN resources.
   Please refer to :ref:`User guide <add_resource>` for details.

.. parsed-literal::

   sudo mkdir -p /var/lib/ckan/default
   sudo chown \`whoami\` /var/lib/ckan/default
   sudo chmod u+rwx /var/lib/ckan/default

.. _postgres-setup:

------------------------------
4. Setup a PostgreSQL database
------------------------------

a. Create a database user:

   .. parsed-literal::

      sudo -u postgres createuser -S -D -R -P ckan_default

b. Create a new database:

   .. parsed-literal::

      sudo -u postgres createdb -O ckan_default ckan_default -E utf-8

c. Install the PostGIS:

   .. parsed-literal::

      sudo apt-get install postgresql-10-postgis-2.4 python3-dev libxml2-dev libxslt1-dev libgeos-c1v5
      sudo -u postgres psql -d ckan_default -f /usr/share/postgresql/10/contrib/postgis-2.4/postgis.sql
      sudo -u postgres psql -d ckan_default -f /usr/share/postgresql/10/contrib/postgis-2.4/spatial_ref_sys.sql
      sudo -u postgres psql -d ckan_default -c 'ALTER VIEW geometry_columns OWNER TO ckan_default;'
      sudo -u postgres psql -d ckan_default -c 'ALTER TABLE spatial_ref_sys OWNER TO ckan_default;'

d. Create a new database user and a new database for DataStore:

   .. note::

      The CKAN DataStore extension provides an ad hoc database for storage of structured data from CKAN resources. Data can be pulled out of resource files and stored in the DataStore.

   .. parsed-literal::

      sudo -u postgres createuser -S -D -R -P -l datastore_default
      sudo -u postgres createdb -O ckan_default datastore_default -E utf-8


e. (For |site_name| administrator) Restore database backup:

   .. parsed-literal::

      cat main_db.sql.gz | gunzip | sudo -u postgres psql ckan_default
      cat datastore_db.sql.gz | gunzip | sudo -u postgres psql datastore_default

----------------------------
5. Create a CKAN config file
----------------------------

a. Create a directory to contain the site's config files:

   .. parsed-literal::

      sudo mkdir -p /etc/ckan/default
      sudo chown -R \`whoami\` /etc/ckan/

b. Create a CKAN config file:

   .. important::

      (For |site_name| administrator) Please ignore the following step. c
      and use ``production.ini`` the in the ``configs.tar.gz``.

   .. important::

      The virtualenv has to remain active when running the paster command.
      You can always reactivate the virtualenv with this command: ::

      . /usr/lib/ckan/default/bin/activate

   .. parsed-literal::

      ckan generate config /etc/ckan/default/ckan.ini
      ckan config-tool /etc/ckan/default/ckan.ini -f /usr/lib/ckan/default/src/ckanext-data-depositario/config/custom_options.ini

c. Edit the ckan.ini file in a text editor, changing the following options:

   .. note::

      * The settings below is the minimum requirements to run the CKAN.

   .. parsed-literal::

      ## Database Settings
      ## This should refer to the database we created in :ref:`postgres-setup` above
      ## Replace ``pass`` with the ``CKAN database`` password that you created
      sqlalchemy.url = postgresql://ckan_default:pass@localhost/ckan_default
      ## Replace ``pass`` with the ``CKAN database`` password that you created
      ckan.datastore.write_url = postgresql://ckan_default:pass@localhost/datastore_default
      ## Replace ``pass`` with the ``DataStore database`` password that you created
      ckan.datastore.read_url = postgresql://datastore_default:pass@localhost/datastore_default

      ## Add the following lines above Logging configuration

      ## Schema Settings
      scheming.presets = ckanext.scheming:presets.json
                         ckanext.data_depositario:presets.json
                         ckanext.wikidatakeyword:presets.json
      scheming.dataset_schemas = ckanext.data_depositario.schemas:dataset.yaml

      ## Spatial Settings
      ckanext.spatial.search_backend = solr-spatial-field

      ## DCAT Settings
      ckanext.dcat.rdf.profiles = dcat
      ckanext.dcat.translate_keys = False
      ckanext.dcat.enable_content_negotiation = True

      ## ckanext-data-depositario Settings
      ## GMAP_AKI_KEY is the API key for Google Maps
      ckanext.data_depositario.gmap.api_key = GMAP_AKI_KEY
      ## GA_ID is the id for Google Analytics
      ckanext.data_depositario.googleanalytics.id = GA_ID

-------------------------------------------------------
6. Setup Solr (with Chinese and spatial search support)
-------------------------------------------------------

.. note::

   This section is adapted from `How To Install Solr 5.2.1 on Ubuntu 14.04 <https://www.digitalocean.com/community/tutorials/how-to-install-solr-5-2-1-on-ubuntu-14-04>`_ by `DigitalOcean™ Inc. <https://www.digitalocean.com/>`_ licensed under `Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International <https://creativecommons.org/licenses/by-nc-sa/4.0/>`_.

a. Download and extract the service installation file:

   .. parsed-literal::

      cd ~
      wget http://archive.apache.org/dist/lucene/solr/8.11.1/solr-8.11.1.tgz
      tar xzf solr-8.11.1.tgz solr-8.11.1/bin/install_solr_service.sh --strip-components=2

b. Install Solr as a service using the script:

   .. parsed-literal::

      sudo bash ./install_solr_service.sh solr-8.11.1.tgz

c. Create the Solr core for CKAN:

   .. parsed-literal::

      sudo -u solr /opt/solr/bin/solr create -c ckan
      sudo ln -sf /usr/lib/ckan/default/src/ckanext-data-depositario/solr/schema.xml /var/solr/data/ckan/conf/managed-schema

d. Download Chinese tokenizer ``ik-analyzer`` and copy it to the Solr directory:

   .. parsed-literal::

      wget https://repo1.maven.org/maven2/com/github/magese/ik-analyzer/8.5.0/ik-analyzer-8.5.0.jar
      sudo cp ik-analyzer-8.5.0.jar /opt/solr/server/solr-webapp/webapp/WEB-INF/lib/.
      sudo mkdir /opt/solr/server/solr-webapp/webapp/WEB-INF/classes
      sudo ln -s /usr/lib/ckan/default/src/ckanext-data-depositario/solr/IKAnalyzer.cfg.xml /opt/solr/server/solr-webapp/webapp/WEB-INF/classes/.
      sudo ln -s /usr/lib/ckan/default/src/ckanext-data-depositario/solr/dic/words.dic /opt/solr/server/solr-webapp/webapp/WEB-INF/classes/words.dic

e. Download geometry library JTS Topology Suite 1.18 (or above) and copy it to the Solr directory:

   .. parsed-literal::

      wget https://repo1.maven.org/maven2/org/locationtech/jts/jts-core/1.18.2/jts-core-1.18.2.jar
      sudo cp jts-core-1.18.2.jar /opt/solr/server/solr-webapp/webapp/WEB-INF/lib/.

f. Restart Solr:

   .. parsed-literal::

      sudo service solr restart

g. Open http://127.0.0.1:8983/solr/#/ckan in a web browser, and you should see the Solr front page.

----------------------
7. Link to ``who.ini``
----------------------

.. parsed-literal::

   ln -s /usr/lib/ckan/default/src/ckan/who.ini /etc/ckan/default/who.ini

-------------------------
8. Create database tables
-------------------------

.. important::

   (For |site_name| administrator) Please ignore this step.

a. Set up the DataStore:

   .. parsed-literal::

      ckan -c /etc/ckan/default/ckan.ini db init

   You should see Initialising DB: SUCCESS.

b. Then you can use this connection to set up the DataStore:

   .. parsed-literal::

      ckan -c /etc/ckan/default/ckan.ini datastore set-permissions | sudo -u postgres psql --set ON_ERROR_STOP=1

----------------------------
9. Creating a sysadmin user
----------------------------

.. important::

   (For |site_name| administrator) Please ignore this step.

Set password for the default CKAN sysadmin user from the command line.

.. parsed-literal::

   ckan -c /etc/ckan/default/ckan.ini user setpass default

-----------------------------------------
10. Serve CKAN under a development server
-----------------------------------------

a. Run the XLoader:

   .. note::

      This XLoader is a service that automatically uploads data to the DataStore from suitable files (like CSV or Excel files), whether uploaded to CKAN’s FileStore or externally linked.

      The CKAN DataStore extension provides an ad hoc database for storage of structured data from CKAN resources. Data can be pulled out of resource files and stored in the DataStore.

   .. parsed-literal::

      ckan -c /etc/ckan/default/ckan.ini jobs worker

b. Open another terminal and use the Paste development server to serve CKAN from the command-line:

   .. parsed-literal::

      . /usr/lib/ckan/default/bin/activate
      ckan -c /etc/ckan/default/development.ini

c. Open http://127.0.0.1:5000/ in a web browser, and you should see the CKAN front page.

Now that you've installed CKAN.
