"""
This is the file containing all of the endpoints for our flask app.
The endpoint called `endpoints` will return all available endpoints.
"""

from http import HTTPStatus
from flask import Flask
from flask_restx import Resource, Api
import werkzeug.exceptions as wz

import db.db as db

app = Flask(__name__)
api = Api(app)


@api.route('/hello')
class HelloWorld(Resource):
    """
    The purpose of the HelloWorld class is to have a simple test to see if the
    app is working at all.
    """
    def get(self):
        """
        A trivial endpoint to see if the server is running.
        It just answers with "hello world."
        """
        return {'hello': 'world'}


@api.route('/endpoints')
class Endpoints(Resource):
    """
    This class will serve as live, fetchable documentation of what endpoints
    are available in the system.
    """
    def get(self):
        """
        The `get()` method will return a list of available endpoints.
        """
        endpoints = sorted(rule.rule for rule in api.app.url_map.iter_rules())
        return {"Available endpoints": endpoints}


@api.route('/get_subscription_statistics/<username>')
class get_subscription_statistics(Resource):
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    def post(self, username):
        '''
        Return all subscription statistics for the users
        '''
        sub_list = []
        active_subs = db.get_active_subs()['username']
        inactive_subs = db.get_inactive_subs()['username']
        if active_subs is None:
            raise(wz.NotFound("User not found in database"))
        else:
            sub_list.append(active_subs)
        if inactive_subs is None:
            raise(wz.NotFound("User not found in database"))
        else:
            sub_list.append(inactive_subs)
        return sub_list


@api.route('/get_active_subscriptions/<username>')
class get_active_subscriptions(Resource):
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    def post(self, username):
        '''
        Returns active subscriptions for the user
        '''
        # active_subs = db.get_active_subs(username)["test2"]
        active_subs = db.get_active_subs(username)['username']
        if active_subs is None:
            raise(wz.NotFound("User not found in database"))
        else:
            print(active_subs)
            return active_subs
        # return {"Current Subsciptions": {"Best Buy": {"type": "newsletter"},
        #                             "Target": {"Category": "Promotional"}}}


@api.route('/get_inactive_subscriptions/<username>')
class get_inactive_subscriptions(Resource):
    def post(self, username):
        '''
        Returns deleted or inactive subscriptions for the user
        '''
        # inactive_subs = db.get_inactive_subs(username)["test2"]
        inactive_subs = db.get_inactive_subs(username)['username']
        if inactive_subs is None:
            raise(wz.NotFound("User not found in database"))
        else:
            return inactive_subs


@api.route('/list_users')
class ListUsers(Resource):
    """
    This endpoint returns a list of all users.
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    def get(self):
        """
        Returns a list of all users.
        """
        users = db.get_users()
        if users is None:
            raise (wz.NotFound("User db not found."))
        else:
            return users


@api.route('/create_user/<username>')
class CreateUser(Resource):
    """
    This class supports adding a user to the chat room.
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    @api.response(HTTPStatus.NOT_ACCEPTABLE, 'A duplicate key')
    def post(self, username):
        """
        This method adds a user to the chatroom.
        """
        """
        This method adds a room to the room db.
        """
        ret = db.add_user(username)
        if ret == db.NOT_FOUND:
            raise (wz.NotFound("User db not found."))
        elif ret == db.DUPLICATE:
            raise (wz.NotAcceptable("User name already exists."))
        return f"{username} added."


# @api.route('/pets')
# class Pets(Resource):
#     """
#     This class supports fetching a list of all pets.
#     """
#     def get(self):
#         """
#         This method returns all pets.
#         """
#         return db.fetch_pets()
