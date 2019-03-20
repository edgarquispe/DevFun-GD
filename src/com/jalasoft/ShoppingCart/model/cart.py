class Cart:

    def getBilling(self):
        return self.__billingId

    def setBilling(self, billingId):
        self.__billingId = billingId

    def getUserId(self):
        return self.__userId

    def setUserId(self, userId):
        self.__userId = userId

    def getProdutId(self):
        return self.__productId

    def setProdutId(self, productId):
        self.__productId = productId

    def getQuantity(self):
        return self.__quantity

    def setQuantity(self, quantity):
        self.__quantity = quantity

    def getCartPrice(self):
        return self.__cartPrice

    def setCartPrice(self, cartPrice):
        self.__cartPrice = cartPrice