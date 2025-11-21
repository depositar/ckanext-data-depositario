============
Data Package
============

`Data Package`_ 是一種描述資料集與其所包含資料的標準，由 Open Knowledge Foundation 設計。本平台透過 `ckanext-datapackager`_ 套件，提供使用者下載與上傳符合 Data Package 標準的 ``資料封裝包 (Data Package)`` ，為內含以下檔案的 zip 壓縮檔：

* ``datapackage.json`` 描述檔：以 `JSON Schema`_ :doc:`設定檔 (profile) <../appendix/datapackage/index>` 描述資料集與資源
* 一或多個資料檔案：資料集中包含的實際資源

.. note::

    此功能正在測試中，如有任何問題或建議，請 聯絡我們_。

主要功能
--------

下載資料集為 Data Package
~~~~~~~~~~~~~~~~~~~~~~~~~

您可於資料集頁面右上角，點選「下載 Data Package」按鈕，以取得最新版本之 Data Package：

.. image:: /images/datapackage/datapackage_1.png
    :width: 700

匯入 Data Package 為資料集
~~~~~~~~~~~~~~~~~~~~~~~~~~

-----------------
準備 Data Package
-----------------

#. 請參考以下範例，並根據 :doc:`後設資料對應 <../appendix/metadata-mapping/datapackage/index>` ，撰寫 ``datapackage.json`` 描述檔：

.. dropdown:: 範例：包含選填屬性的完整 ``datapackage.json`` 內容（點選以顯示）
    :color: primary
    :icon: file-code

    .. code-block:: json

        {
          "resources": [
            {
              "name": "resource_1",
              "path": "http://example.com",
              "title": "Resource 1",
              "description": "A longer description of the resource.",
              "encoding": "utf-8",
              "resource_crs": "4326",
              "format": "HTML"
            }
          ],
          "title": "Sample Dataset",
          "name": "sample-dataset",
          "description": "A longer description of the dataset.",
          "data_type": [
            "other"
          ],
          "wd_keywords": [
            "http://www.wikidata.org/entity/Q484000"
          ],
          "keywords": [
            "free_keyword_1",
            "free_keyword_2"
          ],
          "language": ["eng"],
          "remarks": "Some supplementary information for the dataset.",
          "temp_res": "daily",
          "start_time": "2024-01-01",
          "end_time": "2025-01-01",
          "spatial": {"type": "Polygon", "coordinates": [[[120.01,22.96], [120.01,23.12], [120.23,23.12], [120.23,22.96], [120.01,22.96]]]},
          "x_min": "120.01",
          "x_max": "120.23",
          "y_min": "22.96",
          "y_max": "23.12",
          "spatial_res": "1.0",
          "licenses": [
            {
              "name": "notspecified"
            }
          ],
          "contributors": [
            {
              "title": "Creator Name",
              "roles": [
                "author"
              ]
            }
          ],
          "process_step": "Steps of data generating process.",
          "contact_person": "Joe Bloggs",
          "contact_email": "joe@example.com"
        }

.. dropdown:: 範例：可供匯入的精簡 ``datapackage.json`` 內容（點選以顯示）
    :color: primary
    :icon: file-code

    .. code-block:: json

        {
          "resources": [
            {
              "name": "resource_1",
              "path": "http://example.com"
            }
          ],
          "name": "sample-dataset",
          "title": "Sample Dataset",
          "licenses": [
            {
              "name": "notspecified"
            }
          ],
          "contributors": [
            {
              "title": "Creator Name",
              "roles": [
                "author"
              ]
            }
          ],
          "data_type": [
            "other"
          ]
        }

2. 若 Data Package 包含 **欲上傳至本站** 之資料檔案，請將資料檔案與 ``datapackage.json`` 壓縮為一 zip 壓縮檔（請注意：檔案仍受 :doc:`limitation` 之規範）

.. note::
    * ``datapackage.json`` 必須放置於 zip 壓縮檔之最上層目錄
    * ``datapackage.json`` 為 JSON 檔案，可使用任何文字編輯器（Visual Studio Code 等）或 `JSON Editor Online`_ 網頁服務撰寫
    * 若包含欲上傳至本站之資料檔案，請於 ``datapackage.json`` 之 ``resources`` 屬性，所包含的各 resource 之 ``path`` 屬性，填寫該資料檔案相對於最上層目錄的路徑
    * 必填屬性： ``resources`` 、 ``name`` 、 ``licenses`` 、 ``contributors`` 、 ``data_type``

-----------------
匯入 Data Package
-----------------

#. 透過下列兩種方式之一，連結至「匯入 Data Package」頁面：

.. grid:: 2

    .. grid-item-card:: 自頁面上方選單「資料集」進入

        於接下來顯示的資料搜尋頁面，即可看見「匯入 Data Package」連結

    .. grid-item-card:: 自頁面上方選單「專案」進入

        選擇欲匯入 Data Package 所屬的專案，若您的使用者帳號為該專案的編輯或管理者，即可看見「匯入 Data Package」連結

2. 於匯入頁面選擇資料集所屬之專案，並上傳 Data Package（或所在網址），以及設定公開與否：

.. grid:: 2

    .. grid-item-card:: 若 Data Package 不包含資料檔案

        於「匯入 Data Package」頁面上傳 ``datapackage.json``

    .. grid-item-card:: 若 Data Package 包含資料檔案

        於「匯入 Data Package」頁面上傳 zip 壓縮檔

.. image:: /images/datapackage/datapackage_2.png
    :width: 700

.. note::

    匯入之 Data Package 屬性，經轉換為本平台欄位後，若不符合 :doc:`../appendix/fields/index` 之資料範圍規定，將顯示錯誤訊息，並停止匯入。

自動產製 Data Package
~~~~~~~~~~~~~~~~~~~~~

當您建立與編輯資料集，且資料集內（上傳至本站的）資源大小合計 **小於或等於 50 MB** ，本平台將自動產製 Data Package，並上傳為一資源：

* Data Package 檔案名稱固定為 ``datapackage.zip``
* Data Package 資源 **不列於** 資料集資源列表與資料集編輯頁面
* Data Package 資源 **列於** API、 :doc:`rdf-serializations` 與 :doc:`binder` ，若您使用 API 計算資源數量，需自行排除
* Data Package 內僅包含上傳至本平台的資源；外部連結資源將僅列示於 ``datapackage.json`` ；無網址之資源將被排除
* 若資料集經編輯後，資源大小合計超過 50 MB，或所有資源均無網址，將不再產製 Data Package，並刪除既有 Data Package 資源

.. note::

    自動產製 Data Package 為背景作業。若未見「下載 Data Package」按鈕，請確認符合上述條件，並重新整理資料集頁面。

API 方法
~~~~~~~~

-----------------
更新 Data Package
-----------------

您可以使用以下指令更新 Data Package：

.. code-block:: bash

    curl -X POST \
         -H 'Authorization: YOUR_API_TOKEN' \
         -d '{"id": "DATASET_ID"}' \
         https://data.depositar.io/api/action/datapackage_update

.. note::

    * Data Package 將於建立與編輯資料集時自動產製，通常無需手動執行更新
    * 資料集仍需符合「資源合計小於或等於 50 MB」與「至少一個具網址資源」條件
    * 請參考 :doc:`data-api` 最下方說明，以取得 API token

-----------------
匯入 Data Package
-----------------

您可以使用以下指令匯入 Data Package 為本平台資料集：

上傳本機檔案：

.. code-block:: bash

    curl -X POST \
         -H 'Authorization: YOUR_API_TOKEN' \
         -F 'owner_org=project_id' \
         -F 'upload=@/path/to/datapackage.json/or/file.zip' \
         https://data.depositar.io/api/action/package_create_from_datapackage

上傳遠端網址：

.. code-block:: bash

    curl -X POST \
         -H 'Authorization: YOUR_API_TOKEN' \
         -d '{"url": "https://link.to/datapackage.json", "owner_org": project_id}' \
         https://data.depositar.io/api/action/package_create_from_datapackage

.. _Data Package: https://datapackage.org/
.. _ckanext-datapackager: https://github.com/depositar/ckanext-datapackager
.. _JSON Schema: https://json-schema.org/
.. _JSON Editor Online: https://jsoneditoronline.org/
