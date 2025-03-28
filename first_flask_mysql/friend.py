# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class Friend:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.occupation = data['occupation']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Using a class method to create a friend
    @classmethod
    def save(cls,data):
        query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (%(fname)s, %(lname)s, %(occ)s), NOW(), NOW());"
        return connectToMySQL('first_flask').query_db(query, data)
    
    # update class
    @classmethod
    def update(cls, data):
        query = "UPDATE friends SET first_name = %(first_name)s, last_name = %(last_name)s, occupation = %(occ)s WHERE id = %(id)s;"
        return connectToMySQL('first_flask').query_db(query, data)
    
    # to delete a friend
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM friends WHERE id = %(id)s;"
        data = {"id": friend_id}
        return connectToMySQL("first_flask").query_db(query,data)


    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM friends;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('first_flask').query_db(query)
        # Create an empty list to append our instances of friends
        friends = []
        # Iterate over the db results and create instances of friends with cls.
        for friend in results:
            friends.append(cls(friend))
        return friends