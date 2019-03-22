from PyQt5.QtWidgets import QWidget, QFormLayout, QLineEdit, QLabel, QVBoxLayout, QGroupBox, QPushButton, QComboBox, \
    QMessageBox

from src.com.jalasoft.ShoppingCart.controller.utilities.utilities import Util


class CategoryInsertView(QWidget):
    def __init__(self):
        self._validator = Util()
        super().__init__()
        self.initUI()


    def initUI(self):
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
        self.category_name.setText("")

    def getSaveCategoryButton(self):
        return self.btn_save_category

    def getCategoryName(self):
        return self.category_name.text()

    def display_message_success_after_save_category(self):
        QMessageBox.information(self, 'Success', 'New Category Registered Successfully')