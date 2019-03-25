from src.com.jalasoft.ShoppingCart.DB.connectionDB import ConnectionDB
from src.com.jalasoft.ShoppingCart.DB.product_query import ProductQuery
from src.com.jalasoft.ShoppingCart.model.cart import Cart


class CartQuery:
    def __init__(self):
        self.__conn = ConnectionDB().getConnection()

    def insertCart(self, productPurchase):
        cursor = self.__conn.cursor()
        # print("DB insert ....")
        billing_id = productPurchase.get_billing_id()
        user_id = productPurchase.get_user_id()
        prod_id = productPurchase.get_product_id()
        prod_quantity = productPurchase.get_quantity()
        prod_total = productPurchase.get_price()

        # print(billing_id)
        # print(user_id)
        # print(prod_id)
        # print(prod_quantity)
        # print(prod_total)

        insertQuery = "insert into purchase(billing_id, user_id, product_id, quantity, price) values ('" + str(billing_id) + "','" + str(user_id)+ "', " + str(prod_id)+ ", " + str(prod_quantity)+ ", " + str(prod_total)+ ");"
        cursor.execute(insertQuery)

        p = ProductQuery()
        stockprod = p.product_Id(prod_id)
        newstock = stockprod - int(prod_quantity)


        updateQuantity = "update product set stock = '" + str(newstock) + "' where product_id = '" + str(prod_id) + "';"
        cursor.execute(updateQuantity)





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

    """Este metodo devuelve la lista de billing que se tiene"""
    def LoadAllBilling(self):
        cursor = self.__conn.cursor()
        cursor.execute(
            "select b.billing_id from purchase b, product p where p.product_id = b.product_id Group by b.billing_id;")
        rows = cursor.fetchall()

        BillingtList = []
        for row in rows:
            bill = Billing()
            bill.setBillId(row[0])

            BillingtList.append(bill)
        return BillingtList

    """Este metodo muestra todo el detalle de la venta pasandole el bill"""
    def PurchaseDetail(self, bill):

        cursor = self.__conn.cursor()
        cursor.execute(
            "select b.billing_id, p.product_name, b.quantity, p.price from purchase b, product p where p.product_id = b.product_id and b.billing_id = '" + bill + "';")
        rows = cursor.fetchall()
        ProdDetailList = []
        for row in rows:
            prodet = Billing()
            prodet.setBillId(row[0])
            prodet.setProdName(row[1])
            prodet.setProdQuantity(row[2])
            prodet.setProdPrice(row[3])

            ProdDetailList.append(prodet)
        return ProdDetailList

# # purchaseList = ("Bill1", 1, 5, 2, 4)
# c = CartQuery()
# # c.insertCart(purchaseList)
# l = c.loadAllCart()
# print(l)
# for i in l:
#     print(i.getBilling())