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
        self.description = QLineEdit()
        self.price = QLineEdit()
        self.stock = QLineEdit()
        self.category = QLineEdit()

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
