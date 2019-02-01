vcrypt(1) - 少量のデータを暗号化/暗号化解除するためのツール
===============================================================

## 概要

使用法: vcrypt --decrypt|-d  --encrypt|-e  --genkey|-g [ OPTIONS ]

## 説明

`vcrypt` は主に、コネクター・フレームワークで使用するパスワードを暗号化するために使用されます。

### 鍵の長さに関する特別な注記

Java 仮想マシンの実装は、デフォルトで 128 ビット/16 バイトの AES 鍵をサポートするはずです。Java Cryptographic Extension が
インストールされているシステムでは、256 ビット/32 バイトの AES 鍵を使用できる場合もあります。32 バイトの鍵を
指定した場合に、`vcrypt` の起動に使用した JVM がその鍵をサポートしていなければ、エラーが表示されます。

## コマンド

### --encrypt | -e OPTIONS INPUT
ファイル内や標準入力内のデータを暗号化します。

### --decrypt | -d OPTIONS INPUT
ファイル内や標準入力内のデータを暗号化解除します。

### --genkey | -g
`vcrypt` での使用に適した暗号鍵を生成して標準出力に送ります。

## オプション

### --keyfile|-k PATH/TO/ID_VCRYPT
該当する Base64 エンコードの鍵 (通常は `--genkey|-g` コマンドを使用して生成した鍵) が
入っているファイルのパスを指定します。

## 入力

### 暗号化モード

    $FILE_CONTAINING_CLEARTEXT | -- $CLEARTEXT

### 暗号化解除モード

    $FILE_CONTAINING_CRYPTED_TEXT | -- $CRYPTED_TEXT

## 例

鍵を生成して `id_vcrypt` ファイルに書き込みます。

    vcrypt --genkey > id_vcrypt

標準入力のパスワードを暗号化して標準出力に送り、出力リダイレクトによって
`my_secret_data.txt` に書き込みます。

    ./vcrypt --encrypt --keyfile id_vcrypt -- "my secret password" > my_secret_data.txt

パイプ接続によって `xclip` や `pbcopy` などに出力を送り、オペレーティング・システムの
クリップボードに出力を配置することもできます。

ファイル内のパスワードを暗号化解除します。

    vcrypt --decrypt --keyfile id_vcrypt my_secret_data.txt

## プロパティーと環境変数

### `VCRYPT_OPTS` 環境変数
この環境変数を使用して、`vcrypt` の開始に使用する `java` コマンドにオプションを渡すことができます。

### `vcrypt.key` プロパティー
`--keyfile | -k keyfile` オプションを渡す代わりに、コマンド・ラインで鍵として使用する 16 バイトまたは 32 バイトの
ストリングを `VCRYPT_OPTS` の `-D` プロパティーで渡します。

使用例:

    VCRYPT_OPTIONS="-Dvcrypt.key='1234qwerasdfzxcv'" vcrypt --encrypt file_to_encrypt

### `VIV_VCRYPT_KEY` 環境変数
`vcrypt` では、この環境変数を使用して鍵を設定できます。16 バイトか 32 バイトのどちらかでなければなりません。

## 関連資料

crawler(1)

crawler.conf(5)

crawler-options.conf(5)

crawler-seed.conf(5)

orchestration_service.conf(5)
