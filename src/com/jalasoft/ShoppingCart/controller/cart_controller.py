import random

from PyQt5.QtWidgets import QTableWidgetItem, QLineEdit, QMessageBox, QPushButton, QDialog, QLabel, QVBoxLayout, \
    QTableWidget

from src.com.jalasoft.ShoppingCart.controller.utilities.utilities import Util
from src.com.jalasoft.ShoppingCart.model.category import Category
from src.com.jalasoft.ShoppingCart.model.product import Product
from src.com.jalasoft.ShoppingCart.model.purchase import Purchase
from src.com.jalasoft.ShoppingCart.view.category_insert_view import CategoryInsertView
from src.com.jalasoft.ShoppingCart.view.product_insert_view import ProductInsertView
from src.com.jalasoft.ShoppingCart.view.product_show_view import ProductShowView
from src.com.jalasoft.ShoppingCart.view.style import StyleApp


class CartController:



    def __init__(self, mainView, cartModel):
        """
        Constructor that recieve View, Model objects and assigs to a variables, also calls to initUI method to
        initialize his components. Also initialize a cart list to purcharse , creates a Util object.
        """
        # mainView.initUI()
        self.mainView = mainView
        self.cartModel = cartModel
        self.mainView.initUI(self)
        self.cartList = []
        self.cart_list_to_purchase = []
        self._validator = Util()
        self._index = 0
        self._billing_id_sale = self.generate_billing_id()


    def generate_billing_id(self):
        return "BILL"+random.choice("1234567890")


    def addActionListener(self):
        """
        Methods that manage all the events according every Widget call
        """
        self.centralWidget = self.mainView.centralWidget()
        if isinstance(self.centralWidget, ProductInsertView):
            self.centralWidget.getSaveProductButton().clicked.connect(lambda: self.saveProduct())
            self.centralWidget.getSaveProductButton().clicked.connect(lambda: self.clean_the_form_fields())
        if isinstance(self.centralWidget, ProductShowView):
            self.centralWidget.getAddTocartButton().clicked.connect(lambda: self.addToCart())
        if isinstance(self.centralWidget, ProductShowView):
            self.centralWidget.getSaveToPurchaceButton().clicked.connect(lambda: self.addProducts_to_Cart())
        if isinstance(self.centralWidget, ProductShowView):
            self.centralWidget.getCategory_ComboBox().currentIndexChanged.connect(lambda: self.loadProduct())
        if isinstance(self.centralWidget, CategoryInsertView):
            self.centralWidget.getSaveCategoryButton().clicked.connect(lambda: self.save_Category_in_db())
            self.centralWidget.getSaveCategoryButton().clicked.connect(lambda: self.clean_the_form_fields())


    def clean_the_form_fields(self):

        """
        Method that clean all the form fields
        """
        self.centralWidget = self.mainView.centralWidget()
        self.centralWidget.clear_fields()

    def saveProduct(self):
        """
        Method to save the product
        """

        # self.clean_cart_table()
        self.centralWidget = self.mainView.centralWidget()
        product_name = self.centralWidget.getProductName()
        description = self.centralWidget.getProductDescription()
        price = self.centralWidget.getPrice()
        stock = self.centralWidget.getProductStock()
        category_id = self.centralWidget.getProductCategory()


        prod = Product()
        prod.setProductName(product_name)
        prod.setProductDescription(description)
        prod.setProductPrice(price)
        prod.setProductStock(stock)
        prod.setProductCategory(category_id)
        self.cartModel.saveProduct(prod)

        self.centralWidget.display_message_success_after_save_product()

    def save_Category_in_db(self):
        """
        Method to save all Categories in DB
        """
        self.centralWidget = self.mainView.centralWidget()
        category_name = self.centralWidget.getCategoryName()

        category = Category()
        category.setCategoryName(category_name)
        self.cartModel.save_Category(category)
        self.centralWidget.display_message_success_after_save_category()

    def loadPurchase(self):
        """
        Method to load all the purchase made
        """
        self.centralWidget = self.mainView.centralWidget()
        listPurchase = self.cartModel.get_all_detail_of_purchase()
        listSize = len(listPurchase)

        self.centralWidget.get_purchase_Table().setRowCount(listSize)
        index = 0
        for purchase_item in listPurchase:
            self.btn_show_purchase_detail = QPushButton("View Detail")
            self.centralWidget.get_purchase_Table().setItem(index, 0, QTableWidgetItem(str(purchase_item.getBillId())))
            self.centralWidget.get_purchase_Table().setCellWidget(index, 1, self.btn_show_purchase_detail)
            self.btn_show_purchase_detail.clicked.connect(lambda: self.show_detail_purchase_by_billing())
            index = index + 1

    def buttonclicked(self):
        print(self.btn_show_purchase_detail.parent())

        """
        Method that maange the purchase detail 
        """


    def show_detail_purchase_by_billing(self):

        """
        Method that shows the detail of the purchase according the billing
        """
        print("Show detail purchase by billing....!!")
        self._style = StyleApp()
        self.ui_report_purchase = QDialog()
        self.ui_report_purchase.setWindowTitle(".::: Show Detail Purchase :::.")
        self.ui_report_purchase.setStyleSheet(self._style.get_style_app())
        self.ui_report_purchase.resize(500, 300)
        self.vLayout_to_report = QVBoxLayout()

        purchase_index = self.centralWidget.get_purchase_Table().currentRow()
        billing_id = self.centralWidget.get_purchase_Table().item(purchase_index, 0).text()

        lb_title = QLabel("...::: Shopping Cart :::...")
        lb_billing_id = QLabel("Billing: "+billing_id+"\n________________________________")
        btn_report = QPushButton("Print Report Purchase")

        list_purchase_detail = self.cartModel.get_all_detail_of_purchase_by_billing_id(billing_id)

        index = 0
        self.vLayout_to_report.addWidget(lb_title)
        self.vLayout_to_report.addWidget(lb_billing_id)
        suma = 0
        for item in list_purchase_detail:
            detail_purchase_string = str(item.getProdName())+" -- "+str(item.getProdPrice())+" -- "+str(item.getProdQuantity())
            suma = suma + int(item.getProdQuantity())
            print(detail_purchase_string)
            self.vLayout_to_report.addWidget(QLabel(detail_purchase_string))
            index = index + 1

        self.vLayout_to_report.addWidget(QLabel("_________________________________\nTotal: "+str(suma)))
        self.vLayout_to_report.addWidget(btn_report)

        self.ui_report_purchase.setLayout(self.vLayout_to_report)
        self.ui_report_purchase.show()


    def loadProduct(self):
        """
        Method to load products
        """
        self.centralWidget = self.mainView.centralWidget()

        category_flag = self.centralWidget.get_select_current_category_products()
        print(category_flag)
        if int(category_flag) == 0:
            listProduct = self.cartModel.getAllProduct()
        else:
            listProduct = self.cartModel.getAll_products_by_category(category_flag)

        listSize = len(listProduct)

        self.centralWidget.getTable().setRowCount(listSize)
        index = 0
        for prod in listProduct:
            self.centralWidget.getTable().setItem(index, 0, QTableWidgetItem(str(prod.getProductId())))
            self.centralWidget.getTable().setItem(index, 1, QTableWidgetItem(prod.getProductName()))
            self.centralWidget.getTable().setItem(index, 2, QTableWidgetItem(prod.getProductDescription()))
            self.centralWidget.getTable().setItem(index, 3, QTableWidgetItem(str(prod.getProductPrice())))
            self.centralWidget.getTable().setItem(index, 4, QTableWidgetItem(str(prod.getProductStock())))
            index = index + 1


    def addToCart(self):
        """
        Method to add the items to the cart
        """
        indexes = self.centralWidget.getTable().selectionModel().selectedIndexes()
        id = indexes[0].sibling(indexes[0].row(), indexes[0].column()).data();

        if not self.__isProductInList(id):
            name = indexes[1].sibling(indexes[1].row(), indexes[1].column()).data();
            description = indexes[2].sibling(indexes[2].row(), indexes[2].column()).data();
            price = indexes[3].sibling(indexes[3].row(), indexes[3].column()).data();
            stock = indexes[4].sibling(indexes[4].row(), indexes[4].column()).data();

            # create product and add to cart
            pro = Product()
            pro.setProductId(id)
            pro.setProductName(name)
            pro.setProductDescription(description)
            pro.setProductPrice(price)
            pro.setProductStock(stock)

            self.cartList.append(pro)
            self.loadCartTable()


    """
    Method that verifies if the product is in the list of the cart
    """

    def __isProductInList(self, id):
        for prod in self.cartList:
            if id == prod.getProductId():
                return True
        return False


    """
    Method that return the new list of the cart
    """
    def get_cart_list(self):
        new_list = list(set(self.cartList))
        print(new_list)
        return new_list


    """
    Method that load the cart Table

    """
    def loadCartTable(self):
        listSize = len(self.cartList)
        self.centralWidget.getCartTable().setRowCount(listSize)
        prod = self.cartList[self._index]
        self.quantity = QLineEdit()
        self.btn_remove_item = QPushButton("Remove")
        self.quantity.setText("1")
        self.quantity.setValidator(self._validator.validate_Number())
        self.quantity.editingFinished.connect(lambda: self.getValueQuantity(prod))
        self.centralWidget.getCartTable().setItem(self._index, 0, QTableWidgetItem(str(prod.getProductId())))
        self.centralWidget.getCartTable().setItem(self._index, 1, QTableWidgetItem(prod.getProductName()))
        self.centralWidget.getCartTable().setItem(self._index, 2, QTableWidgetItem(prod.getProductDescription()))
        self.centralWidget.getCartTable().setItem(self._index, 3, QTableWidgetItem(str(prod.getProductPrice())))
        self.centralWidget.getCartTable().setCellWidget(self._index, 4, self.quantity)
        self.centralWidget.getCartTable().setItem(self._index, 5, QTableWidgetItem(str(0)))
        #self.centralWidget.getCartTable().setCellWidget(self._index, 6, self.btn_remove_item)
        #self.btn_remove_item.clicked.connect(lambda: self.remove_row_selected(prod))
        self._index = self._index + 1

    """
    def remove_row_selected(self, product):
        for i in range(self._index):
            pro_id = self.centralWidget.getCartTable().item(i, 0).text()
            if pro_id == product.getProductId():
                index_cart = i
                break
        print("index tabla ", self.centralWidget.getCartTable().currentRow())
        self.centralWidget.getCartTable().removeRow(self.centralWidget.getCartTable().currentRow())
    """

    """
    Method to get the total of the quantity value

    """
    def getValueQuantity(self, product):
        bill = self._billing_id_sale

        billing_id = bill

        for i in range(self._index):
            pro_id = self.centralWidget.getCartTable().item(i, 0).text()
            if pro_id == product.getProductId():
                self.index_cart = i
                stock = product.getProductStock()
                break

        user_id = 1
        product_id = self.centralWidget.getCartTable().item(self.index_cart, 0).text()
        quantity_value = self.centralWidget.getCartTable().cellWidget(self.index_cart, 4).text()
        price_value = self.centralWidget.getCartTable().item(self.index_cart, 3).text()

        if int(quantity_value) < int(stock):
            total = int(float(price_value)) * int(quantity_value)
            print(bill)
            self.centralWidget.getCartTable().setItem(self.index_cart, 5, QTableWidgetItem(str(total)))
            purchase = Purchase(billing_id, user_id, product_id, quantity_value, total)
            self.cart_list_to_purchase.append(purchase)
        else:
            self.centralWidget.display_message_when_quantity_is_grather_that_stock()


        """
        Method that clean the cart Table

        """
    def clean_cart_table(self):
        self.cartList = []
        self.cart_list_to_purchase = []
        self._index = 0
        self.centralWidget.getCartTable().setRowCount(0)

        """
        Method that add products to the cart

        """
    def addProducts_to_Cart(self):
        if len(self.cart_list_to_purchase) > 0:
            self.cartModel.addToCart(self.cart_list_to_purchase)
            self.centralWidget.display_message_success()
            self.clean_cart_table()
            self.loadProduct()
            self._billing_id_sale = self.generate_billing_id()
        else:
            self.centralWidget.display_message_when_the_cart_list_is_empty()