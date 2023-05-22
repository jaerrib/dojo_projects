from books_app import app
from flask import render_template, request, redirect
from books_app.models.model_author import Author
from books_app.models.model_book import Book


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


@app.route('/authors/<int:id>')
def author_show(id):
    (favorites, author_name) = Author.get_author_with_favorites({'id': id})
    all_books = Book.get_all()
    return render_template('author_show.html',
                           favorites=favorites,
                           author_name=author_name,
                           author_id=id,
                           all_books=all_books)


@app.route('/authors/add_favorite', methods=['POST'])
def add_favorite():
    Author.add_favorite(request.form)
    return redirect(f'/authors/{request.form["author_id"]}')