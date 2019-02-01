#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# import-docs.py
# 
# パラメータで指定した対応可能ファイルをDiscoveryに取り込みます 
#

import os
import sys
import json
import urllib.parse
from os.path import join, dirname
from watson_developer_cloud.watson_service import WatsonApiException

import common
discovery = common.discovery
environment_id = common.environment_id
collection_id = common.collection_id

# 対応可能ファイル PDF,WORD(doc,docx),HTMl(.htm,html),XHTML(.xhtml),JSON(.json)
accept_extension = {".pdf":"application/pdf",".doc":"application/msword",".docx":"application/vnd.openxmlformats-officedocument.wordprocessingml.document",
".html":"text/html",".htm":"text/html",".xhtml":"application/xhtml+xml",".json":"application/json"}

# コマンドプロント引数
argvs = sys.argv
path = argvs[1]

# 拡張子取得
extension = os.path.splitext(path)[1]
print(extension)

#mimetype設定
for key in accept_extension:
    if(extension == key):
        this_mimetype = accept_extension[extension]
        print(this_mimetype)

# ドキュメント追加
with open(argvs[1],"rb") as fileinfo:
    try:
        add_doc = discovery.add_document(environment_id.encode("utf-8"),collection_id.encode("utf-8"),file=fileinfo,file_content_type=this_mimetype.encode("utf-8")).get_result()
        print(json.dumps(add_doc, indent=2))
    except WatsonApiException as e:
        print(e)
        try:
            add_doc = discovery.add_document(environment_id.encode("utf-8"),collection_id.encode("utf-8"),file=fileinfo).get_result()
            print(json.dumps(add_doc,indent=2))
        except WatsonApiException as e:
            print(e)
            print("watsonに送れませんでした")



