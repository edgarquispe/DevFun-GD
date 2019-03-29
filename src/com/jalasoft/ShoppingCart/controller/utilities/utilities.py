from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator


class Util:

    def __init__(self):
        self._validator = ""
        self._message = ""

    def validate_String(self):
        """
        Validator for every input that has to accept strings
        """
        self._validator = QRegExpValidator(QRegExp("[a-zA-ZÑñ\-'\s]+"))
        return self._validator

    def validate_Number(self):
        """
        Validator for every input that has to accept integers
        """
        self._validator = QRegExpValidator(QRegExp("[0-9_]+"))
        return self._validator

    def validate_Float(self):
        """
        Validator for every input that has to accept a price
        """
        self._validator = QRegExpValidator(QRegExp("[+-]?([0-9]*[.])?[0-9]+"))
        return self._validator
