import re
from flask import flash
from users_app.config.mysqlconnection import connectToMySQL

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class User:
    DB = 'users_schema'

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def validate_user(cls, user):
        is_valid = True
        if len(user['first_name']) < 1:
            flash("First name must not be blank")
            is_valid = False
        if len(user['last_name']) < 1:
            flash("Last name must not be blank")
            is_valid = False
        if len(user['email']) < 1:
            flash("Email must not be blank")
            is_valid = False
        elif not EMAIL_REGEX.match(user['email']):
            flash("Invalid email address!")
            is_valid = False
        connection = connectToMySQL(cls.DB)
        query = "SELECT * FROM users WHERE email = %(email)s"
        results = connection.query_db(query, user)
        if len(results) != 0:
            flash('This email already exists')
            is_valid = False
        return is_valid

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.DB).query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users ( first_name , last_name , email ) \
            VALUES ( %(first_name)s , %(last_name)s , %(email)s);"
        return connectToMySQL('users_schema').query_db(query, data)

    @classmethod
    def get_one(cls, user_id):
        query = "SELECT * FROM users WHERE id = %(id)s"
        data = {'id': user_id}
        results = connectToMySQL(cls.DB).query_db(query, data)
        return cls(results[0])

    @classmethod
    def update(cls, data):
        query = """UPDATE users
                SET first_name=%(first_name)s,last_name=%(last_name)s,email=%(email)s
                WHERE id = %(id)s;"""
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def delete(cls, user_id):
        query = "DELETE FROM users WHERE id = %(id)s;"
        data = {"id": user_id}
        return connectToMySQL(cls.DB).query_db(query, data)
