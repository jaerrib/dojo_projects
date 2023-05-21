from books_app import app
from flask import render_template, request, redirect
from books_app.models.model_author import Author

@app.route('/')
def index():
    return redirect('/authors')

@app.route('/authors')
def authors():
    authors = Author.get_all()
    return render_template('authors.html', authors=authors)

@app.route('/authors/new_author', methods=['POST'])
def new_author():
    Author.save(request.form)
    return redirect('/authors')