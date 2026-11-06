from lib.user import User


class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def create(self, user):
        self._connection.execute(
            "INSERT INTO users (username, password) VALUES (%s, %s)",
            [user.username, user.password],
        )

    def find(self, username):
        rows = self._connection.execute(
            "SELECT * FROM users WHERE username = %s", [username]
        )

        if len(rows) == 0:
            return None
        
        user_details = rows[0]

        return User(
            user_details["username"], user_details["password"], user_details["id"]
        )
