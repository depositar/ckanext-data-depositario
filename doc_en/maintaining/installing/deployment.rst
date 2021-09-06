==========================
Deploying a source install
==========================

Since CKAN is written mainly in Pylons and supports WSGI,
CKAN can be used with a number of different web server and deployment configurations.

This guide explains how to deploy CKAN using Gunicorn and proxied 
with Nginx on an Ubuntu server. These instructions have been tested on Ubuntu 16.04.

-----------------------------------
1. Create a ``production.ini`` file
-----------------------------------

.. important::

   (For |site_name| administrator) Please ignore this step
   and use ``production.ini`` the in the ``configs.tar.gz``.

.. parsed-literal::

   cp /etc/ckan/default/development.ini /etc/ckan/default/production.ini

-------------------------------------
2. Modify the ``production.ini`` file
-------------------------------------

.. important::

   (For |site_name| administrator) Please ignore this step.

Edit the production.ini  file in a text editor, changing the [server:main] and [app:main] sections
as follows:

.. parsed-literal::

   [server:main]
   #use = egg:Paste#http
   #host = 0.0.0.0
   #port = 5000
   use = egg:gunicorn#main
   bind = unix:/var/run/gunicorn/ckan_socket.sock
   preload = true
   ## The Error log file to write to.
   errorlog = /etc/ckan/default/ckan.log
   loglevel = warning
   ## ``USER`` is the owner of ``/etc/ckan/default``
   user = USER
   group = www-data
   umask = 0113

   [app:main]
   ...
   ## Site Settings

   ckan.site_url = http://127.0.0.1

   ## XLoader Settings
   ## Refer to the CKAN database
   ckanext.xloader.jobs_db.uri = postgresql://ckan_default:pass@localhost/ckan_default

-------------------
3. Install Gunicorn
-------------------

Install Gunicorn into a Python virtual environment:

.. parsed-literal::

   . /usr/lib/ckan/default/bin/activate
   pip install gunicorn

----------------------------------
4. Set the startup script for CKAN
----------------------------------

a. Create a Systemd service for CKAN:

   .. parsed-literal::

      sudo vi /etc/systemd/system/ckan.service

b. In the vi editor, add the following contents:

   .. parsed-literal::

      [Unit]
      Description=Gunicorn instance to serve CKAN
      After=network.target

      [Service]
      WorkingDirectory=/usr/lib/ckan/default/src/ckan
      RuntimeDirectory=gunicorn
      ExecStart=/usr/lib/ckan/default/bin/gunicorn --paste /etc/ckan/default/production.ini
      ExecReload=/bin/kill -s HUP $MAINPID
      ExecStop=/bin/kill -s TERM $MAINPID
      StandardError=syslog
      PrivateTmp=true

      [Install]
      WantedBy=multi-user.target

c. Start the Systemd service:

   .. parsed-literal::

      sudo systemctl enable ckan

d. To start the installed service, run the following command:

   .. parsed-literal::

      sudo service ckan start

e. You can check the site status via:

   .. parsed-literal::

      sudo service ckan status

   You should now be able to see the following output:

   .. parsed-literal::

      ● ckan.service - Gunicorn instance to serve CKAN
         Loaded: loaded (/etc/systemd/system/ckan.service; enabled; vendor preset: enabled)
         Active: active (running) since Thr 2017-12-14 14:36:37 CST; 2s ago
        Process: 20152 ExecStop=/bin/kill -s TERM $MAINPID (code=exited, status=0/SUCCESS)
       Main PID: 20191 (gunicorn)
          Tasks: 2
         Memory: 88.0M
            CPU: 1.596s
         CGroup: /system.slice/ckan.service
                 ├─20191 /usr/lib/ckan/default/bin/python2 /usr/lib/ckan/default/bin/gunicorn --paste /etc/ckan/default/production.ini
                 └─20198 /usr/lib/ckan/default/bin/python2 /usr/lib/ckan/default/bin/gunicorn --paste /etc/ckan/default/production.ini

f. You can stop the Systemd service by:

   .. parsed-literal::

      sudo service ckan stop

-------------------------------------
5. Set the startup script for XLoader
-------------------------------------

.. note::

   This XLoader is a service that automatically uploads data to the DataStore from suitable files (like CSV or Excel files), whether uploaded to CKAN’s FileStore or externally linked.

a. Install Supervisor:

   .. parsed-literal::

      sudo apt install supervisor

b. Copy the configuration file template:

   .. parsed-literal::

      sudo cp /usr/lib/ckan/default/src/ckan/ckan/config/supervisor-ckan-worker.conf /etc/supervisor/conf.d

c. Restart Supervisor:

   .. parsed-literal::

      sudo service supervisor restart

d. You can check the status via:

   .. parsed-literal::

      sudo supervisorctl status

e. You can restart the worker via:

   .. parsed-literal::

      sudo supervisorctl restart ckan-worker:*

--------------------------
6. Install and setup Nginx
--------------------------

a. Install Nginx:

   .. parsed-literal::

      sudo apt-get install nginx

b. Create your site's Nginx config file at /etc/nginx/sites-available/ckan, with the
following contents:

   .. parsed-literal::

      proxy_cache_path /tmp/nginx_cache levels=1:2 keys_zone=cache:30m max_size=250m;

      server {
          listen 80;
          server_name 127.0.0.1;
          client_max_body_size 1000M;
          access_log /var/log/nginx/ckan_access.log;
          error_log /var/log/nginx/ckan_error.log error;

          location / {
              try_files $uri @proxy_to_app;
          }

          location @proxy_to_app {
              proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
              # enable this if and only if you use HTTPS
              # proxy_set_header X-Forwarded-Proto https;
              proxy_set_header Host $http_host;
              # we don't want nginx trying to do something clever with
              # redirects, we set the Host: header above already.
              proxy_redirect off;
              proxy_pass http://unix:/var/run/gunicorn/ckan_socket.sock;
          }
      }

c. To prevent conflicts, disable your default Nginx sites. Finally, enable your CKAN site in Nginx:

   .. parsed-literal::

      sudo rm /etc/nginx/sites-enabled/default
      sudo ln -s /etc/nginx/sites-available/ckan /etc/nginx/sites-enabled/ckan

d. Restart Nginx:

   .. parsed-literal::

      sudo service nginx restart

----------------
7. Test the site
----------------

You should now be able to visit your server (at http://127.0.0.1) in a web browser
and see your new CKAN instance.
