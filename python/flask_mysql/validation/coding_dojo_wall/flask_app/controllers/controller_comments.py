from flask_app import app
from flask import redirect, render_template, request, session
from flask_app.controllers import controller_users
from flask_app.models.model_comment import Comment


@app.route('/comments/create', methods=['POST'])
def create_comment():
    if not Comment.validate_comment(request.form):
        return redirect('/wall')
    data = {
        'content': request.form['content'],
        'user_id': session['user_id'],
        'post_id': request.form['post_id']
    }
    Comment.save(data)
    return redirect('/wall')

@app.route('/comments/delete', methods=['POST'])
def delete_comment():
    Comment.delete(request.form)
    return redirect('/wall')
