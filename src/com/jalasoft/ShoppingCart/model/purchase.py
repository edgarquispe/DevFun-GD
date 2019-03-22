
class Purchase:

    def __init__(self, billing_id, user_id, product_id, quantity, product_price):
        self._billing_id = billing_id
        self._user_id = user_id
        self._product_id = product_id
        self._quantity = quantity
        self._product_price = product_price

    def set_billing_id(self, new_billing_id):
        self._billing_id = new_billing_id

    def get_billing_id(self):
        return self._billing_id

    def set_user_id(self, new_user_id):
        self._user_id = new_user_id

    def get_user_id(self):
        return self._user_id

    def set_product_id(self, new_product_id):
        self._product_id = new_product_id

    def get_product_id(self):
        return self._product_id

    def set_quantity(self, new_quantity):
        self._quantity = new_quantity

    def get_quantity(self):
        return self._quantity

    def set_price(self, new_price):
        self._product_price = new_price

    def get_price(self):
        return self._product_price