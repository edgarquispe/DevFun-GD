from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator


class Util:

    def __init__(self):
        self._validator = ""
        self._message = ""

    def validate_String(self):
        self._validator = QRegExpValidator(QRegExp("[a-z-A-Z_]+"))
        return self._validator

    def validate_Number(self):
        self._validator = QRegExpValidator(QRegExp("[0-9_]+"))
        return self._validator