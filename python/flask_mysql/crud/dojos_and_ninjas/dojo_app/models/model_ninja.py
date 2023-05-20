from dojo_app.config.mysqlconnections import connectToMySQL


class Ninja:

    DB = 'dojos_and_ninjas_schema'

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojo_id = data['dojo_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = None

    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO ninjas (first_name, last_name, age, dojo_id)
        VALUES ( %(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s )
        """
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM ninjas;'
        results = connectToMySQL(cls.DB).query_db(query)
        all_ninjas = []
        for ninja in results:
            all_ninjas.append(cls(ninja))
        return all_ninjas

    @classmethod
    def get_one_dojo(cls, data):

        query = """
        SELECT * FROM dojos
        LEFT JOIN ninjas
        ON ninjas.dojo_id = dojos.id
        WHERE dojos.id = %(id)s;
        """

        results = connectToMySQL(cls.DB).query_db(query, data)
        dojos = []
        dojo_name = results[0]["name"]
        for row_from_db in results:
            dojo = cls(row_from_db)
            ninja_data = {
                "id": row_from_db["ninjas.id"],
                "first_name": row_from_db["first_name"],
                "last_name": row_from_db["last_name"],
                "age": row_from_db["age"],
                "dojo_id": row_from_db["dojo_id"],
                "created_at": row_from_db["ninjas.created_at"],
                "updated_at": row_from_db["ninjas.updated_at"]
            }

            dojo.ninjas = Ninja(ninja_data)
            dojos.append(dojo)
        return (dojos, dojo_name)
