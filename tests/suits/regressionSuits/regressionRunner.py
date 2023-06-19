import unittest
from tests.loginTest import TestCase
from tests.addToCardTest import AddToCartTest
from tests.deletProductFromCartTest import DeleteProductFromCartTest


suite = unittest.TestSuite()
suite.addTest(TestCase("test_logIn_test"))
suite.addTest(AddToCartTest("test_add_to_cart"))
suite.addTest(DeleteProductFromCartTest("test_delete_from_cart"))

runner = unittest.TextTestRunner()
runner.run(suite)


