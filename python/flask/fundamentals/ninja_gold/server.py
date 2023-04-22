from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "this is a secret"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process_money", methods=["POST"])
def process():
    if request.form["building"] == "farm":
        print("Farm")
        return redirect("/")
    elif request.form["building"]  == "cave":
        print("Cave")
        return redirect("/")
    elif request.form["building"]  == "house":
        print("House")
        return redirect("/")
    elif request.form["building"]  == "casino":
        print("Casino")
        return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)