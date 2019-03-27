from src.com.jalasoft.ShoppingCart.DB.category_query import QueryCategory
from src.com.jalasoft.ShoppingCart.DB.cart_query import CartQuery
from src.com.jalasoft.ShoppingCart.DB.product_query import ProductQuery


class CartModel:
    def __init__(self):
        print("cartModel class")

    def saveProduct(self, product):
        self.qProduct = ProductQuery()
        self.qProduct.insertProduct(product)

    def save_Category(self, category):
        self.qCategory = QueryCategory()
        self.qCategory.insertCategory(category)

    def getAllProduct(self):
        query = ProductQuery()
        return query.loadAllProduct()

    def getAll_products_by_category(self, new_category_id):
        query = ProductQuery()
        return query.loadAllProductByCategory(new_category_id)

    def getAllCategories(self):
        query = QueryCategory()
        return query.loadAllCategories()

    def get_all_detail_of_purchase(self):
        self.qPurchase = CartQuery()
        return self.qPurchase.LoadAllBilling()

    def get_all_detail_of_purchase_by_billing_id(self, billing_id):
        self.qPurchaseByBill = CartQuery()
        return self.qPurchaseByBill.PurchaseDetail(billing_id)

    def addToCart(self, listProduct):
        self.qProduct = CartQuery()
        for row in listProduct:
            self.qProduct.insertCart(row)

# p = CartModel()
# list = [("b4", 1, 12, 2, 4), ("b4", 1, 24, 6, 10)]
#
# p.addToCart(list)


# p = CartModel()
# #
# # list = p.getAllProduct()
# #
# # for i in list:
# #     print(f"name: {i.getProductName()}, price: {i.getProductPrice()}")
# #
# list1 = p.getAllCategories()
# #
# print(list1)