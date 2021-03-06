from flask import Flask, render_template, request, redirect
from config import config
from werkzeug.security import check_password_hash, generate_password_hash

import psycopg2

application = Flask(__name__)

@application.route('/')
def home():
    return render_template("index.html")

@application.route('/register', methods=["Get", "Post"])
def register():
    if request.method=="POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            error = "Error: No username was entered."
            return render_template("apology.html", value=error)

        # Ensure password was submitted
        elif not request.form.get("password"):
            error = "Error: You must provide a password"
            return render_template("apology.html", value=error)

        # Ensure that the passwords match
        elif request.form.get("password") != request.form.get("confirmation"):
            error = "Error: Password must match"
            return render_template("apology.html", value=error)

        else:
            # Insert the new user into the database

            # Generate a hash key to be placed in the data base instead of the password
            hashkey = generate_password_hash(request.form.get("password"), method='pbkdf2:sha256', salt_length=8)
            try:
                # Create a connection
                params = config()
                conn = psycopg2.connect(**params)
                # Create a cursor
                cur = conn.cursor()
                Query = "INSERT INTO TEST (name, password) values (%s, %s)"
                cur.execute(Query, (request.form.get("username"), hashkey))
                conn.commit()
                cur.close()
                conn.close()
                #db.execute("insert into users (username, hash) values (? , ?)", request.form.get("username"), hashkey)
            except:
                error = "Error: That user name is already in use"
                return render_template("apology.html", value=error)

        return redirect("/")
    else:
        return render_template("register.html")

@application.route('/login')
def login():
    return render_template("login.html")
    