from PyQt5.QtWidgets import QMainWindow, QMenu, QAction

from src.com.jalasoft.ShoppingCart.view.category_insert_view import CategoryInsertView
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

        productMenu  = QMenu("Product", self)
        categoryMenu = QMenu("Category", self)

        prodOption.addMenu(productMenu)
        prodOption.addMenu(categoryMenu)

        insertOption = QAction("Insert Product", self)
        showOption = QAction("Show Product", self)
        insertCategoryOption = QAction("Insert Category", self)

        productMenu.addAction(insertOption)
        productMenu.addAction(showOption)
        categoryMenu.addAction(insertCategoryOption)

        insertOption.triggered.connect(lambda: self.loadProductInsertView())
        showOption.triggered.connect(lambda: self.loadProductShowView())
        insertCategoryOption.triggered.connect(lambda: self.loadProductInsertCategoryView())

    def loadProductInsertView(self):
        self.setCentralWidget(ProductInsertView())
        self.__controller.addActionListener()

    def loadProductShowView(self):
        self.setCentralWidget(ProductShowView())
        self.__controller.loadProduct()
        self.__controller.addActionListener()

    def loadProductInsertCategoryView(self):
        self.setCentralWidget(CategoryInsertView())
        self.__controller.addActionListener()