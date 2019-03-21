from src.com.jalasoft.ShoppingCart.DB.connectionDB import ConnectionDB
from src.com.jalasoft.ShoppingCart.model.user import User


class QueryUser:
    def __init__(self):
        self.__conn = ConnectionDB().getConnection()

    """Method to insert a category, it will receive a category object"""
    def insertUser(self, user):
        cursor = self.__conn.cursor()
        insertQuery = "insert into user(user_name, password, email, firstname, lastname, phonenumber, type_user, state_user) values ('" +user.getUserName() + "','" + user.getUserPassword()+ "', '" + user.getUserEmail()+ "', '" + user.getUserFirstName()+ "', '" + user.getUserLastName()+ "'," + str(user.getUserPhoneNumber())+",'" + user.getUserType()+ "', '" + user.getUserState()+ "');"
        cursor.execute(insertQuery)
        self.__conn.commit()

    """This method will load all categories and add it to list, this will return a list of objects"""
    def loadUserDetail(self, userid):

        cursor = self.__conn.cursor()
        cursor.execute("select user_name from user where user_id = '"+str(userid)+"';")
        rows = cursor.fetchall()
        userList = []
        for row in rows:

            user = User()
            user.setUserName(row[0])
            userList.append(user)

        return userList



"""Here an example on how to call the methods"""
# user = User()
#
# user_name = user.setUserName("user1")
# user_pass = user.setUserPassword("")
# email = user.setUserEmail("test@test.com")
# firstname = user.setUserFirstName("grupoD")
# lastname = user.setUserLastName("grupoD")
# phonenumber = user.setUserPhoneNumber(12345678)
# type_user = user.setUserType("Admin")
# state_user = user.setUserState("Active")
#
#
# u = QueryUser()
# u.insertUser(user)
#
# u1 = u.loadUserDetail(2)
#
# for row in u1:
#    print(row.getUserName())
