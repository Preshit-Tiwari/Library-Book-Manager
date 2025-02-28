import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    user = db.execute(
            "SELECT * FROM users WHERE id = ?", session["user_id"]
        )
    user= user[0]
    index_data = db.execute("select symbol, sum(shares) as shares from history group by symbol having id = ?", session["user_id"])
    total = 0
    for i in index_data:
        i["price"] = int(lookup(i["symbol"])["price"])
        i["total"] = i["price"] * i["shares"]
        i["price"] = usd(int(lookup(i["symbol"])["price"]))
        total += i["total"]
        i["total"] = usd(i["total"])

    return render_template("index.html", data = index_data, total = usd(total + user["cash"]), cash = usd(user["cash"]))


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        symbol= request.form.get("symbol")
        try:
            shares= int(request.form.get("shares"))
        except:
            return apology("Invalid Shares", 400)

        shares= eval(request.form.get("shares"))
        if not shares.is_integer():
            return apology("Invlaid Shares", 400)

        if shares <= 0:
            return apology("Invalid Shares", 400)

        lu= lookup(symbol)
        if lu == None:
            return apology("Invalid Symbol", 400)

        user = db.execute(
            "SELECT * FROM users WHERE id = ?", session["user_id"]
        )
        user= user[0]

        if int(shares) * int(lu["price"]) > int(user["cash"]):
            return apology("Don't have enough cash", 400)

        user["cash"]-= shares * int(lu["price"])

        db.execute(
            "UPDATE users set cash = ? WHERE id = ?", user["cash"], session["user_id"]
        )

        db.execute(
            "INSERT into history(id, symbol, shares) values(?,?,?)", session["user_id"], lu["symbol"], shares
        )
        return redirect("/")
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""

    history = db.execute("select symbol, shares, trans from history where id = ?", session["user_id"])
    for i in history:
        i["price"] = usd(int(lookup(i["symbol"])["price"]))

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


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":

        sym= request.form.get("symbol")
        dic= lookup(sym)
        if dic == None:
            return apology("invalid symbol", 400)
        return render_template("quoted.html", symbol=dic["symbol"], price=usd(dic["price"]))
    else:
        return render_template("quote.html")

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


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":
        symbol= request.form.get("symbol")
        try:
            shares= int(request.form.get("shares"))
        except:
            return apology("Invalid Shares", 400)

        shares= eval(request.form.get("shares"))
        if not shares.is_integer():
            return apology("Invlaid Shares", 400)

        if shares <= 0:
            return apology("Invalid Shares", 400)
        
        u_data = db.execute("select sum(shares) as shares from history group by symbol having id = ? and symbol = ?", session["user_id"], symbol)

        if u_data[0]["shares"] < shares:
            return apology("Invalid Shares", 400)

        lu= lookup(symbol)
        if lu == None:
            return apology("Invalid Symbol", 400)

        user = db.execute(
            "SELECT * FROM users WHERE id = ?", session["user_id"]
        )
        user= user[0]

        user["cash"]+= shares * int(lu["price"])

        db.execute(
            "UPDATE users set cash = ? WHERE id = ?", user["cash"], session["user_id"]
        )

        db.execute(
            "INSERT into history(id, symbol, shares) values(?,?,?)", session["user_id"], lu["symbol"], -shares
        )
        return redirect("/")
    else:
        symbols = db.execute("select symbol from history group by symbol having id =?", session["user_id"])
        return render_template("sell.html", data= symbols)

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
