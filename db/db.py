"""
This file will manage interactions with our data store.
At first, it will just contain stubs that return fake data.
Gradually, we will fill in actual calls to our datastore.
"""
import json
import os

if ('DEMO_HOME' not in os.environ):
    os.environ["DEMO_HOME"] = "/home/anubis/SWE-Team"

DEMO_HOME = os.environ["DEMO_HOME"]
TEST_MODE = os.environ.get("TEST_MODE", 0)

if TEST_MODE:
    DB_DIR = f"{DEMO_HOME}/db/test_dbs"
else:
    DB_DIR = f"{DEMO_HOME}/db"

USERS_DB = f"{DB_DIR}/users.json"
print(USERS_DB)

OK = 0
NOT_FOUND = 1
DUPLICATE = 2


def get_users():
    """
    A function to return a dictionary of all users.
    """
    try:
        with open(USERS_DB) as file:
            # print(file.read())
            return json.loads(file.read())
    except FileNotFoundError:
        print(USERS_DB)
        print("Users db not found.")
        return None


def write_users(users):
    pass


def add_user(username):
    """
    Add a user to the user database.
    Until we are using a real DB, we have a potential
    race condition here.
    """
    users = get_users()
    if users is None:
        return NOT_FOUND
    elif username in users:
        return DUPLICATE
    else:
        users[username] = {"num_users": 0}
        write_users(users)
        return OK
