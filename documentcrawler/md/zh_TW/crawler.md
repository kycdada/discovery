crawler(1) - 搜索器，用來將資料從點 A 移動至點 B
====================================================================

## 用法概要

用法：crawler [ crawl | testit | restart | resume | refresh | summary ][ options ]

## 說明

「資料搜索器」可用來搜索資料的各種儲存庫，例如內容管理系統和檔案系統，然後將產生的文件推送至遠端服務。

## 廣域選項

    --version
        顯示程式版本
    --help
        顯示此用法文字

## 指令

### crawl [ options ]

以現行配置執行搜索。

    -c <value> | --config <value>  # 指定要使用的配置檔。預設值是 "config/crawler.conf"。
    --pii-checking <value>         # 切換 PII 檢查

### testit [ options ]

執行測試搜索，只搜索種子 URL，並顯示任何放入佇列的 URL。如果種子 URL 造成可檢索的內容（例如，它是文件），則會將該內容傳送到輸出配接器，並將內容列印至畫面。如果種子 URL 擷取使 URL 放入佇列，將會顯示那些 URL，且不會將內容傳送至輸出配接器。依預設，會顯示五個放入佇列的 URL。

    -c <value> | --config <value>  # 指定要使用的配置檔。預設值是 "config/crawler.conf"。
    -l <n> | --limit <n>           # 限制所顯示放入佇列的 URL 數量。
    --pii-checking <value>         # 切換 PII 檢查

### restart [ options ]

執行「重新啟動」搜索；以現行配置啟動新的搜索。

    -c <value> | --config <value>  # 指定要使用的配置檔。
    --pii-checking <value>         # 切換 PII 檢查

### resume [ options ]

從停止搜索處繼續搜索。

    -c <value> | --config <value>  # 指定要使用的配置檔。
    --pii-checking <value>         # 切換 PII 檢查

### refresh [ options ]

重新整理前一個搜索。

    -c <value> | --config <value>  # 指定要使用的配置檔。
    --pii-checking <value>         # 切換 PII 檢查

### summary [ options ]

產生一份搜索報告。

    --submitted                    # 查詢所有提交的文件
    --processed                    # 僅查詢成功處理的文件
    --failed                       # 僅查詢無法成功處理的文件
    --group-id <value>             # 查詢針對指定群組執行的搜索。一個群組包含一個起始搜索，以及該起始搜索的任何回復、重新整理或重新啟動。如果未指定值，此查詢會預設為搜索最新的群組。
    --show-content                 # 顯示與查詢關聯的任何其他內容
    --filter                       # 依 URL 和 hashID 過濾查詢結果

## 範例

使用位於 `config/crawler.conf` 的配置檔執行搜索：

    crawler crawl

使用位於 `config/crawler.conf` 的配置檔執行測試：

    crawler testit

使用位於 `/home/watson/office-share.conf` 的配置檔執行搜索：

    crawler crawl --config /home/watson/office-share.conf

使用位於 `/home/watson/office-share.conf` 的配置檔重新啟動搜索：

    crawler restart --config /home/watson/office-share.conf

取得群組 ID 為 `2` 之失敗文件的摘要資訊：

    crawler summary --failed --group-id 2 --show-content

顯示用法，包括版本：

    crawler --help

## 配置

`crawler` 需要配置檔作為其選項。配置檔的範例是在 `crawler` 安裝目錄的 `share` 目錄中提供。複製這些範例並加以修改。*請勿就地修改範例。*

如果沒有指定 `--config | -c` 選項，`crawler` 會在已啟動 `crawler` 目錄的 `config` 目錄中尋找其配置。也就是說，`crawler` 會尋找 `config/crawler.conf`。

## 診斷

使用這些特性來診斷問題。

### 除錯

啟動除錯模式。在 `crawler.conf` 檔案中，設定：

    debugging.full_node_debugging = true

### 記載

啟用記載功能。在 `log4j_custom.properties` 檔案中，設定：

    log4j.rootLogger=INFO, Console, Log

這是檔案輸出的預設記載層次。對於主控台日誌，預設值是：

    log4j.appender.Console.Threshold=WARN

記載層次可以設定為下列值：

    OFF - 可能的最高等級，這預期會關閉記載。
    FATAL - 指定將可能導致應用程式中止的非常重大錯誤事件。
    ERROR - 指定仍可能讓應用程式繼續執行的錯誤事件。
    WARN - 指定可能有害的狀況。
    INFO - 指定參考訊息，以粗略層次強調顯示應用程式的進度。
    DEBUG - 指定對於除錯應用程式最實用的精細參考資訊事件。
    TRACE - 指定較 DEBUG 更精細的參考資訊事件。
    ALL - 可能的最低等級，這預期會開啟所有記載。

## 節流控制

定義大小限制以協助管理傳輸量。在 `crawler.conf` 檔案中，設定：

`shutdown_timeout` 指定關閉應用程式之前的逾時值（分鐘）；預設值是 10。

    shutdown_timeout = <n>

`output_limit` 是可攜式搜索器將同步傳送至輸出配接器等待傳回的可檢索項目之最高數量；預設值是 10。這可能會另外受可供用來執行作業的核心數所限制。

    output_limit = <n>

`input_limit` 限制一次可以向連接器要求的 URL 數量；預設值是 3。

    input_limit = <n>

`output_timeout` 是可攜式搜索器放棄對輸出配接器的要求，然後從限制佇列移除項目以允許更多處理之前的時間量（以秒為單位）。預設值是 150。

    output_timeout = <n>

應該考量輸出配接器所強制施行的限制，因為那些限制可能與這裡定義的限制相關。上方定義的 `output_limit` 只與一次可以傳送至輸出配接器的可檢索物件數量相關。一旦將可檢索物件傳送至輸出配接器後，它便「計入工作」，如 `output_timeout` 變數所定義。輸出配接器本身有可能具有節流控制，使得它無法處理所接收的諸多輸入。例如，編排輸出配接器可能有連線儲存區，可配置對服務的 HTTP 連線。例如，如果它預設為 8，且如果您將 `output_limit` 設定為大於該連線儲存區配置的數量，則您會有計入工作的程序在等候執行。接著您可能會遇到逾時。

`num_threads` 可一次執行的平行執行緒數目。此值可以是整數，直接指定平行執行緒的數目，也可以是字串，帶有格式 `"xNUM"`，指定可用處理器數量的乘法係數。預設值是 "x1.5"，或 1.5 乘上可用處理器的數量（如同採用 `Runtime.availableProcessors`）。

    num_threads = <n>

用於在「資料搜索器」儲存區中計算平行化的公式：`min(maxThreads, max(minThreads, numThreads))`。

## 環境變數 `CRAWLER_OPTS` 

以下為可透過 `CRAWLER_OPTS` 環境變數傳遞至 `crawler` 的內容，列出時加上預設值。

以此方式傳遞它們：

    CRAWLER_OPTS="-Dproperty=value -Dproperty=value" crawler

應該僅針對除錯目的，並且在 IBM 支援中心指示的情況下才變更它們。

### cfa.java_bin

`cfa.java_bin` 可以變更用來啟動「連接器架構輸入配接器」的 `java` 指令。依預設，`crawler` 會使用用來啟動 `crawler` 本身的相同 `java` 二進位。

您也可以透過設定 `java.home` 內容來變更它，然後它用來計算 `java` 執行檔的路徑。

### cfa.lib_dir

`cfa.lib_dir` 會將路徑變更為「連接器架構」的 `lib` 目錄。這應該不太需要變更。依預設，`crawler` 會使用「連接器架構」計算路徑內的 `lib` 目錄，通常只是 `connectorFramework`。

### cfa.framework_jars_dir

`cfa.framework_jars_dir` 會將路徑變更為「連接器架構」的 JAR 目錄，預設是在 `connectorFramework/<version>/lib/java` 中。

### cfa.plugins_dir

`cfa.plugins_dir` 會指定「連接器架構」plugins 目錄的路徑，實際的「連接器」都儲存在此處。依預設，這是從 `framework_jars_dir` 建置，並且將會是 `connectorFramework/<version>/lib/java/plugins`。

## 已知限制

現行版本資料搜索器中已知限制的詳細資料

* 使用無效或遺漏的 URL 執行「檔案系統」連接器時，「資料搜索器」可能會當掉。
* 配置 `config/crawler.conf` 檔案中的 `urls_to_filter` 值，這樣所有白名單 URL 或正規表示式都包含在單一正規表示式中。
* 傳入 `--config | -c` 選項的配置檔路徑必須是完整路徑。也就是說，它必須採用相對格式 `config/crawler.conf` 或 `./crawler.conf`，或絕對路徑 `/path/to/config/crawler.conf`。若且唯若使用 `crawler.conf` 檔案中的 `include` 參照的檔案為行內，而不是使用 `include` 時，可以僅指定 `crawler.conf`。例如，將 `discovery/discovery_service.conf` `include`，以便讓配置更易於閱讀。必須將其內容複製到 `output_adapter.discovery_service` 金鑰內的 `crawler.conf`，以便在配置選項中使用不完整路徑。

## 變更日誌

請參閱安裝目錄中的 `changelog.txt` 檔案，以取得此版本中的變更清單。

## 作者

IBM Watson - https://www.ibm.com/smarterplanet/us/en/ibmwatson/

由匹茲堡的 yinz 製作。

## 另請參閱

vcrypt(1)

crawler.conf(5)

crawler-options.conf(5)

crawler-seed.conf(5)

orchestration_service.conf(5)
