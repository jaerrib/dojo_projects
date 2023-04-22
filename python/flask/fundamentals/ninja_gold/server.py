from flask import Flask, render_template, request, redirect, session
from random import randint
app = Flask(__name__)
app.secret_key = "this is a secret"

@app.route("/")
def index():
    if not "gold" in session:
        session["gold"] = 0
    return render_template("index.html")

@app.route("/process_money", methods=["POST"])
def process():
    if request.form["building"] == "farm":
        print("Farm")
        session["gold"] += randint(10, 20)
        return redirect("/")
    elif request.form["building"]  == "cave":
        print("Cave")
        session["gold"] += randint(5, 10)
        return redirect("/")
    elif request.form["building"]  == "house":
        print("House")
        session["gold"] += randint(2, 5)
        return redirect("/")
    elif request.form["building"]  == "casino":
        session["gold"] =+ randint(-50, 50)
        print("Casino")
        return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)