import os


import sqlite3
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import apology,login_required,create_connection
import datetime
import smtplib
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

conn = sqlite3.connect('sqlite.sql///project.db')

print ("Opened database successfully")


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)



@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
def index():
    return render_template('home.html')

@app.route("/home")
def home():
    return render_template('home.html')
    #return redirect("/")
    

@app.route("/login", methods=["GET", "POST"])
def login():
    
    ##be able too open the data base in login 
    """Log user in"""
    conn = sqlite3.connect('sqlite.sql///project.db')
    cursor = conn.cursor()
    rows = cursor.execute('SELECT rowid,Username,hash,email FROM USERS').fetchall()
    rows = [dict(zip(["rowid","Username","hash","email"],row))for row in rows]

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        username = request.form.get("username")
        password = request.form.get("password")
        #name = rows[0]['Username']
        
        print(username)
        print(password)
        #loop over dictionary
        for user in rows:
            name = user["Username"]
            passwordRow = user["hash"]
            #get id with the value 0
            rowid = user["rowid"] - 1 
            #print(user)
            
            
             #look if  match with the data base
            if  name == username:
                #print(cursor.lastrowid)
                print("rowid",rowid,"Username match --name:",name,"username:",username,"user:",user, )
                
            #look if the password good
                if passwordRow != password:                   
                   print("Password Match ----Username:",username,"hash:",passwordRow,"name:",name)
            #compare hash        
                elif len(user) != 1 or not check_password_hash(user["hash"],passwordRow):
                    return apology("invalid username and/or password", 403)
                else:
                    print("Fail")
                    return apology("Bad Password", 403)
                
                #remember who was log in 
                session["user_id"] = rowid 
                #session["user_id"] = cursor.lastrowid
                print(session["user_id"])
                
                #redirect home page
                return redirect("/")

        # return if password or username dont match
        return apology("invalid username and/or password",403)
        

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")
        

    
@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "GET":
        return render_template("register.html")
    else:
        #make the connection
        conn = sqlite3.connect('sqlite.sql///project.db')
        cursor = conn.cursor()
        #get data from the form
        username = request.form.get("username")
        name = username.lower()
        print("name",name)
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        email = request.form.get("email")
        
        
        if not username:
            return apology("Sorry this username is not valide")

        if not password:
            return apology("Must put a password")

        if not confirmation:
            return apology("Must confirm")

        if password != confirmation:
            
            return apology("Must be the same password")
        
        passHash = generate_password_hash(password)
        
        if not email:
            return apology("Must add an email")

# verifie si username exist, si exist return apology
        cursor = conn.cursor()
        
        cursor.execute("SELECT count(*) FROM USERS where lower(username) = ?",[name])
        countUsername = cursor.fetchone()
        

        if countUsername[0] != 0:
            return apology("User Already exist, choose other username")



        try:

            id = cursor.lastrowid
            sql = """INSERT INTO USERS(Username,hash,email) VALUES (?,?,?)"""  
            user_new = cursor.execute(sql, (username,passHash,email)) 
            

            conn.commit()
        
        except:
            return apology("username already existe")
        
       
        session["user_id"] = cursor.lastrowid 
        print(session["user_id"])
        
        #send email when register if the box is check
        send_email = request.form.get("send_email")

        if not send_email == None:
            server = smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login('fknight.tech@gmail.com','bdomtqqdxccrzyro')
            server.sendmail('fknight.tech@gmail.com',email,'Welcome In Walrus Family News!')
            print('Mail Sent')
        else:
            return redirect("/")
        

        return redirect("/")

    
@app.route("/roadmap")
@login_required
def roadmap():
    
    
    
    
    return render_template("roadmap.html")

@app.route("/about")
def about():
    
    
    
    return render_template("about.html")

@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@app.route("/market", methods =["GET","POST"])
def market():
    
    
    
    return render_template("market.html")


conn.close()

if __name__ == '__main__':
    app.run(port=5000, debug=True)
    
