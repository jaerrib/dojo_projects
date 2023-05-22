from books_app.config.mysqlconnections import connectToMySQL
from books_app.models.model_book import Book

class Author:

    DB = 'books_schema'

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.favorites = []

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM authors'
        results = connectToMySQL(cls.DB).query_db(query)
        authors = []
        for author in results:
            authors.append(cls(author))
        return authors

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO authors (name) VALUES (%(name)s)'
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def get_author_with_favorites(cls, data):
        query = 'SELECT * FROM authors \
            LEFT JOIN favorites ON favorites.author_id = authors.id \
                LEFT JOIN books on favorites.book_id = books.id \
                    WHERE authors.id = %(id)s;'
        results = connectToMySQL(cls.DB).query_db(query, data)
        book = cls(results[0])
        all_books = []
        author_name = results[0]["name"]
        for row_from_db in results:
            book_data = {
                "id": row_from_db['books.id'],
                "title": row_from_db['title'],
                "num_of_pages": row_from_db['num_of_pages'],
                "created_at": row_from_db['books.created_at'],
                "updated_at": row_from_db['books.updated_at']
            }
            all_books.append(Book(book_data))
            
        return (all_books, author_name)


    @classmethod
    def add_favorite(cls, data):
        print(data)
        query = 'INSERT INTO favorites (author_id, book_id) VALUES (%(author_id)s, %(book_id)s)'
        return connectToMySQL(cls.DB).query_db(query, data)
