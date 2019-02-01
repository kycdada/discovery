vcrypt (1) - 用來加密和解密少量資料的工具
===============================================================

## 用法概要

用法：vcrypt --decrypt|-d  --encrypt|-e  --genkey|-g [ OPTIONS ]

## 說明

`vcrypt` 主要用來加密「連接器架構」使用的密碼。

### 有關金鑰長度的特殊附註

依預設，Java 虛擬機器 (JVM) 實作必須支援 128 位元/16 個位元組的 AES 金鑰。如果系統已安裝「Java 加密延伸」，也許能使用 256 位元/32 個位元組的 AES 金鑰。如果提供了 32 個位元組的金鑰，但用來啟動 `vcrypt` 的 JVM 並不支援，將會顯示錯誤。

## 指令

### --encrypt | -e OPTIONS INPUT
在檔案中或以標準輸入提供加密資料。

### --decrypt | -d OPTIONS INPUT
在檔案中或以標準輸入提供解密資料。

### --genkey | -g
產生適用於與 `vcrypt` 搭配使用的加密金鑰至標準輸出。

## 選項

### --keyfile|-k PATH/TO/ID_VCRYPT
指定包含適當 Base64 編碼金鑰的檔案路徑，最可能是使用 `--genkey|-g` 指令來產生。

## 輸入

### 加密模式

    $FILE_CONTAINING_CLEARTEXT | -- $CLEARTEXT

### 解密模式

    $FILE_CONTAINING_CRYPTED_TEXT | -- $CRYPTED_TEXT

## 範例

產生金鑰並將它放入 `id_vcrypt` 檔案：

    vcrypt --genkey > id_vcrypt

將在此寫入的密碼從標準輸入加密至標準輸出，並透過輸出重新導向至 `my_secret_data.txt`：

    ./vcrypt --encrypt --keyfile id_vcrypt -- "my secret password" > my_secret_data.txt

您也可以將輸出以管線傳送至 `xclip`、`pbcopy` 或是類似項目，以將輸出放在您的作業系統剪貼簿上。

從檔案解密密碼：

    vcrypt --decrypt --keyfile id_vcrypt my_secret_data.txt

## 內容及環境變數

### `VCRYPT_OPTS` 環境變數
此環境變數可以用來傳遞選項至用來開始 `vcrypt` 的 `java` 指令。

### `vcrypt.key` 內容
在 `VCRYPT_OPTS` 中以 16 或 32 位元組字串將此傳遞為 `-D` 內容，以在指令行使用金鑰，而非傳遞 `--keyfile | -k keyfile` 選項。

用法範例：

    VCRYPT_OPTIONS="-Dvcrypt.key='1234qwerasdfzxcv'" vcrypt --encrypt file_to_encrypt

### `VIV_VCRYPT_KEY` 環境變數
`vcrypt` 允許使用此環境變數來設定金鑰。它必須是 16 或 32 個位元組。

## 另請參閱

crawler(1)

crawler.conf(5)

crawler-options.conf(5)

crawler-seed.conf(5)

orchestration_service.conf(5)
