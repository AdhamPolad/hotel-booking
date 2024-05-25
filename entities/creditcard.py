class CreditCard:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def validate_credit_card(self, card_number, expiration, cvc, holder):
        query = "SELECT holder FROM credit_cards WHERE number = %s AND expiration = %s AND cvc = %s"
        cursor = self.db_connection.execute_query(query, (card_number, expiration, cvc))
        result = cursor.fetchone()
        if result:
            return True, result[0]  
        else:
            # If the card is not in the database, insert it
            query = "INSERT INTO credit_cards (number, expiration, cvc, holder) VALUES (%s, %s, %s, %s)"
            self.db_connection.execute_query(query, (card_number, expiration, cvc, holder))
            self.db_connection.commit()
            return True, holder  