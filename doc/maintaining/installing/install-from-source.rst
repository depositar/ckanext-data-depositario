============
自原始碼安裝
============

本節將描述如何自原始碼安裝本平台（|site_name|）使用之 CKAN 軟體。示範系統為 Ubuntu 22.04。

---------------
1. 安裝必須套件
---------------

.. parsed-literal::

   sudo apt install uchardet python3-dev libpq-dev python3-pip python3-venv git redis-server postgresql openjdk-11-jdk

-------------------------------
2. 安裝 CKAN 於 Python 虛擬環境
-------------------------------

a. 新增一個 Python 虛擬環境（virtualenv）供 CKAN 使用，並進入該虛擬環境

   .. parsed-literal::

      sudo mkdir -p /usr/lib/ckan/default
      sudo chown \`whoami\` /usr/lib/ckan/default
      python3 -m venv /usr/lib/ckan/default
      . /usr/lib/ckan/default/bin/activate

   .. important::

      上述指令中的最後一個用以啟動虛擬環境。在剩餘安裝步驟中需維持此虛擬環境於執行狀態，否則安裝作業可能會失敗。當虛擬環境執行時，命令提示字元（shell prompt）會有類似以下前綴： ::

        (default) $ _

      若您於登出後再次登入，將會離開目前執行中的虛擬環境。您可隨時執行以下指令以返回虛擬環境： ::

        . /usr/lib/ckan/default/bin/activate

b. 安裝 CKAN 於虛擬環境

   .. important::

      執行以下指令時，請確定您位於虛擬環境根目錄：

      .. parsed-literal::

         cd /usr/lib/ckan/default/

   .. parsed-literal::

      pip install -e 'git+https://github.com/depositar/ckan.git#egg=ckan[requirements]'

c. 安裝本平台客製套件

   .. parsed-literal::

      pip install -e 'git+https://github.com/depositar/ckanext-data-depositario.git#egg=ckanext-data-depositario'

d. 安裝其他所需 Python 套件

   .. parsed-literal::

      pip install -r /usr/lib/ckan/default/src/ckanext-data-depositario/requirements.txt
      pip install -r /usr/lib/ckan/default/src/ckanext-spatial/pip-requirements.txt
      pip install -r /usr/lib/ckan/default/src/ckanext-dcat/requirements.txt
      pip install -r /usr/lib/ckan/default/src/datapusher-plus/requirements.txt

----------------------
3. 建立 FileStore 目錄
----------------------

.. note::

   CKAN 的 FileStore 功能提供使用者上傳本機檔案作為資源，詳細請參考 :ref:`使用手冊 <add_resource>` 的說明。

.. parsed-literal::

   sudo mkdir -p /var/lib/ckan/default
   sudo chown \`whoami\` /var/lib/ckan/default
   sudo chmod u+rwx /var/lib/ckan/default

.. _postgres-setup:

-------------
4. 設定資料庫
-------------

a. 新增 CKAN 使用之 PostgreSQL 使用者

   .. parsed-literal::

      sudo -u postgres createuser -S -D -R -P ckan_default

b. 新增 CKAN 使用之資料庫

   .. parsed-literal::

      sudo -u postgres createdb -O ckan_default ckan_default -E utf-8

c. 本平台使用 CKAN 之 DataStore 功能，故需要建立相關之資料庫與使用者

   .. note::

      DataStore 是一個內建於 CKAN 的功能，透過一獨立資料庫儲存上傳至 CKAN 之結構資料內容。

   .. parsed-literal::

      sudo -u postgres createuser -S -D -R -P -l datastore_default
      sudo -u postgres createdb -O ckan_default datastore_default -E utf-8


d. （供本平台管理員資訊）自已備份資料庫還原

   還原資料庫指令如下

   .. parsed-literal::

      cat main_db.sql.gz | gunzip | sudo -u postgres psql ckan_default
      cat datastore_db.sql.gz | gunzip | sudo -u postgres psql datastore_default

-------------------------
5. 建立與修改 CKAN 設定檔
-------------------------

a. 新增放置 CKAN 設定檔之目錄

   .. parsed-literal::

      sudo mkdir -p /etc/ckan/default
      sudo chown -R \`whoami\` /etc/ckan/

b. 新增設定檔

   .. important::

      （供本平台管理員資訊）請忽略此處關於 CKAN 設定檔之相關說明，直接使用備份之 ``configs.tar.gz`` 壓縮檔內之 ``production.ini`` 檔案，以下提及設定檔時亦請忽略。

   .. important::

      執行任何 ckan 指令時，請確認是在 CKAN 虛擬環境下。您可隨時執行以下指令以返回虛擬環境： ::

      . /usr/lib/ckan/default/bin/activate

   .. parsed-literal::

      ckan generate config /etc/ckan/default/ckan.ini
      ckan config-tool /etc/ckan/default/ckan.ini -f /usr/lib/ckan/default/src/ckanext-data-depositario/config/custom_options.ini
      sed -i -e '/^\\[app:main\\]/a\\\\' -e '/^\\[app:main\\]/r /usr/lib/ckan/default/src/ckanext-data-depositario/config/custom_options_extra.ini' /etc/ckan/default/ckan.ini

c. 修改前面新增的 ckan.ini 檔案中對應之設定如下

   .. note::

      此僅為使本系統正常運作之最小需求設定。

   .. parsed-literal::

      ## 資料庫連線設定，請依照 :ref:`postgres-setup` 所新增的資料庫設定
      ## ``pass`` 請填寫 ``CKAN 資料庫`` 密碼
      sqlalchemy.url = postgresql://ckan_default:pass@localhost/ckan_default
      ## ``pass`` 請填寫 ``CKAN 資料庫`` 密碼
      ckan.datastore.write_url = postgresql://ckan_default:pass@localhost/datastore_default
      ## ``pass`` 請填寫 ``DataStore 資料庫`` 密碼
      ckan.datastore.read_url = postgresql://datastore_default:pass@localhost/datastore_default

      ## GMAP_AKI_KEY 請填入申請之 Google Maps API key
      ckanext.data_depositario.gmap.api_key = GMAP_AKI_KEY

------------------------------------
6. 安裝 Solr（含中文與空間搜尋支援）
------------------------------------

.. note::

   本部分參考 DigitalOcean™ Inc. 所編寫之 `How To Install Solr 5.2.1 on Ubuntu 14.04 <https://www.digitalocean.com/community/tutorials/how-to-install-solr-5-2-1-on-ubuntu-14-04>`_ ，該作品以 `創用 CC 姓名標示-非商業性-相同方式分享 4.0 國際 <https://creativecommons.org/licenses/by-nc-sa/4.0/>`_ 授權釋出。

a. 下載並解壓縮 Solr

   .. parsed-literal::

      cd ~
      wget http://archive.apache.org/dist/lucene/solr/8.11.3/solr-8.11.3.tgz
      tar xzf solr-8.11.3.tgz solr-8.11.3/bin/install_solr_service.sh --strip-components=2

b. 執行 Solr 安裝腳本

   .. parsed-literal::

      sudo bash ./install_solr_service.sh solr-8.11.3.tgz

c. 建立供 CKAN 使用之 Solr core

   .. parsed-literal::

      sudo -u solr /opt/solr/bin/solr create -c ckan
      sudo ln -sf /usr/lib/ckan/default/src/ckanext-data-depositario/solr/schema.xml /var/solr/data/ckan/conf/managed-schema

d. 下載中文斷詞函式庫 ``ik-analyzer``，並複製至 Solr 目錄

   .. parsed-literal::

      wget https://repo1.maven.org/maven2/com/github/magese/ik-analyzer/8.5.0/ik-analyzer-8.5.0.jar
      sudo cp ik-analyzer-8.5.0.jar /opt/solr/server/solr-webapp/webapp/WEB-INF/lib/.
      sudo mkdir /opt/solr/server/solr-webapp/webapp/WEB-INF/classes
      sudo ln -s /usr/lib/ckan/default/src/ckanext-data-depositario/solr/IKAnalyzer.cfg.xml /opt/solr/server/solr-webapp/webapp/WEB-INF/classes/.
      sudo ln -s /usr/lib/ckan/default/src/ckanext-data-depositario/solr/dic/words.dic /opt/solr/server/solr-webapp/webapp/WEB-INF/classes/words.dic

e. 下載空間搜尋函式庫 JTS 1.18 或以上版本並複製至 Solr 目錄

   .. parsed-literal::

      wget https://repo1.maven.org/maven2/org/locationtech/jts/jts-core/1.19.0/jts-core-1.19.0.jar
      sudo cp jts-core-1.19.0.jar /opt/solr/server/solr-webapp/webapp/WEB-INF/lib/.

f. 重新啟動 Solr

   .. parsed-literal::

      sudo service solr restart

g. 打開瀏覽器，前往 http://127.0.0.1:8983/solr/#/ckan ，若能看到畫面則代表安裝完成

---------------
7. 初始化資料庫
---------------

.. important::

   （供本平台管理員資訊）請忽略此步驟。

a. 初始化 CKAN 資料庫

   .. parsed-literal::

      ckan -c /etc/ckan/default/ckan.ini db init

   如果一切正常，則會看到此訊息：Initialising DB: SUCCESS

b. DataStore 資料庫設定

   .. parsed-literal::

      ckan -c /etc/ckan/default/ckan.ini datastore set-permissions | sudo -u postgres psql --set ON_ERROR_STOP=1

c. ARK 資料庫設定

   .. parsed-literal::

      ckan -c /etc/ckan/default/ckan.ini ark initdb

   如果一切正常，則會看到此訊息：ARK table created

d. DataPusher+ 資料庫設定

   .. code-block:: shell

      ckan -c /etc/ckan/default/ckan.ini datapusher init-db

   如果一切正常，則會看到此訊息：Datapusher Plus tables created

------------------------
8. 設定 CKAN 系統管理者
------------------------

.. important::

   （供本平台管理員資訊）請忽略此步驟。

請執行以下指令，以修改預設 CKAN 系統管理者密碼（帳號為 default）

.. parsed-literal::

   ckan -c /etc/ckan/default/ckan.ini user setpass default

-------------------
9. 設定 DataPusher+
-------------------

.. note::

   DataPusher+ 是一個 CKAN 的擴充套件，當使用者新增結構資料（如 CSV 或 XLS 檔案，無論為上傳至本機的檔案或僅有連結）至 CKAN 時，DataPusher+ 會自動上傳資料內容至 CKAN 的 DataStore 資料庫，以提供 :doc:`../../user-guide/data-api` 等功能。

a. 下載並安裝 qsv

   .. code-block:: shell

      cd ~
      wget https://github.com/jqnatividad/qsv/releases/download/0.128.0/qsv-0.128.0-x86_64-unknown-linux-gnu.zip
      unzip qsv-0.128.0-x86_64-unknown-linux-gnu.zip
      rm qsv-0.128.0-x86_64-unknown-linux-gnu.zip
      sudo mv qsv* /usr/local/bin

b. 新增 DataPusher+ 使用的 API token

   .. code-block:: shell

      ckan -c /etc/ckan/default/ckan.ini user token add default datapusher-plus

c. 更新 CKAN 設定檔

   .. code-block:: ini
      :caption: /etc/ckan/default/ckan.ini

      ckan.datapusher.api_token = <前一步驟取得的 token>

--------------------
10. 在開發環境下執行
--------------------

a. 執行 DataPusher+

   .. parsed-literal::

      ckan -c /etc/ckan/default/ckan.ini jobs worker

b. 開啟另一終端機視窗，並透過啟動新安裝的 CKAN 網站

   .. parsed-literal::

      . /usr/lib/ckan/default/bin/activate
      ckan -c /etc/ckan/default/ckan.ini run

c. 打開瀏覽器，前往 http://127.0.0.1:5000/ ，若能看到網站畫面即表示安裝完成。
