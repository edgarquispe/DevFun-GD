from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator, QDoubleValidator
from PyQt5.QtWidgets import QWidget, QLineEdit

#Control what user insert
class MyWidget(QWidget):
    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)
        self.le_input = QLineEdit(self)

        reg_ex = QRegExp("[a-zA-Z_][0-9a-zA-Z_]*")
        input_validator = QRegExpValidator(reg_ex, self.le_input)
        self.le_input.setValidator(input_validator)


# Validator for Decimal numbers
class DecimalValidator(QDoubleValidator):
    def __init__(self, *args):
        QDoubleValidator.__init__(self, *args)
        self.setNotation(QDoubleValidator.StandardNotation)
    def validate(self, input, pos):
        '''
        When we're left of the separator, and separator is pressed,
        remove the inserted separator and move right of the old separator.
        When we're right of the separator, and all decimal places are used already,
        go into overwrite mode (by removing the old digit)
        '''
        sep = self.locale().decimalPoint()
        if pos and (input[pos-1]==sep) and (sep in input[pos:]):
            input = input[:pos-1] + input[pos:]
            pos = input.find(sep)+1
        elif sep in input[:pos] and (len(input.split(sep)[1]) > self.decimals()):
            input = input[:pos] + input[pos+1:]
        return QDoubleValidator.validate(self, input, pos)


#Validate if a QTableWidget has lost focus, so I can validate the entry text and change its text
# if it's not valid for my program.

import sys
from PyQt5.QtWidgets import QItemDelegate, QWidget, QVBoxLayout, QTableWidget, QApplication, QLineEdit


class HexDelegate(QItemDelegate):
    def createEditor(self, parent, option, index):
        w = QLineEdit(parent)
        w.setInputMask("HHHHH")
        return w

class App(QWidget):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        self.setLayout(QVBoxLayout())

       # Create table
        self.tableWidget = QTableWidget(self)
        self.layout().addWidget(self.tableWidget)
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setItemDelegate(HexDelegate())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())