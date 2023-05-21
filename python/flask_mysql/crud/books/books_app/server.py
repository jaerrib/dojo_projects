from books_app import app
from books_app.controllers import controller_authors
from books_app.controllers import controller_books

if __name__ == "__main__":
    app.run(debug=False)
