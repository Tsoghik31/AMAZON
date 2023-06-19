from sources.base.basePage import BasePage
from selenium.webdriver.common.by import By


class SearchResultPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.firstResultLocator = (By.XPATH, "(//div[@class = 'a-section aok-relative s-image-square-aspect'])[1]")

    def click_on_first_searchResul(self):
        self.firstResultElement = self.find_element(self.firstResultLocator)
        self.click(self.firstResultElement)

