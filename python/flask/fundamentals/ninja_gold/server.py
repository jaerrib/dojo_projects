from flask import Flask, render_template, request, redirect, session
from random import randint
from datetime import date, time, datetime
app = Flask(__name__)
app.secret_key = "this is a secret"


@app.route("/")
def index():
    if not "gold" in session:
        session["gold"] = 0
    if not "activities" in session:
        session["activities"] = []
    if not "moves" in session:
        session["moves"] = 0
    return render_template("index.html")


@app.route("/process_money", methods=["POST"])
def process():
    selection = request.form["building"]
    event_time = f" ({datetime.now().strftime('%Y/%m/%d %l:%M %p')})"
    
    # match selection:
    #     case "farm":
    #         something here
    #     case "cave":
    #         something here
    #     case "house":
    #         something here
    #     case "casino":
    #         something here

    if request.form["building"] == "farm":
        gold = randint(10, 20)
    elif request.form["building"] == "cave":
        gold = randint(5, 10)
    elif request.form["building"] == "house":
        gold = randint(2, 5)
    elif request.form["building"] == "casino":
        gold = randint(-50, 50)
    if gold >= 0:
        message = f"Earned {gold} gold from the {selection}!"
    if gold < 0 and selection == "casino":
        message = f"Entered a casino and lost {gold} gold...ouch!"
    session["activities"].append(message + event_time)
    session["gold"] += gold
    session["moves"] += 1
    return redirect("/")

@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
