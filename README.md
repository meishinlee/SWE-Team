# flask-api
An example flask rest API server.

To build production, type `make prod`.

To create the env for a new developer, run `make dev_env`.

## User Requirements:
1. A method for the user to login. 
2. A database that stores each user's information. 

## System Requirements: 
1. We will use the Gmail API to update the person's filters to unsubscribe or resubscribe to a service 
2. We will need a Database Storage syste, such as MongoDB/Firebase/Postgres SQL to help us store user activity and ata 
3. We will use Flask 
4. OAuth 2.0 to allow users to log in through authorized accounts such as through Gmail/Facebook/etc. 
5. Google Calendar API to help set reminders and tasks for the user 
