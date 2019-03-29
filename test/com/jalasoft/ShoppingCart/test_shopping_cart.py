import unittest

from src.com.jalasoft.ShoppingCart.DB.cart_query import CartQuery
from src.com.jalasoft.ShoppingCart.DB.category_query import QueryCategory
from src.com.jalasoft.ShoppingCart.DB.product_query import ProductQuery
from src.com.jalasoft.ShoppingCart.model.category import Category
from src.com.jalasoft.ShoppingCart.model.product import Product
from src.com.jalasoft.ShoppingCart.model.cart_model import CartModel


class ShoppingCartTest(unittest.TestCase):

    def test_db_insertCategory(self):
        category = Category()
        category.setCategoryName("Clothes")


        c = QueryCategory()
        c.insertCategory(category)
        self.assertTrue(c.category_Name("Clothes"))

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

    def test_db_loadAllProduct(self):
        product = ProductQuery()
        list = product.loadAllProduct()
        for i in list:
           actual = i.getProductName()
        expected = "Dresses"
        self.assertEqual(actual, expected)


    def test_db_loadAllProductByCategory(self):
        p = ProductQuery()
        listA = p.loadAllProductByCategory(1)
        for a in listA:
             actual = a.getProductName()
        expected = "Dresses"
        self.assertEqual(actual, expected)


    def test_db_product_Id(self):
        product = ProductQuery()
        prodId = product.product_Id(1)
        expected = 40
        self.assertEqual(prodId, expected)

    def test_db_loadAllCategories(self):
        c = QueryCategory()
        list = c.loadAllCategories()
        for i in list:
            actual = i.getCategoryName()
        expected = "Clothes"
        self.assertEqual(actual, expected)


    def test_model_get_category(self):

        expected = 'toys'
        cart = CartModel()
        c1 = cart.getAllCategories()
        c2 = c1[0].getCategoryName()

        self.assertEqual(expected, c2)


   
if __name__ == '__main__':
    unittest.main()
