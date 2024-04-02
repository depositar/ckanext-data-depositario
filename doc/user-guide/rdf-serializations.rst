RDF Serializations (串列化輸出)
===============================

本平台使用 ckanext-dcat 提供之 `RDF 串聯器 (serializer) <https://github.com/ckan/ckanext-dcat/tree/v1.1.0#rdf-dcat-serializer>`_ 輸出 RDF graph。

關於本平台後設資料與 RDF graph 輸出語彙間之對照，請參閱 :doc:`../appendix/metadata-mapping/dcat/index`。

.. note::

   此功能正在測試中，如有任何問題或建議，請 聯絡我們_。

.. note::

   支援的輸出格式如下表所示：

   ========= ========= ===================
   格式      副檔名    網際網路媒體類型
   ========= ========= ===================
   RDF/XML   xml       application/rdf+xml
   Turtle    ttl       text/turtle
   Notation3 n3        text/n3
   JSON-LD   jsonld    application/ld+json
   ========= ========= ===================

.. hint::

   以下說明中出現之 ``{}``：

   * ``dataset-id`` 請填寫資料集 **網址 (名稱)**
   * ``format`` 請填寫上方表格之 **副檔名**
   * ``media_type`` 請填寫上方表格之 **網際網路媒體類型**

方法一：RDF Endpoints
----------------------

.. parsed-literal::

   全站資料集：

   :site_url:`catalog.{format}`

   單一資料集：

   :site_url:`dataset/{dataset-id}.{format}`

您亦可至資料集頁面左下角「其他存取方式」獲得該資料集之 RDF 串列化結果，如下圖：

.. image:: /images/rdf_serializations.png

方法二：內容協商 (Content Negotiation)
--------------------------------------

請於終端機執行以下指令：

.. parsed-literal::

   curl :site_url:`dataset/{dataset-id}` -H Accept:{media_type}

範例
----

以此 :site_url:`範例資料集 <dataset/place-names-in-west-central-district-of-tainan>`，取得 RDF/XML 格式為例：

方法一：

.. parsed-literal::

   :site_url:`dataset/place-names-in-west-central-district-of-tainan.xml`

方法二：

於終端機執行以下指令：

.. parsed-literal::

   curl :site_url:`dataset/place-names-in-west-central-district-of-tainan` -H Accept:application/rdf+xml
