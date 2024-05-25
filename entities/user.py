class User:
    def __init__(self, db_connection,):
        self.db_connection = db_connection

    def create_account(self, username, password, email):
        query = "INSERT INTO users (username, password, email) VALUES (%s, %s, %s)"
        self.db_connection.execute_query(query, (username, password, email))
        self.db_connection.commit()

    def authenticate(self, username, password):
        query = "SELECT id FROM users WHERE username = %s AND password = %s"
        cursor = self.db_connection.execute_query(query, (username, password))
        result = cursor.fetchone()
        if result:
            return True, result[0]  
        else:
            return False, None
    
    