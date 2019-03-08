from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMenu
from src.com.jalasoft.ShoppingCart.view.productView import ProductView


class Login(QtWidgets.QDialog):

    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.textName = QtWidgets.QLineEdit(self)
        self.textPass = QtWidgets.QLineEdit(self)
        self.buttonLogin = QtWidgets.QPushButton('Login', self)
        self.buttonLogin.clicked.connect(self.handleLogin)

        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.textName)
        layout.addWidget(self.textPass)
        layout.addWidget(self.buttonLogin)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('.:: Login ::.')
        self.__initComponent()
        self.show()

    def __initComponent(self):
        pass

    def handleLogin(self):
        if (self.textName.text() == 'test' and self.textPass.text() == 'test123'):
            self.accept()
        else:
            QtWidgets.QMessageBox.warning(self, 'Error', 'Bad user or password')


class Window(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('.:: Shopping Cart ::.')
        self.__initComponent()
        self.show()

    def __initComponent(self):
        menuBar = self.menuBar()
        product = menuBar.addMenu("Product")
        insert = QMenu('Insert', self)
        product.addMenu(insert)
        # aqui tiene q haber un if pa establecer segun una accion del menu
        self.setCentralWidget(self.__getProductView())

    def __getProductView(self):
        proView = ProductView()
        return proView

        

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login = Login()

    if login.exec_() == QtWidgets.QDialog.Accepted:
        window = Window()
        window.show()
        sys.exit(app.exec_())    