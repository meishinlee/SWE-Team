"""
This file contains some common MongoDB code.
"""
import os
import json
import pymongo as pm
from pymongo.server_api import ServerApi
import bson.json_util as bsutil

# from mongo_test import DB_NAME

# all of these will eventually be put in the env:
user_nm = "meishinlee"
cloud_db = "email-filter.6vns1.mongodb.net"
cloud_db_url = "email-filter.6vns1.mongodb.net"
# cloud_db = "cluster0.lh6bk.mongodb.net"
# cloud_db = "serverlessinstance0.irvgp.mongodb.net"
passwd = os.environ.get("MONGO_PASSWD", 'emailfilter')
cloud_mdb = "mongodb+srv"
db_params = "retryWrites=true&w=majority"
db_nm = "emailfilterDB"

# client = pm.MongoClient("mongodb+srv://meishinlee:<password>@email-filter.6vns1.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

# client = pm.MongoClient(f"mongodb+srv://meishinlee:emailfilter"
#                                 + f"@email-filter.6vns1.mongodb.net/{db_nm}"
#                                 + f"?{db_params}", connect=False)
# print("hi")
# print(client)
# db = client.test

client = None

def get_client():
    """
    This provides a uniform way to get the client across all uses.
    Returns a mongo client object... maybe we shouldn't?
    Also set global client variable.
    """
    global client
    if os.environ.get("LOCAL_MONGO", False):
        client = pm.MongoClient()
        print("Local test")
    else:
        # client = pm.MongoClient(f"mongodb+srv://{user_nm}:{passwd}.@{cloud_db}"
        #                         + f"/{db_nm}?{db_params}")
        #                         server_api=pm.ServerApi('1'))
        client = pm.MongoClient(f"mongodb+srv://{user_nm}:{passwd}"
                                + f"@{cloud_db_url}/myFirstDatabase"
                                + f"?{db_params}", connect=False)
    return client

def fetch_one(collect_nm, filters = {}):
    '''
    Fetch one record that meets filter.
    '''
    return client[db_nm][collect_nm].find_one(filters)

def del_one (collect_nm, filters = {}):
    '''
    Fetch one record that meets filter.
    '''
    return client[db_nm][collect_nm].delete_one(filters)

def fetch_many(collect_nm, key_nm, filters = {}):
    many_docs = {}
    for doc in client[db_nm][collect_nm].find(filters):
        print(doc)
        many_docs[doc[key_nm]] = json.loads(bsutil.dumps(doc))
    return many_docs
    
def fetch_all(collect_nm, key_nm):
    # all_users = {}
    # users = client[db_nm]["users"].find()
    # for user in users:
    #     id = str(user["_id"])
    #     user_name = user["Name"]
    #     user_email = user["Email"]
    #     all_users[id] = (user_name, user_email)
    # return all_users

    all_docs = {}
    for doc in client[db_nm][collect_nm].find():
        print(doc)
        all_docs[doc[key_nm]] = json.loads(bsutil.dumps(doc))
    return all_docs

def create_user(name, email):
    """
    Adds a new user to the database
    """
    try:
        new_user = client[db_nm]['users'].insert_one({"Name": name, "Email": email})
        return new_user["_id"]
    except pm.errors.DuplicateKeyError:
        return None

def insert_doc(collect_nm, doc):
    client[db_nm][collect_nm].insert_one(doc)

