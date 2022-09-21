from flask import Flask
from flask import request, render_template, flash, session, redirect, url_for, send_from_directory
from flask_bootstrap import Bootstrap
import sqlite3
import hashlib

app = Flask(__name__, static_folder='static')
Bootstrap(app)

#routes for static files
@app.route('/robots.txt')
@app.route('/favicon.ico')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/yournextchallenge")
def chall_2():
    return render_template("challenge_2.html")

@app.route("/thisisthesecondsolution")
def chall_3():
    return render_template("challenge_3.html")

@app.route("/youfoundthehiddentext")
def chall_4():
    return render_template("challenge_4.html")

@app.route("/youhavefoundthefourthsolution")
def chall_5():
    return render_template("challenge_5.html")

@app.route("/youhavefoundthefourthsolution", methods=["POST"])
def challenge_5_login():
    #get details from form
    password = request.form["password"]
    if password == "securepassword":
        return redirect(url_for("unsanitary"))
    else:
        return render_template("challenge_5.html")


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