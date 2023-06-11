import re
from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'[a-zA-Z]')


class User:

    DB = 'coding_dojo_wall'

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.posts = []

    @classmethod
    def get_by_email(cls, data):
        query = 'SELECT * FROM users WHERE email = %(email)s;'
        result = connectToMySQL(cls.DB).query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        data = {"id": data}
        results = connectToMySQL(cls.DB).query_db(query, data)
        return cls(results[0])

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO users (first_name, last_name, email, password) \
            VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);'
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def validate_login(cls, data):
        is_valid = True
        for key in data:
            is_blank = False
            if data[key] == "":
                is_blank = True
        if is_blank:
            flash('All fields required', 'login')
            is_valid = False
        return is_valid

    @classmethod
    def validate_registration(cls, data):
        is_valid = True
        for key in data:
            is_blank = False
            if data[key] == "":
                is_blank = True
        if is_blank:
            flash('All fields required', 'register')
            is_valid = False
        if not NAME_REGEX.match(data['first_name']):
            flash('First name must be at all letters', 'register')
            is_valid = False
        if not NAME_REGEX.match(data['last_name']):
            flash('Last name must be at all letters', 'register')
            is_valid = False
        if len(data['first_name']) < 2 or \
                len(data['last_name']) < 2:
            flash('First / last names must be at least 2 characters', 'register')
            is_valid = False
        if len(data['password']) < 8:
            flash('Password must be at least 8 characters', 'register')
            is_valid = False
        elif not EMAIL_REGEX.match(data['email']):
            flash('Invalid email address', 'register')
            is_valid = False
        query = 'SELECT * FROM users WHERE email = %(email)s;'
        results = connectToMySQL(cls.DB).query_db(query, data)
        if len(results) != 0:
            flash('This email already exists')
            is_valid = False
        if data['password'] != data['confirm_password']:
            flash('Passwords do not match', 'register')
            is_valid = False
        return is_valid
