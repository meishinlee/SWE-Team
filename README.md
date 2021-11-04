# Gmail Unsubscribe to Newletters and Paid Subscriptions Filter
An example flask rest API server.

To build production, type `make prod`.

To create the env for a new developer, run `make dev_env`.

[![Build Status](https://app.travis-ci.com/meishinlee/SWE-Team.svg?branch=master)](https://app.travis-ci.com/meishinlee/SWE-Team)

Note to Dennis and Gordon: While we wrote the technicals, we spoke with Callahan and he said no points will be taken off.

## User Requirements:
  The user can filter their Gmail emails from infrequently engaged with subscriptions. The user will have the option to delete unwanted emails or make them not visible. 

## Design: 
1. We will use the Gmail API to update the person's filters to unsubscribe or resubscribe to a service. 
2. We will need a Database Storage system, such as MongoDB/Firebase/Postgres SQL to help us store user activity. 
3. We will use Flask to allow Python to act as a backend.
4. We will use Jinja2 to act as a messenger for data transfer.  
5. If allowed, we can use OAuth 2.0 to allow users to log in through authorized accounts such as through Gmail/Facebook/etc. 
6. If allowed, we will also integrate the Google Calendar API to help set reminders and tasks for the user. 

## System Requirements: 
1. CREATE: A user can register for an account by using the `/user_registration` endpoint. 
2. A user can login to their accounts using the `/user_login_auth` endpoint. 
3. UPDATE: A user can add a new subscription status through the `/add_subscription` endpoint 
4. DELETE: A user can delete a subscription through the `/delete_subscription` endpoint 
5. READ: A user can view all of their current subscriptions and statuses through the `/get_active_subscriptions` endpoint 
6. READ: A user can view all of their unsubscribed subscriptions and statuses through the `/inactive_user_subscriptions` endpoint
7. READ: If the project allows, a user can view their subscription habits (eg. summary statistics and categorize by subscription topic) through `/get_subsciption_statistics` 
