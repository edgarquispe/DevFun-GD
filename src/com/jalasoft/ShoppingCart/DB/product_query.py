from src.com.jalasoft.ShoppingCart.DB.connectionDB import ConnectionDB
from src.com.jalasoft.ShoppingCart.model.product import Product


class ProductQuery:
    def __init__(self):
        self.__conn = ConnectionDB().getConnection()

    """Method to insert a product, it will receive a product object"""
    def insertProduct(self, product):
        cursor = self.__conn.cursor()
        insertQuery = "insert into product(product_name, description, price, stock, category_id) values ('" + product.getProductName() + "','" + product.getProductDescription()+ "', " + str(product.getProductPrice())+ ", " + str(product.getProductStock())+ ", " + str(product.getProductCategory())+ ");"

        cursor.execute(insertQuery)
        self.__conn.commit()

    """This method will load all product and add it to list, this will return a list of objects"""
    def loadAllProduct(self):
        cursor = self.__conn.cursor()
        cursor.execute("select product_id, product_name, description, price, stock from product;")
        rows = cursor.fetchall()

        productList = []
        for row in rows:
            prod = Product()
            prod.setProductId(row[0])
            prod.setProductName(row[1])
            prod.setProductDescription(row[2])
            prod.setProductPrice(row[3])
            prod.setProductStock(row[4])


            productList.append(prod)

        return productList

    """This method will load all product filtered by category and add it to list, this will return a list of objects"""
    def loadAllProductByCategory(self, category_id):
        cursor = self.__conn.cursor()
        cursor.execute("select product_id, product_name, description, price, stock from product where category_id = '"+str(category_id)+"';")
        rows = cursor.fetchall()
        productList = []
        for row in rows:
            prod = Product()
            prod.setProductId(row[0])
            prod.setProductName(row[1])
            prod.setProductDescription(row[2])
            prod.setProductPrice(row[3])
            prod.setProductStock(row[4])

            productList.append(prod)

        return productList

    """Este metodo devuelve la cantidad en stock de un producto"""
    def product_Id(self, product_id):
        cursor = self.__conn.cursor()
        id = cursor.execute("select stock from product where product_id = '" + str(product_id) + "';")
        row = id.fetchone()
        # print(row[0])

        return row[0]

    def product_Name(self, product_name):
        cursor = self.__conn.cursor()
        id = cursor.execute("select product_name from product where product_name = '" + product_name + "';")
        row = id.fetchone()
        # print(row[0])

        return row[0]

#
# p = ProductQuery()
# #
# # list = p.loadAllProduct()
# #
# # for i in list:
# #     print(i.getProductName())
# prodId = p.product_Id(3)
#
#
# print(prodId - 10)

#
# listA = p.loadAllProductByCategory(1)
# for a in listA:
#     print(a.getProductDescription())