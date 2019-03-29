from PyQt5.QtWidgets import QWidget, QFormLayout, QLineEdit, QLabel, QVBoxLayout, QGroupBox, QPushButton, QComboBox, \
    QTableWidget, QTableWidgetItem, QAbstractItemView, QMessageBox

from src.com.jalasoft.ShoppingCart.DB.category_query import QueryCategory


class PurchaseShowView(QWidget):
    def __init__(self):
        """
        contructor donde llamamos al metodo initUI
        """
        super().__init__()
        self.initUI()

    def initUI(self):
        """
        metodo initUI donde llamamos al metodo initComponent
        :return:
        """
        self.initComponent()

    def initComponent(self):
        """
        Metodo donde inicializamos los componentes de UI de la vista Purchase
        :return:
        """
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
        """
        Metodo que retorna la tabla purchase
        :return:
        """
        return self.purchase_Table

    def display_message_success(self):
        """
        Metodo q muetra un mensaje en la UI de tipo Success
        :return:
        """
        QMessageBox.information(self, 'Success', 'Show Purchase...')