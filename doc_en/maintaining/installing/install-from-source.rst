================================
Installing depositar from source
================================

This section describes how to install |site_name| from source on an Ubuntu 22.04 server.

--------------------------------
1. Install the required packages
--------------------------------

.. parsed-literal::

   sudo apt install uchardet python3-dev libpq-dev python3-pip python3-venv git redis-server postgresql openjdk-11-jdk

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

b. Install CKAN into your virtualenv:

   .. important::

      Please run all the commands below under the `ckan` directory:

      .. parsed-literal::

         cd /usr/lib/ckan/default/

   .. parsed-literal::

      pip install -e 'git+https://github.com/depositar/ckan.git#egg=ckan[requirements]'

c. Install customized extesion into your virtualenv:

   .. parsed-literal::

      pip install -e 'git+https://github.com/depositar/ckanext-data-depositario.git#egg=ckanext-data-depositario'

d. Install other required Python modules into your virtualenv:

   .. parsed-literal::

      pip install -r /usr/lib/ckan/default/src/ckanext-data-depositario/requirements.txt
      pip install -r /usr/lib/ckan/default/src/ckanext-spatial/pip-requirements.txt
      pip install -r /usr/lib/ckan/default/src/ckanext-dcat/requirements.txt
      pip install -r /usr/lib/ckan/default/src/datapusher-plus/requirements.txt

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

c. Create a new database user and a new database for DataStore:

   .. note::

      The CKAN DataStore extension provides an ad hoc database for storage of structured data from CKAN resources. Data can be pulled out of resource files and stored in the DataStore.

   .. parsed-literal::

      sudo -u postgres createuser -S -D -R -P -l datastore_default
      sudo -u postgres createdb -O ckan_default datastore_default -E utf-8


d. (For |site_name| administrator) Restore database backup:

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

      The virtualenv has to remain active when running the ckan command.
      You can always reactivate the virtualenv with this command: ::

      . /usr/lib/ckan/default/bin/activate

   .. parsed-literal::

      ckan generate config /etc/ckan/default/ckan.ini
      ckan config-tool /etc/ckan/default/ckan.ini -f /usr/lib/ckan/default/src/ckanext-data-depositario/config/custom_options.ini
      sed -i -e '/^\\[app:main\\]/a\\\\' -e '/^\\[app:main\\]/r /usr/lib/ckan/default/src/ckanext-data-depositario/config/custom_options_extra.ini' /etc/ckan/default/ckan.ini

c. Edit the ckan.ini file in a text editor, changing the following options:

   .. note::

      The settings below is the minimum requirements to run the CKAN.

   .. parsed-literal::

      ## Database Settings. This should refer to the database we created in :ref:`postgres-setup` above
      ## Replace ``pass`` with the ``CKAN database`` password that you created
      sqlalchemy.url = postgresql://ckan_default:pass@localhost/ckan_default
      ## Replace ``pass`` with the ``CKAN database`` password that you created
      ckan.datastore.write_url = postgresql://ckan_default:pass@localhost/datastore_default
      ## Replace ``pass`` with the ``DataStore database`` password that you created
      ckan.datastore.read_url = postgresql://datastore_default:pass@localhost/datastore_default

      ## GMAP_AKI_KEY is the API key for Google Maps
      ckanext.data_depositario.gmap.api_key = GMAP_AKI_KEY

-------------------------------------------------------
6. Setup Solr (with Chinese and spatial search support)
-------------------------------------------------------

.. note::

   This section is adapted from `How To Install Solr 5.2.1 on Ubuntu 14.04 <https://www.digitalocean.com/community/tutorials/how-to-install-solr-5-2-1-on-ubuntu-14-04>`_ by `DigitalOcean™ Inc. <https://www.digitalocean.com/>`_ licensed under `Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International <https://creativecommons.org/licenses/by-nc-sa/4.0/>`_.

a. Download and extract the service installation file:

   .. parsed-literal::

      cd ~
      wget http://archive.apache.org/dist/lucene/solr/8.11.3/solr-8.11.3.tgz
      tar xzf solr-8.11.3.tgz solr-8.11.3/bin/install_solr_service.sh --strip-components=2

b. Install Solr as a service using the script:

   .. parsed-literal::

      sudo bash ./install_solr_service.sh solr-8.11.3.tgz

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

      wget https://repo1.maven.org/maven2/org/locationtech/jts/jts-core/1.19.0/jts-core-1.19.0.jar
      sudo cp jts-core-1.19.0.jar /opt/solr/server/solr-webapp/webapp/WEB-INF/lib/.

f. Restart Solr:

   .. parsed-literal::

      sudo service solr restart

g. Open http://127.0.0.1:8983/solr/#/ckan in a web browser, and you should see the Solr front page.

-------------------------
7. Create database tables
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

c. Set up the ARK database:

   .. parsed-literal::

      ckan -c /etc/ckan/default/ckan.ini ark initdb

   You should see ARK table created.

d. Set up the DataPusher+ database:

   .. code-block:: shell

      ckan -c /etc/ckan/default/ckan.ini datapusher init-db

   You should see Datapusher Plus tables created.

----------------------------
8. Creating a sysadmin user
----------------------------

.. important::

   (For |site_name| administrator) Please ignore this step.

Set password for the default CKAN sysadmin user from the command line.

.. parsed-literal::

   ckan -c /etc/ckan/default/ckan.ini user setpass default

--------------------
9. Setup DataPusher+
--------------------

.. note::

   This DataPusher+ is an extension that automatically uploads data to the DataStore from suitable files (like CSV or Excel files), whether uploaded to CKAN’s FileStore or externally linked, to provide functions such as the :doc:`../../user-guide/data-api`.

a. Download and install qsv:

   .. code-block:: shell

      cd ~
      wget https://github.com/jqnatividad/qsv/releases/download/0.128.0/qsv-0.128.0-x86_64-unknown-linux-gnu.zip
      unzip qsv-0.128.0-x86_64-unknown-linux-gnu.zip
      rm qsv-0.128.0-x86_64-unknown-linux-gnu.zip
      sudo mv qsv* /usr/local/bin

b. Create an API token for DataPusher+:

   .. code-block:: shell

      ckan -c /etc/ckan/default/ckan.ini user token add default datapusher-plus

c. Update the CKAN config file:

   .. code-block:: ini
      :caption: /etc/ckan/default/ckan.ini

      ckan.datapusher.api_token = <The newly created token>

-----------------------------------------
10. Serve CKAN under a development server
-----------------------------------------

a. Run the DataPusher+:

   .. parsed-literal::

      ckan -c /etc/ckan/default/ckan.ini jobs worker

b. Open another terminal and use the Paste development server to serve CKAN from the command-line:

   .. parsed-literal::

      . /usr/lib/ckan/default/bin/activate
      ckan -c /etc/ckan/default/development.ini

c. Open http://127.0.0.1:5000/ in a web browser, and you should see the CKAN front page.

Now that you've installed CKAN.
