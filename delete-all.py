#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# delete-all.py
#
# 対象コレクションのドキュメントを全部削除します。
#

import common
discovery = common.discovery
environment_id = common.environment_id
collection_id = common.collection_id

# 文書件数取得
collection = discovery.get_collection(environment_id, collection_id)
doc_count = collection.result['document_counts']['available']

print (discovery.query(environment_id, collection_id, return_fields='id', count=doc_count))
results = discovery.query(environment_id, collection_id, return_fields='id', count=doc_count).result["results"]
ids = [item["id"] for item in results]

for id in ids:
    print('deleting doc: id =' + id)
    discovery.delete_document(environment_id, collection_id, id)
