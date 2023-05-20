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
        SELECT ninjas.id as id,
        first_name,
        last_name,
        age,
        ninjas.created_at as created_at,
        ninjas.updated_at as updated_at,
        ninjas.dojo_id as dojo_id,
        name as dojo_name
        FROM dojos
        LEFT JOIN ninjas
        ON ninjas.dojo_id = dojos.id
        WHERE dojos.id = %(id)s;
        """

        results = connectToMySQL(cls.DB).query_db(query, data)
        all_members = []
        dojo_name = results[0]["dojo_name"]
        for row_from_db in results:
            dojo_member = cls(row_from_db)
            ninja_data = {
                "id": row_from_db["id"],
                "first_name": row_from_db["first_name"],
                "last_name": row_from_db["last_name"],
                "age": row_from_db["age"],
                "dojo_id": row_from_db["dojo_id"],
                "created_at": row_from_db["created_at"],
                "updated_at": row_from_db["updated_at"]
            }
            dojo_member.ninjas = Ninja(ninja_data)
            all_members.append(dojo_member)
        return (all_members, dojo_name)

    @classmethod
    def get_one(cls, ninja_id):
        query = "SELECT * FROM ninjas WHERE id = %(id)s;"
        data = {"id": ninja_id}
        results = connectToMySQL(cls.DB).query_db(query, data)
        return cls(results[0])

    @classmethod
    def update(cls, data):
        query = """UPDATE ninjas
        SET first_name=%(first_name)s, last_name=%(last_name)s, age=%(age)s, dojo_id=%(dojo_id)s
        WHERE id = %(id)s;"""
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def delete(cls, ninja_id):
        query = "DELETE FROM ninjas WHERE id = %(id)s;"
        data = {"id": ninja_id}
        return connectToMySQL(cls.DB).query_db(query, data)
