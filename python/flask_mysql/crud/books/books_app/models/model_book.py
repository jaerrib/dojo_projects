from books_app.config.mysqlconnections import connectToMySQL
import books_app.models.model_author as model_author
# topping.on_burgers.append( burger.Burger( burger_data ) )

class Book:

    DB = 'books_schema'

    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # self.books = []
        self.favorites = []

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

    @classmethod
    def get_book_with_favorites(cls, data):
        query = 'SELECT * from books \
            LEFT JOIN favorites ON favorites.book_id = books.id \
                LEFT JOIN authors ON favorites.author_id = authors.id \
                    WHERE books.id = %(id)s;'
        results = connectToMySQL(cls.DB).query_db(query, data)
        book = cls(results[0])
        all_favorites = []
        book_title = results[0]["title"]
        for row_from_db in results:
            author_data = {
                "id": row_from_db['authors.id'],
                "name": row_from_db['name'],
                "created_at": row_from_db['authors.created_at'],
                "updated_at": row_from_db['authors.updated_at']
            }
            all_favorites.append(model_author.Author(author_data))
        return (all_favorites, book_title)


    @classmethod
    def add_favorite(cls, data):
        print(data)
        query = 'INSERT INTO favorites (author_id, book_id) VALUES (%(author_id)s, %(book_id)s)'
        return connectToMySQL(cls.DB).query_db(query, data)
