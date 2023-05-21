from books_app.config.mysqlconnections import connectToMySQL

class Author:

    DB = 'books_schema'

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.authors = []

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM authors'
        results = connectToMySQL(cls.DB).query_db(query)
        authors = []
        for author in results:
            authors.append(cls(author))
        return authors