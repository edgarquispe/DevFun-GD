from src.com.jalasoft.ShoppingCart.DB.connectionDB import ConnectionDB
from src.com.jalasoft.ShoppingCart.model.product import Product


class ProductQuery:
    def __init__(self):
        self.__conn = ConnectionDB().getConnection()

    """Method to insert a product, it will receive a product object"""
    def insertProduct(self, product):
        cursor = self.__conn.cursor()
        insertQuery = "insert into product(product_name, description, price, stock, category_id) values ('" + product.getProductName() + "','" + product.getProductDescription()+ "', " + str(product.getProductPrice())+ ", " + str(product.getProductStock())+ ", " + str(product.getProductCategory())+ ");"
        print(insertQuery)
        cursor.execute(insertQuery)
        self.__conn.commit()

    """This method will load all product and add it to list, this will return a list of objects"""
    def loadAllProduct(self):

        cursor = self.__conn.cursor()
        cursor.execute("select product_id, product_name, description, price from product;")
        rows = cursor.fetchall()

        productList = []
        for row in rows:
            prod = Product()
            prod.setProductId(row[0])
            prod.setProductName(row[1])
            prod.setProductDescription(row[2])
            prod.setProductPrice(row[3])


            productList.append(prod)

        return productList

    """This method will load all product filtered by category and add it to list, this will return a list of objects"""
    def loadAllProductByCategory(self, category_id):
        cursor = self.__conn.cursor()
        cursor.execute("select product_id, product_name, description, price from product where category_id = '" + str(category_id) + "';")
        rows = cursor.fetchall()
        productList = []
        for row in rows:
            prod = Product()
            prod.setProductId(row[0])

            prod.setProductName(row[1])
            prod.setProductDescription(row[2])
            prod.setProductPrice(row[3])
            # prod.setProductStock(row[4])
            # prod.setProductCategory(row[5])

            productList.append(prod)

        return productList

    """Method to update a product quantity after a pruchase is executed"""
    def updateItem(self, stock, product_id):
        newstock = stock -1
        query = "update product set stock = " + str(newstock) + " where product_id = ?;"
        cur = self.conn.cursor()
        cur.execute(query, product_id)
        self.conn.commit()

    """Method that can be used to delete a product"""
    def deleteItem(self, product_id):
        query = " delete from product where product_id = ?;"
        cur = self.conn.cursor()
        cur.execute(query,product_id)
        self.conn.commit()



# p = ProductQuery()
#
# # list = p.loadAllProduct()
# #
# # for i in list:
# #     print(i.getProductName())
#
#
# listA = p.loadAllProductByCategory(1)
# for a in listA:
#     print(a.getProductDescription())