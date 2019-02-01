# 配置編排服務
編排服務會指示搜索器如何管理搜索的檔案。可以直接變更預設選項，方法是開啟 `config/orchestration/orchestration-service.conf` 檔案，並修改您的使用案例特定的下列值：

*  **http_timeout** - 文件讀取/索引作業的逾時（以秒為單位）；預設值是 `585`。
*  **concurrent_upload_connection_limit** - 允許上傳文件的同時連線的數量；預設值是 `10`。一般而言，此數量應該大於或等於配置搜索選項時所設定的 `output_limit`。
*  **base_url** - 將傳送您的已搜索文件的目標 URL。
*  **endpoint** - 在 `base-url` 您的已搜索文件集合的位置。
*  **username** - 用來向 `endpoint` 位置鑑別的使用者名稱。
*  **password** - 用來向 `endpoint` 位置鑑別的密碼。**重要事項** - 請**勿**使用「資料搜索器」隨附的 vcrypt 程式來加密此密碼。
*  **config_file** - 編排服務所使用的配置檔。

「編排服務輸出配接器」可以傳送統計資料，以讓 IBM 更充分瞭解及為其使用者提供服務。您可以為 `send_stats` 變數設定下列選項：
*  **jvm** - 傳送的 Java 虛擬機器 (JVM) 統計資料包括 Java 供應商及版本，如用來執行資料搜索器的 JVM 所報告。值為 `true` 或 `false`。
*  **os** - 傳送的作業系統 (OS) 統計資料包括作業系統名稱、版本及架構，如用來執行資料搜索器的 JVM 所報告。值為 `true` 或 `false`。

## 另請參閱

crawler(1)

vcrypt(1)

crawler.conf(5)

crawler-options.conf(5)

crawler-seed.conf(5)
