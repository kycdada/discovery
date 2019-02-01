#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# common.py
#
# 共通処理 
#

import json
import sys
import os
import json
from watson_developer_cloud import DiscoveryV1
#from dotenv import load_dotenv
from os.path import join, dirname

#dotenv_path = join(dirname(__file__), '.env')
#load_dotenv(dotenv_path)
#username = os.environ.get("DISCOVERY_USERNAME")
#password = os.environ.get("DISCOVERY_PASSWORD")
#environment_id = os.environ.get("ENVIRONMENT_ID")
environment_id = ""
#collection_id = os.environ.get("COLLECTION_ID")
collection_id = ""
configuration_id = ""
#
#if ( username is None ):
#    print("username is null")
#    exit(1)
#
#if ( password is None ):
#    print("password is null")
#    exit(1)
#
#discovery = DiscoveryV1(
#  username=username,
#  password=password,
#  version="2017-11-07"
#)

# credentials
discovery = DiscoveryV1(
    url="https://gateway.watsonplatform.net/discovery/api",
    iam_apikey="",
    version="2018-12-03"
)

# 環境詳細を取得
#config = discovery.get_configuration(environment_id,configuration_id).get_result()
#print(json.dumps(config,indent=4))

# 環境設定を置き換える
#with open(os.path.join(os.getcwd(),"WDSconfig.json"),"rb") as config_data:
#    data = json.load(config_data)
#    updated_config =discovery.update_configuration(environment_id,configuration_id,data["name"],data["description"],data["conversions"],
#    data["enrichments"],data["normalizations"]).get_result()
#print(json.dumps(updated_config,indent=2))

# document詳細を取得する(error情報等を取得することが可能)
document_id = "71c04a22-12ea-4846-9b7c-6dde6bc80ebe" # 好きなidを入れる
doc_info = discovery.get_document_status(environment_id,collection_id,document_id).get_result()
print(json.dumps(doc_info,indent=2))
