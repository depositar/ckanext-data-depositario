ARK 持續識別碼
==============

`資源典藏碼 <https://arks.org/about/>`_ (Archival Resource Key, ARK) 是一種多用途、可以用來指稱各類資訊物件的通用識別碼。本平台透過 `ckanext-ark <https://github.com/depositar/ckanext-ark>`_ 套件，賦予符合條件的資料集以 ARK 為編碼規格的持續識別碼 (persistent identifier, PID)，提供資料集長期不變的網址，功能類同於數位物件識別碼 (Digital Object Identifier, DOI)。

.. note::

   此功能正在測試中，如有任何問題或建議，請 聯絡我們_。

本服務發行的 ARK 持續識別碼均以 ``ark:`` 開頭（例如： ``ark:37281/k5c8w2q9c`` ），依序以下列編碼規則產生：

* ``37281`` ：註冊於 `N2T.net <https://n2t.net/ark:37281/>`__ 之 `NAAN <https://arks.org/about/ark-naans-and-systems/>`_ (Name Assigning Authority Number)，用以識別 ARK 的發行組織
* ``k5`` ：固定且專用於本平台資料集的子命名空間（ARK 稱之為 `shoulder <https://www.ietf.org/archive/id/draft-kunze-ark-34.html#name-optional-shoulders>`_ ）
* 唯一識別碼：ARK 稱之為 blade，為使用 ``redededk`` 規則（ARK 稱之為 `template <https://metacpan.org/dist/Noid/view/noid#TEMPLATES>`_ ）編碼之 7 位英數字：

  * ``r`` 代表該 7 位英數字識別碼為準隨機生成 (quasi-randomly generated)
  * ``e`` 代表該位數為右列擴充字元 (extended digit) 之一： ``{0123456789bcdfghjkmnpqrstvwxz}``
  * ``d`` 代表該位數為右列純數字 (pure digit) 之一： ``{0123456789}``
  * ``k`` 代表最後一位的校驗字元 (check character)

關於 ARK 的技術規格，請參考此 `IETF 網際網路草案 <https://datatracker.ietf.org/doc/draft-kunze-ark/>`_ 。

ARK 識別碼發放條件
------------------

為確保 ARK 識別碼得以廣泛流通，與滿足後設資料需求，資料集需設定為公開，且至少填寫以下欄位：

* 標題
* 起始時間（與「結束時間」至少填寫其中之一）
* 結束時間（與「起始時間」至少填寫其中之一）
* 產製者

.. note::

   * 請參考 :ref:`後設資料項目 <dataset_fields>` 。
   * 關於資料集的公開與非公開，請參考 :ref:`editing-a-dataset` 。將不公開資料集設為公開，亦可獲得 ARK 識別碼。
   * 若您於 ARK 識別碼配發後，移除上述欄位，ARK 仍為有效，且會保留包含上述欄位的後設資料 (ERC)。

透過 ARK 識別碼連結至資料集
---------------------------

您可以在資料集頁面左下角的「ARK 識別碼」查詢以 ``ark:`` 開頭之 ARK 識別碼與網址，如下圖：

.. image:: /images/ark_1.png
  :width: 300

此 ARK 網址將自動導向資料集頁面。

本平台所使用的 ARK 識別碼名稱對應服務 (Name Mapping Authority, NMA) 為 https://pid.depositar.io/。您亦可使用 `N2T.net <https://n2t.net/>`__ 所提供的對應服務，僅需將網址的 https://pid.depositar.io/ 代換為 https://n2t.net/ 即可。

.. note::

   展示用網站 (https://demo.depositar.io/) 的 NMA 為 https://demo.depositar.io/，且不支援 N2T.net 對應服務，亦不保證 ARK 識別碼之持續性。

ARK 識別碼後設資料 (ERC)
------------------------

您可於 ARK 識別碼網址後方加上 ``?info`` ，即可獲得該描述該識別碼的簡要後設資料。

.. note::

   此後設資料稱為 `ERC (Electronic Resource Citation) <https://n2t.net/ark:/13030/c7sn0141m>`_ 。本平台使用 ERC 記載資料集的摘要資訊。

ERC 資訊以 JSON 格式呈現，在 ``erc`` 屬性內包含以下資料：

====== ================= =============================================
欄位   內容              取自 :ref:`後設資料項目 <dataset_fields>`
====== ================= =============================================
what   標題              標題
when   時間資訊          起始時間與結束時間，以 YYYYMMDD-YYYYMMDD 呈現
where  此 ARK 識別碼網址 無（由系統自動產生）
who    產製者            產製者
====== ================= =============================================

已失效 ARK 識別碼
-----------------

在資料集獲配 ARK 識別碼後，若您執行以下動作，將令 ARK 識別碼失效：

* 將資料集設為不公開
* 將資料集刪除
* 將資料集永久刪除（僅系統管理員具有此權限）

在上述情況下，連結至 ARK 識別碼網址，系統將顯示以下已失效 ARK 頁面：

.. image:: /images/ark_2.png
  :width: 400

針對以上前兩種情形，已失效的 ARK 識別碼仍可如下部份運作：

* 雖已將資料集設為不公開，但登入具有該資料集瀏覽權限之帳號時
* 雖已將資料集刪除，但登入該資料集產製者之帳號時

.. note::

   * 若您將資料集重新公開，或復原已刪除資料集，對應之 ARK 識別碼即會恢復有效狀態。
   * 已失效 ARK 識別碼仍會保留其後設資料 (ERC)。
