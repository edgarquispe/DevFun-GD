import sys

from PyQt5.QtWidgets import QApplication

from src.com.jalasoft.ShoppingCart.controller.controller import Controller
from src.com.jalasoft.ShoppingCart.model.model import Model
from src.com.jalasoft.ShoppingCart.view.view import View

if __name__ == "__main__":
    app = QApplication(sys.argv)
    view = View()
    model = Model()
    controller = Controller(view, model)
    sys.exit(app.exec_())