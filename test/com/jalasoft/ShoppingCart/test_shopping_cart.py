import unittest

from src.com.jalasoft.ShoppingCart.DB.product_query import ProductQuery
from src.com.jalasoft.ShoppingCart.model.product import Product


class ShoppingCartTest(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_add_product(self):

        """self.store.add_product("The Elements Anorak", 148, 100)
        self.assertTrue(Product.query.filter_by(title="The Elements Anorak"))"""
        prod = Product()
        # prod.setProductId()
        prod.setProductName("Rings")
        prod.setProductDescription("This is only a test")
        prod.setProductPrice(55)
        prod.setProductStock(40)
        prod.setProductCategory(1)


        productIn = ProductQuery()
        productIn.insertProduct(prod)
        self.assertTrue(productIn.product_Id(str(6)))


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
