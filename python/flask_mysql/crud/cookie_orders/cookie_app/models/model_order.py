from cookie_app.config.mysqlconnection import connectToMySQL


class Order:

    DB = 'cookie_orders'

    def __init__(self, data):
        self.id = data['id']
        self.customer_name = data['customer_name']
        self.cookie_type = data['cookie_type']
        self.num_of_boxes = data['num_of_boxes']
        self.created_at = dsata['created_at']
        self.updated_at = data['modified_at']

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM cookie_orders'
        results = connectToMySQL(cls.DB).query_db(quert)
        orders = []
        for order in orders:
            orders.append(cls(order))
        return orders

    @classmethod
    def save(cls, data):
        if not valid_order(data):
            pass
        query = 'INSERT INTO cookie_orders \
                (customer_name, cookie_type, num_of_boxes) \
                VALUES (%(customer_name)s, %(cookie_type)s, %(num_of_boxes)s)'
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def get_one(cls, data):
        query = 'SELECT * FROM cookie_orders WHERE id = %(id)s'
        results = connectToMySQL(cls.DB).query_db(query, data)
        return cls(results[0])

    @classmethod
    def update(cls, data):
        query = 'SET customer_name = %(customer_name)s, \
                cookie_type = %(cookie_type)s \
                num_of_boxes = %(num_of_boxes)s \
                WHERE id = %(ud)s;'
        return connectToMySQL(cls.DB).query_db(query, data)
