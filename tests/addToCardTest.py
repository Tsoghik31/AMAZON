from tests.baseTest.baseTest import BaseTest
from sources.logInPage import LoginPage
from sources.navigationBar.navigationBar import NavigationBar
from sources.searchResultPage import SearchResultPage
from sources.productDetailsPage import ProductDetailsPage
from sources.cartPage import CartPage
import time

class AddToCartTest(BaseTest):
    # search smth in amazon, and add to card the first result
    def test_add_to_cart(self):
        self.driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")
        self.logInPage = LoginPage(self.driver)
        self.logInPage.fill_username_field("acompap@yahoo.com")
        self.logInPage.click_on_continue_button()
        self.logInPage.fill_password_field("Selenium!")
        time.sleep(3)
        self.logInPage.click_on_signIn_button()
        time.sleep(5)

        self.navigationBar = NavigationBar(self.driver)
        self.navigationBar.fill_search_field("python books")
        self.navigationBar.click_on_search_button()


        self.searchResultPage = SearchResultPage(self.driver)
        self.searchResultPage.click_on_first_searchResul()

        self.cartPage = CartPage(self.driver)
        itemsQuanityBeforeAddingNewItem = self.cartPage.get_cartItems_quantity()

        self.productDetailsPage = ProductDetailsPage(self.driver)
        self.productDetailsPage.add_to_cart()

        itemsQuanityAfterAddingNewItem = self.cartPage.get_cartItems_quantity()
        assert itemsQuanityAfterAddingNewItem == itemsQuanityBeforeAddingNewItem + 1










