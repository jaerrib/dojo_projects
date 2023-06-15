from flask_app import app
from flask import redirect, request, session
from flask_app.models.model_message import Message
from flask_app.controllers import controller_rides


@app.route('/messages/add_message', methods=['POST'])
def add_message():
    data = {
        'content': request.form['content'],
        'user_id': session['user_id'],
        'ride_id': request.form['ride_id']
    }
    Message.save(data)
    return redirect(f'/rides/view/{request.form["ride_id"]}')
