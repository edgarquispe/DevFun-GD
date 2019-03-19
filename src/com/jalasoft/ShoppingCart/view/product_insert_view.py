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
        self.price = QLineEdit()
        form.addRow(QLabel("Product Name:"), self.name)
        form.addRow(QLabel("Produt Price:"), self.price)
        group.setLayout(form)

        self.saveButton = QPushButton("Save Product", self)

        vLayout.addWidget(group)
        vLayout.addWidget(self.saveButton)
        self.setLayout(vLayout)

    def getSaveProductButton(self):
        return self.saveButton

    def getName(self):
        return self.name.text()

    def getPrice(self):
        return self.price.text()
