from flask import Flask, render_template, request, redirect
from users_schema import User
app = Flask(__name__)


@app.route('/')
def index():
    return redirect('/users')


@app.route('/users')
def read():
    users = User.get_all()
    print(users)
    return render_template("users.html", all_users=users)


@app.route('/new')
def add():
    return render_template("new.html")


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
