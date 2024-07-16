==========================
Deploying a source install
==========================

Since CKAN is written mainly in Flask and supports WSGI,
CKAN can be used with a number of different web server and deployment configurations.

This guide explains how to deploy CKAN using uwsgi and proxied with nginx.

------------------------------
1. Create the WSGI script file
------------------------------

.. parsed-literal::

   sudo cp /usr/lib/ckan/default/src/ckan/wsgi.py /etc/ckan/default/

-------------------------
2. Create the WSGI Server
-------------------------

Install uwsgi into a Python virtual environment and create the configuration file:

.. parsed-literal::

   . /usr/lib/ckan/default/bin/activate
   pip install uwsgi
   sudo cp /usr/lib/ckan/default/src/ckan/ckan-uwsgi.ini /etc/ckan/default/

Edit the /etc/ckan/default/ckan-uwsgi.ini and replace the uid and pid with
the owner of the virtual environment.

--------------------------------
3. Modify the configuration file
--------------------------------

.. important::

   (For |site_name| administrator) Please ignore this step
   and use the backed up ``production.ini``.

Edit the production.ini file in a text editor, changing the [app:main] sections
as follows:

.. parsed-literal::

   ## Site Settings

   ckan.site_url = http://127.0.0.1

---------------------
4. Install Supervisor
---------------------

.. parsed-literal::

   sudo apt-get install supervisor

----------------------------------
5. Set the startup script for CKAN
----------------------------------

a. Create the Supervisor configuration for CKAN:

   .. parsed-literal::

      sudo vi /etc/supervisor/conf.d/ckan-uwsgi.conf

b. In the vi editor, add the following contents:

   .. parsed-literal::

      [program:ckan-uwsgi]

      command=/usr/lib/ckan/default/bin/uwsgi -i /etc/ckan/default/ckan-uwsgi.ini

      ; Start just a single worker. Increase this number if you have many or
      ; particularly long running background jobs.
      numprocs=1
      process_name=%(program_name)s-%(process_num)02d

      ; Log files - change this to point to the existing CKAN log files
      stdout_logfile=/etc/ckan/default/uwsgi.OUT
      stderr_logfile=/etc/ckan/default/uwsgi.ERR

      ; Make sure that the worker is started on system start and automatically
      ; restarted if it crashes unexpectedly.
      autostart=true
      autorestart=true

      ; Number of seconds the process has to run before it is considered to have
      ; started successfully.
      startsecs=10

      ; Need to wait for currently executing tasks to finish at shutdown.
      ; Increase this if you have very long running tasks.
      stopwaitsecs = 600

      ; Required for uWSGI as it does not obey SIGTERM.
      stopsignal=QUIT

-----------------------------------------
6. Set the startup script for DataPusher+
-----------------------------------------

.. parsed-literal::

   sudo mkdir -p /var/log/ckan
   sudo cp /usr/lib/ckan/default/src/ckan/ckan/config/supervisor-ckan-worker.conf /etc/supervisor/conf.d

---------------------
7. Restart Supervisor
---------------------

.. parsed-literal::

   sudo service supervisor restart

You can check the status via:

.. parsed-literal::

   sudo supervisorctl status

You can restart CKAN and workers via:

.. parsed-literal::

   sudo supervisorctl restart ckan-uwsgi:*
   sudo supervisorctl restart ckan-worker:*

--------------------------
8. Install and setup nginx
--------------------------

a. Install nginx:

   .. parsed-literal::

      sudo apt-get install nginx

b. Create your site's Nginx config file at /etc/nginx/sites-available/ckan, with the following contents:

   .. parsed-literal::

      proxy_temp_path /tmp/nginx_proxy 1 2;

      server {
          client_max_body_size 100M;
          location / {
              proxy_pass http://127.0.0.1:8080/;
              proxy_set_header X-Forwarded-For $remote_addr;
              proxy_set_header Host $host;
          }
      }

c. To prevent conflicts, disable your default nginx sites. Finally, enable your CKAN site in nginx:

   .. parsed-literal::

      sudo rm /etc/nginx/sites-enabled/default
      sudo ln -s /etc/nginx/sites-available/ckan /etc/nginx/sites-enabled/ckan

d. Restart nginx:

   .. parsed-literal::

      sudo service nginx restart

----------------
9. Test the site
----------------

You should now be able to visit your server (at http://127.0.0.1) in a web browser
and see your new CKAN instance.
