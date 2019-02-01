# 配置資料搜索器

`crawler` 需要配置檔作為其選項。配置的範例是在 `crawler` 安裝目錄的 `share` 目錄中提供。複製這些範例並加以修改。*請勿就地修改範例。*

檔案 `crawler.conf` 包含的資訊會告知搜索器要用於其搜索的檔案（輸入配接器），一旦搜索完成後，要傳送所搜索檔案集合的位置（輸出配接器），以及其他的搜索管理選項。

**附註**：除非另行註明，否則所有檔案路徑都是與 `config` 目錄相對。

可在此檔案中設定的選項如下：

## 輸入配接器
*  **class** - 僅供內部使用；定義「資料搜索器」輸入配接器類別。預設值是：`com.ibm.watson.crawler.connectorframeworkinputadapter.Crawl`。
*  **config** - 僅供內部使用；定義「連接器架構」配置。此區塊內要傳遞至所選輸入配接器的預設配置金鑰為：`connector_framework`。**附註** -「連接器」架構可讓您與資料通訊。它可以是在企業中的內部資料，或也可以是 Web 上或雲端中的外部資料。連接器允許存取許多不同的資料來源，而連線實際上是由搜索程序控制。
  -  **重要事項** -「連接器架構輸入配接器」所擷取的資料會在本端快取。不會採用加密格式儲存它。依預設，該資料會快取至重新開機時應該先清除的暫存目錄中，而且應該只供執行搜索器指令的使用者讀取。如果連接器架構是要在它之後自行清除之前離開，此目錄的存留時間有機會比搜索器還長。請仔細考量快取資料的位置 - 您可以將它放在已加密的檔案系統中，但請注意這樣做的效能含意。只有您才能決定搜索速度與安全之間的適當平衡。
*  **crawl_config_file** - 用於搜索的配置檔。預設值是：`connectors/filesystem.conf`。
*  **crawl_seed_file** - 要用於搜索的搜索種子檔。預設值是：`seeds/filesystem-seed.conf`。
*  **id_vcrypt_file** - 用於由搜索器進行資料加密的金鑰檔；搜索器隨附的預設金鑰是 `id_vcrypt`。如果您需要產生新的 id_vcrypt_file，請使用 `bin` 資料夾中的 vcrypt Script
*  **crawler_temp_dir** - 用於連接器日誌的「搜索器」暫存資料夾。提供預設值 `tmp`。如果它還不存在，則將在現行工作目錄中建立 `tmp` 資料夾。
*  **extra_jars_dir** - 僅供內部使用；將額外的 JAR 新增至「連接器架構」類別路徑。使用 SharePoint 連接器時，此值必須是 `oakland`；而使用資料庫連接器時，此值必須是 `database`。使用其他連接器時，您可以將其保留為空白（也就是空字串 ""）。**附註**：相對於連接器架構 `lib/java` 目錄。
*  **urls_to_filter** - 要搜索的 URL 以換行區隔的白名單，採用正規表示式格式。「資料搜索器」僅搜索符合提供的其中一個正規表示式的 URL。網域清單包含最常見的最上層網域；必要的話可新增至該清單。副檔名類型清單包含這個版本的「資料搜索器」發行時，「編排服務」支援的副檔名。請確保過濾器允許您的種子 URL 網域。例如，如果種子 URL 看起來類似 `http://testdomain.test.in`，請將 `in` 新增到網域過濾器。請確保您的種子 URL 不會被過濾器排除，否則「搜索器」可能會當掉。
*  **max_text_size** -「連接器架構」將文件寫入磁碟之前可以具備的大小上限（以位元組為單位）。將它調高會減少寫入磁碟的文件量，但會增加記憶體需求。
*  **extra_vm_params** - 可讓您將額外的 Java 參數新增至用來啟動「連接器架構」的指令。
*  **bootstrap_logging** - 寫入連接器架構啟動日誌；僅適用進階除錯。值為 `true` 或 `false`。日誌檔將寫入到 `crawler_temp_dir`。

## 儲存體配接器

允許將搜索器的內部狀態器儲存至資料庫。需要此設定，搜索 `restart` 及 `resume` 選項才能正確運作。

```javascript
storage_adapter {
 config = "storage_in_db"
  storage_in_db {
    include "storage/database_storage.conf"
  } 
}
```
參照的檔案 `storage/database_storage.conf` 預設會使用 H2 資料庫。您可以對 JDBC 驅動程式使用任何資料庫，而不是提供的預設值。請參閱 JDBC 驅動程式的說明文件，以尋找有關部分設定的特定資訊。可以直接變更預設選項，方法是開啟 `config/storage/database_storage.conf` 檔案，並修改您的使用案例特定的下列值：
*  **class** - 此類別會指向要使用的資料庫配接器類別。預設值是 `com.ibm.watson.crawler.storageadapters.DatabasePersistAdapter`
*  **driver** - JDBC 驅動程式的類別。預設值是 `org.h2.Driver` 以使用 H2
*  **url** - 請參閱驅動程式的 JDBC 選項。這是 JDBC 連線字串的 URL 字首。預設值是 `jdbc:h2:file:`
*  **database_location** - 要放置資料庫的位置。這僅適用檔案型資料庫，像是 sqlite 與 H2。預設值是 `./storage/database`
*  **database_name** - 資料庫的名稱。預設值是 `ActivityDB`
*  **table_name** - 要使用的表格名稱。預設值是 `Ledger`
*  **username** - 用來連接資料庫的使用者名稱
*  **password** - 用來連接資料庫的密碼

預設配置對大部分活動已足夠。

## 輸出配接器

有一些*輸出配接器*可供選擇。透過設定 `crawler.conf` 中的 `output_adapter.class` 來輸出配接器。選項有：

*  **class** - 定義「資料搜索器」輸出配接器類別。預設值是 `com.ibm.watson.crawler.discoveryserviceoutputadapter.DiscoveryServiceOutputAdapter`
*  **config** - 定義要傳遞至輸出配接器的配置金鑰。字串必須對應於此配置物件內的金鑰。在下列程式碼範例中：
```javascript
  orchestration_service {
    include "orchestration_service.conf"
  },
  test {
    output_directory = "/tmp/crawler-test-output"
  }
}
```
配置金鑰是 `orchestration_service`。預設值是 `discovery_service`

您必須透過指定其 `class` 參數和 `config` 金鑰來選取輸出配接器。

* **編排服務輸出配接器**：將已搜索的文件上傳至「Watson Developer Cloud 的編排服務」。透過設定 `class` 參數及 `config` 金鑰來選取此配接器，如下所示： 
```javascript
  class = "com.ibm.watson.crawler.orchestrationserviceoutputadapter.oneatatime.OrchestrationServiceOutputAdapter"
  config = "orchestration_service"
  orchestration_service {
    include "orchestration/orchestration_service.conf"
  }
```
* **Discovery Service 輸出配接器**：將已搜索的文件上傳至「Watson Developer Cloud 的 Discovery Service」。透過設定 `class` 參數及 `config` 金鑰來選取此配接器，如下所示：
```javascript
  class = "com.ibm.watson.crawler.discoveryserviceoutputadapter.DiscoveryServiceOutputAdapter"
  config = "discovery_service"
  discovery_service {
    include "discovery/discovery_service.conf"
  }
```
* **Watson 測試輸出配接器**：會將所搜索檔案的呈現寫入磁碟的指定位置中。透過設定 `class` 參數及 `config` 金鑰來選取此配接器，如下所示：

**附註** - 額外的參數 `output_directory` 會選取要將所搜索資料的呈現寫入其中之目錄。
```javascript
  class = "com.ibm.watson.crawler.testoutputadapter.TestOutputAdapter"
  config = "test"
  output_directory = "/tmp/crawler-test-output"
```
* **retry** - 指定若嘗試推送至輸出配接器失敗，用於重試的選項。
  * max_attempts - 重試次數上限。預設值是 `10`
  * delay - 嘗試之間的延遲下限量（以秒為單位）。預設值是 `2`
  * exponent_base - 因數，決定隨著每一個失敗嘗試延遲時間的成長。預設值是 `2`

 公式為：
```
 d(nth_retry) = delay * (exponent_base ^ nth_retry)
```

 例如，帶有 1 秒延遲和指數基數 2 的設定，將造成第二次重試到第三次重試之間延遲 2 秒，而不是 1 秒，以及下一次則延遲 4 秒。
 ```
 d(0) = 1 * (2 ^ 0) = 1 second
 d(1) = 1 * (2 ^ 1) = 2 seconds
 d(2) = 1 * (2 ^ 2) = 4 seconds
```
因此，利用預設值，提交最多會嘗試 10 次，最多等待大約 1,022 秒（稍微超出 17 分鐘）。此時間為大約值，因為有新增額外的時間，以避免多個重新提交同步執行。這個模糊時間最長為 10%，所以在前一個範例中，最後一次重試最多可能延遲 4.4 秒。等待時間不包括連接至服務、上傳資料或等待回應所耗費的時間。 *警告：*減少等待時間，透過降低任何預設值，可能導致文件無法透過已配置的輸出配接器成功上傳。使用 Watson Developer Cloud 服務時，此情況的證明為日誌中的 RetryFailure 訊息，說明「429 太多要求」速率限制。
 
## 除錯選項
*  **full_node_debugging** - 啟動除錯模式；可能的值為 `true` 或 `false`。**警告**：這會將已搜索的每個文件之完整資料放置到日誌中。
*  **heartbeat_wait_time** - 報告文件汲取統計資料（僅限除錯模式）之間的時間間隔（毫秒）。預設值是 1000 毫秒。

## 記載選項
*  **configuration_file** - 用於記載的配置檔。在範例 `crawler.conf` 檔案中，此選項是定義在 `logging.log4j`，並且其預設值是 `log4j_custom.properties`。使用 `.properties` 或 `.conf` 檔案時，也必須以類似方式定義此選項。

## 其他搜索管理選項
*  **shutdown_timeout** - 指定關閉應用程式之前的逾時值（分鐘）。預設值是 `10`。
*  **output_limit** -「搜索器」將嘗試同步傳送至輸出配接器的可檢索項目之最高數量。這可以利用可供用來執行作業的核心數進一步限制。它指出任何指定時候均不得將超過 "x" 個可檢索項目傳送至等待傳回的輸出配接器。預設值是 `10`。
*  **input_limit** - 限制一次可以向連接器要求的 URL 數量。預設值是 `3`。
*  **output_timeout** -「資料搜索器」放棄對輸出配接器的要求，然後從輸出配接器佇列移除項目以允許更多處理之前的時間量（以秒為單位）。預設值是 `1200`。**附註** - 應該考量輸出配接器強制施行的限制，因為那些限制可能與這裡定義的限制相關。上方定義的 `output_limit` 只與一次可以傳送至輸出配接器的可檢索物件數量相關。
一旦將可檢索物件傳送至輸出配接器後，它便「計入工作」，如 `output_timeout` 變數所定義。輸出配接器本身有可能具有節流控制，使得它無法處理所接收的諸多輸入。例如，編排輸出配接器可能有連線儲存區，可配置對服務的 HTTP 連線。例如，如果它預設為 8，且如果您將 `output_limit` 設定為大於 8 數量，則您會有計入工作的程序在等候執行。接著您可能會遇到逾時。
*  **num_threads** - 可一次執行的平行執行緒數目。此值可以是整數，其直接指定平行執行緒的數目，也可以是字串，帶有格式 "xNUM"，指定可用處理器數量的乘法係數，例如，"x1.5"。預設值是 `"30"`。

## 另請參閱

crawler(1)

vcrypt(1)

crawler-options.conf(5)

crawler-seed.conf(5)

orchestration_service.conf(5)
