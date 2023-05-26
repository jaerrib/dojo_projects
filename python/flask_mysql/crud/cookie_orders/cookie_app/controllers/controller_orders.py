from cookie_app import app
from flask import render_template, redirect, request, session
from cookie_app.models.model_order import Order

@app.route('/')
def index():
    return redirect('/cookies')

@app.route('/cookies')
def cookies():
    orders = Order.get_all()
    return render_template('cookies.html', orders=orders)

@app.route('/cookies/new')
def new():
    return render_template('new.html')

@app.route('/cookies/create', methods=['POST'])
def create():
    data = {
        'customer_name': request.form['customer_name'],
        'cookie_type': request.form['cookie_type'],
        'num_of_boxes': request.form['num_of_boxes']
    }
    if not Order.is_valid_order(data):
        if 'data' not in session:
            session['data'] = data
        return redirect('/cookies/new')
    Order.save(data)
    return redirect('/cookies')

@app.route('/cookies/edit/<int:id>')
def edit_order(id):
    order = Order.get_one(id)
    return render_template('edit.html', order=order)
