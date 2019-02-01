#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# import-docs.py
# 
# パラメータで指定した対応可能ファイルをDiscoveryに上書きします 
# 第一引数がパス、第二引数が、documnent_id

import os
import sys
import json
from os.path import join, dirname
from watson_developer_cloud.watson_service import WatsonApiException
import common

discovery = common.discovery
environment_id = common.environment_id
collection_id = common.collection_id

# コマンドプロント引数
argvs = sys.argv
path = argvs[1]
document_id = argvs[2]

# 対応可能ファイル PDF,WORD(doc,docx),HTMl(.htm,html),XHTML(.xhtml),JSON(.json)
accept_extension = {".pdf":"application/pdf",".doc":"application/msword",".docx":"application/vnd.openxmlformats-officedocument.wordprocessingml.document",
".html":"text/html",".htm":"text/html",".xhtml":"application/xhtml+xml",".json":"application/json"}

# 拡張子取得
extension = os.path.splitext(path)[1]
print(extension)

#mimetype設定
for key in accept_extension:
    if(extension == key):
        this_mimetype = accept_extension[extension]
        print(this_mimetype)

# ドキュメント上書き
with open(argvs[1],"rb") as fileinfo:
    try:
        update_doc = discovery.update_document(environment_id.encode("utf-8"),collection_id.encode("utf-8"),document_id,file=fileinfo,file_content_type=this_mimetype.encode("utf-8")).get_result()
        print(json.dumps(update_doc, indent=2))
    except WatsonApiException as e:
        print(e)
        try:
            update_doc = discovery.update_document(environment_id.encode("utf-8"),collection_id.encode("utf-8"),document_id,file=fileinfo).get_result()
            print(json.dumps(update_doc,indent=2))
        except WatsonApiException as e:
            print(e)
            print("watsonに送れませんでした")



