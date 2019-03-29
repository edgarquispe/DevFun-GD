class Category:
    def getCategoryId(self):
        return self.__categoryId

    """metodo que setea el el id de ua categoria"""
    def setCategoryId(self, categoryId):
        self.__categoryId = categoryId
    """metodo que obtiene el nombre de ua categoria"""
    def getCategoryName(self):
        return self.__categoryName

    """este metodo setea una categoria que puede ser usada para ser insertada en tabla category"""
    def setCategoryName(self, categoryName):
        self.__categoryName = categoryName