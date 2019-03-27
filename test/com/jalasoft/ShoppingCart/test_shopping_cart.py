import unittest

from src.com.jalasoft.ShoppingCart.DB.product_query import ProductQuery
from src.com.jalasoft.ShoppingCart.model.product import Product
from src.com.jalasoft.ShoppingCart.model.cart_model import CartModel


class ShoppingCartTest(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_db_add_product(self):
        prod = Product()
        prod.setProductName("Dresses")
        prod.setProductDescription("This is only a test")
        prod.setProductPrice(55)
        prod.setProductStock(40)
        prod.setProductCategory(1)

        productIn = ProductQuery()
        productIn.insertProduct(prod)
        self.assertTrue(productIn.product_Name("Dresses"))

    def test_model_get_category(self):

        expected = 'toys'
        cart = CartModel()
        c1 = cart.getAllCategories()
        c2 = c1[0].getCategoryName()

        self.assertEqual(expected, c2)


    def test_get_products(self):
        pass

    def test_get_cart(self):
        pass

    def test_add_to_cart(self):
        pass

    def test_update_quantity_in_cart(self):
        pass

    def test_checkout_cart(self):
        pass

    def test_get_purchase_history(self):
        pass

if __name__ == '__main__':
    unittest.main()
