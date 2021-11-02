#Import Flask Library
from flask import Flask, render_template, request, session, url_for, redirect
import pymysql.cursors

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

@app.route('/user_registration_auth', methods = ['GET', 'POST'])
def user_registration_auth(): 
    user_email_1 = request.form['email']
    user_password_1 = request.form['password']
    user_password_repeat = request.form['password-repeat']
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

@app.route('/user_login_auth', methods = ['GET', 'POST'])
def user_login_auth(): 
    #get information from form
    username = request.form['email']
    password = request.form['password']
    cursor = conn.cursor()
    query = 'SELECT user_email, password FROM users WHERE user_email = %s AND password = md5(%s)'
    cursor.execute(query, (username, password))
    data = cursor.fetchone()
    cursor.close()
    if (data): 
        return render_template('index.html') #if it works it goes to the login form
    else: 
        return render_template('register.html') #if it doesnt work it goes to register 
