import sys

from PyQt5.QtWidgets import QApplication

from src.com.jalasoft.ShoppingCart.controller.cart_controller import CartController
from src.com.jalasoft.ShoppingCart.controller.controller import Controller
from src.com.jalasoft.ShoppingCart.model.cart_model import CartModel
from src.com.jalasoft.ShoppingCart.model.model import Model
from src.com.jalasoft.ShoppingCart.view.main_view import MainView
from src.com.jalasoft.ShoppingCart.view.view import View

if __name__ == "__main__":
    """
    Archivo principal donde hacemos la integracion de las capas MVC
    """
    app = QApplication(sys.argv)
    view = MainView()
    model = CartModel()
    controller = CartController(view, model)
    sys.exit(app.exec_())