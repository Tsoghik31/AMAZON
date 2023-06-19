import names
from sources.base.basePage import BasePage
from selenium.webdriver.common.by import By


class EditYourNameWindow(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.enterYourNameFieldLocator = (By.ID, "profile-name-text-input")
        self.saveChangesButtonLocator = (By.ID, "profile-name-edit-submit-button-announce")


    def input_generated_name(self):
        generatedName = names.get_first_name(gender='female')
        self.enterYourNameFieldElement = self.find_element(self.enterYourNameFieldLocator)
        self.send_keys(self.enterYourNameFieldElement, generatedName)

    def click_on_save_changes_button(self):
        self.saveChangesButtonElement = self.find_element(self.saveChangesButtonLocator)
        self.click(self.saveChangesButtonElement)


        
        