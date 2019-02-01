# 配置 Orchestration Service
Orchestration Service 会告知搜寻器如何管理已搜寻的文件。要直接更改缺省选项，请打开 `config/orchestration/orchestration-service.conf` 文件，并根据您的用例来修改以下值：

*  **http_timeout** - 文档读取/建立索引操作的超时值（以秒计）；缺省值为 `585`。
*  **concurrent_upload_connection_limit** - 可用于上载文档的并发连接数；缺省值为 `10`。 通常，此数字应大于或等于在配置搜寻选项时设置的 `output_limit`。
*  **base_url** - 要将已搜寻文档发送到的 URL。
*  **endpoint** - `base-url` 的已搜寻文档集合所在的位置。
*  **username** - 用于向 `endpoint` 位置进行认证的用户名。
*  **password** - 用于向 `endpoint` 位置进行认证的密码。**要点** - **请勿**使用 Data Crawler 随附的 vcrypt 程序来加密此密码。
*  **config_file** - Orchestration Service 使用的配置文件。

Orchestration Service 输出适配器可以发送统计信息，让 IBM 能够更好地理解用户需求并服务于用户。可设置 `send_stats` 变量的以下选项：
*  **jvm** - 已发送的 Java 虚拟机 (JVM) 统计信息（包括 Java 供应商和版本），这些统计信息由用于执行 Data Crawler 的 JVM 来报告。值为 `true` 或 `false`。
*  **os** - 已发送的操作系统 (OS) 统计信息（包括 OS 名称、版本和体系结构），这些统计信息由用于执行 Data Crawler 的 JVM 来报告。值为 `true` 或 `false`。

## 另请参阅

crawler(1)

vcrypt(1)

crawler.conf(5)

crawler-options.conf(5)

crawler-seed.conf(5)
