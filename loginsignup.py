import mysql.connector
import datetime
from flask import Flask, render_template, request, session,redirect
import pymysql
pymysql.install_as_MySQLdb()

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="pythondb"
)
app = Flask(__name__)
app.secret_key = 'ks'

@app.route("/registration")
def registration():
    return render_template("registration.html")
@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/login_post", methods=["post"])
def login_post():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="pythondb"
    )

    mycursor = mydb.cursor()
    a = request.form.get("k1")
    b = request.form.get("k2")
    mycursor.execute("select * from login where loginid='" + a + "' and password='" + b + "'")

    records = mycursor.fetchall()

    flag = 0
    for row in records:
        flag = 1

    if flag == 1:
        session['loginid'] = a
        return render_template('profile.html', data=a)

    else:
        return render_template('registration.html', data="invalid user name or password")


@app.route("/profile")
def profile():
    return render_template("profile.html")


@app.route("/profile_post", methods=["POST"])
def profile_post():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="pythondb"
    )

    posts = Posts.query.all()

    return render_template("admin.html", posts=posts)


app.run(debug=True)