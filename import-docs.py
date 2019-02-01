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
import uuid
import shutil
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


# フォルダ内ファイル取得
def find_all_files(directory):
    for root, dirs, files in os.walk(directory):
        yield root
        for file in files:
            yield os.path.join(root, file)
            
# uuidと、フルパス、docment_idの一覧保存用csvファイルから読み込み、最後尾から5行表示
df = pd.read_csv("./id_list.csv",sep=",")
df.tail()


# 拡張子ごとに、周回対象に追加
files = find_all_files(path)
files_ext = [os.path.splitext(file) for file in files]
target_files = [file+ext for file, ext in files_ext if ext in ['.pdf']]
target_doc= [file + ext for file, ext in files_ext if ext in[".doc"]]
target_docx = [file + ext for file, ext in files_ext if ext in[".docx"]]
target_json = [file + ext for file, ext in files_ext if ext in[".json"]]

for doc in target_doc:
    target_files.append(doc)
for docx in target_docx:
    target_files.append(docx)
for json in target_json:
    target_files.append(json)
    

# ワトソンに入れる
for target_file in target_files:
    print("adding ducument " + target_file)
    file_name = os.path.basename(target_file)
    file_extension = os.path.splitext(target_file)[1]
    print(file_extension)
    
    # ファイルパスをから、一致するdocument_idを取得 TODO 各種データ(csvのカラム等)が空の場合の処理
    update_document_id = ""
    for index, row in df.iterrows():
        print(row.full_path)
        if(target_file == row.full_path):
            update_document_id = row.document_id
            if(update_document_id):
                print(target_file + "update_target")
    
    
    # ファイル名代わりのuuid生成、100ループで強制的に抜ける
    pd_loop = 100
    while True:
        if(update_document_id):
            break
        pd_loop-=1
        break_flg = True
        this_uuid = uuid.uuid1()
        
        # pandasフレームを列で回す、uuidが被っていたら,やり直し
        for id in df["uuid"]:
            print(id)
            if(str(this_uuid) == str(id)):
                break_flg = False
                print("loop")
            
        if(break_flg):
            break
            print("重複なし")
        if(pd_loop <= 0):
            print("uuid重複確認ループが止まらないため、強制終了")
            sys.exit()
            
    
    # tempファイル作成
    this_temp_path = os.path.join( os.path.splitext(target_file)[0], this_uuid) + ".temp"
    shutil.copy2(target_file, this_temp_path)
    
    # ファイルの拡張子と、受け入れ可能拡張子が一致したら処理開始
    for key in accept_extension:
    
        if(file_extension == key):
            print(file_name)
            this_mimetype = accept_extension[key]
            
            # ファイル名が、おそらく文字コードの都合上、弾かれることがあるので、tempに仮の、ファイル名つけて、upload
            with open(this_temp_path,"rb") as fileinfo:
                
                # アップデートするドキュメントがあったら、アップデート
                if(update_document_id):
                    try:
                        update_doc = discovery.update_document(environment_id.encode("utf-8"), collection_id.encode("utf-8"), update_document_id.encode("utf-8"), file = fileinfo, file_content_type = this_mimetype.encode("utf-8")).get_result()
                        print(json.dumps(add_doc, indent = 2))
                        print("update with mimetype")
                        break
                    except WatsonApiException as e:
                        print(e)
                        try:
                            update_doc = discovery.update_document(environment_id.encode("utf-8"),collection_id.encode("utf-8"),update_document_id.encode("utf-8"),file = fileinfo).get_result()
                            print(json.dumps(add_doc, indent = 2))
                            print("update")
                            break
                        except WatsonApiException as e:
                            print(e)
                            print("watsonに送れませんでした。")
                            break
                
                # mimetypeで固定しなければ、エラーのファイルと、固定したらエラーが出るファイルが双方存在するため、exceptionで分岐
                # それでもだめなら、諦めて正規品で手動ファイル変換お願いします
                try:
                    
                    # ディスカバリーにfile追加、(拡張子ごとにmime設定) TODO 既に追加されているものの判別(updatemethodを走らせる)
                    
                    add_file = discovery.add_document(environment_id.encode("utf-8"), collection_id.encode("utf-8"), file=fileinfo,
                    file_content_type = this_mimetype).get_result()
                    print(add_file)
                    document_id = add_file["document_id"]
                    # 追加用データフレーム
                    add_df = pd.DataFrame([[target_file, document_id, this_uuid]],columns=["full_path","document_id","uuid"])
                    
                    # データフレームにデータ追加 元のindex番号は無視
                    df = df.append(add_df,ignore_index=True)
                    
                    
                    
                except WatsonApiException as e:
                    print(e)
                    try :
                        add_file = discovery.add_document(environment_id.encode("utf-8"), collection_id.encode("utf-8"), file=fileinfo).get_result()
                        print(add_file)
                        document_id =  add_file["document_id"]
                        
                    except WatsonApiException as e:
                        print("watsonに送れませんでした。")
                        print(e)
    

