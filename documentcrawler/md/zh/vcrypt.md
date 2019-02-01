vcrypt(1) - 用于加密和解密少量数据的工具
===============================================================

## 摘要

用法：vcrypt --decrypt|-d  --encrypt|-e  --genkey|-g [选项]

## 描述

`vcrypt` 主要用于加密供 Connector Framework 使用的密码。

### 关于密钥长度的特别说明

缺省情况下，Java 虚拟机实施必须支持 128 位/16 字节 AES 密钥。如果系统安装了 Java Cryptographic Extension，那么它或许能够使用 256 位/32 字节 AES 密钥。如果提供了 32 字节密钥，但用于启动 `vcrypt` 的 JVM 不支持此密钥，那么将显示一条错误。

## 命令

### --encrypt | -e OPTIONS INPUT
对文件或标准输入中提供的数据进行加密。

### --decrypt | -d OPTIONS INPUT
对文件或标准输入中提供的数据进行解密。

### --genkey | -g
生成适用于 `vcrypt` 的加密密钥，并将其放到标准输出中。

## 选项

### --keyfile|-k PATH/TO/ID_VCRYPT
指定包含相应 Base64 编码密钥的文件的路径，此密钥很可能是使用 `--genkey|-g` 命令生成的。

## 输入

### 加密方式

    $FILE_CONTAINING_CLEARTEXT | -- $CLEARTEXT

### 解密方式

    $FILE_CONTAINING_CRYPTED_TEXT | -- $CRYPTED_TEXT

## 示例

生成密钥，并将其放到文件 `id_vcrypt` 中：

    vcrypt --genkey > id_vcrypt

对标准输入中的密码进行加密，并将其放到标准输出中（此处通过输出重定向到 `my_secret_data.txt` 来写入）：

    ./vcrypt --encrypt --keyfile id_vcrypt -- "my secret password" > my_secret_data.txt

您可以将输出传送到 `xclip`、`pbcopy` 或类似工具，以将输出放到操作系统剪贴板中。

对来自文件的密码进行解密：

    vcrypt --decrypt --keyfile id_vcrypt my_secret_data.txt

## 属性和环境变量

### `VCRYPT_OPTS` 环境变量
可使用此环境变量来将选项传递到用于启动 `vcrypt` 的 `java` 命令。

### `vcrypt.key` 属性
在命令行中，将此属性作为 `VCRYPT_OPTS` 中的 `-D` 属性（采用 16 或 32 字节字符串形式）传递以使用密钥，而不会传递 `--keyfile | -k keyfile` 选项。

用法示例：

    VCRYPT_OPTIONS="-Dvcrypt.key='1234qwerasdfzxcv'" vcrypt --encrypt file_to_encrypt

### `VIV_VCRYPT_KEY` 环境变量
`vcrypt` 允许使用此环境变量来设置密钥。该密钥必须为 16 或 32 字节。

## 另请参阅

crawler(1)

crawler.conf(5)

crawler-options.conf(5)

crawler-seed.conf(5)

orchestration_service.conf(5)
