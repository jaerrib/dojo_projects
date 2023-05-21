from books_app.config.mysqlconnections import connectToMySQL

class Book:

    DB = 'books_schema'

    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.books = []

    @classmethod
    def get_all(cls):
        query = 'SELECT * from books'
        results = connectToMySQL(cls.DB).query_db(query)
        books = []
        for book in results:
            books.append(cls(book))
        return books

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO books (title, num_of_pages) \
            VALUES (%(title)s, %(num_of_pages)s)'
        return connectToMySQL(cls.DB).query_db(query, data)
