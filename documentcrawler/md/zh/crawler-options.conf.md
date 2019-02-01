# 配置搜寻选项
Data Crawler 将收集最终用于形成 IBM Watson Retrieve and Rank 服务的搜索结果的原始数据。

目前，Data Crawler 提供了一些连接器以用于从以下存储库收集数据：

*	文件系统
*	使用 JDBC 的数据库
*	CMIS（内容管理互操作性服务）
*	SMB（服务器消息块）、CIFS（公共因特网文件系统）或 Samba 文件共享
*	SharePoint 和 SharePoint Online
*	Box

此外还提供了一个连接器配置模板，您可以使用此模板来定制连接器。

## 入门：
在搜寻数据存储库时，搜寻器从用户指定的起始种子 URL 开始，并开始下载信息页面。另外，搜寻器还会查找已下载页面中的链接，并安排进一步搜寻新发现的页面。

系统将使用配置信息来确定要搜寻的页面及其搜寻方式。此文件解释了每个连接器的可配置选项。

**注**：每个连接器还有一个对应的种子配置文件；在其他位置会单独描述种子配置选项。

### 配置文件系统连接器
您可以使用文件系统连接器来搜寻 Data Crawler 安装的本地文件。下面是使用文件系统连接器时需要设置的基本配置选项。要设置这些值，请打开文件 `config/connectors/filesystem.conf`，并根据您的用例来修改以下值：

*  **protocol** - 用于搜寻的连接器协议的名称。请对此连接器使用 `sdk-fs`。
*  **collection** - 该属性用于解包临时文件。
*  **logging-config** - 指定用于配置日志记录选项的文件；它必须格式化为 `log4j` XML 字符串。
*  **classname** - 连接器的 Java 类名。使用此连接器时，该值必须为 `plugin:filesystem.plugin@filesystem`。

### 配置数据库连接器
您可以使用数据库连接器，通过执行定制 SQL 命令并针对每行（记录）创建一个文档且针对每列（字段）创建一个内容元素，以搜寻数据库。您可以指定要用作唯一键的列，还可以指定包含时间戳记（表示每个记录的上次修改日期）的列。该连接器将从指定数据库中检索所有记录，也可以通过 SQL 语句限制为特定的表和连接等。

您可以使用数据库连接器来搜寻以下数据库：

*  IBM DB2
*  MySQL
*  Oracle
*  PostgreSQL
*  Microsoft SQL Server
*  Sybase
*  使用 JDBC 3.0 兼容驱动程序的其他 SQL 兼容数据库

该连接器将从指定数据库和表中检索所有记录。

**JDBC 驱动程序** 数据库连接器随附了 Oracle JDBC（Java 数据库连接）驱动程序 V1.5。Data Crawler 随附的所有第三方 JDBC 驱动程序均位于 Data Crawler 安装目录的 `/lib/java/database` 目录中，您可以根据需要在此目录中添加、移除和修改驱动程序。您也可以使用 `crawler.conf` 文件中的 `extra_jars_dir` 设置来指定其他位置。

***DB2 JDBC 驱动程序*** 由于许可问题，Data Crawler 未随附适用于 DB2 的 JDBC 驱动程序。但是，已安装 JDBC 支持的所有 DB2 安装都包含 Data Crawler 所需的 JAR 文件，因此能够搜寻 DB2 安装。要搜寻 DB2 实例，您必须将这些文件复制到 Data Crawler 安装目录中的相应目录中，这样，数据库连接器才能使用这些文件。

要使 Data Crawler 能够搜寻 DB2 安装，请找到 DB2 安装目录中的 `db2jcc.jar` 和许可证（通常为 `db2jcc_license_cu.jar`）JAR 文件，然后将这些文件复制到 Data Crawler 安装目录中的 `lib/java` 子目录中，或者您可以使用 `crawler.conf` 文件中的 `extra_jars_dir` 设置来指定其他位置。

***MySQL JDBC 驱动程序***
如果驱动程序作为产品的一部分交付，那么 Data Crawler 可能会因为许可问题而未随附适用于 MySQL 的 JDBC 驱动程序。但是，下载包含 MySQL JDBC 驱动程序的 JAR 文件并将该 JAR 文件集成到 Data Crawler 安装中是一件非常容易的事情：

1.	使用 Web 浏览器访问 MySQL 下载站点，找到您要使用的归档格式（通常，对于 Microsoft Windows 系统，格式为 zip；对于 Linux 系统，格式为 gzipped tarball）的源文件和二进制文件下载链接。单击此链接以启动下载过程。可能需要进行注册。

2.	根据您下载的归档文件的类型和名称，使用相应的 `unzip archive-file-name` 或 `tar zxf archive-file-name` 命令来解压缩该归档文件的内容。

3.	切换该归档文件解压到的目录，然后将 JAR 文件从此目录复制到 Data Crawler 安装目录中的 `lib/java` 子目录中，或者您可以使用 `crawler.conf` 文件中的 `extra_jars_dir` 设置来指定其他位置。

下面是使用数据库连接器时需要设置的基本配置选项。要设置这些值，请打开文件 `config/connectors/database.conf`，并根据您的用例来修改以下值：

*  **protocol** - 用于搜寻的连接器协议的名称。此连接器的该值取决于要访问的数据库系统。
*  **collection** - 该属性用于解包临时文件。
*  **classname** - 连接器的 Java 类名。使用此连接器时，该值必须为 `plugin:database.plugin@database`。
*  **logging-config** - 指定用于配置日志记录选项的文件；它必须格式化为 `log4j` XML 字符串。

### 配置 CMIS 连接器
您可以使用 CMIS（内容管理互操作性服务）连接器来搜寻支持 CMIS 的 CMS（内容管理系统）存储库（如 Alfresco、Documentum 或 IBM Content Manager），然后对其包含的数据建立索引。

下面是使用 CMIS 连接器时需要设置的基本配置选项。要设置这些值，请打开文件 `config/connectors/cmis.conf`，并根据您的用例来修改以下值：

*  **protocol** - 用于搜寻的连接器协议的名称。请对此连接器使用 `cmis`。
*  **collection** - 该属性用于解包临时文件。
*  **dns** - 未使用的选项。
*  **classname** - 连接器的 Java 类名。使用此连接器时，该值必须为 `plugin:cmis-v1.1.plugin@connector`。
*  **logging-config** - 指定用于配置日志记录选项的文件；它必须格式化为 `log4j` XML 字符串。
*  **endpoint** - 与 CMIS 兼容的存储库的服务端点 URL。例如，SharePoint 的 URL 结构包括：
   *  对于 AtomPub 绑定：   
      http://<server>:<port>/_vti_bin/cmis/rest?getRepositories
   *  对于 WebService 绑定：   
      http://<server>:<port>/_vti_bin/cmissoapwsdl.aspx

*  **username** - 用于访问内容的 CMIS 存储库用户的用户名。该用户必须有权访问要搜寻和建立索引的所有目标文件夹和文档。
*  **password** - 用于访问内容的 CMIS 存储库的密码。此密码不得加密，应以纯文本格式提供。
*  **repositoryid** - 要访问其内容的 CMIS 存储库的标识。
*  **bindingtype** - 标识在连接 CMIS 存储库时要使用的绑定类型。值为 `AtomPub` 或 `WebServices`。
*  **authentication** - 标识在联系与 CMIS 兼容的存储库时要使用的认证机制类型：`基本 HTTP 认证`、`NTLM` 或 `WS-Security（用户名令牌）`。
*  **enable-acl** - 启用用于检索已搜寻数据 ACL 的功能。如果您不担心此集合中文档的安全性，那么禁用此选项可以提高性能，因为将不会向文档请求这些信息，也不会对这些信息进行检索和编码。值为 `true` 或 `false`。
*  **user-agent** - 搜寻文档时发送到服务器的头。
*  **method** - 用于传递参数的方法（`GET` 或 `POST`。
*  **url-logging** - 已搜寻 URL 的日志记录范围。可能的值包括：

   *  ***full-logging*** - 记录有关 URL 的所有信息。
   *  ***refined-logging*** - 只记录浏览搜寻器日志所需的信息以及使连接器正常运作所需的信息；这是缺省值。
   *  ***minimal-logging*** - 只记录使连接器正确运作所需的最少信息量。

   因为将要记录的数据量降至最少将会减少相关 I/O，因此将此选项设置为 minimal-logging 将减小日志大小并能略微提升性能。
*  **ssl-version** - 指定要用于 HTTPS 连接的 SSL 版本。缺省情况下，会使用安全性最高的协议。

### 配置 SMB/CIFS/Samba 连接器
您可以使用 Samba 连接器来搜寻服务器消息块 (SMB) 和公共因特网文件系统 (CIFS) 文件共享。这种类型的文件共享在 Windows 网络上十分普遍，也可通过开放式源代码项目 [Samba](https://www.samba.org/) 来提供。

下面是使用 Samba 连接器时需要设置的基本配置选项。要设置这些值，请打开文件 `config/connectors/samba.conf`，并根据您的用例来修改以下值：

*  **protocol** - 用于搜寻的连接器协议的名称。使用此连接器时，此值为 `smb`。
*  **collection** - 该属性用于解包临时文件。
*  **classname** - 连接器的 Java 类名。使用此连接器时，该值必须为 `plugin:smb.plugin@connector`。
*  **logging-config** - 指定用于配置日志记录选项的文件；它必须格式化为 `log4j` XML 字符串。
*  **username** - 用于进行认证的 Samba 用户名。如果已提供此选项，那么还必须提供域和密码。如果未提供此选项，那么将使用访客帐户。
*  **password** - 用于进行认证的 Samba 密码。如果提供了用户名，那么此选项为必填。必须使用 Data Crawler 随附的 VCrypt 库来加密密码。
*  **archive** - 可使 Samba 连接器搜寻归档文件中压缩的文件并对其建立索引。值为 `true` 或 `false`；缺省值为 `false`。
*  **max-policies-per-handle** - 指定可以为单个 RPC 句柄打开的本地安全授权 (LSA) 策略的最大数量。这些策略定义在各种情况下查询或修改特定系统所需的访问许可权。此选项的缺省值为 `255`。
*  **crawl-fs-metadata** - 开启此选项会使 Data Crawler 添加 VXML 文档，此文档中包含有关此文件的可用文件系统元数据（创建日期、上次修改日期、文件属性等）。
*  **enable-arc-connector** - 未使用的选项。
*  **disable-indexes** - 要禁用的索引的换行符分隔列表，此选项可能会加快搜寻，例如：

   *  disable-url-index
   *  disable-error-state-index
   *  disable-crawl-time-index
*  **exact-duplicates-hash-size** - 设置用于解析完全重复项的散列表的大小。修改此数字时请格外小心。您选择的值必须适宜；此值越大，查找速度越快但需要更多内存，反之，此值越小，搜寻速度越慢但会显著降低内存使用率。
*  **user-agent** - 未使用的选项。
*  **timeout** - 未使用的选项。
*  **n-concurrent-requests** - 并行发送到单个 IP 地址的请求数。缺省值为 `1`。

*  **enqueue-persistence** - 未使用的选项。

### 配置 SharePoint 连接器
您可以使用 SharePoint 连接器来搜寻 SharePoint Server 和 SharePoint Online 对象并对其包含的信息建立索引。可以使用与对象关联的元数据，对文档、用户概要文件、站点集合、博客、列表项、成员列表、目录页面等对象建立索引。对于列表项和文档，索引可以包含附件。

**注**：SharePoint 连接器支持所有 SharePoint 对象上的 `noindex` 属性，无论其具体类型（博客、文档、用户概要文件等）如何。将针对每个结果返回一个文档。

**要点**：用于搜寻 SharePoint 站点的 SharePoint 帐户必须至少拥有完全读访问权限。

下面是使用 SharePoint 连接器时需要设置的基本配置选项。要设置这些值，请打开文件 `config/connectors/sharepoint.conf`，并根据您的用例来修改以下值：

*  **protocol** - 用于搜寻的连接器协议的名称。请对此连接器使用 `io-sp`。
*  **collection** - 该属性用于解包临时文件。
*  **classname** - 连接器的 Java 类名。使用此连接器时，该值必须为 `plugin:io-sharepoint.plugin@connector`。
*  **logging-config** - 指定用于配置日志记录选项的文件；它必须格式化为 `log4j` XML 字符串。
*  **seed-url-type** - 标识所提供的种子 URL 所指向的 SharePoint 对象类型：站点集合或 Web 应用程序（也称为虚拟服务器）。

   *  ***站点集合*** - 如果种子 URL 类型设置为`站点集合`，那么只会搜寻该 URL 引用的站点集合的子代。
   *  ***Web 应用程序*** - 如果种子 URL 类型设置为 `Web 应用程序`，那么将搜寻属于各个 URL 所引用的 Web 应用程序的所有站点集合（及其子代）。
*  **auth-type** - 在联系 SharePoint 服务器时要使用的认证机制：`BASIC`、`NTLM2`、`KERBEROS` 或 `CBA`。缺省认证类型为 `NTLM2`。
*  **spUser** - 用于访问内容的 SharePoint 用户的用户名。该用户必须有权访问要搜寻和建立索引的所有目标站点和列表，并且必须能够检索和解析相关许可权。输入此用户名时最好带有域名，例如：`MYDOMAIN\\Administrator`。
*  **spPassword** - 用于访问内容的 SharePoint 用户的密码。必须使用 Data Crawler 随附的 vcrypt 程序来加密密码。
*  **cba-sts** - 尝试认证搜寻用户的安全性令牌服务 (STS) 端点的 URL。对于预置 ADFS 的 SharePoint，此值应该是 ADFS 端点。如果认证类型设置为 `CBA`（基于声明的认证），那么此字段为必填字段。
*  **cba-realm** - 从 STS 请求安全性令牌时要使用的中继方信任标识。有时称为“AppliesTo”值或“域”。对于 SharePoint Online，此值应该是 SharePoint Online 实例根目录的 URL（例如，`https://mycompany.sharepoint.com`）。对于 ADF，此值是 SharePoint 和 ADF 之间的中继方信任的标识值（例如，`"urn:SHAREPOINT:adfs"`）。
*  **everyone-group** - 如果指定此选项，那么当为所有人提供访问权时，ACL 中将使用该组名。如果启用了搜寻用户概要文件，那么此字段为必填字段。**注** - Retrieve and Rank 服务尚未考虑安全性。
*  **user-profile-master-url** - 连接器用于构建用户概要文件链接的基本 URL。此 URL 应配置为指向用户概要文件的显示表单。如果发现令牌 `%FIRST_SEED%`，该令牌将替换为第一个种子 URL。启用了搜寻用户概要文件的功能时，这为必填项。
*  **urls** - 要搜寻的 SharePoint Web 应用程序或站点集合的 HTTP URL 的换行符分隔列表。
*  **ehcache-config** - 未使用的选项。
*  **method** - 用于传递参数的方法（`GET` 或 `POST`。
*  **cache-types** - 未使用的选项。
*  **cache-size** - 未使用的选项。
*  **enable-acl** - 启用用于搜寻 SharePoint 用户概要文件的功能；值为 `true` 或 `false`。缺省值为 `false`。

### 配置 Box 连接器
您可以使用 Box 连接器来搜寻 Enterprise Box 实例，并对其包含的信息建立索引。下面是使用 Box 连接器时需要设置的基本配置选项。要设置这些值，请打开文件 `config/connectors/box.conf`，并根据您的用例来修改以下值：

*  **protocol** - 用于搜寻的连接器协议的名称。请对此连接器使用 `box`。
*  **classname** - 连接器的 Java 类名。使用此连接器时，该值必须为 `plugin:box.plugin@connector`。
*  **logging-config** - 指定用于配置日志记录选项的文件；它必须格式化为 `log4j` XML 字符串。
*  **box-crawl-seed-url** - Box 的基本 URL。对于此连接器，此值为 `box://app.box.com/`。您可以搜寻不同类型的 URL，例如：

   *  ***搜寻整个企业***：`box://app.box.com/`
   *  ***搜寻特定文件夹***：`box://app.box.com/user/USER_ID/folder/FOLDER_ID/FolderName`
   *  ***搜寻特定用户***：`box://app.box.com/user/USER_ID/`
*  **client-id** - 输入创建 Box 应用程序时由 Box 提供的客户端标识。
*  **client-secret** - 输入创建 Box 应用程序时由 Box 提供的客户端密钥。
*  **path-to-private-key** - 这是本地文件系统上专用密钥的位置，该专用密钥是为与 Box 通信而生成的专用-公用密钥对的一部分。
*  **kid** - 指定公用密钥标识。这是为与 Box 通信而生成的专用-公用密钥对的另一部分。
*  **enterprise-id** - 为您的应用程序授权的企业。企业标识会在 Box 管理员控制台的主页中列出。
*  **enable-acl** - 仅供内部使用。启用用于检索已搜寻数据 ACL 的功能。
*  **user-agent** - 搜寻文档时发送到服务器的头。
*  **method** - 用于传递参数的方法（`GET` 或 `POST`。
*  **url-logging** - 已搜寻 URL 的日志记录范围。可能的值包括：

   *  ***full-logging*** - 记录有关 URL 的所有信息。
   *  ***refined-logging*** - 只记录浏览搜寻器日志所需的信息以及使连接器正常运作所需的信息；这是缺省值。
   *  ***minimal-logging*** - 只记录使连接器正确运作所需的最少信息量。

   因为将要记录的数据量降至最少将会减少相关 I/O，因此将此选项设置为 minimal-logging 将减小日志大小并能略微提升性能。
*  **ssl-version** - 指定要用于 HTTPS 连接的 SSL 版本。缺省情况下，会使用安全性最高的协议。

Box 连接器确实存在一些限制：

* 不检索关于文件的注释或任务。
* 注释内容正文将作为 JSON 进行检索。可能需要另外转换注释数据。
* 不能通过 TestIt 检索单个文档。只能通过 TestIt 检索种子 URL、文件夹 URL 和用户 URL。


## 另请参阅

crawler(1)

vcrypt(1)

crawler.conf(5)

crawler-seed.conf(5)

orchestration_service.conf(5)
