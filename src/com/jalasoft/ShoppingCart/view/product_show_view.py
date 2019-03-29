from PyQt5.QtWidgets import QWidget, QFormLayout, QLineEdit, QLabel, QVBoxLayout, QGroupBox, QPushButton, QComboBox, \
    QTableWidget, QTableWidgetItem, QAbstractItemView, QMessageBox

from src.com.jalasoft.ShoppingCart.DB.category_query import QueryCategory


class ProductShowView(QWidget):
    def __init__(self):
        """
        Constructor donde llamamos al metodo initUI para inicializar los componentes de UI
        """
        super().__init__()
        self.initUI()

    def initUI(self):
        """
        Metodo initUI() que se encarga de inicializar los componentes de UI haciendo referencia
        al metodo iniComponente().
        :return:
        """
        self.initComponent()

    def initComponent(self):
        """
        Metodo initComponent es el encargado de instancias objetos de UI como formulario, grupos, botones, tablas.
        :return:
        """
        vLayout = QVBoxLayout()
        self.category_form = QFormLayout()
        self.category_group = QGroupBox()
        self.chbx_category = QComboBox()
        self.chbx_category.addItem("All", 0)
        query_category = QueryCategory()
        result_category = query_category.loadAllCategories()
        for row in result_category:
            self.chbx_category.addItem(row.getCategoryName(), str(row.getCategoryId()))

        self.category_group.setTitle("Select Category")

        self.category_form.addRow(QLabel("Select Category Product:"), self.chbx_category)
        self.category_group.setLayout(self.category_form)

        self.table = QTableWidget(self)
        self.table.setAlternatingRowColors(True)
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["ID", "Product Name", "Product Details", "Price", "In Stock"])
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)

        self.addButton = QPushButton("Add to Cart", self)

        self.cartTable = QTableWidget(self)
        self.cartTable.setAlternatingRowColors(True)
        self.cartTable.setColumnCount(6)
        self.cartTable.setHorizontalHeaderLabels(["ID", "Product Name", "Product Details", "Price", "Quantity", "Total Price"])

        self.checkoutbutton = QPushButton("CheckOut", self)

        vLayout.addWidget(self.category_group)
        vLayout.addWidget(self.table)
        vLayout.addWidget(self.addButton)
        vLayout.addWidget(self.cartTable)
        vLayout.addWidget(self.checkoutbutton)

        self.setLayout(vLayout)

    def getTable(self):
        """
        este metodo se encarga de retornar la tabla
        :return:
        """
        return self.table

    def getCartTable(self):
        """
        este metodo se encarga de retornar la tabla carro
        :return:
        """
        return self.cartTable

    def getAddTocartButton(self):
        """
        este metodo retorna el boton add
        :return:
        """
        return self.addButton

    def getSaveToPurchaceButton(self):
        """
        este metodo retorna el boton de checkout
        :return:
        """
        return self.checkoutbutton

    def display_message_success(self):
        """
        este metodo es encargado de mostrar un mensaje de success en UI
        :return:
        """
        QMessageBox.information(self, 'Success', 'New Product Registered Successfully in Purchace...')

    def display_message_when_the_cart_list_is_empty(self):
        """
        este metodo es encargado de mostrar un mensaje de informacion en UI
        :return:
        """
        QMessageBox.information(self, 'Information', 'No hay ningun registro para guardar en el Carrito...!!!')

    def display_message_when_quantity_is_grather_that_stock(self):
        """
        este metodo es encargado de mostrar un mensaje de warning en UI
        :return:
        """
        QMessageBox.information(self, 'Warnning', 'La cantidad no puede ser mayor que el Stock...')

    def getCategory_ComboBox(self):
        """
        este metodo retorna el combobox de categoria
        :return:
        """
        return self.chbx_category

    def get_select_current_category_products(self):
        """
        este metodo retorna el category_id actual cuando se selecciona una categoria del checkbox.
        :return:
        """
        category_id = self.chbx_category.itemData(self.chbx_category.currentIndex())
        return category_id

