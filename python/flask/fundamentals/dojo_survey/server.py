from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = "this is a secret"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():
    session["name"] = request.form["name"]
    session["location"] = request.form["location"]
    session["language"] = request.form["language"]
    session["comments"] = request.form["comments"]
    return redirect("/result")


@app.route("/result")
def result():
    data = {
        "name": session["name"],
        "location": session["location"],
        "language": session["language"],
        "comments": session["comments"],
    }
    return render_template("result.html", data=data)


@app.route("/restart")
def restart():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
