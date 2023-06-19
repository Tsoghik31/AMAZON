from sources.base.basePage import BasePage
from selenium.webdriver.common.by import By


class YourAccountPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.yourProfilesButtonLocator = (By.XPATH, "(//*[@class = 'a-spacing-none ya-card__heading--rich a-text-normal'])[7]")


    def click_on_yourProfiles_button(self):
        self.yourProfilesButtonElement = self.find_element(self.yourProfilesButtonLocator)
        self.click(self.yourProfilesButtonElement)




