from dojo_app.config.mysqlconnections import connectToMySQL
from dojo_app.models.model_ninja import Ninja


class Dojo:

    DB = 'dojos_and_ninjas_schema'

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

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

    @classmethod
    def get_dojo_with_ninjas(cls, data):
        query = "SELECT * FROM dojos JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(data)s;"
        results = connectToMySQL(cls.DB).query_db(query, data)
        print(query, data, results)
        dojo = cls(results[0])

        for row_from_db in results:
            ninja_data = {
                "id": row_from_db["id"],
                "name": row_from_db["name"],
                "first_name": row_from_db["ninjas.first_name"],
                "last_name": row_from_db["ninjas.last_name"],
                "age": row_from_db["ninjas.age"],
                "dojo_id": row_from_db["ninjas.dojo_id"],
                "created_at": row_from_db["ninjas.created_at"],
                "updated_at": row_from_db["ninjas.updated_at"]
            }
            dojo.ninjas.append(ninja.Ninjas(ninja_data))
        return dojo
