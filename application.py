from email.mime import application
from flask import Flask, render_template
from config import config

import psycopg2

conn = None
try:
    # read connection parameters
    params = config()

    # connect to the PostgreSQL server
    print('Connecting to the PostgreSQL database...')
    conn = psycopg2.connect(**params)
    
    # create a cursor
    cur = conn.cursor()
    
# execute a statement
    print('PostgreSQL database version:')
    cur.execute('SELECT version()')

    # display the PostgreSQL database server version
    db_version = cur.fetchall()
    print(db_version)
    
# close the communication with the PostgreSQL
    cur.close()
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()
        print('Database connection closed.')


application = Flask(__name__)

@application.route('/')
def Hello():
    return render_template("index.html")

@application.route('/register')
def register():
    return render_template("register.html")

@application.route('/login')
def login():
    return render_template("login.html")
    