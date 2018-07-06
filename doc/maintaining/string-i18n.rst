========
程式翻譯
========

------------
字串翻譯方法
------------

本平台客製套件支援多語系翻譯，定義字串翻譯的方式簡述如下。

.. note::

   本節僅簡要記述，詳細作法請直接參考 `String internationalization`_

#. Jinja2 模板內字串翻譯

   一般為以下形式。單引號內的字元（Hello World!）即可被翻譯為其他語系。

   .. code-block:: jinja

      {% set hello = _('Hello World!') %}

#. Python 程式內字串翻譯

   一般為以下形式。雙引號（或單引號）內的字元（This paragraph is translatable.）即可被翻譯為其他語系。

   .. code-block:: python

      my_string = _("This paragraph is translatable.")

----------------------
產生與編譯字串翻譯檔案
----------------------

在定義好可翻譯字串後，需產生對應語系之翻譯檔案方能生效。

.. important::

   執行以下指令時，請確認您位於 Python 虛擬環境中，否則安裝作業可能會失敗。當虛擬環境執行時，命令提示字元（shell prompt）會有類似以下前綴： ::

     (default) $ _

   您可隨時執行以下指令以返回虛擬環境： ::

     . /usr/lib/ckan/default/bin/activate

.. important::

   執行以下指令時，請確定您位於客製套件根目錄：

   .. parsed-literal::

      cd /usr/lib/ckan/default/src/ckanext-data-depositario

a. 擷取所有待翻譯字串

   .. parsed-literal::

      python setup.py extract_messages

b. 建立個別語系待翻譯字串

   .. note::

      以下均以台灣繁體中文為例說明。

      另因本語系已存在，故使用 update_catalog 參數以保留已翻譯字串。若欲新增語系，請改為 init_catalog。

   .. parsed-literal::

      python setup.py update_catalog -l zh_TW

c. 開啟以下檔案並開始翻譯字串（msgstr 部分）

   .. parsed-literal::

      vi ckanext/data_depositario/i18n/zh_TW/LC_MESSAGES/ckanext-data_depositario.po

d. 編譯已翻譯字串

   .. parsed-literal::

      python setup.py compile_catalog

e. 重新啟動 CKAN 以使更改生效

   .. note::

      此處假設您已完成 CKAN 部署工作，若尚未完成請先參考 :doc:`installing/deployment` 完成部署。

   .. parsed-literal::

      sudo stop ckan && sudo start ckan
