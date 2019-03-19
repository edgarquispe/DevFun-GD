from src.com.jalasoft.test.db.product_query import ProductQuery


class CartModel:
    def __init__(self):
        print("cartModel class")

    def saveProduct(self, product):
        self.qProduct = ProductQuery()
        self.qProduct.insertProduct(product)


    def loadProduct(self):
        self.gProduct = ProductQuery()
        return self.gProduct.loadAllProduct()


