from sources.base.basePage import BasePage
from selenium.webdriver.common.by import By


class NavigationBar(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.searchFieldLocator = (By.ID, "twotabsearchtextbox")
        self.searchButton_Locator = (By.ID, "nav-search-submit-button")
        self.accountAndListsButtonLocator = (By.ID, "nav-link-accountList-nav-line-1")

    def fill_search_field(self, searchText):
        self.searchFieldElement = self.find_element(self.searchFieldLocator)
        self.send_keys(self.searchFieldElement, searchText)

    def click_on_search_button(self):
        self.searchButtonElement = self.find_element(self.searchButton_Locator)
        self.click(self.searchButtonElement)

    def mouse_move_action_and_list_menu(self):
        self.accountAndListsButtonElement = self.find_element(self.accountAndListsButtonLocator)
        self.mouse_move(self.accountAndListsButtonElement)



