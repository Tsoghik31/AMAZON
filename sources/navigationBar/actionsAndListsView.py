from sources.base.basePage import BasePage
from selenium.webdriver.common.by import By


class ActionsAndListsView(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        # self.accountsAndListButtonLocator = (By.ID, "nav-link-accountList-nav-line-1")
        # self.accountButtonLocator = (By.XPATH, "(//span[@class = 'nav-text'])[4]")


    def click_on_account_button(self):
        self.accountsAndListButtonElement = self.find_element(self.accountsAndListButtonLocator)
        self.mouse_move(self.accountsAndListButtonElement)












