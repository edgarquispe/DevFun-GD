import random

from PyQt5.QtWidgets import QTableWidgetItem, QLineEdit, QMessageBox, QPushButton, QDialog, QLabel, QVBoxLayout

from src.com.jalasoft.ShoppingCart.controller.utilities.utilities import Util
from src.com.jalasoft.ShoppingCart.model.category import Category
from src.com.jalasoft.ShoppingCart.model.product import Product
from src.com.jalasoft.ShoppingCart.model.purchase import Purchase
from src.com.jalasoft.ShoppingCart.view.category_insert_view import CategoryInsertView
from src.com.jalasoft.ShoppingCart.view.product_insert_view import ProductInsertView
from src.com.jalasoft.ShoppingCart.view.product_show_view import ProductShowView


class CartController:

    def __init__(self, mainView, cartModel):
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
        self.centralWidget = self.mainView.centralWidget()
        self.centralWidget.clear_fields()

    def saveProduct(self):

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
        self.centralWidget = self.mainView.centralWidget()
        category_name = self.centralWidget.getCategoryName()

        category = Category()
        category.setCategoryName(category_name)
        self.cartModel.save_Category(category)
        self.centralWidget.display_message_success_after_save_category()

    def loadPurchase(self):
        self.centralWidget = self.mainView.centralWidget()
        listPurchase = self.cartModel.get_all_detail_of_purchase()
        listSize = len(listPurchase)

        self.centralWidget.get_purchase_Table().setRowCount(listSize)
        index = 0
        for purchase_item in listPurchase:
            self.btn_show_purchase_detail = QPushButton("View Detail Purchase")
            self.centralWidget.get_purchase_Table().setItem(index, 0, QTableWidgetItem(str(purchase_item.getBillId())))
            self.centralWidget.get_purchase_Table().setCellWidget(index, 1, self.btn_show_purchase_detail)
            self.btn_show_purchase_detail.clicked.connect(lambda: self.show_detail_purchase_by_billing(index))
            index = index + 1
            print(index)


    def show_detail_purchase_by_billing(self, purchase_index):
        print("Show detail purchase by billing....!!")
        self.ui_report_purchase = QDialog()
        self.ui_report_purchase.setWindowTitle(".::: Show Detail Purchase :::.")
        self.ui_report_purchase.resize(500, 300)
        self.vLayout_to_report = QVBoxLayout()
        lb_title = QLabel("_______________Shopping Cart____________________")
        billing_id = self.centralWidget.get_purchase_Table().item(purchase_index-1, 0).text()
        print(purchase_index)
        print(billing_id)
        ##lb_billing_id = QLabel(billing_id)
        btn_report = QPushButton("Print Report Purchase")

        self.vLayout_to_report.addWidget(lb_title)
        ##self.vLayout_to_report.addWidget(lb_billing_id)
        self.vLayout_to_report.addWidget(btn_report)

        self.ui_report_purchase.setLayout(self.vLayout_to_report)

        self.ui_report_purchase.show()


    def loadProduct(self):
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
        indexes = self.centralWidget.getTable().selectionModel().selectedIndexes()
        id = indexes[0].sibling(indexes[0].row(), indexes[0].column()).data();

        if not self.__isProductInList(id):
            name = indexes[1].sibling(indexes[1].row(), indexes[1].column()).data();
            description = indexes[2].sibling(indexes[2].row(), indexes[2].column()).data();
            price = indexes[3].sibling(indexes[3].row(), indexes[3].column()).data();

            # create product and add to cart
            pro = Product()
            pro.setProductId(id)
            pro.setProductName(name)
            pro.setProductDescription(description)
            pro.setProductPrice(price)

            self.cartList.append(pro)
            self.loadCartTable()

    def __isProductInList(self, id):
        for prod in self.cartList:
            if id == prod.getProductId():
                return True
        return False


    def get_cart_list(self):
        new_list = list(set(self.cartList))
        print(new_list)
        return new_list

    def loadCartTable(self):
        listSize = len(self.cartList)
        self.centralWidget.getCartTable().setRowCount(listSize)
        prod = self.cartList[self._index]
        self.quantity = QLineEdit()
        self.quantity.setText("1")
        self.quantity.setValidator(self._validator.validate_Number())
        self.quantity.editingFinished.connect(lambda: self.getValueQuantity(prod))
        self.centralWidget.getCartTable().setItem(self._index, 0, QTableWidgetItem(str(prod.getProductId())))
        self.centralWidget.getCartTable().setItem(self._index, 1, QTableWidgetItem(prod.getProductName()))
        self.centralWidget.getCartTable().setItem(self._index, 2, QTableWidgetItem(prod.getProductDescription()))
        self.centralWidget.getCartTable().setItem(self._index, 3, QTableWidgetItem(str(prod.getProductPrice())))
        self.centralWidget.getCartTable().setCellWidget(self._index, 4, self.quantity)
        self.centralWidget.getCartTable().setItem(self._index, 5, QTableWidgetItem(str(0)))

        self._index = self._index + 1

    def getValueQuantity(self, product):
        bill = self._billing_id_sale
        print(bill)
        billing_id = bill

        for i in range(self._index):
            pro_id = self.centralWidget.getCartTable().item(i, 0).text()
            if pro_id == product.getProductId():
                self.index_cart = i
                break

        user_id = 1
        product_id = self.centralWidget.getCartTable().item(self.index_cart, 0).text()
        quantity_value = self.centralWidget.getCartTable().cellWidget(self.index_cart, 4).text()
        price_value = self.centralWidget.getCartTable().item(self.index_cart, 3).text()
        total = int(float(price_value)) * int(quantity_value)
        self.centralWidget.getCartTable().setItem(self.index_cart, 5, QTableWidgetItem(str(total)))

        purchase = Purchase(billing_id, user_id, product_id, quantity_value, total)
        self.cart_list_to_purchase.append(purchase)



    def clean_cart_table(self):
        self.cartList = []
        self.cart_list_to_purchase = []
        self._index = 0
        self.centralWidget.getCartTable().setRowCount(0)


    def addProducts_to_Cart(self):
        self.cartModel.addToCart(self.cart_list_to_purchase)
        # print("insert to cart table")
        self.centralWidget.display_message_success()
        self.clean_cart_table()
        self.loadProduct()
