# from src.com.jalasoft.ShoppingCart.DB.connectDB import ConnectionDB
#
#
# class QueryProduct:
#     def __init__(self):
#         self.conn = ConnectionDB().getConnection()
#
#     """Method to insert Item"""
#
#     def insert_item(self, itemname, description, price, stock, categoryId):
#         query = "INSERT INTO items VALUES (?, ?, ?, ?, ?, ?);"
#         cur = self.conn.cursor()
#         cur.execute(query, (None, itemname, description, price, stock, categoryId))
#         self.conn.commit()
#
#
#     """Mehtod that will show all items by a selected category"""
#
#     def select_items(self, categoryid):
#         query = "select itemname, description, price, stock from items where categoryid = ?;"
#         cur = self.conn.cursor()
#         cur.execute(query, categoryid)
#         data = cur.fetchall()
#         return data
#
#     """Method that will return the price of a selected item"""
#     def select_item_price(self, itemid):
#         query = "select price from items where itemid = ?;"
#         cur = self.conn.cursor()
#         cur.execute(query, itemid)
#         data = cur.fetchall()
#         return data
#
#
#     """Method that can be used to update the quantity that we have in stock of the selected product afert a checkout is done"""
#     def updateItem(self, stock, itemid):
#         newstock = stock -1
#         query = "update items set stock = " + str(newstock) + " where itemid = ?;"
#         cur = self.conn.cursor()
#         cur.execute(query, itemid)
#         self.conn.commit()
#
#     """Method that can be used to delete a item"""
#     def deleteItem(self, itemid):
#         query = " delete from items where itemid = ?;"
#         cur = self.conn.cursor()
#         cur.execute(query,itemid)
#         self.conn.commit()
#
#
# q = QueryProduct()
# # q.insertProduct(5, "test")
# # print(q.select_item_price(str(7)))
# q.insert_item('T-Shirt2', 'description T-Shirt2', 3, 15, 2)
# # print(q.deleteItem(str(8)))
from src.com.jalasoft.ShoppingCart.DB.connectionDB import ConnectionDB


class ProductQuery:
    def __init__(self):
        self.__conn = ConnectionDB().getConnection()

    def insertProduct(self, product):
        cursor = self.__conn.cursor()
        insertQuery = "insert into product(name, price) values ('" + product.getProductName() + "', " + str(product.getPrice())+ ");"
        print(insertQuery)
        cursor.execute(insertQuery)
        self.__conn.commit()

    def loadAllProduct(self):
        cursor = self.__conn.cursor()
        cursor.execute("select ID, name, price from product;")
        rows = cursor.fetchall()
        productList = []
        for row in rows:
            prod = Product()
            prod.setID(row[0])
            prod.setProductName(row[1])
            prod.setPrice(row[2])
            productList.append(prod)

        return productList