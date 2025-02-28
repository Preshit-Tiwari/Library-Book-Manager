import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import login_required, usd, apology

book_limit = 5
# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///library.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
@login_required
def home():
    """homepage"""
    return render_template("home.html")


@app.route("/issue", methods=["GET", "POST"])
@login_required
def issue():
    """Issue a book"""
    if request.method == "POST":
        b_id= str(request.form.get("book_id"))

        if b_id == None:
            return apology("Please enter book id!",400)

        user = db.execute(
            "SELECT * FROM users WHERE id = ?", session["user_id"]
        )
        user= user[0]

        if user["issued"] >= book_limit:
            return apology("Can't issue more than 5 books at a time", 400)

        book = db.execute(
            "SELECT * FROM books WHERE id = ?", b_id
        )
        if book == []:
            return apology("No such book exists!",400) 
        book= book[0]

        if book == None:
            return apology("No such book exists!",400)

        if book["issue_to"] != None:
            return apology("Book not available", 400)

        user["issued"]+= 1

        db.execute(
            "UPDATE users set issued = ? WHERE id = ?", user["issued"], session["user_id"]
        )

        db.execute(
            "UPDATE books set issue_to = ? WHERE id = ?", session["user_id"], b_id
        )

        db.execute(
            "INSERT into history(id, bid, bname, type) values(?,?,?,?)", session["user_id"], book["id"], book["name"], "issue"
        )
        success=1
        return redirect(url_for('about',success=success))
    else:
        return render_template("issue.html")

@app.route("/retrn", methods=["GET", "POST"])
@login_required
def retrn():
    """Return a book"""
    if request.method == "POST":
        b_id= request.form.get("book_id")

        user = db.execute(
            "SELECT * FROM users WHERE id = ?", session["user_id"]
        )
        user= user[0]

        book = db.execute(
            "SELECT * FROM books WHERE id = ?", b_id
        )

        if book == []:
            return apology("No such book exists!",400)  
        book = book[0]          

        if book["issue_to"] == None:
            return apology("book already submitted", 400)
        
        if user["issued"] == 0:
            return apology("No book is issued by this user", 400)
        
        if book["issue_to"] != session["user_id"]:
            return apology("Enter correct book id", 400)
        
        user["issued"]-= 1

        db.execute(
            "UPDATE users set issued = ? WHERE id = ?", user["issued"], session["user_id"]
        )

        db.execute(
            "UPDATE books set issue_to = null WHERE id = ?",b_id
        )

        db.execute(
            "INSERT into history(id, bid, bname, type) values(?,?,?,?)", session["user_id"], book["id"], book["name"], "return"
        )
        success=1
        return redirect(url_for('about',success=success))
    else:
        return render_template("retrn.html")

@app.route("/history")
@login_required
def history():
    """Show history"""

    history = db.execute("select * from history where id = ?", session["user_id"])
    return render_template("history.html", data= history)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

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
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

@app.route("/about")
@login_required
def about():
    """list the books with its status"""
    suc= request.args.get('success')
    books = db.execute("select * from books order by id")
    for book in books:
        if book["issue_to"] != None:
            book["available"] = "No"
        else:
            book["available"] = "Yes"
    try:
        suc = int(suc)
    except:
        pass
    return render_template("about.html", data= books, success = suc)

@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":

        user= request.form.get("username")
        pass_wd= request.form.get("password")
        pass_wd_conf= request.form.get("confirmation")

        if not user:
            return apology("must provide username", 400)

        elif not pass_wd:
            return apology("must provide password", 400)

        elif not pass_wd_conf:
            return apology("must provide password", 400)

        if not pass_wd == pass_wd_conf:
            return apology("password not matching", 400)

        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", user
        )

        if len(rows) != 0:
            return apology("user already exists", 400)

        hashed = str(generate_password_hash(pass_wd))

        db.execute("INSERT INTO users (username, hash) values(?,?)",user,hashed)

        print(hashed)

        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", user
        )

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        return redirect("/")
    else:
        return render_template("register.html")

@app.route("/password", methods=["GET", "POST"])
@login_required
def password():
    """Change Password."""
    if request.method == "POST":

        old_pwd= request.form.get("old_p")
        new_pass_wd= request.form.get("new_p")
        new_pass_wd_conf= request.form.get("new_p_conf")

        if not old_pwd:
            return apology("must provide old password", 400)

        elif not new_pass_wd:
            return apology("must provide new password", 400)

        elif not new_pass_wd_conf:
            return apology("must conform new password", 400)

        if not new_pass_wd == new_pass_wd_conf:
            return apology("new password not matching with conformation", 400)

        hash = db.execute(
            "SELECT hash FROM users WHERE id = ?", session["user_id"]
        )

        hash= hash[0]["hash"]

        if not check_password_hash(hash, old_pwd):
            return apology("Incorrect Old password", 400)

        hashed = str(generate_password_hash(new_pass_wd))

        db.execute("UPDATE users set hash = ? WHERE id = ?", hashed, session["user_id"])

        return redirect("/")
    else:
        return render_template("password.html")

