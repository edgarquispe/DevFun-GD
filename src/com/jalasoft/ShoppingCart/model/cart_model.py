from src.com.jalasoft.ShoppingCart.DB.category_query import QueryCategory
from src.com.jalasoft.ShoppingCart.DB.cart_query import CartQuery
from src.com.jalasoft.ShoppingCart.DB.product_query import ProductQuery


class CartModel:
    def __init__(self):
        print("cartModel class")

    """este metodo recive un objeto producto desde el controller para almacenarlo in la tabla product de la Base de datos"""
    def saveProduct(self, product):
        self.qProduct = ProductQuery()
        self.qProduct.insertProduct(product)


    """este metodo recive una objeto category desde el controller para inssertarlo en la tabla cateory de la base de datos"""
    def save_Category(self, category):
        self.qCategory = QueryCategory()
        self.qCategory.insertCategory(category)

    """este metodo obtiene todos los items de la tabla product como y lo retornacomo un objeto"""
    def getAllProduct(self):
        query = ProductQuery()
        return query.loadAllProduct()

    """este metodo carga todos los producto de una categoria determinada"""
    def getAll_products_by_category(self, new_category_id):
        query = ProductQuery()
        return query.loadAllProductByCategory(new_category_id)
    """metodo que deuelve todas las categorias de la tabla category """
    def getAllCategories(self):
        query = QueryCategory()
        return query.loadAllCategories()
    """este mtodo devuelve todos las ventas almacenadas en la tabla purchase"""
    def get_all_detail_of_purchase(self):
        self.qPurchase = CartQuery()
        return self.qPurchase.LoadAllBilling()

    """este metod deuelve todos los item de una venta en base al billingId"""
    def get_all_detail_of_purchase_by_billing_id(self, billing_id):
        self.qPurchaseByBill = CartQuery()
        return self.qPurchaseByBill.PurchaseDetail(billing_id)

    """este metodo inserte la lista listProduct que vuene desde el controller en la tabla purchase"""
    def addToCart(self, listProduct):
        self.qProduct = CartQuery()
        for row in listProduct:
            self.qProduct.insertCart(row)

