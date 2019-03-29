class Product:
    """metodo que obtiene el id de un product"""
    def getProductId(self):
        return self.__productId
    """metodo que setea el id de un product"""
    def setProductId(self, productId):
        self.__productId = productId

    """metodo que obtiene el nombre de un product"""
    def getProductName(self):
        return self.__productName

    """metodo que setea el nombre de un product"""
    def setProductName(self, productName):
        self.__productName = productName

    """metodo que obtiene la descripcion de un product"""
    def getProductDescription(self):
        return self.__productDescription

    """metodo que setea la descripcion de un product"""
    def setProductDescription(self, productDescription):
        self.__productDescription = productDescription

    """metodo que obtiene el precio de un product"""
    def getProductPrice(self):
        return self.__productPrice

    """metodo que setea el precio de un product"""
    def setProductPrice(self, productPrice):
        self.__productPrice = productPrice

    """metodo que obtiene el stock (cantidad en stock) de un product"""
    def getProductStock(self):
        return self.__productStock

    """metodo que setea el stock (cantidad en stock) de un product"""
    def setProductStock(self, productStock):
        self.__productStock = productStock

    """metodo que obtiene la categoria"""
    def getProductCategory(self):
        return self.__productCategory

    """metodo que setea una categoria"""
    def setProductCategory(self, productCategory):
        self.__productCategory = productCategory