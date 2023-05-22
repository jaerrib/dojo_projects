from books_app import app
from flask import render_template, request, redirect
from books_app.models.model_book import Book
from books_app.models.model_author import Author

@app.route('/books')
def books():
    books = Book.get_all()
    return render_template('books.html', books=books)

@app.route('/books/new_book', methods=['POST'])
def new_book():
    Book.save(request.form)
    return redirect('/books')

@app.route('/books/<int:id>')
def book_show(id):
    (all_favorites, book_title) = Book.get_book_with_favorites({'id': id})
    all_authors= Author.get_all()
    return render_template('book_show.html',
                           all_favorites=all_favorites,
                           book_title=book_title,
                           book_id=id,
                           all_authors=all_authors)

@app.route ('/books/add_favorite', methods=['POST'])
def add_favorite_by_author():
    Author.add_favorite(request.form)
    return redirect(f'/books/{request.form["book_id"]}')
