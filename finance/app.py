import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
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
    holdings = db.execute(
        "SELECT symbol, SUM(shares) AS shares FROM transactions WHERE user_id = ? GROUP BY symbol HAVING shares > 0",session["user_id"]
    )
    g_total = 0
    for holding in holdings: stock = lookup(holding["symbol"]);  holding["price"] = stock["price"]; holding["total"] = holding["shares"] * stock["price"]; g_total+=holding["total"]
    rows = db.execute("SELECT cash FROM users WHERE id = ? ", session["user_id"])
    g_total = rows[0]["cash"]

    return render_template("index.html", holdings=holdings, cash= rows[0]["cash"], g_total=g_total)




@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares =request.form.get("shares")

        if not symbol:
           return apology("must provide symbol")
        stock = lookup(symbol)
        if not stock or not shares:
            return apology("must provide shares or invalid symbol")

        try:
            shares=int(shares)
            if shares <= 0:
                int("//")
        except ValueError:
            return apology("not a positive integer")
        else:
            rows = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
        cost =stock["price"] * shares
        if rows[0]["cash"] < cost :
            return apology("not enough money")
        db.execute("INSERT INTO transactions (user_id,symbol,shares,price) VALUES(?,?,?,?)",session["user_id"], stock["symbol"], shares, stock["price"])
        db.execute("UPDATE users SET cash = cash - ? WHERE id= ?", cost, session["user_id"])
        return redirect("/")
    else:
         return render_template("buy.html")



@app.route("/history")
@login_required
def history():
    transactions = db.execute("SELECT symbol, shares, price, timestamp FROM transactions WHERE user_id =? ORDER BY timestamp DESC", session["user_id"])

    return render_template("history.html", transactions=transactions)


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
    if request.method == "POST":
        symbol = request.form.get("symbol")
        if not symbol:
            return apology("must provide symbol")
        stock = lookup(symbol)
        if not stock:
            return apology(f"no {symbol} found")
        else:
            return render_template("quoted.html", stock=stock)
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not username:
            return apology("must provide username")
        elif not password:
            return apology("must provide password")
        elif not confirmation:
            return apology("must provide confirmation")

        if not password == confirmation:
            return apology("password must be the same like confirmation")

        hash = generate_password_hash(password)
        try:
            db.execute("INSERT INTO users(username, hash) VALUES (?, ?)",username,hash)
        except ValueError:
            return apology("username exists")
        else:
            return redirect("/login")
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():

    symbols = db.execute(
        "SELECT symbol, SUM(shares) AS shares FROM transactions WHERE user_id = ? GROUP BY symbol HAVING shares > 0",session["user_id"]
    )
    if request.method == "GET":

        return render_template("sell.html", symbols=symbols)
    else:
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        if not symbol or not shares:
            return apology("invalid symbol or no shares")
    try:
        shares = int(shares)
        if shares <= 0:
            int("//")
    except ValueError:
        return apology("no positive integer in shares")
    else:
        has = db.execute(
        "SELECT SUM(shares) AS shares FROM transactions WHERE user_id = ? AND symbol = ? GROUP BY symbol",session["user_id"], symbol
    )

    if not has or has[0]["shares"] < shares:
        return apology("not enough shares")
    stock=lookup(symbol)
    db.execute("INSERT INTO transactions ( user_id, symbol, shares, price) VALUES (?, ?,?,?)",session["user_id"], symbol, -shares, stock["price"])
    db.execute("UPDATE users SET cash = cash + ? WHERE id= ?", stock["price"] * shares, session["user_id"])
    return redirect("/")



