from flask import Flask, render_template, request, redirect
from users_schema import User
app = Flask(__name__)


@app.route('/')
def index():
    return redirect('/read')


@app.route('/read')
def read():
    users = User.get_all()
    print(users)
    return render_template("read.html", all_users=users)


@app.route('/add')
def add():
    return redirect("add.html")


@app.route('/create', methods=['POST'])
def create():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }
    User.save(data)
    return redirect("/read")


if __name__ == "__main__":
    app.run(debug=True)
