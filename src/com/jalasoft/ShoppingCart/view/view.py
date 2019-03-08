from PyQt5.QtWidgets import QMainWindow, QMenu, QWidget, QLineEdit, QLabel, QFormLayout, QGroupBox, QVBoxLayout, \
    QPushButton, QTableWidget, QTableWidgetItem, QComboBox, QHBoxLayout


class View(QMainWindow):
    def __init__(self):
        # print("view")
        super().__init__()

    def initUI(self):
        print("initUI")
        # self.setWindoWtitle('test')
        self.setWindowTitle('test')
        self.__initComponent()
        self.show()


    def __initComponent(self):
        menuBar = self.menuBar()
        product = menuBar.addMenu('Product')
        insert = QMenu('Insert', self)
        product.addMenu(insert)
        self.setCentralWidget(self.__getProductView())

    def __getProductView(self):
        proView = ProductView()
        return proView

class ProductView(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # form = QFormLayout()
        # form.addRow(QLabel('name'), QLineEdit())
        # self.setLayout(form)
        # vLayout = QHBoxLayout()
        vLayout = QVBoxLayout()
        group = QGroupBox()
        form = QFormLayout()
        form.addRow(QLabel("Path"), QLineEdit())
        form.addRow(QLabel("FN"), QComboBox())
        form.addRow(QLabel("ext"), QLineEdit())
        group.setLayout(form)

        buttonS = QPushButton("Search")
        table = QTableWidget()

        table.setColumnCount(3)
        table.setRowCount(1)
        table.setHorizontalHeaderLabels(["Path", "FN", "ext"])
        table.setItem(0,0, QTableWidgetItem("C:\Test"))
        table.setItem(0,1, QTableWidgetItem("video.mp4"))
        table.setItem(0,2, QTableWidgetItem("mp4"))

        vLayout.addWidget(group)
        vLayout.addWidget(buttonS)
        vLayout.addWidget(table)

        self.setLayout(vLayout)



