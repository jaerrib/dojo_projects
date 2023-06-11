from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import model_user


class Comment:

    DB = 'coding_dojo_wall'

    def __init__(self, data):
        self.id = data['id']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.post_id = data['post_id']

        self.creator = None

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO comments (content, user_id, post_id) \
            VALUES (%(content)s, %(user_id)s, %(post_id)s);'
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def get_all_comments_with_creator(cls, data):
        query = "SELECT * FROM comments \
            JOIN users ON comments.user_id = users.id \
            WHERE post_id = %(post_id)s;"
        data = {'post_id': data}
        results = connectToMySQL(cls.DB).query_db(query, data)
        all_comments = []
        for row in results:
            one_comment = cls(row)
            one_comments_author_info = {
                "id": row['users.id'],
                "first_name": row['first_name'],
                "last_name": row['last_name'],
                "email": row['email'],
                "password": row['password'],
                "created_at": row['users.created_at'],
                "updated_at": row['users.updated_at']
            }
            author = model_user.User(one_comments_author_info)
            one_comment.creator = author
            all_comments.append(one_comment)
        return all_comments

    @classmethod
    def validate_comment(cls, data):
        is_valid = True
        for key in data:
            is_blank = False
            if data[key] == "":
                is_blank = True
        if is_blank:
            flash('*Post content must not be blank', 'comment')
            is_valid = False
        return is_valid

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM comments WHERE id = %(id)s;'
        return connectToMySQL(cls.DB).query_db(query, data)
