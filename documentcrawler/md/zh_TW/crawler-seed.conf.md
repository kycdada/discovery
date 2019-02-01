# 配置搜索種子

種子是搜索的起始點，並可供資料搜索器用來從該種子所識別之資源擷取資料。一般而言，種子會配置 URL 來存取通訊協定型資源，例如檔案共用、SMB 共用、資料庫及可由各種 Web 通訊協定存取的其他資料儲存庫。而且，不同的種子 URL 有不同的功能。

種子也可以是儲存庫特定，以啟用特定協力廠商應用程式（例如客戶關係管理 (CRM) 系統、產品生命週期 (PLC) 系統、內容管理系統 (CMS)、雲端型應用程式及 Web 資料庫應用程式）的搜索。

資料搜索器目前提供的搜索種子可支援下列儲存庫類型的檔案連接器：

*	檔案系統
*	資料庫，透過 JDBC
*	CMIS（內容管理交互作業能力服務）
*	SMB（伺服器訊息區塊）、CIFS（一般網際網路檔案系統）或 Samba 檔案共用
*	SharePoint 與 SharePoint Online
*	Box

也會提供搜索種子配置範本，其可讓您為自訂連接器自訂搜索種子。

## 開始使用：

搜索資料儲存庫時，搜索器會在使用者指定的種子 URL 開始，並開始下載資訊的頁面。搜索器也會尋找所下載頁面中的鏈結，並將新探索到的頁面排定進行進一步搜索。

配置資訊可用來判斷需要搜索哪些頁面，以及如何搜索它們。這個檔案說明您可以對每一個連接器的搜索種子檔配置的選項。

**附註**：每一個搜索種子配置檔，可配合使用對應的檔案連接器配置檔；檔案連接器選項將個別說明。

### 配置檔案系統搜索種子

您可以為「檔案系統」搜索種子檔配置下列值。若要設定這些值，請開啟檔案 `config/seeds/filesystem-seed.conf`，並指定您的使用案例特定的下列值：

*  **url** - 要搜索的檔案與資料夾以換行區隔清單。UNIX 使用者可以使用 `/usr/local/` 之類的路徑。URL 的開頭必須是 `sdk-fs://`。因此比方說，若要搜索 `/home/watson/mydocs`，此 URL 的值會是 `sdk-fs:///home/watson/mydocs` - 第三個 `/` 是必要的！**附註**：「檔案系統」連接器會使用自訂通訊協定 `sdk-fs://` 來建立有效的 URL。請勿將 `file://` 附加到所列出路徑的前面；URL 的開頭必須是 `sdk-fs://`。
*  **hops** - 僅供內部使用。
*  **default-allow** - 僅供內部使用。

### 配置資料庫搜索種子

您可以為資料庫搜索種子檔配置下列值。若要設定這些值，請開啟檔案 `config/seeds/database-seed.conf`，並指定您的使用案例特定的下列值：

*  **url** - 要擷取表格或視圖的 URL。定義您的自訂 SQL 資料庫種子 URL。結構為：

   	`database-system://host:port/database?[per=num]&[sql=SQL]`

   測試種子 URL 將顯示放入佇列的所有 URL。例如，測試下列 URL 可取得含有 200 筆記錄的資料庫：

   	`sqlserver://test.mycompany.com:1433/WWII_Navy/?per=100&sql=select%20*%20from%20vessel&`

   顯示下列放入佇列的 URL：

   	`sqlserver://test.mycompany.com:1433/WWII_Navy/?key-val=0&`

   	`sqlserver://test.mycompany.com:1433/WWII_Navy/?key-val=100&`

   	`sqlserver://test.mycompany.com:1433/WWII_Navy/?key-val=200&`

   當測試下列 URL 時，將顯示從列 43 擷取的資料：

   	`sqlserver://test.mycompany.com:1433/WWII_Navy/?per=1&key-val=43`
*  **hops** - 僅供內部使用。
*  **default-allow** - 僅供內部使用。
*  **user-password** - 資料庫系統的認證。使用者名稱和密碼需要以 `:` 來區隔，且密碼必須使用「資料搜索器」隨附的 vcrypt 程式來加密。例如：`username:[[vcrypt/3]]passwordstring`。
*  **max-data-size** - 文件資料的大小上限。這是一次將載入的最大記憶體區塊。只有在您的電腦上有足夠的記憶體時才增加此限制。
*  **filter-exact-duplicates** - 僅供內部使用。
*  **jdbc-class**（延伸器選項）- 若指定，當您選擇 `(other)` 作為資料庫系統時，此字串會置換連接器所使用的 JDBC 類別。
*  **connection-string**（延伸器選項）- 若指定，此字串會置換連接器自動產生的 JDBC 連線字串。如此一來，您就可以提供關於資料庫連線更詳細的配置，例如負載平衡或 SSL 連線。例如：`jdbc:netezza://127.0.0.1:5480/databasename`。
*  **save-frequency-for-resume**（延伸器選項）- 指定直欄或關聯標籤的名稱，以便能夠回復搜索或執行局部重新整理。種子會在繼續進行搜索時定期儲存此直欄的名稱，並在搜索您的資料庫最後一列之後，再次儲存該名稱。回復搜索或重新整理它時，搜索會從此欄位所儲存值中識別的列開始。

### 配置 CMIS 搜索種子

您可以為 CMIS 搜索種子檔配置下列值。若要設定這些值，請開啟檔案 `config/seeds/cmis-seed.conf`，並修改您的使用案例特定的下列值：

*  **url** - 要作為搜索起始點的 CMIS 儲存庫資料夾的 URL，例如：

   *  `cmis://alfresco.test.com:8080/alfresco/cmisatom?folderToProcess=workspace://SpacesStore/guid`
若要從根資料夾搜索，您需要以下列形式提供 URL：

   *  `cmis://alfresco.test.com:8080/alfresco/cmisatom?folderToProcess=`
*  **at** - 未使用的選項。
*  **default-allow** - 僅供內部使用。

### 配置 Samba 搜索種子

您可以為 Samba 搜索種子檔配置下列值。若要設定這些值，請開啟檔案 `config/seeds/samba-seed.conf`，並修改您的使用案例特定的下列值：

*  **url** - 要搜索的共用以換行區隔清單，例如：

   *  `smb://share.test.com/office`
   *  `smb://share.test.com/cash/money/change`
   *  `smb://share.test.com/C$/Program Files`

*  **hops** - 僅供內部使用。
*  **default-allow** - 僅供內部使用。

### 配置 SharePoint 搜索種子

您可以為 SharePoint 搜索種子檔配置下列額外的值。若要設定這些值，請開啟檔案 `config/seeds/sharepoint-seed.conf`，並修改您的使用案例特定的下列值：

*  **url** - 要搜索的 SharePoint Web 應用程式或網站集合以換行區隔的清單，例如：

   *  `io-sp://a.com`
   *  `io-sp://b.com:83/site`
   *  `io-sp://c.com/site2`

   也會搜索這些網站的子網站（除非它們已由其他搜索規則排除）。
*  **filter-url** - 要搜索的 SharePoint Web 應用程式或網站集合以換行區隔的清單，例如：

   *  `http://a.com`
   *  `http://b.com:83/site`
   *  `http://c.com/site2`

*  **hops** - 僅供內部使用。
*  **n-concurrent-requests** - 僅供內部使用。
*  **delay** - 僅供內部使用。
*  **default-allow** - 僅供內部使用。
*  **seed-protocol** - 設定網站集合子項的種子通訊協定。當網站集合的通訊協定是 SSL、HTTP 或 HTTPS 時為必要。此值必須設定為與網站集合的通訊協定相同。

### 配置 Box 種子

您可以為 Box 搜索種子檔配置下列值。若要設定這些值，請開啟檔案 `config/seeds/box-seed.conf`，並指定您的使用案例特定的下列值：

*  **URL** - 要作為搜索起始點的 URL。預設值是 `box://app.box.com/`。
*  **default-allow** - 僅供內部使用。

## 另請參閱

crawler(1)

vcrypt(1)

crawler.conf(5)

crawler-options.conf(5)

orchestration_service.conf(5)
