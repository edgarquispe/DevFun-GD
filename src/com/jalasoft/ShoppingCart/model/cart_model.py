from src.com.jalasoft.ShoppingCart.DB.cart_query import CartQuery
from src.com.jalasoft.ShoppingCart.DB.product_query import ProductQuery
from src.com.jalasoft.ShoppingCart.DB.QueryCategories import QueryCategory


class CartModel:
    def __init__(self):
        print("cartModel class")

    def saveProduct(self, product):
        self.qProduct = ProductQuery()
        self.qProduct.insertProduct(product)


    def getAllProduct(self):
        query = ProductQuery()
        return query.loadAllProduct()

    def getAllCategories(self):
        query = QueryCategory()
        return query.select_category()

    def addToCart(self,listProduct):
        self.qProduct = CartQuery()

        for row in listProduct:
            print(row)
            self.qProduct.insertCart(row)




p = CartModel()

list = [("b1",1,2,2,4),("b2",1,2,5,10)]

p.addToCart(list)
# #
# list = p.getAllProduct()
#
# for i in list:
#     print(f"name: {i.getProductName()}, price: {i.getProductPrice()}")
