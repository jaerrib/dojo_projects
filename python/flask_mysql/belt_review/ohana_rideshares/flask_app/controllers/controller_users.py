from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.model_user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/users/register', methods=['POST'])
def register():
    if not User.validate_registration(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': pw_hash
    }
    user_id = User.save(data)
    if not 'user_id' in session:
        session['user_id'] = user_id
    return redirect('/dashboard')


@app.route('/users/login', methods=['POST'])
def login():
    if not User.validate_login(request.form):
        return redirect('/')
    data = {
        'email': request.form['email'],
        'password': request.form['password']
    }
    user_in_db = User.get_by_email(data)
    if not user_in_db:
        flash('Invalid email', 'login')
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.password, data['password']):
        flash('Invalid password', 'login')
        return redirect('/')
    if not 'user_id' in session:
        session['user_id'] = user_in_db.id
    return redirect('/dashboard')

@app.route('/users/logout')
def logout():
    session.clear()
    return redirect('/')