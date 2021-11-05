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
	return render_template('index.html')

@app.route('/user_registration')
def user_registration(): 
    return render_template('register.html')

@app.route('/homepage')
def home():
    return render_template('home.html')
    
@app.route('/user_registration_auth', methods = ['GET', 'POST'])
def user_registration_auth(): 
    user_email_1 = request.form['email']
    user_password_1 = request.form['password']
    user_password_repeat = request.form['password-repeat']
    #db.collection('UsersAccounts').add({'Password': user_password_1, 'Username': user_email_1})
    print(request.form)
    
    if user_password_1 == user_password_repeat: 
        #cursor used to send queries 
        cursor = conn.cursor()
        #check for no duplicate emails 
        no_duplicate_emails = 'SELECT user_email FROM users WHERE user_email = %s'
        cursor.execute(no_duplicate_emails, (user_email_1))
        in_database = cursor.fetchone()
        if(in_database): 
            #user exists 
            #print(in_database, user_email_1, "user_exists")
            return render_template('register.html')
        else: 
            #new user, add into database 
            insert_user = 'INSERT INTO users VALUES (%s, md5(%s))'
            #print(user_email_1, user_password_1)
            cursor.execute(insert_user, (user_email_1, user_password_1))
            conn.commit()
            cursor.close()
            return render_template('index.html')
    
    return render_template('index.html')

@app.route('/user_login_auth', methods = ['GET', 'POST'])
def user_login_auth(): 
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
    cursor = conn.cursor()
    query = 'SELECT user_email, password FROM users WHERE user_email = %s AND password = md5(%s)'
    cursor.execute(query, (username, password))
    data = cursor.fetchone()
    cursor.close()
    if (data): 
        return render_template('home.html') #if it works it goes to the login form
    else: 
        return render_template('register.html') #if it doesnt work it goes to register 
    
    #return render_template('index.html')

@app.route('/add_subscription', methods = ['GET', 'POST'])
def add_subscription(): 
    '''
    User can request to add back a previously subscribed a subscription.
    The user would have to manually subscribe back since our application does 
    not store their login info or billing credentials. But it will automatically log 
    in the fact that they are now subscribed to some newsletter in our database 
    '''

@app.route('/delete_subscription', methods = ['GET', 'POST'])
def delete_subscription(): 
    '''
    User can request to cancel a subscription. they can put in the subscription request 
    manually through their accounts. Use gmail API to check if the service is terminated. 
    If the service is not terminated, then terminate it for them 
    '''

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