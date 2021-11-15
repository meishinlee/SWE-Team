#Import Flask Library
from flask import Flask, render_template, request, session, url_for, redirect
#from flask_restx import Resource, Api
import pymysql.cursors

'''
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("serviceAccountKey")
firebase_admin.initialize_app(cred)

db = firestore.client()
user_accounts = db.collection(u'UsersAccounts')
#db.collection('UsersAccounts').add({'Password': '123', 'Username': "bob"})
'''

username_password_dictionary = {}
username_subscriptions_dictionary = {}

#Configure MySQL
conn = pymysql.connect(host='localhost',
                       user='root',
                       password='',
                       db='swe-team-test',
                       charset='utf8mb4',
                       cursorclass=pymysql.cursors.DictCursor)

#Initialize the app from Flask
app = Flask(__name__)

@app.route('/')
def user_login():
    '''
    Takes login information from the user, which consists of a username (email) and password. 
    Returns True (goes to homepage) or False (go to login/register page)
    '''
    return render_template('index.html')

@app.route('/user_registration')
def user_registration(): 
    '''
    Takes user information such as Full Name, Email address, and password. 
    Checks if user exists in the database. Else, add to database 
    '''

    #Endpoint stub outline: 
    #if user_exists == True: 
    #    return render_template('index.html') #currently we have the login page as index.html 
    #else: 
    #    username_password_dictionary[username] = password
    return render_template('register.html')

@app.route('/homepage')
def home():
    '''
    Takes a boolean (True/False) to signify if the user login is successful 
    if user login successful: return the homepage of the user
    else display login page 
    '''
    #if user_login_successful() == True: 
    #    return render_template('home.html')
    #else: 
    #    return render_template('index.html') #return login page
    #return render_template('home.html')
    
@app.route('/user_registration_auth', methods = ['GET', 'POST'])
def user_registration_auth(): 
    '''
    This goes hand in hand with user_registration(), we split this up into two different endpoints 
    when we build it technically
    Takes user information such as Full Name, Email address, and password. 
    Checks if user exists in the database. Else, add to database 
    '''
    user_email_1 = request.form['email']
    user_password_1 = request.form['password']
    user_password_repeat = request.form['password-repeat']
    #db.collection('UsersAccounts').add({'Password': user_password_1, 'Username': user_email_1})
    print(request.form)
    
    # if user_password_1 == user_password_repeat: 
    #     #cursor used to send queries 
    #     cursor = conn.cursor()
    #     #check for no duplicate emails 
    #     no_duplicate_emails = 'SELECT user_email FROM users WHERE user_email = %s'
    #     cursor.execute(no_duplicate_emails, (user_email_1))
    #     in_database = cursor.fetchone()
    #     if(in_database): 
    #         #user exists 
    #         #print(in_database, user_email_1, "user_exists")
    #         return render_template('register.html')
    #     else: 
    #         #new user, add into database 
    #         insert_user = 'INSERT INTO users VALUES (%s, md5(%s))'
    #         #print(user_email_1, user_password_1)
    #         cursor.execute(insert_user, (user_email_1, user_password_1))
    #         conn.commit()
    #         cursor.close()
    #         return render_template('index.html')
    
    if user_password_1 == user_password_repeat:
        if user_email_1 not in username_password_dictionary:
            username_password_dictionary[user_email_1] = user_password_1
            username_subscriptions_dictionary[user_email_1] = []
            return render_template('index.html')
        else:
            return render_template('register.html')
    return render_template('index.html')

@app.route('/user_login_auth', methods = ['GET', 'POST'])
def user_login_auth(): 
    '''
    This goes hand in hand with the user_login() endpoint, but this was split into two 
    parts technically when we tried implementing it. 
    Takes login information from the user, which consists of a username (email) and password. 
    Returns True (goes to homepage) or False (go to login/register page)
    '''
    #get information from form
    username = request.form['email']
    password = request.form['password']
    '''
    entry = user_accounts.where(u'Password', u'==', password).get()
    for item in entry:
        print(item.to_dict())
        item = item.to_dict()
        print(item["Username"])
        print(item["Password"])
    '''
    # cursor = conn.cursor()
    # query = 'SELECT user_email, password FROM users WHERE user_email = %s AND password = md5(%s)'
    # cursor.execute(query, (username, password))
    # data = cursor.fetchone()
    # cursor.close()
    # if (data): 
    #     return render_template('home.html') #if it works it goes to the login form
    # else: 
    #     return render_template('register.html') #if it doesnt work it goes to register 
    if username in username_password_dictionary:
        if username_password_dictionary[username] == password:
            return render_template('home.html')
        else:
            return render_template('register.html')
    
    #return render_template('index.html')

@app.route('/add_subscription', methods = ['GET', 'POST'])
def add_subscription(): 
    '''
    User can request to add back a previously subscribed a subscription.
    The user would have to manually subscribe back since our application does 
    not store their login info or billing credentials. But it will automatically log 
    in the fact that they are now subscribed to some newsletter in our database 
    '''
    new_subscription = request.form['subscription_name']
    if "ac7378@nyu" in username_subscriptions_dictionary:
        if username_subscriptions_dictionary["ac7378@nyu"] == []:
            username_subscriptions_dictionary["ac7378@nyu"].append(new_subscription)
        else:
            for elem in username_subscriptions_dictionary["ac7378@nyu"]:
                if elem == new_subscription:
                    print("Subscription already exists")
            else:
                username_subscriptions_dictionary["ac7378@nyu"].append(new_subscription)
    

@app.route('/delete_subscription', methods = ['GET', 'POST'])
def delete_subscription(): 
    '''
    User can request to cancel a subscription. they can put in the subscription request 
    manually through their accounts. Use gmail API to check if the service is terminated. 
    If the service is not terminated, then terminate it for them 
    '''
    sub_name_to_remove = request.form['subscription_name']
    if "ac7378@nyu" in username_subscriptions_dictionary:
        if username_subscriptions_dictionary["ac7378@nyu"] == []:
            print("No subscriptions to delete")
        else:
            for elem in username_subscriptions_dictionary["ac7378@nyu"]:
                if elem == sub_name_to_remove:
                    username_subscriptions_dictionary["ac7378@nyu"].remove(sub_name_to_remove)
            else:
                print("No such subscription was made previously. Unable to remove an non-existent subscription.")
            

@app.route('/get_active_subscriptions', methods = ['GET'])
def get_active_subscriptions(): 
    '''
    Return the list of subscriptions that the user is currently subscribed to 
    '''

@app.route('/get_inactive_subscriptions', methods = ['GET'])
def get_inactive_subscriptions(): 
    '''
    Return the list of subscriptions that the user used to be subscribed to and the date 
    they last unsubscribed. 
    '''

@app.route('/get_subscription_statistics')
def get_subscription_statistics(): 
    ''' 
    Returns a list of summary statistics for the user (eg. trends and categorize by 
    subscription topic. )
    '''
    
def isSessionLoggedIn(): 
	if len(session) > 0: 
		print(session)
		return True 
	return False
    
@app.route('/logout')
def logout():
	session.pop('username')
	#session.pop('role')
	print(session)
	return redirect('/')