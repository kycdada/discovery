#!/user/bin/python3
# -*- coding: utf-8 -*-
#
# import-docs.py
# 
# パラメータで指定したディレクトリ配下の対応可能ファイルをすべてDiscoveryに取り込みます 
#

import os
import sys
import json
import pandas as pd
import re
import urllib.parse
from os.path import join, dirname
from watson_developer_cloud.watson_service import WatsonApiException

import common
discovery = common.discovery
environment_id = common.environment_id
collection_id = common.collection_id

argvs = sys.argv
path = argvs[1]
os_name = os.name


# 対応可能ファイル PDF,WORD(doc,docx),HTMl(.htm,html),XHTML(.xhtml),JSON(.json)
accept_extension = {".pdf":"application/pdf",".doc":"application/msword",".docx":"application/vnd.openxmlformats-officedocument.wordprocessingml.document",
".html":"text/html",".htm":"text/html",".xhtml":"application/xhtml+xml",".json":"application/json"}

# windowsでの一時ファイルを読み込まないようにするため(Linuxは未確認)
pattern = r"~$"
repatter = re.compile(pattern)


# フォルダ内ファイル取得
def find_all_files(directory):
    for root, dirs, files in os.walk(directory):
        yield root
        for file in files:
            yield os.path.join(root, file)
            

# 拡張子ごとに、周回対象に追加
target_files=[]
files = find_all_files(path)
files_ext = [os.path.splitext(file) for file in files]
target_pdf = [file+ext for file, ext in files_ext if ext in ['.pdf']]
target_doc= [file + ext for file, ext in files_ext if ext in[".doc"]]
target_docx = [file + ext for file, ext in files_ext if ext in[".docx"]]
target_json = [file + ext for file, ext in files_ext if ext in[".json"]]

# windowsでの一時ファイルを取り込まないようにするため~$が先頭につくファイルを排除(Linuxは未確認)

#  matchで行おうとしたら、何故か反応してくれなかったので、ファイル名の先頭2文字カットして、比較
#pattern = r"~$"
#repatter = re.compile(pattern)

# 比較用文字
pattern = "~$"

# 拡張子ごとの分割を一つにまとめる
for pdf in target_pdf:
    slice_name = os.path.basename(pdf)[0:2]
    if not slice_name == pattern:
        target_files.append(pdf)
        
for doc in target_doc:
    slice_name = os.path.basename(doc)[0:2]
    if not slice_name == pattern:
        target_files.append(doc)
        
for docx in target_docx:
    slice_name = os.path.basename(docx)[0:2]
    if not slice_name == pattern:
        target_files.append(docx)
        
for json in target_json:
    slice_name = os.path.basename(json)[0:2]
    if not slice_name == pattern:
        target_files.append(json)
    

# ワトソンに入れる
for target_file in target_files:
    print("adding ducument " + target_file)
    
    # ファイル名が、日本語だと弾かれるので、URLエンコーディング
    file_name = os.path.basename(target_file)
    encoded_name = urllib.parse.quote(file_name)
    file_extension = os.path.splitext(target_file)[1]
    print(file_extension)
    
    
    # ファイルの拡張子と、受け入れ可能拡張子が一致したら処理開始
    for key in accept_extension:
    
        if(file_extension == key):
            print(file_name)
            this_mimetype = accept_extension[key]
            
            # upload
            with open(target_file,"rb") as fileinfo:
                
#                # アップデートするドキュメントがあったら、アップデート
#                if(update_document_id):
#                    try:
#                        update_doc = discovery.update_document(environment_id.encode("utf-8"), collection_id.encode("utf-8"), update_document_id.encode("utf-8"), file = fileinfo, file_content_type = this_mimetype.encode("utf-8")).get_result()
#                        print(json.dumps(add_doc, indent = 2))
#                        print("update with mimetype")
#                        break
#                    except WatsonApiException as e:
#                        print(e)
#                        try:
#                            update_doc = discovery.update_document(environment_id.encode("utf-8"),collection_id.encode("utf-8"),update_document_id.encode("utf-8"),file = fileinfo).get_result()
#                            print(json.dumps(add_doc, indent = 2))
#                            print("update")
#                            break
#                        except WatsonApiException as e:
#                            print(e)
#                            print("watsonに送れませんでした。")
#                            break
                
                # mimetypeで固定しなければ、エラーのファイルと、固定したらエラーが出るファイルが双方存在するため、exceptionで分岐
                # それでもだめなら、諦めて正規品で手動ファイル変換お願いします
                try:
                    
                    # ディスカバリーにfile追加、(拡張子ごとにmime設定) TODO 既に追加されているものの判別(updatemethodを走らせる)
                    
                    add_file = discovery.add_document(environment_id.encode("utf-8"), collection_id.encode("utf-8"), file=fileinfo,
                    file_content_type = this_mimetype,filename=encoded_name).get_result()
                    print(add_file)
                    
                    
                    
                except WatsonApiException as e:
                    print(e)
                    try :
                        add_file = discovery.add_document(environment_id.encode("utf-8"), collection_id.encode("utf-8"), file=fileinfo,
                        filename=encoded_name).get_result()
                        print(add_file)
                        document_id =  add_file["document_id"]
                        
                    except WatsonApiException as e:
                        print("watsonに送れませんでした。")
                        print(e)
    

