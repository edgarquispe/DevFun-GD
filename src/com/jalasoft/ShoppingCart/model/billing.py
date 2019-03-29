

class Billing:

    """metodo que devuelve el billing id de la tabla purchase"""
    def getBillId(self):
        return self.__billId

    def setBillId(self, billId):
        self.__billId = billId
    """metodo usado para obtener el nombre de un producto para ser mostrado en el billing detail"""
    def getProdName(self):
        return self.__prodName
    """metodo que setea el nombre de un producto"""
    def setProdName(self, prodName):
        self.__prodName = prodName
    """metodo que obtiene la cantidad del item en la orden"""
    def getProdQuantity(self):
        return self.__prodQuantity

    """metodo que setea la cantidad de un producto"""
    def setProdQuantity(self, prodQuantity):
        self.__prodQuantity = prodQuantity

    """metodo que obtiene el precio unitario de un producto que puede ser de la tabla purchase"""
    def getProdPrice(self):
        return self.__prodPrice

    """metodo que setea el precio unitario de un producto"""
    def setProdPrice(self, prodPrice):
        self.__prodPrice = prodPrice







