#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# delete-all.py
#
# documentidをすべて拾って削除メソッドを叩く
# 対象コレクションのドキュメントを全部削除します。
# エラーが出ても、とりあえず最後まで動きます.

from watson_developer_cloud.watson_service import WatsonApiException
import common
discovery = common.discovery
environment_id = common.environment_id
collection_id = common.collection_id

# 文書件数取得
collection = discovery.get_collection(environment_id, collection_id)
doc_count = collection.result['document_counts']['available']

# id一覧取得
print (discovery.query(environment_id, collection_id, return_fields='id', count=doc_count))
results = discovery.query(environment_id, collection_id, return_fields='id', count=doc_count).result["results"]
ids = [item["id"] for item in results]

for id in ids:
    print('deleting doc: id =' + id)
    try:
        discovery.delete_document(environment_id, collection_id, id)
    except WatsonApiException as e:
        print(e)

