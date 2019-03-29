from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QWidget, QFormLayout, QLineEdit, QLabel, QVBoxLayout, QGroupBox, QPushButton, QComboBox, \
    QMessageBox

from src.com.jalasoft.ShoppingCart.DB.category_query import QueryCategory
from src.com.jalasoft.ShoppingCart.controller.utilities.utilities import Util


class ProductInsertView(QWidget):
    def __init__(self):
        """
        Contructor donde llamamos al metodo initUI e instanciamos un objeto del tipo Util
        para manejo de validaciones
        """
        self._validator = Util()
        super().__init__()
        self.initUI()


    def initUI(self):
        """
        Metodo iniUI que inicializa componentes de UI de la vista Product
        :return:
        """
        vLayout = QVBoxLayout()

        product_group = QGroupBox()
        product_form  = QFormLayout()

        self.product_name = QLineEdit()
        self.product_description = QLineEdit()
        self.product_price = QLineEdit()
        self.product_stock = QLineEdit()
        self.product_category = QComboBox()

        c = QueryCategory()
        c1 = c.loadAllCategories()
        for row in c1:
            self.product_category.addItem(row.getCategoryName(), str(row.getCategoryId()))

        # self.product_category.addItem("Computer", 2)
        # self.product_category.addItem("Game", 3)

        self.btn_save_product = QPushButton("Save Product", self)

        self.product_name.setValidator(self._validator.validate_String())
        self.product_description.setValidator(self._validator.validate_String())
        self.product_price.setValidator(self._validator.validate_Float())
        self.product_stock.setValidator(self._validator.validate_Number())

        product_form.addRow(QLabel("Product Name:"), self.product_name)
        product_form.addRow(QLabel("Product Description:"), self.product_description)
        product_form.addRow(QLabel("Produt Price:"), self.product_price)
        product_form.addRow(QLabel("Product Quantity:"), self.product_stock)
        product_form.addRow(QLabel("Produt Category:"), self.product_category)

        product_group.setLayout(product_form)

        vLayout.addWidget(product_group)
        vLayout.addWidget(self.btn_save_product)

        self.setLayout(vLayout)

    def clear_fields(self):
        """
        Metodo que se encarga de limpiar los componentes de caja de texto QlineEdit
        :return:
        """
        self.product_name.setText("")
        self.product_description.setText("")
        self.product_price.setText("")
        self.product_stock.setText("")
        self.product_category.setCurrentText("Select a Category")

    def getSaveProductButton(self):
        """
        metodo que retorna el boton save_pproducto
        :return:
        """
        return self.btn_save_product

    def getProductName(self):
        """
        Metodo que retorna el texto escrito en la caja de texto de producto_name(QLineEdit) type.
        :return:
        """
        return self.product_name.text()

    def getProductDescription(self):
        """
        Metodo que retorna el texto capturado del componente caja de texto 'product_description'
        :return:
        """
        return self.product_description.text()

    def getPrice(self):
        """
        Metodo que retorna el texto capturado del componete caja de texto 'product_price'
        :return:
        """
        return self.product_price.text()

    def getProductStock(self):
        """
        Metodo que retorna el texto capturado del componente caja de texto 'product_stock'
        :return:
        """
        return self.product_stock.text()

    def getProductCategory(self):
        """
        Metodo que retorna el category_id selecionado del combobox.
        :return:
        """
        category_id = self.product_category.itemData(self.product_category.currentIndex())
        return category_id

    def display_message_success_after_save_product(self):
        """
        Metodo que muestra un mensaje en UI cuando se registra un nuevo producto
        :return:
        """
        QMessageBox.information(self, 'Success', 'New Product Registered Successfully')