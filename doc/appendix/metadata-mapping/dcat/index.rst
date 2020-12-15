===============
DCAT 語彙設定檔
===============

本設定檔以 `DCAT 2 (版本 20200204) <https://www.w3.org/TR/2020/REC-vocab-dcat-2-20200204/>`__ 為基礎修改。

.. _namespaces:

--------
命名空間
--------

本小節將說明此設定檔使用之語彙與標準，其前綴、命名空間與文件。

.. include:: namespaces.rst

--------
欄位對應
--------

本小節將說明本平台後設資料欄位，與此設定檔語彙之對應關係。

欄位說明：

* **欄位：** 本平台後設資料欄位名稱。
* **對應語彙：** 欄位對應之語彙。以 prefixed name [1]_ 格式呈現。
* **範圍：** 描述對應語彙作為 RDF 三元組 (triple) 之屬性 (property) 時，該三元組受詞 (object) 的範圍。即 rdfs:range_。
* **規範：** 本對應參考之 RDF 語彙規範，以及該規範之文件。

.. include:: mappings.rst

.. _mappings_child:

----------
子元素對應
----------

本小節將說明此設定檔部分具子元素之元素，其使用語彙與本平台後設資料欄位之對應關係。

欄位說明：

* **類型：** 本平台後設資料欄位類型。
* **欄位：** 本平台後設資料欄位名稱。
* **值域：** 描述子元素的範圍。即 rdfs:domain_。
* **對應語彙：** 子元素對應之語彙。以 prefixed name [1]_ 格式呈現。
* **範圍：** 描述對應語彙作為 RDF 三元組 (triple) 之屬性 (property) 時，該三元組之受詞 (Object) 的範圍。即 rdfs:range_。

.. include:: mappings_child.rst

.. _field_transforms:

--------
欄位轉換
--------

本小節將說明本平台部分後設資料欄位值，轉換為符合此設定檔語彙規定數值範圍之方式。

欄位說明：

* **欄位：** 本平台後設資料欄位名稱。
* **識別碼類型 / 綱要：** 轉換後數值使用之識別碼類型或綱要，以及相關文件。
* **URI 前綴：** 轉換值所需之 URI 前綴。
* **原始值範例：** 本平台後設資料原始值。
* **轉換值範例：** 經轉換後之數值，用於 RDF 輸出。

.. include:: field_transforms.rst

.. [1] `prefix label:local part 格式 <https://www.w3.org/TR/turtle/#prefixed-name>`_。prefix label 與對應之 IRI，請參考 :ref:`namespaces` 小節之前綴與命名空間 URI。

.. _rdfs:range: https://www.w3.org/TR/rdf-schema/#ch_range
.. _rdfs:domain: https://www.w3.org/TR/rdf-schema/#ch_domain
