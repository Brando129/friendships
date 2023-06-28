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
        self.friends = []

    # Classmethod for saving a new user
    @classmethod
    def save(cls, data):
        print("Saving User...")
        query = """INSERT INTO users (first_name, last_name)
                VALUES (%(first_name)s, %(last_name)s)"""
        return connectToMySQL(db).query_db(query, data)

    # Classmethod for getting all the users from the database
    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM  users;"
        users_list = []
        results = connectToMySQL(db).query_db(query)

        # "user" is a representation of users data
        for user in results:
            users_list.append(cls(user))
        return users_list