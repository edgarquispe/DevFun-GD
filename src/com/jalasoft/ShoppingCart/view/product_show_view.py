from PyQt5.QtWidgets import QWidget, QFormLayout, QLineEdit, QLabel, QVBoxLayout, QGroupBox, QPushButton, QComboBox, QTableWidget, QTableWidgetItem


class ProductShowView(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.initComponent()

    def initComponent(self):
        vLayout = QVBoxLayout()

        table = QTableWidget(self)
        table.setColumnCount(3)
        table.setHorizontalHeaderLabels(["ID","Product Name","Price"])

        self.addButton = QPushButton("Add to Cart", self)

        vLayout.addWidget(table)
        vLayout.addWidget(self.addButton)

        self.setLayout(vLayout)

