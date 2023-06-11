from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import model_user


class Post:

    DB = 'coding_dojo_wall'

    def __init__(self, data):
        self.id = data['id']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

        self.creator = None

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO posts (content, user_id) \
            VALUES (%(content)s, %(user_id)s);'
        print("sent data", data)
        data = {
            'content': data['content'],
            'user_id': data['user_id']
        }
        print("parsed data", data)
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def get_all_posts_with_creator(cls):
        query = "SELECT * FROM posts JOIN users ON posts.user_id = users.id;"
        results = connectToMySQL(cls.DB).query_db(query)
        all_posts = []
        for row in results:
            one_post = cls(row)
            one_posts_author_info = {
                "id": row['users.id'],
                "first_name": row['first_name'],
                "last_name": row['last_name'],
                "email": row['email'],
                "password": row['password'],
                "created_at": row['users.created_at'],
                "updated_at": row['users.updated_at']
            }
            author = model_user.User(one_posts_author_info)
            one_post.creator = author
            all_posts.append(one_post)
        return all_posts

    @classmethod
    def validate_post(cls, data):
        is_valid = True
        for key in data:
            is_blank = False
            if data[key] == "":
                is_blank = True
        if is_blank:
            flash('*Post content must not be blank', 'post')
            is_valid = False
        return is_valid

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM posts WHERE id = %(id)s;'
        return connectToMySQL(cls.DB).query_db(query, data)
