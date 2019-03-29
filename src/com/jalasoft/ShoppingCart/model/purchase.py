
class Purchase:

    def __init__(self, billing_id, user_id, product_id, quantity, product_price):
        self._billing_id = str(billing_id)
        self._user_id = user_id
        self._product_id = product_id
        self._quantity = quantity
        self._product_price = product_price

    """metodo que setea el billingId de un producto del carrito"""
    def set_billing_id(self, new_billing_id):
        self._billing_id = new_billing_id

    """metodo que obtiene el billingId de un producto del carrito"""
    def get_billing_id(self):
        return self._billing_id

    """metodo que setea el user de una venta para setearlo en la tabla del carrito"""
    def set_user_id(self, new_user_id):
        self._user_id = new_user_id

    """metodo que obtiene el user que hace la compra"""
    def get_user_id(self):
        return self._user_id

    """metodo que setea el id de un producto del carrito"""
    def set_product_id(self, new_product_id):
        self._product_id = new_product_id

    """metodo que obtiene el id de un producto del carrito"""
    def get_product_id(self):
        return self._product_id

    """metodo que setea el quantity de un producto del carrito"""
    def set_quantity(self, new_quantity):
        self._quantity = new_quantity

    """metodo que obtiene el quaantity de la lista del carrito"""
    def get_quantity(self):
        return self._quantity

    """metodo que setea el precio de un producto para agregarlo al purchase"""
    def set_price(self, new_price):
        self._product_price = new_price

    """metodo que obtiene el precio de un producto del carrito"""
    def get_price(self):
        return self._product_price