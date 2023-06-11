from flask_app import app
from flask_app.controllers import controller_users
from flask_app.controllers import controller_posts
from flask_app.controllers import controller_comments

if __name__ == '__main__':
    app.run(debug=True)
