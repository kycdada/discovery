# 配置搜寻种子

种子是搜寻的起点，Data Crawler 使用种子从该种子所识别的资源中检索数据。通常，种子会配置 URL 来访问基于协议的资源，例如，文件共享、SMB 共享、数据库和其他可通过各种 Web 协议访问的数据存储库。此外，不同的种子 URL 具有不同的功能。

种子也可以特定于存储库，可用于搜寻特定的第三方应用程序（例如，客户关系管理 (CRM) 系统、产品生命周期 (PLC) 系统、内容管理系统 (CMS)、基于云的应用程序以及 Web 数据库应用程序）。

Data Crawler 目前提供了支持以下存储库类型文件连接器的搜寻种子：

*	文件系统
*	使用 JDBC 的数据库
*	CMIS（内容管理互操作性服务）
*	SMB（服务器消息块）、CIFS（公共因特网文件系统）或 Samba 文件共享
*	SharePoint 和 SharePoint Online
*	Box

此外还提供了一个搜寻种子配置模板，您可以使用该模板为定制连接器来定制搜寻种子。

## 入门：

在搜寻数据存储库时，搜寻器从用户指定的种子 URL 开始，并开始下载信息页面。另外，搜寻器还会查找已下载页面中的链接，并安排进一步搜寻新发现的页面。

系统将使用配置信息来确定要搜寻的页面及其搜寻方式。此文件解释了每个连接器的搜寻种子文件的可配置选项。

**注**：每个搜寻种子配置文件与对应的文件连接器配置文件配合工作；在其他位置会单独描述文件连接器选项。

### 配置文件系统搜寻种子

可配置文件系统搜寻种子文件的以下值。要设置这些值，请打开文件 `config/seeds/filesystemseed.conf`，并根据您的用例来指定以下值：

*  **url** - 要搜寻的文件和文件夹的换行符分隔列表。UNIX 用户可以使用诸如 `/usr/local/` 的路径。URL 必须以 `sdkfs：//` 开头。例如，要搜寻 `/home/watson/mydocs`，此 URL 的值将为 `sdkfs：///home/watson/mydocs` - 第三个 `/` 是必需的！**注**：文件系统连接器使用定制协议 `sdkfs：//` 来创建有效 URL。请勿在所列路径前面添加 `file://`；URL 必须以 `sdkfs：//` 开头。
*  **hops** - 仅供内部使用。
*  **default-allow** - 仅供内部使用。

### 配置数据库搜寻种子

可配置数据库搜寻种子文件的以下值。要设置这些值，请打开文件 `config/seeds/database-seed.conf`，并根据您的用例来指定以下值：

*  **url** - 要检索的表或视图的 URL。定义定制的 SQL 数据库种子 URL。结构为：

   	`database-system://host:port/database?[per=num]&[sql=SQL]`

   测试种子 URL 将显示所有排队的 URL。例如，测试包含 200 条记录的数据库的以下 URL：

   	`sqlserver://test.mycompany.com:1433/WWII_Navy/?per=100&sql=select%20*%20from%20vessel&`

   将显示以下排队的 URL：

   	`sqlserver://test.mycompany.com:1433/WWII_Navy/?key-val=0&`

   	`sqlserver://test.mycompany.com:1433/WWII_Navy/?key-val=100&`

   	`sqlserver://test.mycompany.com:1433/WWII_Navy/?key-val=200&`

   测试以下 URL 将显示从第 43 行检索的数据：

   	`sqlserver://test.mycompany.com:1433/WWII_Navy/?per=1&key-val=43`
*  **hops** - 仅供内部使用。
*  **default-allow** - 仅供内部使用。
*  **user-password** - 用于数据库系统的凭证。需要使用 `:` 分隔用户名和密码，并且必须使用 Data Crawler 随附的 vcrypt 程序来加密密码。例如 `username:[[vcrypt/3]]passwordstring`。
*  **max-data-size** - 单个文档的最大数据量。这是一次可装入的最大内存块。仅当您的计算机上有足够的内存时，才可增加此限制。
*  **filter-exact-duplicates** - 仅供内部使用。
*  **jdbc-class**（Extender 选项）- 如果指定了此选项，该字符串将覆盖当选择`（其他）`作为数据库系统时连接器使用的 JDBC 类。
*  **connection-string**（Extender 选项）- 如果指定了此选项，此字符串将覆盖自动生成的 JDBC 连接字符串。这样，您便可以提供关于数据库连接的更详细的配置，例如，负载均衡或 SSL 连接。例如：`jdbc:netezza://127.0.0.1:5480/databasename`。
*  **save-frequency-for-resume**（Extender 选项）- 指定列或关联标签的名称，以便能够恢复搜寻或执行部分刷新。种子在搜寻过程中会定期保存该列的名称，并在搜寻完数据库最后一行后再次保存该名称。在恢复搜寻或进行刷新时，搜寻将从此字段保存的值所标识的那一行开始。

### 配置 CMIS 搜寻种子

可配置 CMIS 搜寻种子文件的以下值。要设置这些值，请打开文件 `config/seeds/cmisseed.conf`，并根据您的用例来修改以下值：

*  **url** - CMIS 存储库中用作搜寻起点的文件夹的 URL，例如：

   *  `cmis://alfresco.test.com:8080/alfresco/cmisatom?folderToProcess=workspace://SpacesStore/guid`
   要从根文件夹进行搜寻，您需要提供以下 URL：

   *  `cmis://alfresco.test.com:8080/alfresco/cmisatom?folderToProcess=`
*  **at** - 未使用的选项。
*  **default-allow** - 仅供内部使用。

### 配置 Samba 搜寻种子

可配置 Samba 搜寻种子文件的以下值。要设置这些值，请打开文件 `config/seeds/sambaseed.conf`，并根据您的用例来修改以下值：

*  **url** - 要搜寻的共享的换行符分隔列表，例如：

   *  `smb://share.test.com/office`
   *  `smb://share.test.com/cash/money/change`
   *  `smb://share.test.com/C$/Program Files`

*  **hops** - 仅供内部使用。
*  **default-allow** - 仅供内部使用。

### 配置 SharePoint 搜寻种子

可配置 SharePoint 搜寻种子文件的以下值。要设置这些值，请打开文件 `config/seeds/sharepointseed.conf`，并根据您的用例来修改以下值：

*  **url** - 要搜寻的 SharePoint Web 应用程序或站点集合的换行符分隔列表，例如：

   *  `io-sp://a.com`
   *  `io-sp://b.com:83/site`
   *  `io-sp://c.com/site2`

   同时还会搜寻这些站点的子站点（除非它们被其他搜寻规则排除在外）。
*  **filter-url** - 要搜寻的 SharePoint Web 应用程序或站点集合的换行符分隔列表，例如：

   *  `http://a.com`
   *  `http://b.com:83/site`
   *  `http://c.com/site2`

*  **hops** - 仅供内部使用。
*  **n-concurrent-requests** - 仅供内部使用。
*  **delay** - 仅供内部使用。
*  **default-allow** - 仅供内部使用。
*  **seed-protocol** - 设置站点集合子代的种子协议。如果站点集合的协议为 SSL、HTTP 或 HTTPS，这为必需项。必须将此值设置为与站点集合的协议相同。

### 配置 Box 种子

可配置 Box 搜寻种子文件的以下值。要设置这些值，请打开文件 `config/seeds/boxseed.conf`，并根据您的用例来指定以下值：

*  **url** - 要用作搜寻起点的 URL。缺省值为 `box://app.box.com/`。
*  **default-allow** - 仅供内部使用。

## 另请参阅

crawler(1)

vcrypt(1)

crawler.conf(5)

crawler-options.conf(5)

orchestration_service.conf(5)
