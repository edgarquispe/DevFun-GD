import os

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QMenu, QAction, QStatusBar, QToolBar

from src.com.jalasoft.ShoppingCart.view.category_insert_view import CategoryInsertView
from src.com.jalasoft.ShoppingCart.view.product_insert_view import ProductInsertView
from src.com.jalasoft.ShoppingCart.view.product_show_purchase import PurchaseShowView
from src.com.jalasoft.ShoppingCart.view.product_show_view import ProductShowView
from src.com.jalasoft.ShoppingCart.view.style import StyleApp


class MainView(QMainWindow):

    def __init__(self):
        super().__init__()
        self._style = StyleApp()

    def initUI(self, controller):
        self.__controller = controller
        self.setWindowTitle(".::: Shopping Cart :::.")
        self.setWindowIcon(QIcon("view/imgs/shoppingcart.png"))
        self.setStyleSheet(self._style.get_style_app())
        self.setAutoFillBackground(True)
        self.resize(1000, 600)

        self.initComponent()
        self.show()

    def initComponent(self):
        self.add_menu()
        menuBar = self.menuBar()
        prodOption = menuBar.addMenu("Register")
        prodReportPurchase = menuBar.addMenu("Reports")

        productMenu  = QMenu("Product", self)
        categoryMenu = QMenu("Category", self)
        purchaseMenu = QMenu("Purchase", self)

        prodOption.addMenu(productMenu)
        prodOption.addMenu(categoryMenu)
        prodReportPurchase.addMenu(purchaseMenu)

        insertOption = QAction("Insert Product", self)
        showOption = QAction("Show Product", self)
        insertCategoryOption = QAction("Insert Category", self)
        detail_purchaseOption = QAction("Detail Purchase", self)

        productMenu.addAction(insertOption)
        productMenu.addAction(showOption)
        categoryMenu.addAction(insertCategoryOption)
        purchaseMenu.addAction(detail_purchaseOption)

        insertOption.triggered.connect(lambda: self.loadProductInsertView())
        showOption.triggered.connect(lambda: self.loadProductShowView())
        insertCategoryOption.triggered.connect(lambda: self.loadProductInsertCategoryView())
        detail_purchaseOption.triggered.connect(lambda: self.loadPurchaseDetail())

    def add_menu(self):
        statusBar = QStatusBar()
        self.setStatusBar(statusBar)
        toolbar = QToolBar("ShoppingCart")
        toolbar.setIconSize(QSize(64, 64))

        self.addToolBar(toolbar)
        product_menu = self.menuBar().addMenu("&Product")

        product_item_action = QAction(QIcon("view/imgs/store.png"), "Insert new Products", self)
        product_item_action.setStatusTip("View of Products...")
        product_item_action.triggered.connect(self.loadProductInsertView)
        product_menu.addAction(product_item_action)

        category_item_action = QAction(QIcon("view/imgs/store.png"), "Insert new Category", self)
        category_item_action.setStatusTip("View of Categorys...")
        category_item_action.triggered.connect(self.loadProductInsertCategoryView)
        product_menu.addAction(category_item_action)

        cart_item_action = QAction(QIcon("view/imgs/cart.png"), "View Cart", self)
        cart_item_action.setStatusTip("View Products of Cart...")
        cart_item_action.triggered.connect(self.loadProductShowView)

        sale_item_action = QAction(QIcon("view/imgs/wallet.png"), "View Sale", self)
        sale_item_action.setStatusTip("View details Sale...")
        sale_item_action.triggered.connect(self.loadPurchaseDetail)

        exit_item_action = QAction(QIcon("view/imgs/exit.png"), "Exit App..", self)
        exit_item_action.setStatusTip("Exit of Shopping Cart App...")
        exit_item_action.triggered.connect(self.exit_app)

        toolbar.addAction(product_item_action)
        toolbar.addAction(cart_item_action)
        toolbar.addAction(sale_item_action)
        toolbar.addAction(exit_item_action)

    def exit_app(self):
        self.close()
        print("Exit App...!!!")

    def loadProductInsertView(self):
        self.setCentralWidget(ProductInsertView())
        self.__controller.addActionListener()

    def loadProductShowView(self):
        self.setCentralWidget(ProductShowView())
        self.__controller.loadProduct()
        self.__controller.addActionListener()
        self.__controller.clean_cart_table()

    def loadProductInsertCategoryView(self):
        self.setCentralWidget(CategoryInsertView())
        self.__controller.addActionListener()

    def loadPurchaseDetail(self):
        self.setCentralWidget(PurchaseShowView())
        self.__controller.loadPurchase()
        self.__controller.addActionListener()
