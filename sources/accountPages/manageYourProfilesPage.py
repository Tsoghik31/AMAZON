from sources.base.basePage import BasePage
from selenium.webdriver.common.by import By

class ManageYourAccountPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.profileNameButtonLocator = (By.ID, "home-profile-0")
        self.editProfileButtonLocator = (By.ID, "name-edit-pencil-image")

    def click_on_profileName(self):
        self.profileNameButtonElement = self.find_element(self.profileNameButtonLocator)
        self.click(self.profileNameButtonElement)

    def click_on_edit_username_button(self):
        self.editProfileButtonElement = self.find_element(self.editProfileButtonLocator)
        self.click(self.editProfileButtonElement)
