from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QTableWidgetItem, QLineEdit

from src.com.jalasoft.ShoppingCart.model.product import Product
from src.com.jalasoft.ShoppingCart.view.product_insert_view import ProductInsertView
from src.com.jalasoft.ShoppingCart.view.product_show_view import ProductShowView
class Controller:

    def __init__(self, mainView, cartModel):
        # mainView.initUI()
        self.mainView = mainView
        self.cartModel = cartModel
        self.mainView.initUI(self)
        self.cartList = []

    def addActionListener(self):
        self.centralWidget = self.mainView.centralWidget()
        if isinstance(self.centralWidget, ProductInsertView):
            self.centralWidget.getSaveProductButton().clicked.connect(lambda: self.saveProduct())
        if isinstance(self.centralWidget, ProductShowView):
            self.centralWidget.getAddTocartButton().clicked.connect(lambda: self.addToCart())

    def saveProduct(self):
        self.centralWidget = self.mainView.centralWidget()
        product_name = self.centralWidget.getProductName()
        description = self.centralWidget.getProductDescription()
        price = self.centralWidget.getPrice()
        stock = self.centralWidget.getProductStock()
        category_id = self.centralWidget.getProductCategory()
        prod = Product()
        prod.setProductName(product_name)
        prod.setProductDescription(description)
        prod.setProductPrice(price)
        prod.setProductStock(stock)
        prod.setProductCategory(category_id)
        self.cartModel.saveProduct(prod)

    def addToCart(self):
        indexes = self.centralWidget.getTable().selectionModel().selectedIndexes()
        id = indexes[0].sibling(indexes[0].row(),indexes[0].column()).data();
        product_name = indexes[1].sibling(indexes[1].row(), indexes[1].column()).data();
        description = indexes[2].sibling(indexes[2].row(), indexes[2].column()).data();
        price = indexes[3].sibling(indexes[3].row(), indexes[3].column()).data();
        stock = indexes[3].sibling(indexes[3].row(), indexes[3].column()).data();
        category_id = indexes[3].sibling(indexes[3].row(), indexes[3].column()).data();

        #create product and add to cart
        pro = Product()
        pro.setProductId(id)
        pro.setProductName(product_name)
        pro.setProductDescription(description)
        pro.setProductPrice(price)
        pro.setProductPrice(stock)
        pro.setProductPrice(category_id)

        self.cartList.append(pro)
        self.loadCartTable()

    def loadCartTable(self):
        listSize = len(self.cartList)
        self.centralWidget.getCartTable().setRowCount(listSize)
        index = 0
        for prod in self.cartList:

            quantity = QLineEdit()
            regex = QRegExp("[0-9_]+")
            validator = QRegExpValidator(regex)
            quantity.setValidator(validator)
            self.centralWidget.getCartTable().setItem(index, 0, QTableWidgetItem(str(prod.getProductId())))
            self.centralWidget.getCartTable().setItem(index, 1, QTableWidgetItem(prod.getProductName()))
            self.centralWidget.getCartTable().setItem(index, 2, QTableWidgetItem(prod.getProductDescription()))
            self.centralWidget.getCartTable().setItem(index, 3, QTableWidgetItem(str(prod.getProductPrice())))

            self.centralWidget.getCartTable().setCellWidget(index, 4, quantity)

            index = index + 1
