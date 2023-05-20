from dojo_app.config.mysqlconnections import connectToMySQL


class Dojo:

    DB = 'dojos_and_ninjas_schema'

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM dojos;'
        results = connectToMySQL(cls.DB).query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos

    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO dojos (name)
        VALUES ( %(name)s )
        """
        return connectToMySQL(cls.DB).query_db(query, data)
