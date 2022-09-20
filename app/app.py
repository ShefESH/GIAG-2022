from flask import Flask
from flask import request, render_template, flash, session, redirect, url_for
from flask_bootstrap import Bootstrap
import sqlite3
import hashlib

app = Flask(__name__)
Bootstrap(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/unsanitary")
def unsanitary():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    #get details from form
    username = request.form["username"]
    password = hashlib.md5(request.form["password"].encode("utf-8")).hexdigest()
    print(password)
    con = sqlite3.connect("raspi.db")

    #SQLI Vulnerable Code
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute(f"SELECT id, username FROM users WHERE username='{username}' AND password='{password}'")
    users = cur.fetchall()

    #login as returned user
    if len(users) > 0:
        session["id"], session["username"] = users[0]
        return redirect(url_for("admin"))
    else:
        print("Wrong username or password")
        return redirect(url_for("index", error="Wrong email or password"))