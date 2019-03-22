from src.com.jalasoft.ShoppingCart.DB.connectionDB import ConnectionDB
from src.com.jalasoft.ShoppingCart.model.cart import Cart


class CartQuery:
    def __init__(self):
        self.__conn = ConnectionDB().getConnection()

    def insertCart(self, productPurchase):
        cursor = self.__conn.cursor()
        print("DB insert ....")
        billing_id = productPurchase.get_billing_id()
        user_id = productPurchase.get_user_id()
        prod_id = productPurchase.get_product_id()
        prod_quantity = productPurchase.get_quantity()
        prod_total = productPurchase.get_price()

        print(billing_id)
        print(user_id)
        print(prod_id)
        print(prod_quantity)
        print(prod_total)

        insertQuery = "insert into purchase(billing_id, user_id, product_id, quantity, price) values ('" + str(billing_id) + "','" + str(user_id)+ "', " + str(prod_id)+ ", " + str(prod_quantity)+ ", " + str(prod_total)+ ");"
        cursor.execute(insertQuery)
        self.__conn.commit()


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