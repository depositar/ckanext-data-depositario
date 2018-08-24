===========================
Installing CKAN from source
===========================

This section describes how to install CKAN used by |site_name| from source on an Ubuntu 16.04 server.

--------------------------------
1. Install the required packages
--------------------------------

.. parsed-literal::

   sudo apt-get install build-essential libxslt1-dev libxml2-dev python-dev postgresql libpq-dev python-pip python-virtualenv git-core openjdk-8-jdk redis-server

-------------------------------------------------
2. Install CKAN into a Python virtual environment
-------------------------------------------------

a. Create a Python virtual environment (virtualenv) to install CKAN into, and activate it:

   .. parsed-literal::

      sudo mkdir -p /usr/lib/ckan/default
      sudo chown \`whoami\` /usr/lib/ckan/default
      virtualenv --no-site-packages /usr/lib/ckan/default
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

      pip install setuptools==36.1

c. Install the CKAN source code and customized extesion into your virtualenv.

   .. parsed-literal::

      pip install -e 'git+https://github.com/depositar-io/ckanext-data-depositario.git#egg=ckanext-data-depositario'

d. Install the Python modules that customized extesion requires into your virtualenv:

   .. parsed-literal::

      pip install -r /usr/lib/ckan/default/src/ckanext-data-depositario/requirements.txt

e. Install the Python modules that CKAN requires into your virtualenv:

   .. parsed-literal::

      pip install -r /usr/lib/ckan/default/src/ckan/requirements.txt

f. Install other required Python modules into your virtualenv:

   .. parsed-literal::

      pip install -r /usr/lib/ckan/default/src/ckanext-spatial/pip-requirements.txt
      pip install -r /usr/lib/ckan/default/src/ckanext-scheming/requirements.txt

-------------------------------------------------------
3. Install DataPusher into a Python virtual environment
-------------------------------------------------------

.. note::

   This DataPusher is a service that automatically uploads data to the DataStore from suitable files (like CSV or Excel files), whether uploaded to CKAN’s FileStore or externally linked.

   The CKAN DataStore extension provides an ad hoc database for storage of structured data from CKAN resources. Data can be pulled out of resource files and stored in the DataStore.

a. Create a Python virtual environment (virtualenv) to install DataPusher into, and activate it:

   .. parsed-literal::

      sudo mkdir -p /usr/lib/ckan/datapusher
      sudo chown \`whoami\` /usr/lib/ckan/datapusher
      virtualenv --no-site-packages /usr/lib/ckan/datapusher
      . /usr/lib/ckan/datapusher/bin/activate

b. Install the DataPusher source code into your virtualenv:

   .. important::

      Please run all the commands below under the `ckan` directory:

      .. parsed-literal::

         cd /usr/lib/ckan/datapusher/

   Install the DataPusher：

   .. parsed-literal::

      pip install -e 'git+https://github.com/ckan/datapusher.git#egg=datapusher'

c. Install the Python modules that DataPusher requires into your virtualenv:

   .. parsed-literal::

      pip install -r /usr/lib/ckan/datapusher/src/datapusher/requirements.txt

---------------------------------
4. Create the FireStore directory
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
5. Setup a PostgreSQL database
------------------------------

a. Create a database user:

   .. parsed-literal::

      sudo -u postgres createuser -S -D -R -P ckan_default

b. Create a new database:

   .. parsed-literal::

      sudo -u postgres createdb -O ckan_default ckan_default -E utf-8

c. Install the PostGIS:

   .. parsed-literal::

      sudo apt-get install postgresql-9.5-postgis-2.2 python-dev libxml2-dev libxslt1-dev libgeos-c1v5
      sudo -u postgres psql -d ckan_default -f /usr/share/postgresql/9.5/contrib/postgis-2.2/postgis.sql
      sudo -u postgres psql -d ckan_default -f /usr/share/postgresql/9.5/contrib/postgis-2.2/spatial_ref_sys.sql
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

      gunzip -c main_db.sql.gz | sudo -u postgres psql ckan_default
      gunzip -c datastore_db.sql.gz | sudo -u postgres psql datastore_default

----------------------------
6. Create a CKAN config file
----------------------------

a. Create a directory to contain the site's config files:

   .. parsed-literal::

      sudo mkdir -p /etc/ckan/default
      sudo chown -R \`whoami\` /etc/ckan/

b. Create the CKAN config file via paster:

   .. important::

      (For |site_name| administrator) Please ignore the following step. c
      and use ``production.ini`` the in the ``configs.tar.gz``.

   .. important::

      The virtualenv has to remain active when running the paster command.
      You can always reactivate the virtualenv with this command: ::

      . /usr/lib/ckan/default/bin/activate

   .. parsed-literal::

      paster make-config ckan /etc/ckan/default/development.ini

c. Edit the development.ini file in a text editor, changing the following options:

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

      ## Site Settings
      ckan.site_url = http://127.0.0.1:5000

      ## Plugins Settings
      ckan.plugins = data_depositario wikidatakeyword stats datastore datapusher
                     resource_proxy recline_view text_view image_view
                     webpage_view recline_grid_view recline_map_view
                     pdf_view spatial_metadata spatial_query
                     geo_view geojson_view wmts_view shp_view
                     scheming_datasets repeating

      ## Front-End Settings
      licenses_group_url = file:///usr/lib/ckan/default/src/ckanext-data-depositario/ckanext/data_depositario/public/license_list.json

      ## Storage Settings
      ckan.storage_path = /var/lib/ckan/default

      ## Datapusher Settings
      ckan.datapusher.url = http://0.0.0.0:8800/

      ## Schema Settings
      ## Add these settings
      scheming.presets = ckanext.scheming:presets.json
                         ckanext.repeating:presets.json
                         ckanext.data_depositario:presets.json
                         ckanext.wikidatakeyword:presets.json
      scheming.dataset_schemas = ckanext.data_depositario:scheming.json

      ## Spatial Settings
      ## Add these settings
      ckanext.spatial.search_backend = solr-spatial-field

      ## ckanext-data-depositario Settings
      ## Add these settings
      ## GMAP_AKI_KEY is the API key for Google Maps
      ckanext.data_depositario.gmap.api_key = GMAP_AKI_KEY

-------------------------------------------------------
7. Setup Solr (with Chinese and spatial search support)
-------------------------------------------------------

.. note::

   This section is adapted from `How To Install Solr 5.2.1 on Ubuntu 14.04 <https://www.digitalocean.com/community/tutorials/how-to-install-solr-5-2-1-on-ubuntu-14-04>`_ by `DigitalOcean™ Inc. <https://www.digitalocean.com/>`_ licensed under `Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International <https://creativecommons.org/licenses/by-nc-sa/4.0/>`_.

a. Download and extract the service installation file:

   .. parsed-literal::

      cd ~
      wget http://archive.apache.org/dist/lucene/solr/5.5.5/solr-5.5.5.tgz
      tar xzf solr-5.5.5.tgz solr-5.5.5/bin/install_solr_service.sh --strip-components=2

b. Install Solr as a service using the script:

   .. parsed-literal::

      sudo bash ./install_solr_service.sh solr-5.5.5.tgz

c. Create the Solr configset for CKAN:

   .. parsed-literal::

      sudo -u solr mkdir -p /var/solr/data/configsets/ckan/conf
      sudo ln -s /usr/lib/ckan/default/src/ckanext-data-depositario/solr/schema.xml /var/solr/data/configsets/ckan/conf/schema.xml
      sudo -u solr cp /opt/solr/server/solr/configsets/basic_configs/conf/solrconfig.xml /var/solr/data/configsets/ckan/conf/.
      sudo -u solr touch /var/solr/data/configsets/ckan/conf/protwords.txt
      sudo -u solr touch /var/solr/data/configsets/ckan/conf/synonyms.txt

d. Download Chinese tokenizer ``Mmseg4j`` and copy it to the Solr directory:

   .. parsed-literal::

      wget http://central.maven.org/maven2/com/chenlb/mmseg4j/mmseg4j-core/1.10.0/mmseg4j-core-1.10.0.jar
      wget http://central.maven.org/maven2/com/chenlb/mmseg4j/mmseg4j-solr/2.3.1/mmseg4j-solr-2.3.1.jar
      sudo cp mmseg4j-\*.jar /opt/solr/server/solr-webapp/webapp/WEB-INF/lib/.

e. Download geometry library JTS Topology Suite 1.13 (or above) and copy it to the Solr directory:

   .. parsed-literal::

      wget -O jts-1.13.jar https://search.maven.org/remotecontent?filepath=com/vividsolutions/jts/1.13/jts-1.13.jar
      sudo cp jts-1.13.jar /opt/solr/server/solr-webapp/webapp/WEB-INF/lib/.

f. Restart Solr:

   .. parsed-literal::

      sudo service solr restart

g. Create a new Solr core called ``ckan`` by entering the following link in a web browser:

   http://127.0.0.1:8983/solr/admin/cores?action=CREATE&name=ckan&configSet=ckan

h. Open http://127.0.0.1:8983/solr/#/ckan in a web browser, and you should see the Solr front page.

i. Modify /etc/ckan/default/development.ini with Solr url:

   .. parsed-literal::

      solr_url = http://127.0.0.1:8983/solr/ckan

-------------------------
8. Create database tables
-------------------------

.. important::

   (For |site_name| administrator) Please ignore this step.

a. Create the database tables via paster:

   .. parsed-literal::

      paster --plugin=ckan db init -c /etc/ckan/default/development.ini

b. You should see Initialising DB: SUCCESS.

c. Then you can use this connection to set the permissions for DataStore:

   .. parsed-literal::

      paster --plugin=ckan datastore set-permissions -c /etc/ckan/default/development.ini | sudo -u postgres psql --set ON_ERROR_STOP=1

----------------------
9. Link to ``who.ini``
----------------------

.. parsed-literal::

   ln -s /usr/lib/ckan/default/src/ckan/who.ini /etc/ckan/default/who.ini

----------------------------
10. Creating a sysadmin user
----------------------------

.. important::

   (For |site_name| administrator) Please ignore this step.

You have to create your first CKAN sysadmin user from the command line. For example, to create a user called `admin` and make him a sysadmin:

.. parsed-literal::

   paster --plugin=ckan sysadmin add admin email=admin@localhost -c /etc/ckan/default/development.ini

-----------------------------------------
11. Serve CKAN under a development server
-----------------------------------------

a. Run the DataPusher:

   .. parsed-literal::

      . /usr/lib/ckan/datapusher/bin/activate
      JOB_CONFIG='/usr/lib/ckan/datapusher/src/datapusher/deployment/datapusher_settings.py' python /usr/lib/ckan/datapusher/src/datapusher/wsgi.py

b. Open another terminal and use the Paste development server to serve CKAN from the command-line:

   .. parsed-literal::

      . /usr/lib/ckan/default/bin/activate
      paster serve /etc/ckan/default/development.ini

c. Open http://127.0.0.1:5000/ in a web browser, and you should see the CKAN front page.

Now that you've installed CKAN.
