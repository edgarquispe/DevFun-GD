from src.com.jalasoft.ShoppingCart.DB.connectionDB import ConnectionDB
from src.com.jalasoft.ShoppingCart.model.cart import Cart


class CartQuery:
    def __init__(self):
        self.__conn = ConnectionDB().getConnection()

    def insertCart(self, productPurchase):
        cursor = self.__conn.cursor()
        print("DB insert ....")
        product_name = productPurchase.getProductName()

        #insertQuery = "insert into purchase(billing_id, user_id, product_id, quantity, price) values ('" + productPurchase[0] + "','" + str(productPurchase[1])+ "', " + str(productPurchase[2])+ ", " + str(productPurchase[3])+ ", " + str(productPurchase[4])+ ");"
        #cursor.execute(insertQuery)
        #self.__conn.commit()


    def loadAllCart(self):

        cursor = self.__conn.cursor()
        c = cursor.execute("select billing_id, user_id, product_id, quantity, price from purchase;")
        print(c.fetchall)
        rows = cursor.fetchall()

        cartList = []
        for row in rows:

            cart = Cart()
            cart.setBilling(row[0])
            cart.setUserId(row[1])
            cart.setProdutId(row[2])
            cart.setQuantity(row[3])
            cart.setCartPrice(row[4])

            cartList.append(cart)

        return cartList


# # purchaseList = ("Bill1", 1, 5, 2, 4)
# c = CartQuery()
# # c.insertCart(purchaseList)
# l = c.loadAllCart()
# print(l)
# for i in l:
#     print(i.getBilling())