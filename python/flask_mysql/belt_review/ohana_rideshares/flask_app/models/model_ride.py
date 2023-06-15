from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import model_user


class Ride:

    DB = 'rideshares_schema'

    def __init__(self, data):
        self.id = data['id']
        self.destination = data['destination']
        self.pickup_location = data['pickup_location']
        self.date = data['date']
        self.details = data['details']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.driver_id = data['driver_id']

        self.creator = None
        self.driver = None
        self.messages = []

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO rides (destination, pickup_location, date, details, user_id) \
        VALUES(%(destination)s, %(pickup_location)s, %(date)s, %(details)s, %(user_id)s);'
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM rides WHERE id = %(id)s;'
        data = {'id': data}
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def validate_ride(cls, data):
        is_valid = True
        for key in data:
            is_blank = False
            if data[key] == "":
                is_blank = True
        if is_blank:
            flash('All fields required', 'ride')
            is_valid = False
        if len(data['destination']) < 3 \
                or len(data['pickup_location']) < 3:
            flash('Destination/pickup location must be > 3 characters', 'ride')
        if len(data['details']) < 10:
            flash('Details must be > 10 characters', 'ride')
            is_valid = False
        return is_valid

    @classmethod
    def get_all_rides_with_creator(cls):
        query = 'SELECT * FROM rides JOIN users ON rides.user_id = users.id;'
        results = connectToMySQL(cls.DB).query_db(query)
        all_rides = []
        for row in results:
            one_ride = cls(row)
            one_rides_creator_info = {
                "id": row['users.id'],
                "first_name": row['first_name'],
                "last_name": row['last_name'],
                "email": row['email'],
                "password": row['password'],
                "created_at": row['users.created_at'],
                "updated_at": row['users.updated_at']
            }
            creator = model_user.User(one_rides_creator_info)
            one_ride.creator = creator
            if one_ride.driver_id != None:
                driver = model_user.User.get_one(one_ride.driver_id)
                one_ride.driver = driver
            all_rides.append(one_ride)
        return all_rides

    @classmethod
    def get_one_ride(cls, data):
        query = "SELECT * FROM rides WHERE id = %(id)s;"
        data = {'id': data}
        result = connectToMySQL(cls.DB).query_db(query, data)
        return cls(result[0])

    @classmethod
    def add_driver(cls, data):
        query = "UPDATE rides \
                SET driver_id=%(driver_id)s\
                WHERE id = %(id)s"
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def remove_driver(cls, data):
        query = "UPDATE rides SET driver_id = NULL \
                WHERE id = %(id)s;"
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def delete_ride(cls, data):
        query = 'DELETE FROM rides WHERE id = %(id)s;'
        data = {'id': data}
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def update_details(cls, data):
        query = "UPDATE rides \
                SET pickup_location=%(pickup_location)s, \
                details=%(details)s\
                WHERE id = %(id)s"
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def validate_changes(cls, data):
        is_valid = True
        for key in data:
            is_blank = False
            if data[key] == "":
                is_blank = True
        if is_blank:
            flash('All fields required', 'update')
            is_valid = False
        if len(data['pickup_location']) < 3:
            flash('Pickup location must be > 3 characters', 'update')
        if len(data['details']) < 10:
            flash('Details must be > 10 characters', 'update')
            is_valid = False
        return is_valid
