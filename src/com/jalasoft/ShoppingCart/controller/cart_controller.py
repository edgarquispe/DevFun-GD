from PyQt5.QtWidgets import QApplication

from PyQt5.QtWidgets import QApplication

from src.com.jalasoft.test.model.product import Product
from src.com.jalasoft.test.view.main_view import MainView
from src.com.jalasoft.test.model.cart_model import CartModel
from src.com.jalasoft.test.view.product_insert_view import ProductInsertView


class CartController:

    def __init__(self, mainView, cartModel):
        # mainView.initUI()
        self.view = mainView
        self.model = cartModel
        self.view.initUI(self)
    def addActionListener(self):
        self.centralWidget = self.view.centralWidget()
        if isinstance(self.centralWidget, ProductInsertView):
            self.centralWidget.getSaveProductButton().clicked.connect(lambda: self.saveProduct())

    def saveProduct(self):
        self.centralWidget = self.view.centralWidget()
        name = self.centralWidget.getName()
        price = self.centralWidget.getPrice()
        prod = Product()
        prod.setProductName(name)
        prod.setPrice(price)
        self.model.saveProduct(prod)