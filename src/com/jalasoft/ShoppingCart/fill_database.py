from src.com.jalasoft.ShoppingCart.DB.category_query import QueryCategory
from src.com.jalasoft.ShoppingCart.DB.connectionDB import ConnectionDB
from src.com.jalasoft.ShoppingCart.DB.user_query import QueryUser
from src.com.jalasoft.ShoppingCart.model.category import Category
from src.com.jalasoft.ShoppingCart.model.user import User

"""Para llenar categorias y ver sus datos"""
categorys = Category()
category_id = categorys.setCategoryId(1)
category_name = categorys.setCategoryName("Games")


c = QueryCategory()
c.insertCategory(categorys)
c1 = c.loadAllCategories()

for row in c1:
   print(row.getCategoryName())

"""Para llenar users y ver sus datos"""
user = User()

user_name = user.setUserName("user1")
user_pass = user.setUserPassword("")
email = user.setUserEmail("test@test.com")
firstname = user.setUserFirstName("grupoD")
lastname = user.setUserLastName("grupoD")
phonenumber = user.setUserPhoneNumber(12345678)
type_user = user.setUserType("Admin")
state_user = user.setUserState("Active")


u = QueryUser()
u.insertUser(user)

u1 = u.loadUserDetail(2)

for row in u1:
   print(row.getUserName())