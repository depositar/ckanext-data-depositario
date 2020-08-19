.. list-table::
   :widths: 20 5 45 30
   :header-rows: 1

   * - 名稱
     - 必填
     - 說明
     - 資料範圍

   * - 網址
     - 否
     - 線上資源的連結位址。
     - 必須是 unicode 字元。

   * - 名稱
     - 否
     - 本筆資源的名稱。資料集內不同的資源應用不同的名稱區別。
     - 必須是 unicode 字元。

   * - 摘要
     - 否
     - 關於資源的簡短描述。
     - Markdown 欄位。

   * - 字元編碼
     - 否
     - 此資源所使用之編碼系統，如 UTF-8、Big5 等。目前僅用於 shapefile 資源。
     - 限以下 `IANA Character Sets <https://www.iana.org/assignments/character-sets/character-sets.xhtml>`_ 編碼之一：

       | Big5 (繁體中文大五碼)
       | UTF-8
       | ISO-8859-1 (西歐字元)
       | GB2312 (簡體中文)
       | GB18030 (簡體中文)
       | Shift_JIS (日文)
       | EUC-JP (日文)

   * - 座標參考系統
     - 否
     - 當您所新增之資源為 shapefile 檔案，且未提供投影格式（.prj）檔案時，則需另外填寫此欄位，否則將無法開啟預覽功能。採用 EPSG （歐洲石油測量組織）編碼。
     - 必須是正整數。

   * - 格式
     - 否
     - 資源的檔案格式，例如：CSV、XLS、JSON、PDF 等。格式填寫內容將會影響本平台所設定的資源預覽的預設畫面。請參考 :ref:`data_preview`。
     - 必須是 unicode 字元。
