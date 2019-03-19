from src.com.jalasoft.ShoppingCart.DB.connectionDB import ConnectionDB


class QueryCategory:
    def __init__(self):
        self.conn = ConnectionDB().getConnection()


    """Method to insert Category"""

    def insert_category(self, categoryid, name):
        query = "INSERT INTO categories VALUES (?, ?);"
        cur = self.conn.cursor()
        cur.execute(query, (categoryid, name))
        self.conn.commit()

    """Mehtod that will show all categories"""
    def select_category(self):
        query = "select categoryId, name from categories;"
        cur = self.conn.cursor()
        cur.execute(query)
        data = cur.fetchall()
        return data





# c = QueryCategory()
# c1 = c.select_category()
#
# for row in c1:
#     print(row)