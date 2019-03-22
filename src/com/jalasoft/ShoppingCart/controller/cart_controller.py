from PyQt5.QtWidgets import QTableWidgetItem, QLineEdit, QMessageBox

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

    def addActionListener(self):
        self.centralWidget = self.mainView.centralWidget()
        if isinstance(self.centralWidget, ProductInsertView):
            self.centralWidget.getSaveProductButton().clicked.connect(lambda: self.saveProduct())
            self.centralWidget.getSaveProductButton().clicked.connect(lambda: self.clean_the_form_fields())
        if isinstance(self.centralWidget, ProductShowView):
            self.centralWidget.getAddTocartButton().clicked.connect(lambda: self.addToCart())
        if isinstance(self.centralWidget, ProductShowView):
            self.centralWidget.getSaveToPurchaceButton().clicked.connect(lambda: self.addProducts_to_Cart())
        if isinstance(self.centralWidget, CategoryInsertView):
            self.centralWidget.getSaveCategoryButton().clicked.connect(lambda: self.save_Category_in_db())
            self.centralWidget.getSaveCategoryButton().clicked.connect(lambda: self.clean_the_form_fields())


    def clean_the_form_fields(self):
        self.centralWidget = self.mainView.centralWidget()
        self.centralWidget.clear_fields()

    def saveProduct(self):
        self.clean_cart_table()
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


    def loadProduct(self):
        self.centralWidget = self.mainView.centralWidget()
        listProduct = self.cartModel.getAllProduct()

        listSize = len(listProduct)

        self.centralWidget.getTable().setRowCount(listSize)
        index = 0
        for prod in listProduct:
            self.centralWidget.getTable().setItem(index, 0, QTableWidgetItem(str(prod.getProductId())))
            self.centralWidget.getTable().setItem(index, 1, QTableWidgetItem(prod.getProductName()))
            self.centralWidget.getTable().setItem(index, 2, QTableWidgetItem(prod.getProductDescription()))
            self.centralWidget.getTable().setItem(index, 3, QTableWidgetItem(str(prod.getProductPrice())))
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
        self.quantity.setValidator(self._validator.validate_Number())
        self.quantity.editingFinished.connect(lambda: self.getValueQuantity(self._index))
        self.centralWidget.getCartTable().setItem(self._index, 0, QTableWidgetItem(str(prod.getProductId())))
        self.centralWidget.getCartTable().setItem(self._index, 1, QTableWidgetItem(prod.getProductName()))
        self.centralWidget.getCartTable().setItem(self._index, 2, QTableWidgetItem(prod.getProductDescription()))
        self.centralWidget.getCartTable().setItem(self._index, 3, QTableWidgetItem(str(prod.getProductPrice())))
        self.centralWidget.getCartTable().setCellWidget(self._index, 4, self.quantity)
        self.centralWidget.getCartTable().setItem(self._index, 5, QTableWidgetItem(str(0)))

        self._index = self._index + 1

    def getValueQuantity(self, index):
        billing_id = "Test1"
        user_id = 1
        product_id = self.centralWidget.getCartTable().item(index-1, 0).text()
        quantity_value = self.centralWidget.getCartTable().cellWidget(index-1, 4).text()
        price_value = self.centralWidget.getCartTable().item(index-1, 3).text()
        total = int(float(price_value)) * int(quantity_value)
        self.centralWidget.getCartTable().setItem(index-1, 5, QTableWidgetItem(str(total)))

        purchase = Purchase(billing_id, user_id, product_id, quantity_value, total)
        self.cart_list_to_purchase.append(purchase)



    def clean_cart_table(self):
        self.cartList = []
        self._index = 0
        self.centralWidget.getCartTable().setRowCount(0)


    def addProducts_to_Cart(self):
        self.cartModel.addToCart(self.cart_list_to_purchase)
        print("insert to cart table")
        self.centralWidget.display_message_success()
        self.clean_cart_table()