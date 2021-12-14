"""
This program is written to port text JSON files into Mongo collections.
It assumes the JSON files have the structure:
    {
        "some_fld1": { some more fields },
        "some_fld2": { some more fields },
        .
        .
        .
        "some_fldN": { some more fields },
    }
It assumes that cause that's what we've been using!
"""
import sys
import json
import pymongo as pm 

# DB_NAME = "testDB"
# COLLECT_NAME = "some_collect"

DB_NAME = 'emailfilterDB'
COLLECT_NAME = 'users'

client = pm.MongoClient()
print(f"{client=}")
# returns something like client=MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True)

# You can use this so you avoid typing client[DB_NAME][COLLECT_NAME] over and over again.
this_collect = client[DB_NAME][COLLECT_NAME]

#insert_ret = client['testDB']['some_collect'].insert_one({'fid':'value'})
insert_ret = client[DB_NAME][COLLECT_NAME].insert_one({'test5': {'Email': 'maple@nyu.edu'}})
print(f"{insert_ret=}")
# insert_ret=<pymongo.results.InsertOneResult object at 0x7fc730fb3540>

# docs = client['testDB']['some_collect'].find()
docs = client[DB_NAME][COLLECT_NAME].find()
print(f"{docs=}")
for doc in docs:
    print(f"{doc=}")
'''
docs=<pymongo.cursor.Cursor object at 0x7fc730fb53a0>
doc={'_id': ObjectId('61b8ca16bbb11f07d99dc28d'), 'fid': 'value'}
doc={'_id': ObjectId('61b8cae3054db13b48f4c840'), 'test1': {'Email': 'msl608@nyu.edu'}}
'''

doc = client[DB_NAME][COLLECT_NAME].find_one({'test2': {'Email': 'ac7378@nyu.edu'}})
print(f"find one = {doc=}")

doc = client[DB_NAME][COLLECT_NAME].delete_one({'test3': {'Email': 'devin@nyu.edu'}})
print(f"delete one = {doc=}")

docs = client[DB_NAME][COLLECT_NAME].find()
print(f"{docs=}")
for doc in docs:
    print(f"{doc=}")
