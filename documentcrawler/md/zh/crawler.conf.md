# 配置 Data Crawler

`搜寻器`需要通过一个配置文件来设置其选项。`搜寻器`安装目录中的 `share` 目录中提供了一些配置示例。请复制这些示例并作出修改。*请勿在原始位置中修改这些示例。*

`crawler.conf` 文件包含的信息用于告知搜寻器要使用哪些文件进行搜寻（输入适配器）、完成搜寻后将已搜寻文件的集合发送到的位置以及其他搜寻管理选项。

**注**：所有文件路径都相对于 `config` 目录，除非另有说明。

可在此文件中设置以下选项：

## 输入适配器
*  **class** - 仅供内部使用；定义 Data Crawler 输入适配器类。缺省值为 `com.ibm.watson.crawler.connectorframeworkinputadapter.Crawl`。
*  **config** - 仅供内部使用；定义 Connector Framework 配置。此块中要传递到所选输入适配器的缺省配置键为 `connector_framework`。
**注** - 您可以使用 Connector Framework 来与自己的数据进行交互。这可以是企业的内部数据，也可以是 Web 或云上的外部数据。可通过连接器来访问大量不同的数据源，但连接实际由搜寻过程控制。
  -  **要点** - 将在本地缓存 Connector Framework 输入适配器所检索的数据。这些数据在存储时不进行加密。缺省情况下，用于缓存这些数据的临时目录应该会在重新引导时被清除，且只能由执行 crawler 命令的用户来读取。如果 Connector Framework 在可执行清除之前就已消失，那么此目录可能比搜寻器存在时间更长。请谨慎考虑缓存数据的存放位置 - 您可以将这些数据放到加密的文件系统中，但需要注意这样做所产生的性能影响。只有您可以决定搜寻速度与安全性之间的适度平衡。
*  **crawl_config_file** - 要用于搜寻的配置文件。缺省值为 `connectors/filesystem.conf`。
*  **crawl_seed_file** - 要用于搜寻的搜寻种子文件。缺省值为 `seeds/filesystem-seed.conf`。
*  **id_vcrypt_file** - 搜寻器执行数据加密所使用的密钥文件；搜寻器随附的缺省密钥为 `id_vcrypt`。
如果需要生成新的 id_vcrypt_file，请使用 `bin` 文件夹中的 vcrypt 脚本。
*  **crawler_temp_dir** - 用于连接器日志的搜寻器临时文件夹。提供的缺省值为 `tmp`。如果还不存在 `tmp` 文件夹，那么将在当前工作目录中创建该文件夹。
*  **extra_jars_dir** - 仅供内部使用；向 Connector Framework 类路径添加额外的 JAR。
在使用 SharePoint 连接器时，该值必须为 `oakland`，而在使用数据库连接器时，该值必须为 `database`。在使用其他连接器时，可将该值留空（即空字符串 ""）。**注**：相对于 Connector Framework `lib/java` 目录。
*  **urls_to_filter** - 要搜寻的 URL 白名单（用换行符分隔），采用正则表达式形式。Data Crawler 只会搜寻与提供的正则表达式之一相匹配的 URL。域列表包含最常见的顶级域；可根据需要向此列表中添加域。从 Data Crawler 的这一发行版开始，文件扩展名类型列表包含 Orchestration Service 支持的文件扩展名。确保过滤器不会排除您的种子 URL 域。例如，如果种子 URL 类似于 `http://testdomain.test.in`，那么将向域过滤器添加“`in`”。确保过滤器不会排除您的种子 URL，否则 Crawler 可能挂起。
*  **max_text_size** - Connector Framework 将文档写入到磁盘前该文档的最大大小（以字节计）。调高该值将会减少向磁盘写入的文档数量，但会增加内存需求。
*  **extra_vm_params** - 允许您向用于启动 Connector Framework 的命令中添加额外的 Java 参数。
*  **bootstrap_logging** - 编写 Connector Framework 启动日志；仅用于高级调试。值为 `true` 或 `false`。将日志文件写入到 `crawler_temp_dir` 中。

## 存储适配器

允许将搜寻器的内部状态存储到数据库中。必须使用此设置，才能使搜寻的 `restart` 和 `resume` 选项正确工作。

```javascript
storage_adapter {
 config = "storage_in_db"
  storage_in_db {
    include "storage/database_storage.conf"
  } 
}
```
缺省情况下，引用的文件 `storage/database_storage.conf` 使用 H2 数据库。您可以使用任何具有 JDBC 驱动程序的数据库来代替所提供的缺省值。请参阅您的 JDBC 驱动程序文档，以查找有关其中某些设置的特定信息。要直接更改缺省选项，请打开 `config/storage/database_storage.conf` 文件，并根据您的用例来修改以下值：
*  **class** - 此类指向要使用的数据库适配器类。缺省值为 `com.ibm.watson.crawler.storageadapters.DatabasePersistAdapter`。
*  **driver** - JDBC 驱动程序类。缺省值为 `org.h2.Driver`（即使用 H2）。
*  **url** - 请参阅您驱动程序的 JDBC 选项。这是 JDBC 连接字符串的 URL 前缀。缺省值为 `jdbc:h2:file:`。
*  **database_location** - 您希望数据库所在的位置。这仅适用于基于文件的数据库（如，sqlite 和 H2）。缺省值为 `./storage/database`。
*  **database_name** - 数据库的名称。缺省值为 `ActivityDB`。
*  **table_name** - 要使用的表的名称。缺省值为 `Ledger`。
*  **username** - 用于连接到数据库的用户名
*  **password** - 用于连接到数据库的密码

缺省配置可满足大多数活动的需求。

## 输出适配器

提供了一对可供选择的*输出适配器*。可通过设置 `crawler.conf` 中的 `output_adapter.class` 来设置输出适配器。选项包括：

*  **class** - 定义 Data Crawler 输出适配器类。缺省值为 `com.ibm.watson.crawler.discoveryserviceoutputadapter.DiscoveryServiceOutputAdapter`。
*  **config** - 定义要传递到输出适配器的配置键。该字符串必须与此配置对象中的键相对应。在以下代码示例中：
```javascript
  orchestration_service {
    include "orchestration_service.conf"
  },
  test {
    output_directory = "/tmp/crawler-test-output"
  }
}
```
配置键为 `orchestration_service`。缺省值为 `discovery_service`。

必须通过指定 `class` 参数和 `config` 键来选择输出适配器。

* **Orchestration Service 输出适配器**：将已搜寻的文档上载到 Watson Developer Cloud 的 Orchestration Service 中。通过设置 `class` 参数和 `config` 键来选择此适配器，如下所示： 
```javascript
  class = "com.ibm.watson.crawler.orchestrationserviceoutputadapter.oneatatime.OrchestrationServiceOutputAdapter"
  config = "orchestration_service"
  orchestration_service {
    include "orchestration/orchestration_service.conf"
  }
```
* **Discovery Service 输出适配器**：将已搜寻的文档上载到 Watson Developer Cloud 的 Discovery Service 中。通过设置 `class` 参数和 `config` 键来选择此适配器，如下所示：
```javascript
  class = "com.ibm.watson.crawler.discoveryserviceoutputadapter.DiscoveryServiceOutputAdapter"
  config = "discovery_service"
  discovery_service {
    include "discovery/discovery_service.conf"
  }
```
* **Watson Test 输出适配器**：将已搜寻文件的表示写入到磁盘上指定的位置。通过设置 `class` 参数和 `config` 键来选择此适配器，如下所示：

**注** - 额外参数 `output_directory` 用于选择要向其中写入已搜寻数据的表示的目录。
```javascript
  class = "com.ibm.watson.crawler.testoutputadapter.TestOutputAdapter"
  config = "test"
  output_directory = "/tmp/crawler-test-output"
```
* **retry** - 指定在推送至输出适配器的尝试失败时可用的重试选项。
  * max_attempts - 最大重试次数。缺省值为 `10`。
  * delay - 两次尝试之间的最短延迟（以秒计）。缺省值为 `2`。
  * exponent_base - 用于确定每次失败尝试后延迟时间增长量的因子。缺省值为 `2`。

 公式为：
```
 d(nth_retry) = delay * (exponent_base ^ nth_retry)
```

 例如，如果将 delay 设置为 1 秒且将 exponent_base 设置为 2，那么将导致第二次尝试与第三次尝试之间的延迟为 2 秒（而不是 1 秒），而下一个延迟为 4 秒。
 ```
 d(0) = 1 * (2 ^ 0) = 1 second
 d(1) = 1 * (2 ^ 1) = 2 seconds
 d(2) = 1 * (2 ^ 2) = 4 seconds
```
因此，如果使用缺省设置，那么最多将尝试提交 10 次，最长等待时间约为 1,022 秒（略微超过 17 分钟）。此时间为近似值，因为其中会额外增加一些时间以防同时执行多个重新提交操作。此“模糊”时间最多为 10%，因此前一示例中最后一次重试的延迟可达 4.4 秒。等待时间不包括连接到服务、上载数据或等待响应所用的时间。
 *警告：*如果通过降低任何这些缺省值来缩短等待时间，可能导致无法通过所配置的输出适配器成功上载文档。在使用 Watson Developer Cloud 服务时，反映这一情况的证据是日志中引用“429 Too Many Requests”速率限制的 RetryFailure 消息。
 
## 调试选项
*  **full_node_debugging** - 激活调试方式；可能的值包括 `true` 或 `false`。**警告**：这会将每个已搜寻文档的全部数据放入日志中。
*  **heartbeat_wait_time** - 两次报告文档摄入统计信息之间的时间间隔，以毫秒计（仅限调试方式）。缺省值为 1000 毫秒。

## 日志记录选项
*  **configuration_file** - 要用于日志记录的配置文件。在样本 `crawler.conf` 文件中，在 `logging.log4j` 中定义此选项，并且其缺省值为 `log4j_custom.properties`。
无论是使用 `.properties` 还是 `.conf` 文件，必须以同样的方式定义此选项。

## 其他搜寻管理选项
*  **shutdown_timeout** - 指定超时值（以分钟计），经过这段时间后才关闭应用程序。缺省值为 `10`。
*  **output_limit** - 搜寻器尝试同时发送到输出适配器的可索引项的最大数量。可用于执行处理的内核数会进一步限制此选项。即，在任何时候向等待返回的输出适配器发送的可索引项的数量不得超过“x”。缺省值为 `10`。
*  **input_limit** - 限制可从连接器同时请求的 URL 数。缺省值为 `3`。
*  **output_timeout** - Data Crawler 放弃对输出适配器的请求并从输出适配器队列中移除此项以释放更多处理资源之前等待的时间量（以秒计）。缺省值为 `1200`。**注** - 应注意输出适配器施加的约束，因为这些约束可能与此处定义的限制有关。上面定义的 `output_limit` 仅与可同时发送到输出适配器的可索引对象数有关。将可索引对象发送到输出适配器后，便开始“计时”（如 `output_timeout` 变量所定义）。输出适配器本身可能具有调速，这会阻止它处理所收到的所有输入。例如，Orchestration 输出适配器可能有一个连接池（可针对到该服务的 HTTP 连接进行配置）。例如，如果将此值缺省设置为 8，并且您为 `output_limit` 设置的数字大于 8，那么会有一些进程已开始计时并等待轮流执行。这样，您可能会遇到超时。
*  **num_threads** - 可同时运行的并行线程数。此值可以为整数（直接指定并行线程数），也可以为“xNUM”格式的字符串（指定可用处理器数的倍增因子，例如“x1.5”）。缺省值为 `"30"`。

## 另请参阅

crawler(1)

vcrypt(1)

crawler-options.conf(5)

crawler-seed.conf(5)

orchestration_service.conf(5)
