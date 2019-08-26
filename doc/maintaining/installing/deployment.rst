============
佈署至伺服器
============

由於 CKAN 使用 pylons 開發，只要使用任何支援 WSGI 標準的網頁伺服器（及相關套件）即可佈署 CKAN。以下示範以 nginx 與 Gunicorn 進行部署。

-----------------------------
1. 新增 production.ini 設定檔
-----------------------------

.. important::

   （供本平台管理員資訊）請忽略此步驟，直接使用備份之 production.ini 設定檔。

.. parsed-literal::

   cp /etc/ckan/default/development.ini /etc/ckan/default/production.ini

----------------------
2. 修改 production.ini
----------------------

.. important::

   （供本平台管理員資訊）請忽略此步驟。

開啟 production.ini，並修改 [server:main] 與 [app:main] 的相關設定如下

.. parsed-literal::

   [server:main]
   #use = egg:Paste#http
   #host = 0.0.0.0
   #port = 5000
   use = egg:gunicorn#main
   bind = unix:/var/run/gunicorn/ckan_socket.sock
   preload = true
   ## CKAN 執行過程若有錯誤將輸出於此檔案
   errorlog = /etc/ckan/default/ckan.log
   loglevel = warning
   ## USER 為目錄 /etc/ckan/default 擁有者
   user = USER
   group = www-data
   umask = 0113

   [app:main]
   ...
   ## Site Settings

   ckan.site_url = http://127.0.0.1

----------------
3. 安裝 Gunicorn
----------------

在虛擬環境下安裝 Gunicorn

.. parsed-literal::

   . /usr/lib/ckan/default/bin/activate
   pip install gunicorn

   . /usr/lib/ckan/datapusher/bin/activate
   pip install gunicorn

------------------------
4. 設定開機自動執行 CKAN
------------------------

a. 建立 Systemd 服務

   .. parsed-literal::

      sudo vi /etc/systemd/system/ckan.service

b. 在開啟的 vi 編輯器中，輸入以下內容

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

c. 啟用此 Systemd 服務

   .. parsed-literal::

      sudo systemctl enable ckan

d. 之後便可使用以下指令啟動網站

   .. parsed-literal::

      sudo service ckan start

e. 你可以使用以下指令確認網站是否正常運作

   .. parsed-literal::

      sudo service ckan status

   你應該可以看到類似下面的輸出

   .. parsed-literal::

      ● ckan.service - Gunicorn instance to serve CKAN
         Loaded: loaded (/etc/systemd/system/ckan.service; enabled; vendor preset: enabled)
         Active: active (running) since 四 2017-12-14 14:36:37 CST; 2s ago
        Process: 20152 ExecStop=/bin/kill -s TERM $MAINPID (code=exited, status=0/SUCCESS)
       Main PID: 20191 (gunicorn)
          Tasks: 2
         Memory: 88.0M
            CPU: 1.596s
         CGroup: /system.slice/ckan.service
                 ├─20191 /usr/lib/ckan/default/bin/python2 /usr/lib/ckan/default/bin/gunicorn --paste /etc/ckan/default/production.ini
                 └─20198 /usr/lib/ckan/default/bin/python2 /usr/lib/ckan/default/bin/gunicorn --paste /etc/ckan/default/production.ini

f. 你可以使用以下指令停止網站

   .. parsed-literal::

      sudo service ckan stop

------------------------------
5. 設定開機自動執行 DataPusher
------------------------------

.. note::

   DataPusher 是一個 CKAN 的擴充套件，當使用者新增結構資料（如 CSV 或 XLS 檔案，無論為上傳至本機的檔案或僅有連結）至 CKAN 時，DataPusher 會自動上傳資料內容至 CKAN 的 DataStore 資料庫，以提供 :ref:`data_api` 等功能。

a. 建立 Systemd 服務

   .. parsed-literal::

      sudo vi /etc/systemd/system/datapusher.service

b. 在開啟的 vi 編輯器中，輸入以下內容

   .. parsed-literal::

      [Unit]
      Description=Gunicorn instance to serve DataPusher
      After=network.target

      [Service]
      RuntimeDirectory=gunicorn
      Environment=JOB_CONFIG=/usr/lib/ckan/datapusher/src/datapusher/deployment/datapusher_settings.py
      ExecStart=/usr/lib/ckan/datapusher/bin/gunicorn wsgi:app
      ExecReload=/bin/kill -s HUP $MAINPID
      ExecStop=/bin/kill -s TERM $MAINPID
      StandardOutput=null
      StandardError=null
      PrivateTmp=true

      [Install]
      WantedBy=multi-user.target

c. 啟用此 Systemd 服務

   .. parsed-literal::

      sudo systemctl enable datapusher

d. 之後便可使用以下指令啟動 DataPusher

   .. parsed-literal::

      sudo service datapusher start

e. 你可以使用以下指令確認 DataPusher 是否正常運作：

   .. parsed-literal::

      sudo service datapusher status

   你應該可以看到類似下面的輸出：

   .. parsed-literal::

      ● datapusher.service - Gunicorn instance to serve DataPusher
         Loaded: loaded (/etc/systemd/system/datapusher.service; enabled; vendor preset: enabled)
         Active: active (running) since 四 2017-12-14 14:48:44 CST; 2min 44s ago
        Process: 20571 ExecStop=/bin/kill -s TERM $MAINPID (code=exited, status=0/SUCCESS)
       Main PID: 20626 (gunicorn)
          Tasks: 2
         Memory: 46.0M
            CPU: 1.790s
         CGroup: /system.slice/datapusher.service
                 ├─20626 /usr/lib/ckan/datapusher/bin/python2 /usr/lib/ckan/datapusher/bin/gunicorn wsgi:app
                 └─20673 /usr/lib/ckan/datapusher/bin/python2 /usr/lib/ckan/datapusher/bin/gunicorn wsgi:app

f. 你可以使用以下指令停止 DataPusher

   .. parsed-literal::

      sudo service datapusher stop

--------------------------
6. 安裝與設定 nginx 伺服器
--------------------------

a. 安裝 nginx

   .. parsed-literal::

      sudo apt-get install nginx

b. 新增 /etc/nginx/sites-available/ckan 檔案，並編輯加入以下設定

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

c. 建立 alies 至 sites-enabled 以啟用剛才新增之設定（並刪除預設設定檔）

   .. parsed-literal::

      sudo rm /etc/nginx/sites-enabled/default
      sudo ln -s /etc/nginx/sites-available/ckan /etc/nginx/sites-enabled/ckan

d. 重新啟動 nginx

   .. parsed-literal::

      sudo service nginx restart

-----------
7. 執行測試
-----------

打開瀏覽器，前往 http://127.0.0.1/ ，若能看到頁面，代表您已經完成所有佈署設定。
