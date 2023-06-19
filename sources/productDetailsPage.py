from sources.base.basePage import BasePage
from selenium.webdriver.common.by import By


class ProductDetailsPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.deleteProductButtonLocator = (By.XPATH, "(//input[@class = 'a-color-link'])[1]")
        self.addToCartButtonLocator = (By.ID, "add-to-cart-button")

    def add_to_cart(self):
        self.addToCartButtonElement = self.find_element(self.addToCartButtonLocator)
        self.click(self.addToCartButtonElement)

    def delete_first_product_from_cart(self):
        self.deleteProductButtonElement = self.find_element(self.deleteProductButtonLocator)
        self.click(self.deleteProductButtonElement)



