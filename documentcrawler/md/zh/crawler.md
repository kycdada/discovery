crawler(1) - 用于将数据从 A 点移到 B 点的搜寻器
====================================================================

## 摘要

用法：crawler [ crawl | testit | restart | resume | refresh | summary ][ options ]

## 描述

Data Crawler 用于搜寻各种数据存储库（例如，内容管理系统和文件系统），然后将生成的文档推送到远程服务。

## 全局选项

    --version
        显示程序版本
    --help
        显示此用法文本

## 命令

### crawl [选项]

使用当前配置运行搜寻。

    -c <value> | --config <value>  # 指定要使用的配置文件。缺省值为“config/crawler.conf”。--pii-checking <value>         # 切换 PII 检查

### testit [选项]

运行测试搜寻，以仅搜寻种子 URL 并显示任何排队的 URL。如果种子 URL 生成了可索引内容（例如，文档），那么该内容将发送到输出适配器并打印到屏幕上。如果种子 URL 检索操作导致将 URL 排队，那么将显示这些 URL，并且不会将任何内容发送到输出适配器。缺省情况下，将显示五个排队的 URL。

    -c <value> | --config <value>  # 指定要使用的配置文件。缺省值为“config/crawler.conf”。-l <n> | --limit <n>    # 限制要显示的排队 URL 数。
--pii-checking <value>         # 切换 PII 检查

### restart [选项]

运行重新启动搜寻；使用当前配置启动新搜寻。

    -c <value> | --config <value>  # 指定要使用的配置文件。
--pii-checking <value>         # 切换 PII 检查

### resume [选项]

从搜寻的停止位置恢复搜寻。

    -c <value> | --config <value>  # 指定要使用的配置文件。
--pii-checking <value>         # 切换 PII 检查

### refresh [选项]

刷新上一次搜寻。

    -c <value> | --config <value>  # 指定要使用的配置文件。
--pii-checking <value>         # 切换 PII 检查

### summary [选项]

生成搜寻报告。

    --submitted                    # 查询已提交的所有文档
    --processed                    # 只查询已成功处理的文档
    --failed                       # 只查询未成功处理的文档
    --group-id <value>             # 查询指定组的搜寻运行。组由初始搜寻及其任何恢复、刷新或重新启动操作组成。如果未指定此值，那么此查询缺省设置为最近搜寻的组。--show-content                 # 显示与查询关联的其他任何内容
    --filter                       # 根据 URL 和 hashID 过滤查询结果

## 示例

使用 `config/crawler.conf` 中的配置文件来运行搜寻：

    crawler crawl

使用 `config/crawler.conf` 中的配置文件来运行测试：

    crawler testit

使用 `/home/watson/office-share.conf` 中的配置文件来运行搜寻：

    crawler crawl --config /home/watson/office-share.conf

使用 `/home/watson/office-share.conf` 中的配置文件来重新启动搜寻：

    crawler restart --config /home/watson/office-share.conf

获取组标识为 `2` 的失败文档的摘要信息：

    crawler summary --failed --group-id 2 --show-content

显示用法（包括版本）：

    crawler --help

## 配置

`搜寻器`需要通过一个配置文件来设置其选项。`搜寻器`安装目录中的 `share` 目录中提供了一些配置文件示例。请复制这些示例并作出修改。*请勿在原始位置中修改这些示例。*

如果未指定 `--config | -c` 选项，那么`搜寻器`将在`搜寻器`启动目录内的 `config` 目录中查找其配置。即，`搜寻器`将查找 `config/crawler.conf`。

## 诊断

可使用以下功能来诊断问题。

### 调试

激活调试方式。在 `crawler.conf` 文件中，进行以下设置：

    debugging.full_node_debugging = true

### 日志记录

启用日志记录。在 `log4j_custom.properties` 文件中，进行以下设置：

    log4j.rootLogger=INFO, Console, Log

这是文件输出的缺省日志记录级别。对于控制台日志，缺省值为：

    log4j.appender.Console.Threshold=WARN

日志记录级别可设置为以下值：

    OFF - 可实现的最高等级，用于关闭日志记录。
    FATAL - 指示非常严重的错误事件，这些事件可能导致应用程序异常终止。
    ERROR - 指示可能仍允许应用程序继续运行的错误事件。
    WARN - 指示可能有危害的情况。
    INFO - 指示用于强调应用程序进度的粗颗粒度参考消息。
    DEBUG - 指示对于调试应用程序最为有用的细颗粒度参考事件。
    TRACE - 指示比 DEBUG 更详细的参考事件。
    ALL - 可实现的最低等级，用于打开所有日志记录。

## 调速

定义大小限制，以帮助管理吞吐量。在 `crawler.conf` 文件中，进行以下设置：

`shutdown_timeout` 指定超时值（以分钟计），经过这段时间后才关闭应用程序；缺省值为 10。

    shutdown_timeout = <n>

`output_limit` 是便携式搜寻器可同时发送到输出适配器（等待返回）的可索引项的最大数量；缺省值为 10。可用于执行处理的内核数将进一步限制此选项。

    output_limit = <n>

`input_limit` 限制可从连接器同时请求的 URL 数；缺省值为 3。

    input_limit = <n>

`output_timeout` 是便携式搜寻器放弃对输出适配器的请求并从限制队列中移除此项以释放更多处理资源之前等待的时间量（以秒计）。缺省值为 150。

    output_timeout = <n>

应注意输出适配器施加的约束，因为这些约束可能与此处定义的限制有关。上面定义的 `output_limit` 仅与可同时发送到输出适配器的可索引对象数有关。将可索引对象发送到输出适配器后，便开始“计时”（如 `output_timeout` 变量所定义）。输出适配器本身可能具有调速，这会阻止它处理所收到的所有输入。例如，Orchestration 输出适配器可能有一个连接池（可针对到该服务的 HTTP 连接进行配置）。例如，如果将此值缺省设置为 8，那么当您为 `output_limit` 设置的数字大于为该连接池配置的数字时，会有一些进程已开始计时并等待轮流执行。这样，您可能会遇到超时。

`num_threads` 可同时运行的并行线程数。此值可以为整数（直接指定并行线程数），也可以为 `"xNUM"` 格式的字符串（指定可用处理器数的倍增因子）。缺省值为“x1.5”，或可用处理器数（取自 `Runtime.availableProcessors`）的 1.5 倍。

    num_threads = <n>

Data Crawler 池中并行性的计算公式为：`min(maxThreads, max(minThreads, numThreads))`。

## 环境变量 `CRAWLER_OPTS` 

下面列出了可通过 `CRAWLER_OPTS` 环境变量传递到`搜寻器`的属性及其缺省值。

按如下所示传递这些属性：

    CRAWLER_OPTS="-Dproperty=value -Dproperty=value" crawler

只有在 IBM 支持人员的指导下，出于调试目的才可以更改这些属性。

### cfa.java_bin

`cfa.java_bin` 更改用于启动 Connector Framework 输入适配器的 `java` 命令。缺省情况下，`搜寻器`会使用用于启动`搜寻器`本身的 `java` 二进制文件。

也可以通过设置 `java.home` 属性（随后可用于计算 `java` 可执行文件的路径）来更改此属性。

### cfa.lib_dir

`cfa.lib_dir` 更改 Connector Framework 的 `lib` 目录的路径。很少需要更改此路径。缺省情况下，`搜寻器`会使用 Connector Framework 的计算路径（通常就是 `connectorFramework`）中的 `lib` 目录。

### cfa.framework_jars_dir

`cfa.framework_jars_dir` 更改 Connector Framework 的 jars 目录（缺省情况下位于 `connectorFramework/<version>/lib/java` 中）的路径。

### cfa.plugins_dir

`cfa.plugins_dir` 指定 Connector Framework 的 plugins 目录（用于存储实际 Connector 的位置）的路径。
缺省情况下，此路径通过 `framework_jars_dir` 来构建，且为 `connectorFramework/<version>/lib/java/plugins`。

## 已知限制

下面详述了 Data Crawler 当前发行版中的已知限制。

* 使用无效或缺失的 URL 运行文件系统连接器时，Data Crawler 可能会挂起。
* 配置 `config/crawler.conf` 文件中的 `urls_to_filter` 值，以便将所有白名单 URL 或正则表达式都包含在单个正则表达式中。
* `--config | -c` 选项中传递的配置文件的路径必须为标准路径。即，此路径必须为相对路径 `config/crawler.conf` 或 `./crawler.conf`，或者为绝对路径 `/path/to/config/crawler.conf`。当且仅当使用 `crawler.conf` 文件中的 `include` 所引用的文件是直接插入而不是使用 `include` 时，才能指定 `crawler.conf`。例如，为便于阅读配置，已使用 `include` 指定了 `discovery/discovery_service.conf`。必须将其内容复制到 `crawler.conf` 内的 `output_adapter.discovery_service` 键中，才能在 config 选项中使用非标准路径。

## 更改日志

请参阅安装目录中的 `changelog.txt` 文件，以获取此发行版中的更改列表。

## 作者

IBM Watson - https://www.ibm.com/smarterplanet/us/en/ibmwatson/

由 Yinz 著于匹兹堡市。

## 另请参阅

vcrypt(1)

crawler.conf(5)

crawler-options.conf(5)

crawler-seed.conf(5)

orchestration_service.conf(5)
