from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QWidget, QFormLayout, QLineEdit, QLabel, QVBoxLayout, QGroupBox, QPushButton


class ProductInsertView(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        vLayout = QVBoxLayout()

        group = QGroupBox()
        form = QFormLayout()
        self.name = QLineEdit()
        regex_name = QRegExp("[a-z-A-Z_]+")
        validator_name = QRegExpValidator(regex_name)
        self.name.setValidator(validator_name)
        self.description = QLineEdit()
        # regex_description = QRegExp("[a-z-A-Z_]+")
        # validator_name = QRegExpValidator(regex_description)
        # self.description.setValidator(validator_name)
        self.price = QLineEdit()
        regex_price = QRegExp("[0-9_]+")
        validator_name = QRegExpValidator(regex_price)
        self.price.setValidator(validator_name)
        self.stock = QLineEdit()
        regex_stock = QRegExp("[0-9_]+")
        validator_name = QRegExpValidator(regex_stock)
        self.stock.setValidator(validator_name)
        self.category = QLineEdit()
        # regex_category = QRegExp("[a-z-A-Z_]+")
        # validator_name = QRegExpValidator(regex_category)
        # self.category.setValidator(validator_name)

        form.addRow(QLabel("Product Name:"), self.name)
        form.addRow(QLabel("Product Description:"), self.description)
        form.addRow(QLabel("Produt Price:"), self.price)
        form.addRow(QLabel("Product Quantity:"), self.stock)
        form.addRow(QLabel("Produt Category:"), self.category)



        group.setLayout(form)

        self.saveButton = QPushButton("Save Product", self)

        vLayout.addWidget(group)
        vLayout.addWidget(self.saveButton)
        self.setLayout(vLayout)

    def getSaveProductButton(self):
        return self.saveButton

    def getProductName(self):
        return self.name.text()

    def getProductDescription(self):
        return self.description.text()

    def getPrice(self):
        return self.price.text()

    def getProductStock(self):
        return self.stock.text()

    def getProductCategory(self):
        return self.category.text()
