from sources.base.basePage import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.userNameFieldLocator = (By.ID, "ap_email")
        self.continueButtonLocator = (By.ID, "continue")
        self.passwordFieldLocator = (By.ID, "ap_password")
        self.signInButtonLocator = (By.ID, "signInSubmit")
        self.greetingTextLocator = (By.ID, "nav-link-accountList-nav-line-1")


    def fill_username_field(self, username):
        usernNameFieldElement = self.find_element(self.userNameFieldLocator)
        self.send_keys(usernNameFieldElement, username)


    def click_on_continue_button(self):
        continueButtonElement = self.find_element(self.continueButtonLocator)
        self.click(continueButtonElement)

    def fill_password_field(self, password):
        passwordFiledElement = self.find_element(self.passwordFieldLocator)
        self.send_keys(passwordFiledElement, password)

    def click_on_signIn_button(self):

        signInButtonElement = self.find_element(self.signInButtonLocator)
        self.click(signInButtonElement)

    def get_greeting_text(self):
        greetingTextElement = self.find_element(self.greetingTextLocator)
        return self.get_text(greetingTextElement)

    def get_random_name(self):
        names.get




