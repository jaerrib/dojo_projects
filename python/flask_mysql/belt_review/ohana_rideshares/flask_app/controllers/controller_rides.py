from flask_app import app
from flask import redirect, render_template, request, session
from flask_app.controllers import controller_users
from flask_app.models.model_ride import Ride
from flask_app.models.model_user import User
from flask_app.models.model_message import Message


@app.route('/dashboard')
def dashboard():
    if not 'user_id' in session:
        return redirect('/')
    user = User.get_one(session['user_id'])
    all_rides = Ride.get_all_rides_with_creator()
    return render_template('dashboard.html', user=user, all_rides=all_rides)


@app.route('/rides/new')
def new_ride():
    if not 'user_id' in session:
        return redirect('/')
    return render_template('new.html')


@app.route('/rides/create', methods=['POST'])
def create_ride():
    if not 'user_id' in session:
        return redirect('/')
    if not Ride.validate_ride(request.form):
        return redirect('/rides/new')
    data = {
        'destination': request.form['destination'],
        'pickup_location': request.form['pickup_location'],
        'date': request.form['date'],
        'details': request.form['details'],
        'user_id': session['user_id'],
    }
    Ride.save(data)
    return redirect('/dashboard')


@app.route('/rides/view/<int:id>')
def view_ride(id):
    if not 'user_id' in session:
        return redirect('/')
    ride = Ride.get_one_ride(id)
    ride.creator = User.get_one(ride.user_id)
    ride.driver = User.get_one(ride.driver_id)
    ride.messages = Message.get_all_messages(ride.id)
    return render_template('view.html', ride=ride)


@app.route('/rides/drive/<int:id>')
def drive(id):
    data = {
        'driver_id': session['user_id'],
        'id': id
    }
    Ride.add_driver(data)
    return redirect('/dashboard')


@app.route('/rides/cancel/<int:id>')
def cancel_drive(id):
    data = {'id': id}
    Ride.remove_driver(data)
    return redirect('/dashboard')


@app.route('/rides/delete/<int:id>')
def delete_ride(id):
    Ride.delete_ride(id)
    return redirect('/dashboard')


@app.route('/rides/edit/<int:id>')
def edit_ride(id):
    ride = Ride.get_one_ride(id)
    return render_template('edit.html', ride=ride)


@app.route('/rides/update', methods=['POST'])
def update_ride():
    if not Ride.validate_changes(request.form):
        return redirect('/rides/edit/<request.form["id"]>')
    data = {
        'pickup_location': request.form['pickup_location'],
        'details': request.form['details'],
        'id': request.form['id']}
    Ride.update_details(data)
    return redirect('/dashboard')
