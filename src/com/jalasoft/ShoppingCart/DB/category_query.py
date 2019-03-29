from src.com.jalasoft.ShoppingCart.DB.connectionDB import ConnectionDB
from src.com.jalasoft.ShoppingCart.model.cart import Cart
from src.com.jalasoft.ShoppingCart.model.category import Category


class QueryCategory:
    def __init__(self):
        self.__conn = ConnectionDB().getConnection()

    """Method to insert a category, it will receive a category object"""
    def insertCategory(self, category):
        cursor = self.__conn.cursor()
        insertQuery = "insert into category(category_name) values ('"+ category.getCategoryName()+"');"
        cursor.execute(insertQuery)
        self.__conn.commit()

    """This method will load all categories and add it to list, this will return a list of objects"""
    def loadAllCategories(self):
        cursor = self.__conn.cursor()
        cursor.execute("select category_id, category_name from category;")
        rows = cursor.fetchall()
        categoryList = []
        for row in rows:

            cate = Category()
            cate.setCategoryId(row[0])
            cate.setCategoryName(row[1])

            categoryList.append(cate)

        return categoryList
    
    def category_Name(self, category_name):
        cursor = self.__conn.cursor()
        name = cursor.execute("select category_name from category where category_name = '" + category_name + "';")
        row = name.fetchone()
        # print(row[0])

        return row[0]



"""Here an example on how to call the methods"""
# categorys = Category()
# category_id = categorys.setCategoryId(1)
# category_name = categorys.setCategoryName("Games")
#
#
# c = QueryCategory()
# c.insertCategory(categorys)
# c1 = c.loadAllCategories()
#
# for row in c1:
#    print(row.getCategoryName())