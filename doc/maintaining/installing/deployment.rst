============
佈署至伺服器
============

由於 CKAN 使用 Flask 開發，只要使用任何支援 WSGI 標準的網頁伺服器（及相關套件）即可佈署 CKAN。以下示範以 nginx 與 uwsgi 進行部署。

---------------------
1. 建立 WSGI 腳本檔案
---------------------

.. parsed-literal::

   sudo cp /usr/lib/ckan/default/src/ckan/wsgi.py /etc/ckan/default/

-------------------
2. 建立 WSGI 伺服器
-------------------

在虛擬環境下安裝 uwsgi，與建立其設定檔

.. parsed-literal::

   . /usr/lib/ckan/default/bin/activate
   pip install uwsgi
   sudo cp /usr/lib/ckan/default/src/ckan/ckan-uwsgi.ini /etc/ckan/default/

開啟 /etc/ckan/default/ckan-uwsgi.ini，並修改 uid 與 gid 為虛擬環境擁有者

-------------------
3. 修改 CKAN 設定檔
-------------------

.. important::

   （供本平台管理員資訊）請忽略此步驟，直接使用備份之 production.ini 設定檔。

開啟 ckan.ini，並修改 [app:main] 的相關設定如下

.. parsed-literal::

   ## Site Settings

   ckan.site_url = http://127.0.0.1

------------------
4. 安裝 Supervisor
------------------

.. parsed-literal::

   sudo apt-get install supervisor

------------------------
5. 設定開機自動執行 CKAN
------------------------

a. 建立 CKAN 使用之 Supervisor 設定檔

   .. parsed-literal::

      sudo vi /etc/supervisor/conf.d/ckan-uwsgi.conf

b. 在開啟的 vi 編輯器中，輸入以下內容

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

-------------------------------
6. 設定開機自動執行 Datapusher+
-------------------------------

.. parsed-literal::

   sudo mkdir -p /var/log/ckan
   sudo cp /usr/lib/ckan/default/src/ckan/ckan/config/supervisor-ckan-worker.conf /etc/supervisor/conf.d

----------------------
7. 重新啟動 Supervisor
----------------------

.. parsed-literal::

   sudo service supervisor restart

你可以使用以下指令確認 Supervisor 是否正常運作

.. parsed-literal::

   sudo supervisorctl status

你可以使用以下指令重新啟動 CKAN 與 worker

.. parsed-literal::

   sudo supervisorctl restart ckan-uwsgi:*
   sudo supervisorctl restart ckan-worker:*

--------------------------
8. 安裝與設定 nginx 伺服器
--------------------------

a. 安裝 nginx

   .. parsed-literal::

      sudo apt-get install nginx

b. 新增 /etc/nginx/sites-available/ckan 檔案，並編輯加入以下設定

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

c. 建立 alies 至 sites-enabled 以啟用剛才新增之設定（並停用預設設定檔）

   .. parsed-literal::

      sudo rm /etc/nginx/sites-enabled/default
      sudo ln -s /etc/nginx/sites-available/ckan /etc/nginx/sites-enabled/ckan

d. 重新啟動 nginx

   .. parsed-literal::

      sudo service nginx restart

-----------
9. 執行測試
-----------

打開瀏覽器，前往 http://127.0.0.1/ ，若能看到頁面，代表您已經完成所有佈署設定。
