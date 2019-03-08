from PyQt5.QtWidgets import QWidget, QLineEdit, QFormLayout, QLabel, QVBoxLayout, QGroupBox, QPushButton, QTableWidget, \
    QTableWidgetItem, QComboBox, QHBoxLayout


class ProductView(QWidget):
    def __init__(self, parent=None):
        super(ProductView, self).__init__(parent)
        self.initUI()

    def initUI(self):
        #vLayout = QVBoxLayout()
        vLayout = QHBoxLayout()
        group = QGroupBox()
        form = QFormLayout()
        #labelPath = QLabel("Path"), QLineEdit()
        #labelFileName = QLabel("FileName"), QLineEdit()
        #labelExt = QLabel("Ext"), QLineEdit()

        form.addRow(QLabel("Path"), QLineEdit())
        form.addRow(QLabel("FileName"), QComboBox())
        form.addRow(QLabel("Ext"), QLineEdit())

        group.setLayout(form)

        button = QPushButton("Search")
        table = QTableWidget()
        table.setColumnCount(3)
        table.setRowCount(1)
        table.setHorizontalHeaderLabels(["Path", "CN", "Ext"])
        table.setItem(0, 0, QTableWidgetItem("C:\\test"))
        table.setItem(0, 0, QTableWidgetItem("video"))
        table.setItem(0, 0, QTableWidgetItem("mp4"))

        vLayout.addWidget(group)
        vLayout.addWidget(button)
        vLayout.addWidget(table)

        self.setLayout(vLayout)

        #form = QFormLayout()
        #form.addRow(QLabel('Name:'), QLineEdit())
        #self.setLayout(form)