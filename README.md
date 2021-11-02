# flask-api
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
