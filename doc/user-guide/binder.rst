===========
Binder 服務
===========

`Binder`_ 是一種線上服務，提供使用者於瀏覽器建立與執行運算環境，便於重現與展示藉由程式完成之研究成果。

.. note::

    * 此功能正在測試中，如有任何問題或建議，請 聯絡我們_。
    * 本服務由 `中央研究院網格計算中心`_ 提供運算資源，計畫編號 AS-CFII-112-103。

主要功能
--------

* 將 **公開** 資料集載入 JupyterLab 與 RStudio 等運算環境。該資料集內可含 Python、R 等語言撰寫之分析程式。
* 一鍵建立雲端運算環境，無須於個人電腦安裝相關套件。
* 可根據需求調整環境設定，與安裝額外套件。

如何使用
--------

準備資料集
~~~~~~~~~~

一個適合於 Binder 服務執行的資料集（下稱 ``Binder 資料集``)，主要包含以下兩類資料：

* (必要) **程式與分析用資料：** 欲執行的程式 (以 Python、R 等語言撰寫)，與分析的對象資料。
* (可選) **執行環境設定檔：** 指定執行程式環境所需的套件，以及欲在運算環境建立後執行的腳本等。若資料集未包含此設定檔，Binder 服務將提供預設的 JupyterLab 環境。

以如下 Binder 範例資料集 (`Binder Example: Sea turtle sightings in Taiwan`_) 為例：

該資料集包含三個檔案：

* **TurtleSpot2022_v2** (分析用資料，CSV 格式)
* **Example Jupyter notebook** (Python 程式，Jupyter Notebook ipynb 格式)
* **Conda environment file** (執行環境設定檔 ``environment.yml`` ，用以指定於 JupyterLab 安裝的 Python 版本與套件)

執行 Binder 資料集
~~~~~~~~~~~~~~~~~~

您可以於 ``研究資料寄存所`` 或 ``Binder 服務首頁`` 執行 Binder 資料集。

.. tab-set::

    .. tab-item:: 於研究資料寄存所執行

        您可以在資料集頁面左下角點選 |launch binder| 按鈕以啟動 Binder 服務，如下圖：

        .. image:: /images/binder/binder_1.png
            :width: 300

    .. tab-item:: 於 Binder 服務首頁執行

        您亦可至 Binder 服務首頁：https://binder.depositar.io/ 執行 Binder 資料集。

        在 Binder 服務首頁選取 ``CKAN dataset`` 類型，並輸入資料集網址，如下圖：

        .. image:: /images/binder/binder_4.png
            :width: 800

        再點選 launch 按鈕，即可啟動 Binder 服務。

        .. note::

            暫未支援 ARK 網址

Binder 會按照提供的執行環境設定檔，建立環境並安裝所需套件，您亦可於頁面確認建置過程：

.. image:: /images/binder/binder_2.png
    :width: 800

.. note::

    關於環境設定檔，請見下一節 (支援運算環境與客製化) 的說明。

若順利完成環境建置，Binder 將自動開啟執行環境，例如上述資料集將開啟 JupyterLab：

.. image:: /images/binder/binder_3.png
    :width: 800

您便可於開啟的 JupyterLab 環境執行運算或展示。

取得分享用連結
~~~~~~~~~~~~~~

您可在資料集頁面左下角 |launch binder| 按鈕上點選右鍵，並複製連結，如下圖：

.. image:: /images/binder/binder_5.png
    :width: 300

或於 Binder 服務首頁，選取 ``CKAN dataset`` 類型，並輸入資料集網址，再點選「Copy the URL below and share your Binder with others:」右下方按鈕以複製連結，如下圖：

.. image:: /images/binder/binder_6.png
    :width: 800

支援運算環境與客製化
--------------------

Binder 服務提供以下多種介面 (interface)：

=================== ====================================================================
介面名稱            說明
=================== ====================================================================
`JupyterLab`_       預設介面。提供 Python、R、Julia 等語言環境的線上整合開發環境 (IDE)。
`Jupyter Notebook`_ 可單獨開啟 Jupyter 筆記本檔案的傳統介面。
`RStudio`_          專為 R 統計語言設計的 IDE。
`Shiny`_            結合 R 程式與互動式網頁的套件。
=================== ====================================================================

#. JupyterLab

   您無須上傳環境設定檔即可使用此環境。

   JupyterLab 預設已安裝 Python (conda)。內建套件如下 (參見 `repo2docker`_ 套件)：

   .. code-block:: yaml

        - python=3.10
        - nodejs=18
        - pip
        - ipywidgets==8.*   # https://github.com/jupyter-widgets/ipywidgets
        - jupyter-offlinenotebook==0.2.*   # https://github.com/manics/jupyter-offlinenotebook
        - jupyter-resource-usage==0.7.*   # https://github.com/jupyter-server/jupyter-resource-usage
        - jupyter_server==1.*   # https://github.com/jupyter-server/jupyter_server
        - jupyterhub-singleuser==3.*   # https://github.com/jupyterhub/jupyterhub
        - jupyterlab==3.*   # https://github.com/jupyterlab/jupyterlab
        - notebook==6.*   # https://github.com/jupyter/notebook

   若您欲指定 Python 版本與套件，可使用以下兩種方式：

   .. note::

        請將以下提及的檔案，個別上傳為 Binder 資料集的資源

   .. tab-set::

       .. tab-item:: Conda 環境設定檔

           撰寫 Conda 之環境設定檔 ``environment.yml`` 並上傳到資料集。例如：

           .. code-block:: yaml
               :caption: environment.yml

               name: env
               dependencies:
                 - python=3.11
                 - pandas==2.*
                 - plotly==5.*

       .. tab-item:: runtime.txt 與 requirements.txt

           撰寫 ``runtime.txt`` 指定 Python 版本，並以 ``requirements.txt`` 指定欲使用的 Python 套件，並分別上傳到資料集。例如：

           .. code-block:: text
               :caption: runtime.txt

               python-3.11

           .. code-block:: text
               :caption: requirements.txt

               pandas==2.*
               plotly==5.*

   若您欲使用 RStudio 環境，則上傳 ``runtime.txt`` 內容如下：

   .. code-block:: text
       :caption: runtime.txt

       r-<RVERSION>-<YYYY>-<MM>-<DD>

   .. note::

       ``RVERSION`` 填入 R 的版本，``YYYY-MM-DD`` 填寫 `Posit 套件管理器`_ 的快照日期，例如 ``r-4.3.3-2024-02-29`` 。

   此外，您可上傳 ``install.R`` 以指定欲使用的 R 套件。例如：

   .. code-block:: r
       :caption: install.R

       install.packages("rmarkdown")
       install.packages("leaflet")

#. Jupyter Notebook

   欲切換至 Jupyter Notebook，僅需在開啟 JupyterLab 的狀態下，將網址最後的 ``/lab/`` 改為 ``/tree/`` 即可，例如：

   .. code-block:: none

       https://hub.binder.depositar.io/user/XXX/lab/

   切換為 Jupyter Notebook：

   .. code-block:: none

       https://hub.binder.depositar.io/user/XXX/tree/

#. RStudio

   參考上述 ``1. JupyterLab`` 設定 R 語言環境後，即可自開啟的 JupyterLab 頁面，連結至 RStudio IDE，如下圖：

   .. image:: /images/binder/binder_7.png
       :width: 800

#. Shiny

   參考上述 ``1. JupyterLab`` 設定 R 語言環境後，並上傳 Shiny 所需的 ``server.R`` 與 ``ui.R`` (例如 https://github.com/rstudio/shiny-examples/tree/main/034-current-time)，即可自開啟的 JupyterLab 頁面，連結至 Shiny，如下圖：

   .. image:: /images/binder/binder_8.png
       :width: 800

   .. note::

       由於本平台資料集無子資料夾之設計，請將 Shiny 所需檔案個別上傳為資料集的資源。

   其餘詳見 `Binder 環境設定檔說明`_ 。

常見問題
--------

* 此服務是免費的嗎？

  * 是的。同時提醒您，本服務亦適用本平台 `使用條款`_ 與 `隱私政策`_ 之相關內容。

* 此服務與 `mybinder`_ 有何不同？

  * `mybinder`_ 為 Binder 計畫以 `BinderHub`_ 套件建立並提供的公眾服務；本平台提供之 Binder 服務同樣以 BinderHub 套件為基礎，並擴充對 CKAN 資料集的支援。

* 哪裡能找到可於 Binder 執行的倉儲 (repository) 範例？

  * 請參考此 GitHub 組織：https://github.com/binder-examples。

* 為什麼我的資料集無法於 Binder 服務開啟？

  * 若您將資料集設為非公開，資料集頁面將不會顯示 |launch binder| 按鈕，亦無法於 Binder 服務開啟該資料集。
  * 上傳至資料集之環境設定若含有錯誤，亦可能導致 Binder 服務無法順利建置環境。

* 此服務的使用限制？

  * 2 GB 記憶體
  * 1 CPU 核心
  * 10 分鐘閒置將自動關閉
  * 2 GB 暫時儲存空間
  * 目前尚無提供永久儲存空間

* 我需要更多記憶體 / CPU 核心 / 儲存空間？

  * 請 聯絡我們_。

* 我有其他關於 Binder 的使用問題？

  * 請參閱 `Binder 使用手冊`_ 或至 `Binder 官方討論區`_ 參與討論。

.. _Binder: https://mybinder.readthedocs.io/
.. _中央研究院網格計算中心: https://dicos.grid.sinica.edu.tw/
.. _`Binder Example: Sea turtle sightings in Taiwan`: https://data.depositar.io/dataset/binder-example-sea-turtle-sightings-in-taiwan
.. _JupyterLab: https://jupyterlab.readthedocs.io/
.. _Jupyter Notebook: https://jupyter-notebook.readthedocs.io/
.. _RStudio: https://docs.posit.co/ide/user/
.. _Shiny: https://shiny.posit.co/
.. _repo2docker: https://github.com/jupyterhub/repo2docker/blob/main/repo2docker/buildpacks/conda/environment.yml
.. _Posit 套件管理器: https://packagemanager.posit.co/cran/
.. _Binder 環境設定檔說明: https://mybinder.readthedocs.io/en/latest/using/config_files.html
.. _mybinder: https://mybinder.org/
.. _BinderHub: https://binderhub.readthedocs.io/
.. _Binder 使用手冊: https://mybinder.readthedocs.io/
.. _Binder 官方討論區: https://discourse.jupyter.org/c/binder
.. _使用條款: https://data.depositar.io/terms_of_use
.. _隱私政策: https://data.depositar.io/privacy
.. |launch binder| image:: /images/binder/badge_logo.svg
