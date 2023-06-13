from flask import Flask
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import model_user


class Recipe:

    DB = 'recipes'

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_made = data['date_made']
        self.under_30 = data['under_30']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

        self.creator = None

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO recipes (name, description, instructions, date_made, under_30, user_id) \
            VALUES (%(name)s, %(description)s, %(instructions)s, %(date_made)s, %(under_30)s, %(user_id)s);'
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def get_all_recipes_with_creator(cls):
        query = "SELECT * FROM recipes JOIN users ON recipes.user_id = users.id;"
        results = connectToMySQL(cls.DB).query_db(query)
        all_recipes = []
        for row in results:
            one_recipe = cls(row)
            one_recipes_author_info = {
                "id": row['users.id'],
                "first_name": row['first_name'],
                "last_name": row['last_name'],
                "email": row['email'],
                "password": row['password'],
                "created_at": row['users.created_at'],
                "updated_at": row['users.updated_at']
            }
            author = model_user.User(one_recipes_author_info)
            one_recipe.creator = author
            all_recipes.append(one_recipe)
        return all_recipes

    @classmethod
    def get_one_recipe_with_creator(cls, id):
        query = "SELECT * FROM recipes WHERE recipes.id = %(id)s;"
        data = {'id': id}
        result = connectToMySQL(cls.DB).query_db(query, data)
        return cls(result[0])


    @classmethod
    def validate_recipe(cls, data):
        is_valid = True
        for key in data:
            is_blank = False
            if data[key] == "":
                is_blank = True
        if is_blank:
            flash('All fields required', 'recipe')
            is_valid = False
        if len(data['name']) < 3 \
                or len(data['description']) < 3 \
                or len(data['instructions']) < 3:
            flash('Name/description/instructions must be > 3 characters', 'recipe')
            is_valid = False
        return is_valid

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM recipes WHERE id = %(id)s;'
        data = {'id': data}
        return connectToMySQL(cls.DB).query_db(query, data)
