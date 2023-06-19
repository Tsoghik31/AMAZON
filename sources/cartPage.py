from sources.base.basePage import BasePage
from selenium.webdriver.common.by import By


class CartPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.cartButtonLocator = (By.ID, "nav-cart-count")


    def get_cartItems_quantity(self):
        self.cartButtonElement = self.find_element(self.cartButtonLocator)
        return self.get_text_in_int_format(self.cartButtonElement)



    # def add_to_cart(self):
    #     addToCartButtonElement = self.find_element(self.addToCartButtonLocator)
    #     self.click(addToCartButtonElement)

    def click_on_cart_button_if_not_empty(self):
        if self.get_cartItems_quantity() > 0:
            self.click(self.cartButtonElement)
        else:
            print("EMPTY cart")
            exit(6)






