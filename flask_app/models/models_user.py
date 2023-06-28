from flask_app.config.mysqlconnection import connectToMySQL

# Database name
db = "friendships_schema"

# User class
class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # Classmethod for saving a new user
    @classmethod
    def save(cls, data):
        query = """INSERT INTO users (first_name, last_name)
                VALUES (%(first_name)s, %(last_name)s)"""
        return connectToMySQL(db).query_db(query, data)