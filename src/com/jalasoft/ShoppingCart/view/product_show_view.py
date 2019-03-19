from PyQt5.QtWidgets import QWidget, QFormLayout, QLineEdit, QLabel, QVBoxLayout, QGroupBox, QPushButton, QComboBox, QTableWidget, QTableWidgetItem, QAbstractItemView


class ProductShowView(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.initComponent()

    def initComponent(self):
        vLayout = QVBoxLayout()

        self.table = QTableWidget(self)
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["ID", "Product Name", "Product Details", "Price"])
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)

        self.addButton = QPushButton("Add to Cart", self)
        self.addButton.setFixedWidth(140)

        self.cartTable = QTableWidget(self)
        self.cartTable.setColumnCount(5)
        self.cartTable.setHorizontalHeaderLabels(["ID", "Product Name","Product Details", "Price", "Quantity"])

        vLayout.addWidget(self.table)
        vLayout.addWidget(self.addButton)
        vLayout.addWidget(self.cartTable)

        self.setLayout(vLayout)

    def getTable(self):
        return self.table

    def getCartTable(self):
        return self.cartTable

    def getAddTocartButton(self):
        return self.addButton

