============
自原始碼安裝
============

本節將描述如何自原始碼安裝本平台（跨領域區域研究資料集）使用之CKAN軟體。示範系統為Ubuntu 16.04。

---------------
1. 安裝必須套件
---------------

.. parsed-literal::

   sudo apt-get install build-essential libxslt1-dev libxml2-dev python-dev postgresql libpq-dev python-pip python-virtualenv git-core openjdk-8-jdk

---------------------------
2. 安裝CKAN於Python虛擬環境
---------------------------

a. 新增一個Python虛擬環境（virtualenv）供CKAN使用，並進入該虛擬環境

   .. parsed-literal::

      sudo mkdir -p /usr/lib/ckan/default
      sudo chown \`whoami\` /usr/lib/ckan/default
      virtualenv --no-site-packages /usr/lib/ckan/default
      . /usr/lib/ckan/default/bin/activate

   .. important::

      上述指令中的最後一個用以啟動虛擬環境。在剩餘安裝步驟中需維持此虛擬環境於執行狀態，否則安裝作業可能會失敗。當虛擬環境執行時，命令提示字元（shell prompt）會有類似以下前綴： ::

        (default) $ _

      若您於登出後再次登入，將會離開目前執行中的虛擬環境。您可隨時執行以下指令以返回虛擬環境： ::

        . /usr/lib/ckan/default/bin/activate

b. 安裝CKAN於虛擬環境

   .. important::

      執行以下指令時，請確定您位於虛擬環境根目錄：

      .. parsed-literal::

         cd /usr/lib/ckan/default/

   安裝setuptools：

   .. parsed-literal::

      pip install setuptools==36.1

   安裝CKAN：

   .. parsed-literal::

      pip install -e 'git+https://github.com/depositar-io/ckan.git#egg=ckan'

c. 安裝CKAN所需Python套件

   .. parsed-literal::

      pip install -r /usr/lib/ckan/default/src/ckan/requirements.txt

d. 安裝本平台客製套件

   .. parsed-literal::

      pip install -e 'git+https://github.com/depositar-io/ckanext-data-depositario.git#egg=ckanext-data-depositario'

e. 安裝本平台客製套件所需Python套件

   .. parsed-literal::

      pip install -r /usr/lib/ckan/default/src/ckanext-data-depositario/requirements.txt

f. 安裝其他所需Python套件

   .. parsed-literal::

      pip install -r /usr/lib/ckan/default/src/ckanext-spatial/pip-requirements.txt
      pip install -r /usr/lib/ckan/default/src/ckanext-scheming/requirements.txt

---------------------------------
3. 安裝DataPusher於Python虛擬環境
---------------------------------

.. note::

   DataPusher是一個CKAN的擴充套件，當使用者新增結構資料（如CSV或XLS檔案，無論為上傳至本機的檔案或僅有連結）至CKAN時，DataPusher會自動上傳資料內容至CKAN的DataStore資料庫（關於DataStore請見下節的說明），以提供 :ref:`data_api` 等功能。

a. 新增一個Python虛擬環境供DataPusher使用，並進入該虛擬環境

   .. parsed-literal::

      sudo mkdir -p /usr/lib/ckan/datapusher
      sudo chown \`whoami\` /usr/lib/ckan/datapusher
      virtualenv --no-site-packages /usr/lib/ckan/datapusher
      . /usr/lib/ckan/datapusher/bin/activate

b. 安裝DataPusher於虛擬環境

   .. important::

      執行以下指令時，請確定您位於虛擬環境根目錄：

      .. parsed-literal::

         cd /usr/lib/ckan/datapusher/

   安裝DataPusher：

   .. parsed-literal::

      pip install -e 'git+https://github.com/ckan/datapusher.git#egg=datapusher'

c. 安裝DataPusher所需Python套件

   .. parsed-literal::

      pip install -r /usr/lib/ckan/datapusher/src/datapusher/requirements.txt

--------------------
4. 建立FileStore目錄
--------------------

.. note::

   CKAN的FileStore功能提供使用者上傳本機檔案作為資源，詳細請參考 :ref:`使用手冊 <add_resource>` 的說明。

.. parsed-literal::

   sudo mkdir -p /var/lib/ckan/default
   sudo chown \`whoami\` /var/lib/ckan/default
   sudo chmod u+rwx /var/lib/ckan/default

.. _postgres-setup:

-------------
5. 設定資料庫
-------------

a. 新增CKAN使用之PostgreSQL使用者

   .. parsed-literal::

      sudo -u postgres createuser -S -D -R -P ckan_default

b. 新增CKAN使用之資料庫

   .. parsed-literal::

      sudo -u postgres createdb -O ckan_default ckan_default -E utf-8

c. 安裝PostGIS

   .. parsed-literal::

      sudo apt-get install postgresql-9.5-postgis-2.2 python-dev libxml2-dev libxslt1-dev libgeos-c1v5
      sudo -u postgres psql -d ckan_default -f /usr/share/postgresql/9.5/contrib/postgis-2.2/postgis.sql
      sudo -u postgres psql -d ckan_default -f /usr/share/postgresql/9.5/contrib/postgis-2.2/spatial_ref_sys.sql
      sudo -u postgres psql -d ckan_default -c 'ALTER VIEW geometry_columns OWNER TO ckan_default;'
      sudo -u postgres psql -d ckan_default -c 'ALTER TABLE spatial_ref_sys OWNER TO ckan_default;'

d. 本平台使用CKAN之DataStore功能，故需要建立相關之資料庫與使用者

   .. note::

      DataStore是一個內建於CKAN的功能，透過一獨立資料庫儲存上傳至CKAN之結構資料內容（CSV 或 XLS 檔案，無論為上傳至本機的檔案或僅有連結）。

   .. parsed-literal::

      sudo -u postgres createuser -S -D -R -P -l datastore_default
      sudo -u postgres createdb -O ckan_default datastore_default -E utf-8


e. （供本平台管理員資訊）自已備份資料庫還原

   還原資料庫指令如下

   .. parsed-literal::

      gunzip -c main_db.sql.gz | sudo -u postgres psql ckan_default
      gunzip -c datastore_db.sql.gz | sudo -u postgres psql datastore_default

-----------------------
6. 建立與修改CKAN設定檔
-----------------------

a. 新增放置CKAN設定檔之目錄

   .. parsed-literal::

      sudo mkdir -p /etc/ckan/default
      sudo chown -R \`whoami\` /etc/ckan/

b. 透過paster新增範例設定檔

   .. important::

      （供本平台管理員資訊）請忽略此處關於CKAN設定檔之相關說明，直接使用備份之 ``configs.tar.gz`` 壓縮檔內之 ``production.ini`` 檔案，以下提及設定檔時亦請忽略。

   .. important::

      執行任何paster指令時，請確認是在CKAN虛擬環境下。您可隨時執行以下指令以返回虛擬環境： ::

      . /usr/lib/ckan/default/bin/activate

   .. parsed-literal::

      paster make-config ckan /etc/ckan/default/development.ini

c. 修改前面新增的development.ini檔案中對應之設定如下

   .. note::

      * 以 # 開頭之文字為註解，可視需求刪除。
      * 此僅為使本系統正常運作之最小需求設定。

   .. parsed-literal::

      ## Database Settings
      ## CKAN資料庫連線設定，請依照 :ref:`postgres-setup` 所新增的資料庫設定
      ## pass請填寫CKAN資料庫密碼
      sqlalchemy.url = postgresql://ckan_default:pass@localhost/ckan_default
      ## DataStore資料庫連線設定，請依照 :ref:`postgres-setup` 所新增的資料庫設定
      ## pass請填寫CKAN資料庫密碼
      ckan.datastore.write_url = postgresql://ckan_default:pass@localhost/datastore_default
      ## pass請填寫DataStore資料庫密碼
      ckan.datastore.read_url = postgresql://datastore_default:pass@localhost/datastore_default

      ## Site Settings
      ckan.site_url = http://127.0.0.1:5000

      ## Plugins Settings
      ckan.plugins = data_depositario stats datastore datapusher
                     resource_proxy recline_view text_view image_view
                     webpage_view recline_grid_view recline_map_view
                     pdf_view pages spatial_metadata spatial_query
                     geo_view geojson_view wmts_view shp_view
                     scheming_datasets repeating

      ## Front-End Settings
      licenses_group_url = file:///usr/lib/ckan/data_depositario/src/ckanext-data-depositario/ckanext/data_depositario/public/license_list.json

      ## Storage Settings
      ckan.storage_path = /var/lib/ckan/default

      ## Datapusher Settings
      ckan.datapusher.url = http://0.0.0.0:8800/

      ## Schema Settings
      ## 需自行新增
      scheming.presets = ckanext.scheming:presets.json
                         ckanext.repeating:presets.json
                         ckanext.data_depositario:presets.json
      scheming.dataset_schemas = ckanext.data_depositario:scheming.json

      ## Spatial Settings
      ## 需自行新增
      ckanext.spatial.search_backend = solr-spatial-field

      ## ckanext-data-depositario Settings
      ## 需自行新增
      ## GMAP_AKI_KEY請填入申請之Google Maps API key
      ckanext.data_depositario.gmap.api_key = GMAP_AKI_KEY

-----------------------------------
7. 安裝Solr（含中文與空間搜尋支援）
-----------------------------------

.. note::

   本部分參考DigitalOcean™ Inc.所編寫之 `How To Install Solr 5.2.1 on Ubuntu 14.04 <https://www.digitalocean.com/community/tutorials/how-to-install-solr-5-2-1-on-ubuntu-14-04>`_ ，該作品以 `創用CC姓名標示-非商業性-相同方式分享4.0國際 <https://creativecommons.org/licenses/by-nc-sa/4.0/>`_ 授權釋出。

a. 下載並解壓縮Solr

   .. parsed-literal::

      cd ~
      wget http://archive.apache.org/dist/lucene/solr/5.5.5/solr-5.5.5.tgz
      tar xzf solr-5.5.5.tgz solr-5.5.5/bin/install_solr_service.sh --strip-components=2

b. 執行Solr安裝腳本

   .. parsed-literal::

      sudo bash ./install_solr_service.sh solr-5.5.5.tgz

c. 建立供CKAN使用之Solr configset

   .. parsed-literal::

      sudo -u solr mkdir -p /var/solr/data/configsets/ckan/conf
      sudo ln -s /usr/lib/ckan/default/src/ckanext-data-depositario/solr/schema.xml /var/solr/data/configsets/ckan/conf/schema.xml
      sudo -u solr cp /opt/solr/server/solr/configsets/basic_configs/conf/solrconfig.xml /var/solr/data/configsets/ckan/conf/.
      sudo -u solr touch /var/solr/data/configsets/ckan/conf/protwords.txt
      sudo -u solr touch /var/solr/data/configsets/ckan/conf/synonyms.txt

d. 下載中文斷詞函式庫 `mmesg4j <http://pan.baidu.com/s/1dD7qMFf>`_ ，並複製 ``mmseg4j-core-*.jar`` 與 ``mmseg4j-solr-*.jar`` 至Solr目錄（/opt/solr/server/solr-webapp/webapp/WEB-INF/lib）

   .. parsed-literal::

      sudo cp mmseg4j-\*.jar /opt/solr/server/solr-webapp/webapp/WEB-INF/lib/.

e. 下載空間搜尋函式庫JTS 1.13或以上版本並複製至Solr目錄

   .. parsed-literal::

      wget -O jts-1.13.jar https://search.maven.org/remotecontent?filepath=com/vividsolutions/jts/1.13/jts-1.13.jar
      sudo cp jts-1.13.jar /opt/solr/server/solr-webapp/webapp/WEB-INF/lib/.

f. 重新啟動 solr

   .. parsed-literal::

      sudo service solr restart

g. 在瀏覽器輸入以下連結，以建立供CKAN使用之Solr Core（此處命名為ckan）

   http://127.0.0.1:8983/solr/admin/cores?action=CREATE&name=ckan&configSet=ckan

h. 打開瀏覽器，前往 http://127.0.0.1:8983/solr/#/ckan ，若能看到畫面則代表安裝完成

i. 修改/etc/ckan/default/development.ini，指定Solr連線位址

   .. parsed-literal::

      solr_url = http://127.0.0.1:8983/solr/ckan

---------------
8. 初始化資料庫
---------------

.. important::

   （供本平台管理員資訊）請忽略此步驟。

a. 透過paster指令初始化CKAN資料庫

   .. parsed-literal::

      paster --plugin=ckan db init -c /etc/ckan/default/development.ini

b. 如果一切正常，則會看到此訊息：Initialising DB: SUCCESS

c. DataStore資料庫權限設定

   .. parsed-literal::

      paster --plugin=ckan datastore set-permissions -c /etc/ckan/default/development.ini

-------------------
9. 建立who.ini link
-------------------

.. parsed-literal::

   ln -s /usr/lib/ckan/default/src/ckan/who.ini /etc/ckan/default/who.ini

----------------------
10. 新增CKAN系統管理者
----------------------

.. important::

   （供本平台管理員資訊）請忽略此步驟。

透過paster指令新增CKAN系統管理者

.. parsed-literal::

   paster --plugin=ckan sysadmin add admin -c /etc/ckan/default/development.ini

.. note::

   admin請代換為您需要的使用者名稱，並依照程式提示設定密碼。

--------------------
11. 在開發環境下執行
--------------------

a. 執行DataPusher

   .. parsed-literal::

      . /usr/lib/ckan/datapusher/bin/activate
      JOB_CONFIG='/usr/lib/ckan/datapusher/src/datapusher/deployment/datapusher_settings.py' python /usr/lib/ckan/datapusher/src/datapusher/wsgi.py

b. 開啟另一終端機視窗，並透過paster指令啟動新安裝的CKAN網站

   .. parsed-literal::

      . /usr/lib/ckan/default/bin/activate
      paster serve /etc/ckan/default/development.ini

c. 打開瀏覽器，前往 http://127.0.0.1:5000/ ，若能看到網站畫面即表示安裝完成。
