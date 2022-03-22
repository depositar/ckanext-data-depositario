============
自原始碼安裝
============

本節將描述如何自原始碼安裝本平台（|site_name|）使用之 CKAN 軟體。示範系統為 Ubuntu 18.04。

---------------
1. 安裝必須套件
---------------

.. parsed-literal::

   sudo apt install python3-dev postgresql libpq-dev python3-pip python3-venv git openjdk-8-jdk redis-server

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

b. 安裝建議的 setuptools 版本

   .. important::

      執行以下指令時，請確定您位於虛擬環境根目錄：

      .. parsed-literal::

         cd /usr/lib/ckan/default/

   .. parsed-literal::

      pip install setuptools==44.1.0
      pip install --upgrade pip

c. 安裝 CKAN

   .. parsed-literal::

      pip install -e 'git+git://github.com/depositar/ckan.git#egg=ckan[requirements]'

d. 安裝本平台客製套件

   .. parsed-literal::

      pip install -e 'git+https://github.com/depositar/ckanext-data-depositario.git#egg=ckanext-data-depositario'

e. 安裝本平台客製套件所需 Python 套件

   .. parsed-literal::

      pip install -r /usr/lib/ckan/default/src/ckanext-data-depositario/requirements.txt

f. 安裝其他所需 Python 套件

   .. parsed-literal::

      pip install -r /usr/lib/ckan/default/src/ckanext-spatial/pip-requirements.txt
      pip install -r https://raw.githubusercontent.com/ckan/ckanext-xloader/master/requirements.txt
      pip install -r /usr/lib/ckan/default/src/ckanext-dcat/requirements.txt
      pip install -r /usr/lib/ckan/default/src/ckanext-harvest/pip-requirements.txt

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

c. 安裝 PostGIS

   .. parsed-literal::

      sudo apt-get install postgresql-10-postgis-2.4 python3-dev libxml2-dev libxslt1-dev libgeos-c1v5
      sudo -u postgres psql -d ckan_default -f /usr/share/postgresql/10/contrib/postgis-2.4/postgis.sql
      sudo -u postgres psql -d ckan_default -f /usr/share/postgresql/10/contrib/postgis-2.4/spatial_ref_sys.sql
      sudo -u postgres psql -d ckan_default -c 'ALTER VIEW geometry_columns OWNER TO ckan_default;'
      sudo -u postgres psql -d ckan_default -c 'ALTER TABLE spatial_ref_sys OWNER TO ckan_default;'

d. 本平台使用 CKAN 之 DataStore 功能，故需要建立相關之資料庫與使用者

   .. note::

      DataStore 是一個內建於 CKAN 的功能，透過一獨立資料庫儲存上傳至 CKAN 之結構資料內容（CSV 或 XLS 檔案，無論為上傳至本機的檔案或僅有連結）。

   .. parsed-literal::

      sudo -u postgres createuser -S -D -R -P -l datastore_default
      sudo -u postgres createdb -O ckan_default datastore_default -E utf-8


e. （供本平台管理員資訊）自已備份資料庫還原

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

      執行任何 paster 指令時，請確認是在 CKAN 虛擬環境下。您可隨時執行以下指令以返回虛擬環境： ::

      . /usr/lib/ckan/default/bin/activate

   .. parsed-literal::

      ckan generate config /etc/ckan/default/ckan.ini
      ckan config-tool /etc/ckan/default/ckan.ini -f /usr/lib/ckan/default/src/ckanext-data-depositario/config/custom_options.ini

c. 修改前面新增的 ckan.ini 檔案中對應之設定如下

   .. note::

      * 以 # 開頭之文字為註解，可視需求刪除。
      * 此僅為使本系統正常運作之最小需求設定。

   .. parsed-literal::

      ## Database Settings
      ## CKAN 資料庫連線設定，請依照 :ref:`postgres-setup` 所新增的資料庫設定
      ## pass 請填寫 CKAN 資料庫密碼
      sqlalchemy.url = postgresql://ckan_default:pass@localhost/ckan_default
      ## DataStore 資料庫連線設定，請依照 :ref:`postgres-setup` 所新增的資料庫設定
      ## pass 請填寫 CKAN 資料庫密碼
      ckan.datastore.write_url = postgresql://ckan_default:pass@localhost/datastore_default
      ## pass 請填寫 DataStore 資料庫密碼
      ckan.datastore.read_url = postgresql://datastore_default:pass@localhost/datastore_default

      ## 以下需自行新增於 Logging configuration 上方

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
      ## GMAP_AKI_KEY 請填入申請之 Google Maps API key
      ckanext.data_depositario.gmap.api_key = GMAP_AKI_KEY
      ## GA_ID 請填入申請之 Google Analytics id
      ckanext.data_depositario.googleanalytics.id = GA_ID

------------------------------------
6. 安裝 Solr（含中文與空間搜尋支援）
------------------------------------

.. note::

   本部分參考 DigitalOcean™ Inc. 所編寫之 `How To Install Solr 5.2.1 on Ubuntu 14.04 <https://www.digitalocean.com/community/tutorials/how-to-install-solr-5-2-1-on-ubuntu-14-04>`_ ，該作品以 `創用 CC 姓名標示-非商業性-相同方式分享 4.0 國際 <https://creativecommons.org/licenses/by-nc-sa/4.0/>`_ 授權釋出。

a. 下載並解壓縮 Solr

   .. parsed-literal::

      cd ~
      wget http://archive.apache.org/dist/lucene/solr/8.11.1/solr-8.11.1.tgz
      tar xzf solr-8.11.1.tgz solr-8.11.1/bin/install_solr_service.sh --strip-components=2

b. 執行 Solr 安裝腳本

   .. parsed-literal::

      sudo bash ./install_solr_service.sh solr-8.11.1.tgz

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

      wget https://repo1.maven.org/maven2/org/locationtech/jts/jts-core/1.18.2/jts-core-1.18.2.jar
      sudo cp jts-core-1.18.2.jar /opt/solr/server/solr-webapp/webapp/WEB-INF/lib/.

f. 重新啟動 Solr

   .. parsed-literal::

      sudo service solr restart

g. 打開瀏覽器，前往 http://127.0.0.1:8983/solr/#/ckan ，若能看到畫面則代表安裝完成

--------------------
7. 建立 who.ini link
--------------------

.. parsed-literal::

   ln -s /usr/lib/ckan/default/src/ckan/who.ini /etc/ckan/default/who.ini

---------------
8. 初始化資料庫
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

------------------------
9. 設定 CKAN 系統管理者
------------------------

.. important::

   （供本平台管理員資訊）請忽略此步驟。

請執行以下指令，以修改預設 CKAN 系統管理者密碼（帳號為 default）

.. parsed-literal::

   ckan -c /etc/ckan/default/ckan.ini user setpass default

--------------------
10. 在開發環境下執行
--------------------

a. 執行 XLoader

   .. note::

      XLoader 是一個 CKAN 的擴充套件，當使用者新增結構資料（如 CSV 或 XLS 檔案，無論為上傳至本機的檔案或僅有連結）至 CKAN 時，XLoader 會自動上傳資料內容至 CKAN 的 DataStore 資料庫（關於 DataStore 請見第 4 節的說明），以提供 :ref:`data_api` 等功能。

   .. parsed-literal::

      ckan -c /etc/ckan/default/ckan.ini jobs worker

b. 開啟另一終端機視窗，並透過啟動新安裝的 CKAN 網站

   .. parsed-literal::

      . /usr/lib/ckan/default/bin/activate
      ckan -c /etc/ckan/default/ckan.ini run

c. 打開瀏覽器，前往 http://127.0.0.1:5000/ ，若能看到網站畫面即表示安裝完成。
