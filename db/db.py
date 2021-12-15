import os

import db_connect as dbc

if ('FILTER_HOME' not in os.environ):
    os.environ["FILTER_HOME"] = "/home/anubis/SWE-Team"

FILTER_HOME = os.environ["FILTER_HOME"]
TEST_MODE = os.environ.get("TEST_MODE", 0)

if TEST_MODE:
    DB_DIR = f"{FILTER_HOME}/db/test_dbs"
else:
    DB_DIR = f"{FILTER_HOME}/db"

OK = 0
NOT_FOUND = 1
DUPLICATE = 2

client = dbc.get_client()
if client is None:
    print("Failed to connect to MongoDB")
    exit(1)
print(client)

# Collection Names
USERS = "users"
ACTIVE_SUBSCRIPTION_DB = "active_subscriptions"
INACTIVE_SUBSCRIPTION_DB = "inactive_subscriptions"

# Field names in our DB
USER_NAME = "Name"
USER_EMAIL = "Email"
USER_SUBSCRIPTION = "Subscription"

# Need to add subscription db's field names

def get_users():
    """
    A function to return a dictionary of all rooms.
    """
    return dbc.fetch_all(USERS, USER_EMAIL)

def get_active_subs():
    # return dbc.fetch_many(ACTIVE_SUBSCRIPTION_DB, USER_EMAIL, filters = {email})
    return dbc.fetch_many(ACTIVE_SUBSCRIPTION_DB, USER_EMAIL)

def get_inactive_subs():
    # return dbc.fetch_many(INACTIVE_SUBSCRIPTION_DB, USER_EMAIL, filters = {email})
    return dbc.fetch_many(INACTIVE_SUBSCRIPTION_DB, USER_EMAIL)

def user_exists(email):
    """
    See if a user with username is in the db.
    Returns True of False.
    """
    rec = dbc.fetch_one(USERS, filters={USER_EMAIL: email})
    print(f"{rec=}")
    return rec is not None

def add_user(name, email):
    '''
    Returning OK if user successfully added. Else, return DUPLICATE. 
    '''
    if user_exists(email):
        return DUPLICATE
    else:
        dbc.insert_doc(USERS, {USER_NAME: name, USER_EMAIL: email})
        return OK

def add_subs(email, subscription_name):
    '''
    Returning oK if subscription successfully added. Else, return DUPLICATE.
    '''
    dbc.insert_doc(ACTIVE_SUBSCRIPTION_DB, {USER_EMAIL: email, USER_SUBSCRIPTION: subscription_name})

def delete_subs(email, subscription_name):
    dbc.del_one(ACTIVE_SUBSCRIPTION_DB, {USER_EMAIL: email, USER_SUBSCRIPTION: subscription_name})
    dbc.insert_doc(INACTIVE_SUBSCRIPTION_DB, {USER_EMAIL: email, USER_SUBSCRIPTION: subscription_name})

# print("Listing Users Now!\n")
# print(get_users())
# print("\nAdding A User Now!\n")
# print(add_user("Rachel", "rachel@nyu.edu"))
# print("\nList Users After Adding Rachel\n")
# print(get_users())
# print("\nListing All Active Subscriptions\n")
# print(get_active_subs())
# print("\nAdding A Subscription To Aaron\n")
# print(add_subs("aaronchen@nyu.edu", "Whole Foods"))
# print("\nListing All Active Subscriptions Again After Adding")
# print(get_active_subs())
# print("\nListing the Inactive Subscriptions Before We Delete Aaron's Newly Added Subscription")
# print(get_inactive_subs())
# print("\nDeleting Aaron's newly added subscription\n")
# print(delete_subs("aaronchen@nyu.edu", "Whole Foods"))
# print("\nListing the Inactive Subscriptions After We Deleted Aaron's Newly Added Subscription")
# print(get_inactive_subs())
