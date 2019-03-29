from PyQt5.QtWidgets import QWidget, QFormLayout, QLineEdit, QLabel, QVBoxLayout, QGroupBox, QPushButton, QComboBox, \
    QMessageBox

from src.com.jalasoft.ShoppingCart.controller.utilities.utilities import Util


class CategoryInsertView(QWidget):
    def __init__(self):
        """
        Constructor que inicializa un Validador y llama el metodo initUI
        """
        self._validator = Util()
        super().__init__()
        self.initUI()


    def initUI(self):
        """
        Metodo que inicializa componentes de UI
        :return:
        """
        vLayout = QVBoxLayout()

        category_group = QGroupBox()
        category_form  = QFormLayout()

        self.category_name = QLineEdit()
        self.btn_save_category = QPushButton("Save Category", self)

        self.category_name.setValidator(self._validator.validate_String())

        category_form.addRow(QLabel("Category Name:"), self.category_name)
        category_group.setLayout(category_form)

        vLayout.addWidget(category_group)
        vLayout.addWidget(self.btn_save_category)

        self.setLayout(vLayout)

    def clear_fields(self):
        """
        Metodo que se encarga de limpiar el componente de UI de tipo QLineEdit
        :return:
        """
        self.category_name.setText("")

    def getSaveCategoryButton(self):
        """
        Metodo que retorna el boton save_category
        :return:
        """
        return self.btn_save_category

    def getCategoryName(self):
        """
        Metodo que retorna el texto capturado de la caja de texto category_name
        :return:
        """
        return self.category_name.text()

    def display_message_success_after_save_category(self):
        """
        Metodo que se encarga de mostrar un mensaje UI de tipo Success cuando se registra una nueva categoria.
        :return:
        """
        QMessageBox.information(self, 'Success', 'New Category Registered Successfully')