# 配置 Discovery Service
当使用 IBM Watson Discovery Service 时，Discovery Service 会告知搜寻器如何管理已搜寻的文件。要直接更改缺省选项，请打开 `config/discovery/discoveryservice.conf` 文件，并根据您的用例来修改以下值：

*  **http_timeout** - 文档读取/建立索引操作的超时值（以秒计）；缺省值为 `125`。
*  **concurrent_upload_connection_limit** - 可用于上载文档的并发连接数；缺省值为 `2`。当使用 Orchestration Service 输出适配器时，此数字应大于或等于在配置搜寻选项时设置的 `output_limit`。
*  **base_url** - 要将已搜寻文档发送到的 URL。对于 Discovery Service 的当前发行版，此值为 `https://gateway.watsonplatform.net/discovery/api`。
*  **environment_id** - `base-url` 的已搜寻文档集合所在的位置。
*  **collection_id** - 您在 Discovery Service 中设置的文档集合的名称。
*  **configuration_id** - Discovery Service 使用的配置文件的文件名。
*  **check_for_completion** - 检查在端点上是否成功处理了文档。这会让您感到搜寻器的性能有所下降，但会生成与文档上载和转换成功与否有关的可靠通知。值为 `true` 或 `false`。  
**要点** - 启用此参数后，最好将 `concurrent_upload_connection_limit` 增至大于或等于在配置搜寻选项时设置的 `output_limit`，以便充分利用可用的资源。

提供您的 Discovery Service 凭证：
*  **username** - 用于向已搜寻文档集合所在位置进行认证的用户名。
*  **password** - 用于向已搜寻文档集合所在位置进行认证的密码。

Discovery Service 输出适配器可以发送统计信息，让 IBM 能够更好地理解用户需求并服务于用户。可设置 `send_stats` 变量的以下选项：
*  **jvm** - 已发送的 Java 虚拟机 (JVM) 统计信息（包括 Java 供应商和版本），这些统计信息由用于执行 Data Crawler 的 JVM 来报告。值为 `true` 或 `false`。
*  **os** - 已发送的操作系统 (OS) 统计信息（包括 OS 名称、版本和体系结构），这些统计信息由用于执行 Data Crawler 的 JVM 来报告。值为 `true` 或 `false`。

*  **api_version** - 仅供内部使用。上次更改 API 版本的日期。

# 配置 URL 跟踪存储器
`config/discovery` 文件夹还包含一个配置文件，用于在内部映射搜寻器 URL 与文档标识。要直接更改缺省选项，请打开 `config/discovery/uri_tracking_storage.conf` 文件，并根据您的用例来修改以下值：

*  **driver** - 您的数据库的 JDBC H2 驱动程序类。缺省值为 `org.h2.Driver`。
*  **url** - 这是 JDBC 连接字符串的 URL 前缀。格式为 `jdbc:h2:[file:]`。**注**：前缀 `file:` 为可选。如果未提供此前缀，或者只使用了 `database_location` 的相对路径，那么将使用当前工作目录作为起点。缺省值为 `jdbc:h2:file:`。
*  **database_location** - 磁盘上用于存储数据库的位置，例如，`./storage/database` 或 `~/storage/database`。缺省值为 `./storage/database`。
*  **database_name** - 数据库的名称。缺省值为 `ActivityDB`。
*  **table_name** - 要使用的表的名称。缺省值为 `UriTracker`。
*  **username** - 用于连接到数据库的用户名
*  **password** - 用于连接到数据库的密码

## 另请参阅

crawler(1)

vcrypt(1)

crawler.conf(5)

crawler-options.conf(5)

crawler-seed.conf(5)
