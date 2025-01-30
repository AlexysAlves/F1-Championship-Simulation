import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///formula.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")

# Create route that allows user to choose number of races to be simulated
@app.route("/pre_simulate")
@login_required
def pre_simulate():
    return render_template("pre_simulate.html")

# Render simulation template with select forms
@app.route("/simulate", methods=["GET", "POST"])
@login_required
def simulate():

    if request.method == "POST":
        global nraces
        nraces = int(request.form.get("nraces"))
        print(nraces)
        if nraces < 1:
            return apology("Number of races must be a positive integer.")
        elif nraces > 23:
            return apology("Number of races must not be more than 23.")

        
        return redirect(request.url)
    else:
        drivers = db.execute("SELECT initials FROM drivers")
        return render_template("simulate.html", drivers=drivers, nraces=nraces)

# Calculate the final results of the simulation
@app.route("/result", methods=["GET", "POST"])
@login_required
def result():
    
        if request.method == "POST":
           
            for i in range(20):
                db.execute("UPDATE drivers SET laps = 0 WHERE id = ?", i + 1)
                db.execute("UPDATE drivers SET points = 0 WHERE id = ?", i + 1)
                db.execute("UPDATE drivers SET wins = 0 WHERE id = ?", i + 1)
            for i in range(nraces):
                fastestlapA = f"fastestlapA{i+1}"
                fastestlapB = f"fastestlapB{i+1}"
                fastestlapC = f"fastestlapC{i+1}"
                fastestlapD = f"fastestlapD{i+1}"
                fastestlapE = f"fastestlapE{i+1}"
                fastestlapF = f"fastestlapF{i+1}"
                fastestlapG = f"fastestlapG{i+1}"
                fastestlapH = f"fastestlapH{i+1}"
                fastestlapI = f"fastestlapI{i+1}"
                fastestlapJ = f"fastestlapJ{i+1}"
                fastestlap = f"fastestlap{i+1}"
                first = f"first{i+1}"
                second = f"second{i+1}"
                third = f"third{i+1}"
                fourth = f"fourth{i+1}"
                fifth = f"fifth{i+1}"
                sixth = f"sixth{i+1}"
                seventh = f"seventh{i+1}"
                eighth = f"eighth{i+1}"
                nineth = f"nineth{i+1}"
                tenth = f"tenth{i+1}"
                try:
                    if request.form.get(fastestlap) == fastestlapA:
                        db.execute("UPDATE drivers SET laps = laps + 1 WHERE initials = ?", request.form.get(first))
                        db.execute("UPDATE drivers SET points = points + 1 WHERE initials = ?", request.form.get(first))
                    elif request.form.get(fastestlap) == fastestlapB:
                        db.execute("UPDATE drivers SET laps = laps + 1 WHERE initials = ?", request.form.get(second))
                        db.execute("UPDATE drivers SET points = points + 1 WHERE initials = ?", request.form.get(second))
                    elif request.form.get(fastestlap) == fastestlapC:
                        db.execute("UPDATE drivers SET laps = laps + 1 WHERE initials = ?", request.form.get(third))
                        db.execute("UPDATE drivers SET points = points + 1 WHERE initials = ?", request.form.get(third))
                    elif request.form.get(fastestlap) == fastestlapD:
                        db.execute("UPDATE drivers SET laps = laps + 1 WHERE initials = ?", request.form.get(fourth))
                        db.execute("UPDATE drivers SET points = points + 1 WHERE initials = ?", request.form.get(fourth))
                    elif request.form.get(fastestlap) == fastestlapE:
                        db.execute("UPDATE drivers SET laps = laps + 1 WHERE initials = ?", request.form.get(fifth))
                        db.execute("UPDATE drivers SET points = points + 1 WHERE initials = ?", request.form.get(fifth))
                    elif request.form.get(fastestlap) == fastestlapF:
                        db.execute("UPDATE drivers SET laps = laps + 1 WHERE initials = ?", request.form.get(sixth))
                        db.execute("UPDATE drivers SET points = points + 1 WHERE initials = ?", request.form.get(sixth))
                    elif request.form.get(fastestlap) == fastestlapG:
                        db.execute("UPDATE drivers SET laps = laps + 1 WHERE initials = ?", request.form.get(seventh))
                        db.execute("UPDATE drivers SET points = points + 1 WHERE initials = ?", request.form.get(seventh))
                    elif request.form.get(fastestlap) == fastestlapH:
                        db.execute("UPDATE drivers SET laps = laps + 1 WHERE initials = ?", request.form.get(eighth))
                        db.execute("UPDATE drivers SET points = points + 1 WHERE initials = ?", request.form.get(eighth))
                    elif request.form.get(fastestlap) == fastestlapI:
                        db.execute("UPDATE drivers SET laps = laps + 1 WHERE initials = ?", request.form.get(nineth))
                        db.execute("UPDATE drivers SET points = points + 1 WHERE initials = ?", request.form.get(nineth))
                    elif request.form.get(fastestlap) == fastestlapJ:
                        db.execute("UPDATE drivers SET laps = laps + 1 WHERE initials = ?", request.form.get(tenth))
                        db.execute("UPDATE drivers SET points = points + 1 WHERE initials = ?", request.form.get(tenth))
                except:
                    return apology("You haven't filled all fields")
                antitrol = [ request.form.get(first), request.form.get(second), request.form.get(third), request.form.get(fourth), request.form.get(fifth), request.form.get(sixth), request.form.get(seventh), request.form.get(eighth), request.form.get(nineth), request.form.get(tenth)]
                antitrol2 = list(set(antitrol))
                if len(antitrol2) != 10:
                    return apology("You have selected two or more places for the same driver in the same race or haven't filled all fields.")
                db.execute("UPDATE drivers SET wins = wins + 1 WHERE initials = ?", request.form.get(first))
                db.execute("UPDATE drivers SET points = points + 25 WHERE initials = ?", request.form.get(first))
                db.execute("UPDATE drivers SET points = points + 18 WHERE initials = ?", request.form.get(second))
                db.execute("UPDATE drivers SET points = points + 15 WHERE initials = ?", request.form.get(third))
                db.execute("UPDATE drivers SET points = points + 12 WHERE initials = ?", request.form.get(fourth))
                db.execute("UPDATE drivers SET points = points + 10 WHERE initials = ?", request.form.get(fifth))
                db.execute("UPDATE drivers SET points = points + 8 WHERE initials = ?", request.form.get(sixth))
                db.execute("UPDATE drivers SET points = points + 6 WHERE initials = ?", request.form.get(seventh))
                db.execute("UPDATE drivers SET points = points + 4 WHERE initials = ?", request.form.get(eighth))
                db.execute("UPDATE drivers SET points = points + 2 WHERE initials = ?", request.form.get(nineth))
                db.execute("UPDATE drivers SET points = points + 1 WHERE initials = ?", request.form.get(tenth))

            
            return redirect(request.url)
        else:
            result = db.execute("SELECT name, team, points, wins, laps FROM drivers ORDER BY points DESC")
            constructors = []
            points = []
            for i in range(10):
                constructors.append(db.execute("SELECT team, SUM(points), SUM(wins) FROM drivers WHERE team_id = ?", i + 1))
                points.append(constructors[i][0])
            def sorting(e):
                return e["SUM(points)"]
            points.sort(reverse=True, key=sorting)
            print(points)
            return render_template("result.html", result=result, points=points)
    
# Create a new table to store saved results
@app.route("/saved", methods=["GET", "POST"])
@login_required
def saved():
    if request.method == "POST":
        user_id = session["user_id"]
        user_d = f"{user_id}_d"
        user_c = f"{user_id}_c"
        try:
            db.execute("DROP TABLE ?", user_d)
            db.execute("DROP TABLE ?", user_c)
        finally:    
            result = db.execute("SELECT name, team, points, wins, laps FROM drivers ORDER BY points DESC")
            db.execute("CREATE TABLE ? ('name' text NOT NULL, 'team' text NOT NULL, 'points' integer NOT NULL, 'wins' NOT NULL, 'laps' integer NOT NULL)", user_d)
            for driver in result:
                db.execute("INSERT INTO ? (name, team, points, wins, laps) VALUES (?, ?, ?, ?, ?)", user_d, driver['name'], driver['team'], driver['points'], driver['wins'], driver['laps'])
            constructors = []
            points = []
            for i in range(10):
                constructors.append(db.execute("SELECT team, SUM(points) AS points, SUM(wins) AS wins FROM drivers WHERE team_id = ?", i + 1))
                points.append(constructors[i][0])
            def sorting(e):
                return e["points"]
            points.sort(reverse=True, key=sorting)
            db.execute("CREATE TABLE ? ('team' text NOT NULL, 'points' integer NOT NULL, 'wins' integer NOT NULL)", user_c)
            for team in points:
                db.execute("INSERT INTO ? (team, points, wins) VALUES (?, ?, ?)", user_c, team['team'], team['points'], team['wins'])
            return redirect(request.url)
    else:
        return render_template("saved.html")
        
# Create a route that allows user to see results
@app.route("/view_results")
@login_required
def view_results():
    user_id = session["user_id"]
    user_d = f"{user_id}_d"
    user_c = f"{user_id}_c"
    try:
        drivers = db.execute("SELECT * FROM ?", user_d)
        teams = db.execute("SELECT * FROM ?", user_c)
        return render_template("view_results.html", drivers=drivers, teams=teams)
    except:
        return apology("Execute a simulation before viewing results")


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
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["password"], request.form.get("password")):
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

@app.route("/")
@login_required
def index():
    
    user_id = session["user_id"]
    user_get = db.execute("SELECT username FROM users WHERE id = ?", user_id)
    user_name = user_get[0]["username"]
    return render_template("index.html", user_name=user_name)
    
@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        if not username:
            return apology("Please, enter an username.")
        elif not password:
            return apology("Please, enter a password.")
        elif not confirmation:
            return apology("Please, confirm your password.")
        elif password != confirmation:
            return apology("Please, confirm your password properly.")
        hash = generate_password_hash(password)
        try:
            db.execute("INSERT INTO users (username, password) VALUES (?, ?)", username, hash)
            return redirect("/login")
        except:
            return apology("Username already in use. Please, choose another username.")

    else:
        return render_template("register.html")

# Create routes to render templates for all drivers and teams
@app.route("/raikkonen")
@login_required
def raikkonen():
    return render_template("raikkonen.html")
    
@app.route("/giovinazzi")
@login_required
def giovinazzi():
    return render_template("giovinazzi.html")
    
@app.route("/gasly")
@login_required
def gasly():
    return render_template("gasly.html")
    
@app.route("/tsunoda")
@login_required
def tsunoda():
    return render_template("tsunoda.html")
    
@app.route("/alonso")
@login_required
def alonso():
    return render_template("alonso.html")
    
@app.route("/ocon")
@login_required
def ocon():
    return render_template("ocon.html")
    
@app.route("/vettel")
@login_required
def vettel():
    return render_template("vettel.html")
    
@app.route("/stroll")
@login_required
def stroll():
    return render_template("stroll.html")
    
@app.route("/leclerc")
@login_required
def leclerc():
    return render_template("leclerc.html")
    
@app.route("/sainz")
@login_required
def sainz():
    return render_template("sainz.html")
    
@app.route("/mazepin")
@login_required
def mazepin():
    return render_template("mazepin.html")
    
@app.route("/schumacher")
@login_required
def schumacher():
    return render_template("schumacher.html")
    
@app.route("/ricciardo")
@login_required
def ricciardo():
    return render_template("ricciardo.html")
    
@app.route("/norris")
@login_required
def norris():
    return render_template("norris.html")
    
@app.route("/hamilton")
@login_required
def hamilton():
    return render_template("hamilton.html")
    
@app.route("/bottas")
@login_required
def bottas():
    return render_template("bottas.html")
    
@app.route("/perez")
@login_required
def perez():
    return render_template("perez.html")
    
@app.route("/verstappen")
@login_required
def verstappen():
    return render_template("verstappen.html")
    
@app.route("/latifi")
@login_required
def latifi():
    return render_template("latifi.html")
    
@app.route("/russel")
@login_required
def russel():
    return render_template("russel.html")
    
@app.route("/mercedes")
@login_required
def mercedes():
    return render_template("mercedes.html")
    
@app.route("/redbull")
@login_required
def redbull():
    return render_template("redbull.html")
    
@app.route("/mclaren")
@login_required
def mclaren():
    return render_template("mclaren.html")
    
@app.route("/astonmartin")
@login_required
def astonmartin():
    return render_template("astonmartin.html")
    
@app.route("/alpine")
@login_required
def alpine():
    return render_template("alpine.html")
    
@app.route("/ferrari")
@login_required
def ferrari():
    return render_template("ferrari.html")
    
@app.route("/alphatauri")
@login_required
def alphatauri():
    return render_template("alphatauri.html")
    
@app.route("/alfaromeo")
@login_required
def alfaromeo():
    return render_template("alfaromeo.html")
    
@app.route("/haas")
@login_required
def haas():
    return render_template("haas.html")
    
@app.route("/williams")
@login_required
def williams():
    return render_template("williams.html")
    
def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
