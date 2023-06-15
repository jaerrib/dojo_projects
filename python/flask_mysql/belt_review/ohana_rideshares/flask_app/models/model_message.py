from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import model_ride
from flask_app.models import model_user


class Message:

    DB = 'rideshares_schema'

    def __init__(self, data):
        self.id = data['id']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.ride_id = data['ride_id']

        self.creator = None

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO messages (content, user_id, ride_id) \
        VALUES(%(content)s, %(user_id)s, %(ride_id)s);'
        data = {'id'}
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def get_all_messages(cls, data):
        query = 'SELECT * FROM messages JOIN users ON messages.user_id = users.id WHERE ride_id = %(ride_id)s'
        data = {'ride_id': data}
        results = connectToMySQL(cls.DB).query_db(query, data)
        all_messages = []
        for row in results:
            one_message = cls(row)
            one_messages_creator_info = {
                "id": row['users.id'],
                "first_name": row['first_name'],
                "last_name": row['last_name'],
                "email": row['email'],
                "password": row['password'],
                "created_at": row['users.created_at'],
                "updated_at": row['users.updated_at']
            }
            creator = model_user.User(one_messages_creator_info)
            one_message.creator = creator
            all_messages.append(one_message)
        return all_messages