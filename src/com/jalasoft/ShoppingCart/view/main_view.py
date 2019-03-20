from PyQt5.QtWidgets import QMainWindow, QMenu, QAction
from src.com.jalasoft.ShoppingCart.view.product_insert_view import ProductInsertView
from src.com.jalasoft.ShoppingCart.view.product_show_view import ProductShowView




class MainView(QMainWindow):

    def __init__(self):
        super().__init__()

    def initUI(self, controller):
        self.__controller = controller
        self.setWindowTitle(".::: Shopping Cart :::.")
        self.resize(1000, 600)

        self.initComponent()
        self.show()

    def initComponent(self):
        menuBar = self.menuBar()
        prodOption = menuBar.addMenu("Register")

        productMenu = QMenu("Product", self)
        prodOption.addMenu(productMenu)

        insertOption = QAction("Insert", self)
        productMenu.addAction(insertOption)
        showOption = QAction("Show", self)
        productMenu.addAction(showOption)

        insertOption.triggered.connect(lambda: self.loadProductInsertView())
        showOption.triggered.connect(lambda: self.loadProductShowView())

    def loadProductInsertView(self):
        self.setCentralWidget(ProductInsertView())
        self.__controller.addActionListener()

    def loadProductShowView(self):
        self.setCentralWidget(ProductShowView())
        self.__controller.loadProduct()
        self.__controller.addActionListener()
