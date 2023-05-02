from flask import Flask, render_template, request, redirect
from users_schema import User
app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def users():
    print("working")
    users = User.get_all()
    return render_template("users.html", all_users=users)

@app.route('/new', methods=['POST'])
def new():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }
    User.save(data)
    return redirect('/users')

if __name__ == "__main__":
    app.run(debug=True)