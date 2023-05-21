from books_app import app
from flask import render_template, request, redirect
from books_app.models.model_book import Book

@app.route('/books')
def books():
    books = Book.get_all()
    return render_template('books.html', books=books)

@app.route('/books/new_book', methods=['POST'])
def new_book():
    Book.save(request.form)
    return redirect('/books')