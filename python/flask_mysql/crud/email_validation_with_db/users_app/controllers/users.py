from users_app import app
from flask import render_template, request, redirect, session
from users_app.models.user import User


@app.route('/')
def index():
    return redirect('/users')


@app.route('/users')
def read():
    users = User.get_all()
    return render_template("users.html", all_users=users)


@app.route('/new')
def add():
    if 'data' not in session:
        session['data'] = {
        "first_name": "",
        "last_name": "",
        "email": ""
        }
    return render_template("new.html", data=session['data'])


@app.route('/users/<int:id>')
def read_one(id):
    user = User.get_one(id)
    return render_template("profile.html", user=user)


@app.route('/users/<int:id>/edit')
def edit_user(id):
    user = User.get_one(id)
    return render_template("edit.html", user=user)


@app.route('/create', methods=['POST'])
def create():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }
    if not User.validate_user(request.form):
        session['data'] = data
        return redirect('/new')
    User.save(data)
    return redirect("/users")


@app.route('/update', methods=['POST'])
def update():
    User.update(request.form)
    return redirect('/users')


@app.route('/users/<int:id>/delete')
def delete(id):
    User.delete(id)
    return redirect('/users')
