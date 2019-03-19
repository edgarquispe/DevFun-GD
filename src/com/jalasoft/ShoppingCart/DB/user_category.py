from src.com.jalasoft.ShoppingCart.DB.connectionDB import ConnectionDB


class QueryUser:
    def __init__(self):
        self.conn = ConnectionDB().getConnection()


    """Method to insert User"""

    def insert_user(self, username , password ,email , firstname , lastname, phonenumber):
        query = "INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?);"
        cur = self.conn.cursor()
        cur.execute(query, (None, username, password , email , firstname , lastname, phonenumber))
        self.conn.commit()

    """Mehtod that will show user data"""
    def select_user(self, userid):
        query = "select userid, username , password ,email , firstname , lastname, phonenumber from users where userid = ?;"
        cur = self.conn.cursor()
        cur.execute(query, userid)
        data = cur.fetchall()
        return data


# c = QueryUser()
#
# c.insert_user('mfuentesa', 'control123', 'mfuentes@test.com', 'Magali', 'Fuentes', 67556677)
# c1 = c.select_user(str(2))
#
# for row in c1:
#     print(row)