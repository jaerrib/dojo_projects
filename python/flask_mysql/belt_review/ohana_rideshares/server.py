from flask_app import app
from flask_app.controllers import controller_rides
from flask_app.controllers import controller_users
from flask_app.controllers import controller_comments

if __name__ == '__main__':
    app.run(debug=True)
