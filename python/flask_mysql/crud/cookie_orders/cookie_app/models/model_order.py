from flask import flash
from cookie_app.config.mysqlconnection import connectToMySQL


class Order:

    DB = 'cookie_orders'

    def __init__(self, data):
        self.id = data['id']
        self.customer_name = data['customer_name']
        self.cookie_type = data['cookie_type']
        self.num_of_boxes = data['num_of_boxes']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM orders'
        results = connectToMySQL(cls.DB).query_db(query)
        orders = []
        for order in results:
            orders.append(cls(order))
        return orders

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO orders \
                (customer_name, cookie_type, num_of_boxes) \
                VALUES (%(customer_name)s, %(cookie_type)s, %(num_of_boxes)s)'
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def get_one(cls, data):
        query = 'SELECT * FROM orders WHERE id = %(id)s'
        data = {'id': data}
        results = connectToMySQL(cls.DB).query_db(query, data)
        return cls(results[0])

    @classmethod
    def update(cls, data):
        query = 'UPDATE orders \
                SET customer_name = %(customer_name)s, \
                cookie_type = %(cookie_type)s, \
                num_of_boxes = %(num_of_boxes)s  \
                WHERE id = %(id)s;'
        return connectToMySQL(cls.DB).query_db(query, data)

    @staticmethod
    def is_valid_order(data):
        is_valid = True
        if data['customer_name'] == "" or \
           data['cookie_type'] == "" or \
                len(data['num_of_boxes']) < 1:
            flash('All fields required')
            is_valid = False
        if len(data['customer_name']) < 2:
            flash('Name must be at least 2 characters')
            is_valid = False
        if len(data['cookie_type']) < 2:
            flash('Cookie type must be at least 2 characters')
            is_valid = False
        print(is_valid)
        return is_valid

