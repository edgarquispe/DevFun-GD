class Cart:

    def getBilling(self):
        return self.__billingId

    def getUserId(self):
        return self.__userId

    def getProdutId(self):
        return self.__productId

    def getQuantity(self):
        return self.__quantity

    def getCartPrice(self):
        return self.__cartPrice

    def setProductId(self, productId):
        self.__productId = productId

