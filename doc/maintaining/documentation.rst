========
撰寫文件
========

.. note::

   本節僅簡要記述，詳細作法請直接參考 `CKAN 官方文件 <http://docs.ckan.org/en/ckan-2.6.4/contributing/documentation.html>`_

------------
文件編輯方法
------------

安裝本文件於 Python 虛擬環境
============================

新增一個 Python 虛擬環境（virtualenv）供文件使用，並進入該虛擬環境

::

    virtualenv --no-site-packages pyenv
    . pyenv/bin/activate
    pip install -e 'git+https://github.com/depositar-io/ckanext-data-depositario.git#egg=ckanext-data-depositario'
    cd pyenv/src/ckanext-data-depositario
    pip install -r requirements-docs.txt
    cd ../ckan
    pip install -r requirements.txt

開始編輯
========

文件原始碼均位於 ``pyenv/src/ckanext-data-depositario/doc`` 目錄下，使用 `Sphinx <http://sphinx-doc.org/>`_ 建立，內容以 reStructuredText 語法撰寫，您可以參考以下連結的介紹：

* `Sphinx's reStructuredText Primer <http://sphinx-doc.org/rest.html>`_
* `reStructuredText cheat sheet <http://docutils.sourceforge.net/docs/user/rst/cheatsheet.txt>`_
* `reStructuredText quick reference <http://docutils.sourceforge.net/docs/user/rst/quickref.html>`_
* `Sphinx Markup Constructs <http://sphinx-doc.org/markup/index.html>`_

------------
文件產生方法
------------

在發佈文件之前，請先於本機測試生成供發佈用之 HTML 檔案。指令如下

.. parsed-literal::

   cd ../ckanext-data-depositario
   python setup.py build_sphinx

您即可使用瀏覽器開啟 ``build/sphinx/html/index.html`` 檔案瀏覽生成之 HTML 檔案。

.. important::

   請務必確保執行此文件生成指令時，無產生任何警告（warnings）。建議將整個 ``build`` 目錄移除以再次確認：

   .. parsed-literal::

      rm -rf build; python setup.py build_sphinx

------------
文件發佈方法
------------

本文件使用 `ReadTheDocs <https://readthedocs.org/>`_ 服務發佈。您只要完成修改後，利用 ``git push`` 指令將 ckanext-data-depositario 推送至 GitHub，數分鐘後 ReadTheDocs 即會自動生成新版文件。
