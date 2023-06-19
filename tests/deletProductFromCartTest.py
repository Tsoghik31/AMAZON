import time
from tests.baseTest.baseTest import BaseTest
from sources.cartPage import CartPage
from sources.logInPage import LoginPage
from sources.productDetailsPage import ProductDetailsPage


class DeleteProductFromCartTest(BaseTest):


    def test_delete_from_cart(self):
        self.driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")
        self.logInPage = LoginPage(self.driver)
        self.logInPage.fill_username_field("acompap@yahoo.com")
        self.logInPage.click_on_continue_button()
        self.logInPage.fill_password_field("Selenium!")
        time.sleep(3)
        self.logInPage.click_on_signIn_button()
        time.sleep(5)

        self.cartPage = CartPage(self.driver)
        self.cartPage.click_on_cart_button_if_not_empty()


        self.productDetailsPage = ProductDetailsPage(self.driver)
        self.productDetailsPage.delete_first_product_from_cart()
        time.sleep(3)


