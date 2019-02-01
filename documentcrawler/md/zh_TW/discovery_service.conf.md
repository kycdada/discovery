# 配置 Discovery Service
使用 IBM Watson Discovery Service 時，Discovery Service 會指示搜索器如何管理搜索的檔案。可以直接變更預設選項，方法是開啟 `config/discovery/discovery_service.conf` 檔案，並修改您的使用案例特定的下列值：

*  **http_timeout** - 文件讀取/索引作業的逾時（以秒為單位）；預設值是 `125`。
*  **concurrent_upload_connection_limit** - 允許上傳文件的同時連線的數量；預設值是 `2`。使用「編排服務輸出配接器」時，此數量應該大於或等於配置搜索選項時所設定的 `output_limit`。
*  **base_url** - 將傳送您的已搜索文件的目標 URL。對於現行版本的 Discovery Service，此值是 `https://gateway.watsonplatform.net/discovery/api`。
*  **environment_id** - 您的已搜索文件集合在 `base-url` 的位置。
*  **collection_id** - 您在 Discovery Service 中所設定文件集合的名稱。
*  **configuration_id** - Discovery Service 所使用的配置檔的檔名。

*  **check_for_completion** - 檢查是否已在端點上成功處理文件。如此會降低搜索器的既有效能，但會產生已成功上傳和轉換文件的可靠通知。值為 `true` 或 `false`。  
**IMPORTANT** - 啟用此參數時，明智的做法是將 `concurrent_upload_connection_limit` 增加為大於或等於配置搜索選項時所設定的 `output_limit`，以便充分利用您可以使用的資源。

提供您的 Discovery Service 認證：
*  **username** - 用來向您所搜索的文件集合的位置鑑別的使用者名稱。
*  **password** - 用來向您所搜索的文件集合的位置鑑別的密碼。

「Discovery Service 輸出配接器」可以傳送統計資料，以讓 IBM 更充分的瞭解及為其使用者提供服務。您可以為 `send_stats` 變數設定下列選項：
*  **jvm** - 傳送的 Java 虛擬機器 (JVM) 統計資料包括 Java 供應商及版本，如用來執行資料搜索器的 JVM 所報告。值為 `true` 或 `false`。
*  **os** - 傳送的作業系統 (OS) 統計資料包括作業系統名稱、版本及架構，如用來執行資料搜索器的 JVM 所報告。值為 `true` 或 `false`。

*  **api_version** - 僅供內部使用。前次 API 版本變更的日期。

# 配置 URL 追蹤儲存體
`config/discovery` 資料夾也包含一個配置檔，可用於搜索器 URL 與文件 ID 的內部對映。可以直接變更預設選項，方法是開啟 `config/discovery/uri_tracking_storage.conf` 檔案，並修改您的使用案例特定的下列值：

*  **driver** - 資料庫的 JDBC H2 驅動程式類別。預設值是 `org.h2.Driver`
*  **url** - 這是 JDBC 連線字串的 URL 字首。格式為 `jdbc:h2:[file:]`。**附註**：字首 `file:` 是選用的。如果未使用，或只對 `database_location` 使用一個相對路徑，則會使用現行工作目錄作為起始點。預設值是 `jdbc:h2:file:`
*  **database_location** - 儲存資料庫所在磁碟上的位置，例如，`./storage/database` 或 `~/storage/database`。預設值是 `./storage/database`
*  **database_name** - 資料庫的名稱。預設值是 `ActivityDB`
*  **table_name** - 要使用的表格名稱。預設值是 `UriTracker`
*  **username** - 用來連接資料庫的使用者名稱
*  **password** - 用來連接資料庫的密碼

## 另請參閱

crawler(1)

vcrypt(1)

crawler.conf(5)

crawler-options.conf(5)

crawler-seed.conf(5)
