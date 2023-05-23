from users_app import app
from flask import render_template, request, redirect
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
    return render_template("new.html")


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
    if not User.validate_user(request.form):
        return redirect('/new')
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }
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

# @app.route('/register', methods=['POST'])
# def register():
#     if not User.validate_user(request.form):
#         # we redirect to the template with the form.
#         return redirect('/')
#     # ... do other things
#     return redirect('/dashboard')
