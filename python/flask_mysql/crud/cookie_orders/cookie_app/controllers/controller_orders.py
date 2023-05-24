from cookie_app import app
from flask import render_template, redirect, request
# from cookie_app.models.model_order import Order

@app.route('/')
def index():
    return redirect('/cookies')

@app.route('/cookies')
def cookies():
    return render_template('cookies.html')