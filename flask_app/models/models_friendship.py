from flask_app.config.mysqlconnection import connectToMySQL

# Database name
db = "friendships_schema"

# Friendship class
class Friendship:
    def __init__(self, data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.friend_id = data['friend_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.friendships = []

    # Classmethod for saving a friendship
    @classmethod
    def save_friendship(cls, data):
        print("Saving friendship...")
        query = """INSERT INTO friendships (user_id, friend_id)
                VALUES (%(user_id)s, %(friend_id)s)"""
        return connectToMySQL(db).query_db(query, data)

    # Classmethod for getting all the friendships from the database
    @classmethod
    def get_all_friendships(cls):
        print("Getting all the friendships...")
        query = "SELECT * FROM  friendships;"
        friends_list = []
        results = connectToMySQL(db).query_db(query)

        # "friend" is a representation of friendships data
        for friend in results:
            friends_list.append(cls(friend))
        return friends_list

    # classmethod that gets a friendship
    # @classmethod
    # def get_by_id(cls, data):
    #     query = """SELECT * FROM users LEFT JOIN friendships ON users.id = friendships.user_id
    #             WHERE users.id = %(id)s;"""
    #     results = connectToMySQL(db).query_db(query, data)
    #     # Makes friendship into its own instance of the class
    #     friendship = cls(results[0])
    #     # Goes through all the results and gets the data
    #     for row in results:
    #         if row['users.id'] == None:
    #             break
    #         data = {
    #             "id": row['users.id'],
    #             "first_name": row['first_name'],
    #             "lasst_name": row['last_name']
    #         }
    #         friendship.friendships.append(Friendship(data))
    #     return friendship