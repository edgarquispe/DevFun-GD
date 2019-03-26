from PyQt5.QtWidgets import QWidget, QFormLayout, QLineEdit, QLabel, QVBoxLayout, QGroupBox, QPushButton, QComboBox, \
    QTableWidget, QTableWidgetItem, QAbstractItemView, QMessageBox

from src.com.jalasoft.ShoppingCart.DB.category_query import QueryCategory


class PurchaseShowView(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.initComponent()

    def initComponent(self):
        vLayout = QVBoxLayout()
        self.purchase_vLayout = QVBoxLayout()
        self.purchase_group = QGroupBox()

        self.purchase_group.setTitle("Show Purchase")

        self.purchase_Table = QTableWidget(self)
        self.purchase_Table.setAlternatingRowColors(True)
        self.purchase_Table.setColumnCount(2)
        self.purchase_Table.setHorizontalHeaderLabels(["Billing", "Action"])

        #self.purchase_vLayout.addWidget(self.purchase_Table)
        #self.category_group.setLayout(self.purchase_vLayout)

        vLayout.addWidget(QLabel(".::: Detalle de Ventas :::."))
        vLayout.addWidget(self.purchase_Table)

        self.setLayout(vLayout)

    def get_purchase_Table(self):
        return self.purchase_Table

    def display_message_success(self):
        QMessageBox.information(self, 'Success', 'Show Purchase...')