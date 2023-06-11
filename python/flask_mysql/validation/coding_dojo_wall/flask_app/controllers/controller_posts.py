from flask_app import app
from flask import redirect, render_template, request, session
from flask_app.controllers import controller_users
from flask_app.models.model_post import Post
from flask_app.models.model_user import User

@app.route('/posts/create', methods=['POST'])
def create_posts():
    if not Post.validate_post(request.form):
        return redirect('/wall')
    data = {
        'content': request.form['content'],
        'user_id': session['user_id']
    }
    Post.save(data)
    return redirect('/wall')

@app.route('/posts/delete', methods=['POST'])
def delete_post():
    Post.delete(request.form)
    return redirect('/wall')
