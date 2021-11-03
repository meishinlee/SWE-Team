# Gmail Unsubscribe Filter
An example flask rest API server.

To build production, type `make prod`.

To create the env for a new developer, run `make dev_env`.

## User Requirements:
  The user can filter their Gmail emails by different types of subscriptions. The user will have the option to delete unwanted emails or make them not visible. 

## System Requirements: 
1. We will use the Gmail API to update the person's filters to unsubscribe or resubscribe to a service. 
2. We will need a Database Storage system, such as MongoDB/Firebase/Postgres SQL to help us store user activity. 
3. We will use Flask to allow Python to act as a backend.
4. We will use Jinja2 to act as a messenger for data transfer.  
5. If allowed, we can use OAuth 2.0 to allow users to log in through authorized accounts such as through Gmail/Facebook/etc. 
6. If allowed, we will also integrate the Google Calendar API to help set reminders and tasks for the user. 

## Design: 
1. A user can register for an account by using the `register_user` endpoint. 
2. A user can login to their accounts using the `user_login` endpoint. 
3. A user can modify their subscription status through the `modify_subscription_status` endpoint 
4. A user can add a new subscription status through the `add_subscription` endpoint 
5. A user can delete a subscription through the `delete_subscription` endpoint 
6. A user can view all of their current subscriptions and statuses through the `user_subscription_summary` endpoint 
