# -*- coding: utf-8 -*-
#
# id����document���폜
# �R�}���h�v�����g�ő������Ƃ��āAid�����

import common
import sys

args = sys.argv
id = args[1]

discovery = common.discovery
environment_id = common.environment_id
collection_id = common.collection_id

discovery.delete_document(environment_id,collection_id, id)
print(delete + " " + id)
