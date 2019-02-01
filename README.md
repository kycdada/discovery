# Discovery 操作ツール
Discoveryでよく行う操作を簡易的に行うためのツールです。

# 前提
Python3を前提としています。  
動作確認はmacOS 10.13.3, Python 3.6.0で行っています。

# 必要ライブラリ
watson_developer_cloudとdotenvです。  
どちらもpip installコマンドで導入します。  
次のコマンドでまとめて導入することも可能です。  

```sh:
$ pip install -r requirements.txt 
```

# パラメータの設定
認証情報や、各種IDは.envから読み込む前提です。  
以下のコマンドで、.envファイルを作った後、環境に応じて各IDを設定して下さい。

```sh:
$ cp .env.example .env
```

(参考)設定ファイルの内容  

```
DISCOVERY_URL=https://gateway.watsonplatform.net/discovery/api"
DISCOVERY_USERNAME='xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'
DISCOVERY_PASSWORD='xxxxxxxxxxxx'
ENVIRONMENT_ID='xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'
CONFIGURATION_ID='xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'
COLLECTION_ID='xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'
```

# 各シェルの説明

## delete-all.py
(引数なし)
対象コレクションの文書をすべて削除します。

## import-docs.py
(引数1つ)
引数をディレクトリ名と解釈し、該当ディレクトリ配下のPDFファイルをすべて検索して、Discveryにアップロードします。

## extract-text.py
(引数1つ)
対象コレクションの文書をすべて検索し、textフィールドの内容をファイルに書き込みます。  
ファイル名は、``<Discovery上の文書ID>.txt``となります。  
引数をディレクトリ名と解釈し、ファイルの保存先は引数で指定したディレクトリとなります。




