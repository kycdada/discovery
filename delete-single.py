# -*- coding: utf-8 -*-
#
# idからdocumentを削除
# コマンドプロントで第一引数として、idを取る

import common
import sys

args = sys.argv
id = args[1]

discovery = common.discovery
environment_id = common.environment_id
collection_id = common.collection_id

discovery.delete_document(environment_id,collection_id, id)
print(delete + " " + id)
