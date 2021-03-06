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


@api.route('/get_active_subscriptions')
class get_active_subscriptions(Resource):
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    def get(self):
        '''
        Returns active subscriptions for the user
        '''
        # active_subs = db.get_active_subs(username)["test2"]
        active_subs = db.get_active_subs()
        if active_subs is None:
            raise(wz.NotFound("Email not found in database"))
        else:
            print(active_subs)
            return active_subs
        # return {"Current Subsciptions": {"Best Buy": {"type": "newsletter"},
        #                             "Target": {"Category": "Promotional"}}}


@api.route('/get_inactive_subscriptions')
class get_inactive_subscriptions(Resource):
    def get(self):
        '''
        Returns deleted or inactive subscriptions for the user
        '''
        # inactive_subs = db.get_inactive_subs(username)["test2"]
        inactive_subs = db.get_inactive_subs()
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

@api.route('/add_subscription/<email>/<subscription_name>')
class add_subscriptions(Resource):
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    @api.response(HTTPStatus.NOT_ACCEPTABLE, 'A duplicate key')
    def post (self, email, subscription_name):
        '''
        Adds the subscription to active subs for the user
        '''
        ret = db.add_subs(email, subscription_name)
        if ret == db.NOT_FOUND:
            raise (wz.NotFound("Subscription db not found."))
        elif ret == db.DUPLICATE:
            raise (wz.NotAcceptable("Username already exists."))
        return f"{email}, {subscription_name} added."

@api.route('/delete_subscription/<email>/<subscription_name>')
class delete_subscriptions(Resource):
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    @api.response(HTTPStatus.NOT_ACCEPTABLE, 'A duplicate key')
    def post (self, email, subscription_name):
        '''
        Adds the subscription to active subs for the user
        '''
        ret = db.delete_subs(email, subscription_name)
        if ret == db.NOT_FOUND:
            raise (wz.NotFound("Subscription db not found."))
        elif ret == db.DUPLICATE:
            raise (wz.NotAcceptable("Username already exists."))
        return f"{email}, {subscription_name} deleted."

@api.route('/create_user/<username>/<email>')
class CreateUser(Resource):
    """
    This class supports adding a user to the chat room.
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    @api.response(HTTPStatus.NOT_ACCEPTABLE, 'A duplicate key')
    def post(self, username, email):
        """
        This method adds a user to the chatroom.
        """
        """
        This method adds a room to the room db.
        """
        ret = db.add_user(username, email)
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
