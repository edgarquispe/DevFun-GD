from PyQt5.QtWidgets import QMainWindow, QMenu, QWidget, QLineEdit, QLabel, QFormLayout
from self import self


class View(QMainWindow):

    def __init__(self):
        super().__init__()
        # print('view')

    def initUI(self):
        self.setWindowTitle("TitleTest")
        self.__initComponent()
        self.show()
        # print('initUI')

    def __initComponent(self):
        menuBar = self.menuBar()
        product = menuBar.addMenu("Product")
        insert = QMenu("Insert", self)
        product.addMenu(insert)
        self.setCentralWidget(self.__getProductView())
    def __getProductView(self):
        proView = ProductView()
        return proView

# class ProductView(QWidget):
#     def __init__(self, parent=None):
#         super(ProductView,self).__init__(parent)
#         self._initUI()
#     def _initUI(self):
#         form = QFormLayout()
#         form.addRow(QLabel("name:"), QLineEdit())

class ProductView(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        form = QFormLayout()
        form.addRow(QLabel('name'), QLineEdit())
        self.setLayout(form)