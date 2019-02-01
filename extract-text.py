#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Discoveryの全文書のtextを指定ディレクトリにexportする
#

import sys
import codecs

import common
discovery = common.discovery
environment_id = common.environment_id
collection_id = common.collection_id

argvs = sys.argv
path = argvs[1]

# 文書件数取得
collection = discovery.get_collection(environment_id, collection_id)
doc_count = collection.result['document_counts']['available']

results = discovery.query(
        environment_id, 
        collection_id, 
        count=doc_count,
        return_fields='id,text').result["results"]

for result in results:
    id = result['id']
    text = result['text']
    outfn = path + '/' + id + '.txt'
    print(outfn)
    outfile = codecs.open(outfn, 'w', 'utf-8')
    outfile.write(text)
    outfile.close()
