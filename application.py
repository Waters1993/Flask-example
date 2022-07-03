from email.mime import application
from flask import Flask, render_template

application = Flask(__name__)

@application.route('/')
def Hello():
    return render_template("layout.html")