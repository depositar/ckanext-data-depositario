--------
更新日誌
--------

v6.7.1 2024-09-18
=================

注意事項：
 * 此版本需搭配最新版 `ckanext-depositar_theme <https://github.com/depositar/ckanext-depositar_theme>`_ 與 `ckanext-geoview <https://github.com/depositar/ckanext-geoview>`_ 使用。

更新內容：
 * 更新：CKAN 核心至 `2.10.5 <https://docs.ckan.org/en/2.10/changelog.html#v-2-10-5-2024-08-21>`_。
 * 更新：ckanext-depositar_theme 1.1.12 與 ckanext-geoview 0.2.0。

v6.7.0 2024-07-18
=================

升級指引：
 * 請根據 :doc:`maintaining/installing/install-from-source` 第 2 點重新建立 Python 虛擬環境。
 * 請根據 :doc:`maintaining/installing/install-from-source` 第 9 點設定 DataPusher+。
 * 請移除 ``/etc/ckan/default/who.ini`` 。
 * 請根據以下內容更新 CKAN 設定檔

   .. code-block:: ini
      :caption: /etc/ckan/default/ckan.ini

      ## Authorization Settings

      ckan.auth.create_unowned_dataset = true
      ckan.auth.create_user_via_web = true

      ## Search Settings

      ckan.search.solr_allowed_query_parsers = field

      ## Plugins Settings

      ckan.plugins = dcat activity depositar_iso639 data_depositario depositar_theme_rep_str depositar_theme ark citation wikidatakeyword showcase dcat_json_interface structured_data stats datastore resource_proxy datapusher_plus datatables_view recline_view text_view image_view webpage_view recline_grid_view recline_map_view audio_view video_view pdf_view spatial_metadata spatial_query geo_view geojson_view wmts_view shp_view scheming_datasets

      ## XLoader Settings

      (移除此設定) ckanext.xloader.jobs_db.uri

      ## Datapusher settings

      ckan.datapusher.formats = csv xls xlsx tsv application/csv application/vnd.ms-excel application/vnd.openxmlformats-officedocument.spreadsheetml.sheet ods application/vnd.oasis.opendocument.spreadsheet

      ## Theming Settings

      ckan.base_public_folder = public-bs3
      ckan.base_templates_folder = templates-bs3

      ## ckanext-data-depositario Settings

      (移除此設定) ckanext.data_depositario.googleanalytics.id = GA_ID

 * 請執行 CKAN 升級指令如下

   .. code-block:: shell

      . /usr/lib/ckan/default/bin/activate
      ckan -c /etc/ckan/default/ckan.ini db upgrade
      ckan -c /etc/ckan/default/ckan.ini search-index rebuild

 * 修改 nginx 設定檔如下，之後重新啟動 nginx

   .. code-block:: nginx
      :caption: /etc/nginx/sites-available/ckan

      proxy_temp_path /tmp/nginx_proxy 1 2;

      server {
          client_max_body_size 100M;
          location / {
              proxy_pass http://127.0.0.1:8080/;
              proxy_set_header X-Forwarded-For $remote_addr;
              proxy_set_header Host $host;
          }
      }

注意事項：
 * 此版本起將僅支援 Python 3.7 以上環境（目前支援 Python 3.7 至 3.10）。
 * 已移除 Google Analytics 支援。
 * 不再支援舊有的單一 API key 作為認證方式，請改用 API token（詳見 :doc:`../../user-guide/data-api` ）。

更新內容：
 * 更新：CKAN 核心至 `2.10.4 <https://docs.ckan.org/en/2.10/changelog.html#v-2-10-4-2024-03-13>`_ 。來自 CKAN 2.10 的變更：

   - 可選擇以使用者名稱或電子郵件登入
   - Table（表格）檢視（詳見 :ref:`data_preview` ）
   - Font Awesome 6.0 圖示

 （以上更新內容翻譯與修改自 `Open Knowledge Foundation <https://okfn.org/>`_ and `contributors <https://github.com/ckan/ckan/graphs/contributors>`_ 所編寫之 `Changelog — CKAN 2.10.4 documentation <http://docs.ckan.org/en/2.10/changelog.html>`_，該作品以 `創用CC 姓名標示-相同方式分享 3.0 未本地化 <https://creativecommons.org/licenses/by-sa/3.0/deed.zh_TW>`_ (`Creative Commons Attribution-ShareAlike 3.0 Unported <https://creativecommons.org/licenses/by-sa/3.0/>`_) 授權條款釋出。）

v6.6.6 2024-05-15
=================

更新內容：
 * 新增：（操作手冊）Binder 服務介紹

v6.6.5 2024-04-10
=================

注意事項：
 * 此版本需搭配最新版 `ckanext-depositar_theme <https://github.com/depositar/ckanext-depositar_theme>`_ 使用。

更新內容：
 * 更新：CKAN 核心至 `2.9.11 <https://docs.ckan.org/en/2.9/changelog.html#v-2-9-11-2024-03-13>`_。
 * 更新：手冊主題改用 `pydata-sphinx-theme <https://pydata-sphinx-theme.readthedocs.io/>`_ 、修訂與勘誤。
 * 改善：部分文案修正。

v6.6.4 2024-02-15
=================

注意事項：
 * 此版本需搭配最新版 `ckanext-depositar_theme <https://github.com/depositar/ckanext-depositar_theme>`_ 使用。

更新內容：
 * 更新 Python 相依套件，為未來 CKAN 核心升級預作準備。

v6.6.3 2024-01-04
=================

更新內容：
 * 更新：CKAN 核心至 `2.9.10 <https://docs.ckan.org/en/2.9/changelog.html#v-2-9-10-2023-12-13>`_。

v6.6.2 2023-10-26
=================

注意事項：
 * 此版本需搭配最新版 `ckanext-depositar_theme <https://github.com/depositar/ckanext-depositar_theme>`_ 使用。

更新內容：
 * 新增：`BinderHub <https://binderhub.readthedocs.io/>`_ 功能，可將公開的資料集建立為 JupyterLab 等運算環境。
 * 改善：（Solr 索引）設定 dynamic field * 為 string 類型，以避免錯誤斷詞 (discussions #13)。
 * 改善：首頁文案修正。

v6.6.1 2023-09-14
=================

更新內容：
 * 更新：手冊修訂與勘誤。

v6.6.0 2023-06-29
=================

注意事項：
 * 此版本需搭配最新版 `ckanext-depositar_theme <https://github.com/depositar/ckanext-depositar_theme>`_ 使用。

更新內容：
 * 更新：CKAN 核心至 `2.9.9 <https://docs.ckan.org/en/2.9/changelog.html#v-2-9-9-2023-05-24>`_。
 * 改善：首頁文案修正。

v6.5.9 2023-05-11
=================

注意事項：
 * 此版本需搭配最新版 `ckanext-depositar_theme <https://github.com/depositar/ckanext-depositar_theme>`_ 使用。

更新內容：
 * 改善：首頁與頁尾細部介面調整。

v6.5.8 2023-03-09
=================

更新內容：
 * 更新：CKAN 核心至 `2.9.8 <https://docs.ckan.org/en/2.9/changelog.html#v-2-9-8-2023-02-15>`_。

v6.5.7 2022-12-01
=================

注意事項：
 * 此版本需搭配最新版 `ckanext-depositar_theme <https://github.com/depositar/ckanext-depositar_theme>`_ 使用。

更新內容：
 * 改善：首頁效能提升。

v6.5.6 2022-11-03
=================

更新內容：
 * 更新：CKAN 核心至 `2.9.7 <https://docs.ckan.org/en/2.9/changelog.html#v-2-9-7-2022-10-26>`_。
 * 更新：ckanext-xloader 至 0.11.0。

v6.5.5 2022-10-14
=================

注意事項：
 * 此版本需搭配最新版 `ckanext-depositar_theme <https://github.com/depositar/ckanext-depositar_theme>`_ 使用。

更新內容：
 * 更新：CKAN 核心至 `2.9.6 <https://docs.ckan.org/en/2.9/changelog.html#v-2-9-6-2022-09-28>`_。
 * 改善：首頁效能提升與細部介面調整。

v6.5.4 2022-09-23
=================

注意事項：
 * 此版本需搭配最新版 `ckanext-depositar_theme <https://github.com/depositar/ckanext-depositar_theme>`_ 使用。

更新內容：
 * 更新：全新首頁設計。

v6.5.3 2022-07-08
=================

注意事項：
 * 此版本需搭配最新版 `ckanext-citation <https://github.com/depositar/ckanext-citation>`_ 與 `ckanext-ark <https://github.com/depositar/ckanext-ark>`_ 使用。

更新內容：
 * 新增：:ref:`ark-identifier` 功能，賦予符合條件的資料集以 ARK 為編碼規格的持續識別碼。
 * 其他程式最佳化與細部介面調整。

v6.5.2 2022-05-06
=================

注意事項：
 * 此版本需搭配最新版 `ckanext-citation <https://github.com/depositar/ckanext-citation>`_ 使用。

更新內容：
 * 改善：修復 BibTeX generic citation style 月份顯示錯誤。
 * 改善：修復 BibTeX generic citation style 的 citation-key 值可能未落於規範內的問題。
 * 改善：正確讀取 ``ckanext.data_depositario.demo.enabled`` 設定。
 * 更新：手冊勘誤。

v6.5.1 2022-03-25
=================

注意事項：
 * 此版本需搭配最新版 `ckanext-wikidatakeyword <https://github.com/depositar/ckanext-wikidatakeyword>`_ 使用。
 * 此版本將需要 Solr 8。請依序執行以下指令升級 Solr 版本為 8.11.1：

   ::

     sudo service solr stop
     sudo rm /etc/default/solr.in.sh
     sudo bash ./install_solr_service.sh solr-8.11.1.tgz -f
     sudo -u solr /opt/solr/bin/solr delete -c ckan
     sudo -u solr /opt/solr/bin/solr create -c ckan
     sudo ln -sf /usr/lib/ckan/default/src/ckanext-data-depositario/solr/schema.xml /var/solr/data/ckan/conf/managed-schema
     wget https://repo1.maven.org/maven2/com/github/magese/ik-analyzer/8.5.0/ik-analyzer-8.5.0.jar
     wget https://repo1.maven.org/maven2/org/locationtech/jts/jts-core/1.18.2/jts-core-1.18.2.jar
     sudo cp ik-analyzer-8.5.0.jar /opt/solr/server/solr-webapp/webapp/WEB-INF/lib/.
     sudo cp jts-core-1.18.2.jar /opt/solr/server/solr-webapp/webapp/WEB-INF/lib/.
     sudo mkdir /opt/solr/server/solr-webapp/webapp/WEB-INF/classes
     sudo ln -s /usr/lib/ckan/default/src/ckanext-data-depositario/solr/IKAnalyzer.cfg.xml /opt/solr/server/solr-webapp/webapp/WEB-INF/classes/.
     sudo ln -s /usr/lib/ckan/default/src/ckanext-data-depositario/solr/dic/words.dic /var/solr/data/ckan/conf/words.dic
     . /usr/lib/ckan/default/bin/activate
     ckan -c /etc/ckan/default/ckan.ini search-index rebuild

更新內容：
 * 更新：CKAN 核心至 `2.9.5 <http://docs.ckan.org/en/2.9/changelog.html#v-2-9-5-2022-01-19>`_。
 * 改善：修復欄位填寫錯誤時，部分欄位無法顯示的問題。

v6.5.0 2022-02-18
=================

注意事項：
 * 此版本起將僅支援 Python 3.6 以上環境（目前支援 Python 3.6、3.7 與 3.8）。
 * 請根據 :doc:`maintaining/installing/install-from-source` 重新建立 Python 虛擬環境與更新 CKAN 設定檔，並依序執行以下指令：

   ::

     . /usr/lib/ckan/default/bin/activate
     ckan -c /etc/ckan/default/ckan.ini db upgrade
     ckan -c /etc/ckan/default/ckan.ini search-index rebuild
     python /usr/lib/ckan/default/src/ckan/migration/migrate_package_activity.py -c /etc/ckan/default/ckan.ini

更新內容：
 * 更新：CKAN 核心至 `2.9.4 <http://docs.ckan.org/en/2.9/changelog.html#v-2-9-4-2021-09-22>`_。來自 CKAN 2.8 與 2.9 的變更：

   - 以 Bootstrap 3 為基礎的新介面
   - 支援影片（MP4、WebM 與 Ogg 格式）與音訊（MP3、WAV 與 Ogg 格式）預覽
   - :ref:`dataset_collaborators` 功能，可針對非公開資料集個別新增協作者，並賦予編輯或瀏覽權限
   - API Tokens：支援建立多組 API key，並可隨時撤銷（詳見 :ref:`data_api` ）
   - 使用者可自訂個人資料圖片（支援直接上傳或連結）
   - 資料集「歷史紀錄」併入「動態牆」

   （以上更新內容翻譯與修改自 `Open Knowledge Foundation <https://okfn.org/>`_ and `contributors <https://github.com/ckan/ckan/graphs/contributors>`_ 所編寫之 `Changelog — CKAN 2.9.5 documentation <http://docs.ckan.org/en/2.9/changelog.html>`_，該作品以 `創用CC 姓名標示-相同方式分享 3.0 未本地化 <https://creativecommons.org/licenses/by-sa/3.0/deed.zh_TW>`_ (`Creative Commons Attribution-ShareAlike 3.0 Unported <https://creativecommons.org/licenses/by-sa/3.0/>`_) 授權條款釋出。）

 * 其他程式最佳化與細部介面調整。

v6.4.6 2021-09-10
=================

注意事項：
 * 需更新相依套件：

   ::

     pip install -r /usr/lib/ckan/default/src/ckanext-data-depositario/requirements.txt
     pip install -r /usr/lib/ckan/default/src/ckanext-spatial/pip-requirements-py2.txt
     pip install -r https://raw.githubusercontent.com/ckan/ckanext-xloader/master/requirements.txt
     pip install -r /usr/lib/ckan/default/src/ckanext-dcat/requirements.txt

 * 需進行資料庫更新：

   ::

     wget -O- https://github.com/ckan/ckanext-xloader/raw/master/full_text_function.sql | sudo -u postgres psql datastore_default

 * 需調整 CKAN 設定檔，請參照 :doc:`maintaining/installing/install-from-source` 5-c. 小節，更新以下設定：

   - Plugins Settings
   - Schema Settings

 * 需調整佈署設定，設定開機執行 XLoader。請參照 :doc:`maintaining/installing/deployment` 第 2 節（XLoader Settings）與第 5 節進行設定。
 * 以下 Python 相依套件可安全移除：

   - ckanext-repeating
   - DataPusher

更新內容：
 * 新增：（操作手冊）引用資料集功能介紹。
 * 更新：（資料集後設資料）資料類型 (:ref:`parse-insight-content-types`) 說明。

   - 純文字資料：移除 CSV
   - 結構化文字資料：加入 CSV 與 JSON

 * 改善：CSS 重構與精簡化。
 * 改善：以 XLoader 擴充套件取代原 DataPusher 上傳結構化資料至 DataStore 資料庫，避免因資料欄位類型自動判定錯誤導致上傳失敗 (#11)。
 * 更新 Python 相依套件，為未來 CKAN 核心升級預作準備。
 * 其他程式最佳化與細部介面調整。

v6.4.5 2021-07-30
=================

注意事項：
 * 此版本需搭配最新版 `ckanext-wikidatakeyword <https://github.com/depositar/ckanext-wikidatakeyword>`_ 與 `ckanext-depositar_theme <https://github.com/depositar/ckanext-depositar_theme>`_ 使用。

更新內容：
 * 改善：修復自 Action API 上傳資料集時，若未加上 keywords，會發生 HTTP 500 錯誤的問題。
 * 改善：修復於 WebKit 系列瀏覽器網址顯示破版的問題。
 * 其他程式最佳化與細部介面調整。

v6.4.4 2021-06-18
=================

注意事項：
 * 此版本需搭配最新版 `ckanext-citation <https://github.com/depositar/ckanext-citation>`_ 與 `ckanext-depositar_theme <https://github.com/depositar/ckanext-depositar_theme>`_ 使用。

更新內容：
 * 新增：使用條款與隱私政策。
 * 更新：CKAN 核心至 `2.7.11 <https://docs.ckan.org/en/2.7/changelog.html#v-2-7-11-2021-05-19>`_。
 * 其他程式最佳化與細部介面調整。

v6.4.3 2021-04-01
=================

更新內容：
 * 更新：CKAN 核心至 `2.7.10 <https://docs.ckan.org/en/latest/changelog.html#v-2-7-10-2021-02-10>`_。

v6.4.2 2020-12-17
=================

注意事項：
 * 此版本需搭配最新版 `ckanext-spatial <https://github.com/depositar/ckanext-spatial>`_ 與 `ckanext-depositar_theme <https://github.com/depositar/ckanext-depositar_theme>`_ 使用。

更新內容：
 * 新增：:ref:`rdf_serializations` (測試功能)。
 * 其他程式最佳化與細部介面調整。

v6.4.1 2020-08-20
=================

注意事項：
 * 此版本需搭配最新版 `ckanext-wikidatakeyword <https://github.com/depositar/ckanext-wikidatakeyword>`_、`ckanext-spatial <https://github.com/depositar/ckanext-spatial>`_，與 `ckanext-depositar_theme <https://github.com/depositar/ckanext-depositar_theme>`_ 使用。

更新內容：
 * 改善：資料集與資源編輯頁面加入使用手冊連結、欄位圖示，與欄位說明。
 * 更新：手冊勘誤。
 * 更新：CKAN 核心至 `2.7.8 <https://docs.ckan.org/en/latest/changelog.html#v-2-7-8-2020-08-05>`_。
 * 移除：Google+ 分享按鈕。
 * 其他程式最佳化與細部介面調整。

v6.4.0 2020-06-10
=================

注意事項：
 * 此版本需搭配 `ckanext-scheming 1.2.0 <https://github.com/ckan/ckanext-scheming/releases/tag/release-1.2.0>`_ 與最新版 `ckanext-wikidatakeyword <https://github.com/depositar/ckanext-wikidatakeyword>`_ 使用。

更新內容：
 * 改善：簡化後設資料欄位，將 ``描述資訊`` 併入 ``基本資訊`` ，同時新增 ``時空資訊`` 。變更內容詳見以下對照表，完整列表請參考 :doc:`appendix/fields/index` 。

 .. list-table::
    :widths: 25 40 35
    :header-rows: 1

    * - 原欄位名稱
      - 變更
      - 備註

    * - 語言
      - 提供所有 ISO 639-3 選擇、接受多值
      -

    * - 關鍵字
      - 更名為「Wikidata 關鍵字」
      -

    * - 資料類型
      - 採用 `Registry of Research Data Repositories (re3data) <https://www.re3data.org/>`_ 使用之 :ref:`parse-insight-content-types`、接受多值

        原選項與新選項對應如下：

        | 統計資料 → 科學與統計資料
        | 文獻書籍 → 辦公軟體文件
        | 圖像 (非空間類) → 影像
        | 圖像 (空間類) → 影像
        | 向量資料 → 科學與統計資料
        | 三維模型 → 結構化圖形
        | 影音資料 → 影音資料

      -

    * - 時間區間捷徑
      - 移除
      - 此欄位實非屬後設資料欄位，僅為便於輸入時間之工具

    * - 時間解析度
      - 移除「十年」與「一百年」選項
      - 該二選項之定義具爭議，且較少資料集使用

    * - 起始時間
      - 不再受「時間解析度」欄位限制，可自由填寫
      -

    * - 結束時間
      - 不再受「時間解析度」欄位限制，可自由填寫
      - 新增結束時間需晚於或等於起始時間之檢查

    * - 資料類型選擇「文獻書籍」時，顯示之欄位
      - 移除以下欄位：

        | ISBN-13
        | ISSN
        | 期刊
        | 卷期
        | 論文集名稱
        | 出版地
        | 出版單位
        | 出版年
        | 書目查詢
        | 網址
        | 使用史料
        | 研究區的聚落名
        | 研究區的宗教
        | 研究區的家族
        | 研究區的埤圳
        | 研究區的特殊產業
        | 備註

      - 原內容合併至「備註」欄位

    * - 資料類型選擇「圖像」時，顯示之欄位
      - 移除以下欄位：

        | 掃描原件來源
        | 掃描原件尺寸
        | 掃描解析度
        | 比例尺

        以下欄位保留但移動位置：

        | 空間解析度
        | 資料處理歷程

      - 原內容合併至「備註」欄位

    * - 空間解析度
      - 移動至「時空資訊」部分
      - 原「圖像」資料類型之欄位

    * - 資料處理歷程
      - 移動至「管理資訊」部分
      - 原「圖像」資料類型之欄位

    * - 資料產製時間
      -
      - 直接支援 YYYY 與 YYYY-MM 格式，不再自動轉換月 (日) 為 01

    * - 維護者
      - 更名為「聯絡人」
      - 更名後較符合資料管理之實務需求

    * - 維護者的電子郵件
      - 更名為「聯絡人的電子郵件」
      - 更名後較符合資料管理之實務需求。新增電子郵件格式檢查

    * - 維護者的聯絡電話
      - 移除
      - 有個資疑慮故移除

    * - 識別碼
      - 移除
      - 原內容合併至「備註」欄位

    * - 編碼
      - 更名為「字元編碼」
      - 此為資源層級欄位

 * 其他程式最佳化與細部介面調整。

v6.3.6 2019-08-26
=================

 * 新增：於資料集頁面提供資料集引用小工具。
 * 更新：手冊勘誤。
 * 更新：CKAN 核心至 2.7.6。

v6.3.5 2019-03-29
=================

 * 改善：修正使用者註冊後無法立即將資料集加入主題的問題 (#6)。
 * 其他程式最佳化。

v6.3.4 2018-12-18
=================

 * 改善：修正於行動裝置瀏覽資料集頁面時，搜尋過濾條件無法捲動的問題。
 * 更新：CKAN 核心至 2.7.5。

v6.3.3 2018-12-07
=================

 * 改善：修正搜尋過濾條件與搜尋結果頁籤顯示不正常的問題。
 * 其他程式最佳化與細部介面調整。

v6.3.2 2018-10-25
=================

 * 更新：介面修正。

v6.3.1 2018-10-25
=================

 * 更新：細項介面調整。

v6.3.0 2018-10-23
=================

 * 更新：全新設計介面。

同時自即日起開放註冊。

v6.2.1 2018-08-24
=================

 * 更新：建立帳號時需進行電子信箱認證。
 * 更新：手冊勘誤。
 * 更新：依據 https://licenses.opendefinition.org/ 更新授權清單。新增 CC-BY-NC-SA 4.0 條款。
 * 移除：首頁「最新消息」區塊。

v6.2.0 2018-07-20
=================

 * 改善：在所有「授權」過濾條件旁加上授權說明小工具。
 * 更新：CKAN 核心至 2.7.4。
 * 其他程式最佳化與細部介面調整。

v6.1.3 2018-07-06
=================

 * 新增：手冊英文版。
 * 改善：網站語言切換改至頁面右上方處。
 * 改善：修正資料集後設資料「資料處理歷程」欄位無法正確顯示的問題 (#2)。
 * 更新：手冊中文版勘誤。

v6.1.2 2018-05-10
=================

 * 更新：CKAN 核心至 2.6.6。

v6.1.1 2018-04-23
=================

 * 新增：操作手冊與維護手冊。

v6.1.0 2018-03-23
=================

 * 新增：網站即時狀態監測（連結位於網站下方）。
 * 改善：修正錯誤的 positive_float_validator 校驗器。
 * 改善：套用更為適當的校驗器至後設資料欄位。
 * 改善：空間範圍填寫輔助圖台新增 LineString 支援。
 * 改善：空間範圍填寫輔助圖台新增圖徵修改與刪除工具。
 * 更新：Leaflet.draw 版本至 0.4.1。
 * 更新：CKAN 核心至 2.6.5。
 * 將 Wikidata 關鍵字功能分離為獨立套件：https://github.com/depositar-io/ckanext-wikidatakeyword。
 * 其他程式最佳化與細部介面調整。

v6.0 2017-11-03
===============

 * 新增：「關鍵字」欄位，整合既有「主題關鍵字」與「空間範圍關鍵字」，並採用維基數據 (Wikidata) 作為資料來源。
 * 新增：新增資料集時，若輸入標題無法自動產生網址時 (如全中文標題)，將自動產生一組隨機文數字作為網址。
 * 更新：CKAN 核心至 2.6.4。
 * 其他程式最佳化與細部介面調整。

v5.0.x 2017-09-05
=================

 * 改善：簡化後設資料欄位。將資料集層級之後設資料分為「基本資訊」、「描述資訊」與「管理資訊」三大區塊。合併「參考來源」與「所屬子計畫」為一欄位「備註」，並將「編碼」欄位移至資料層級，同時移除部分較少使用之欄位與選項。
 * 改善：使用圖台填寫「空間範圍」欄位時，系統將自動產生空間範圍值與四至座標並鎖定欄位。
 * 改善：「維護者」與「維護者的電子郵件」欄位可帶入登入中的使用者資訊。
 * 改善：將資料集加入任一組織時，可透過核取方塊限制僅對組織內成員公開該資料集。
 * 改善：使用 CKAN 2.5 提供之翻譯功能翻譯客製化部分介面，今後客製化部分與主程式之介面將不再互相干擾。
 * 更新：ckanext-pages 擴充套件版本，並加上中文介面翻譯。
 * 更新：CKAN 核心至 2.6.3。
 * 其他程式最佳化與細部介面調整。
