from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class BasePage():
    def __init__(self, driver: webdriver):
        self.driver = driver

    def is_element_visible(self, locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False

    def find_element(self, locator):
        if self.is_element_visible(locator):
            element = self.driver.find_element(*locator)
            return element
        else:
            print("ELEMENT not found")
            exit(5)


    def send_keys(self, element, text):
        element.clear()
        element.send_keys(text)

    def click(self, webElement):
        webElement.click()

    def get_title(self):
        return self.driver.title

    def send_keys(self, element, text):
        element.clear()
        element.send_keys(text)
        # loger.log("info", "Secessfully added text")

    def click(self, webElement):
        webElement.click()

    def drag_and_drop(self):
        pass

    def press_and_hold(self):
        pass

    def mouse_move(self, webElement):
        action = ActionChains(self.driver)
        action.move_to_element(webElement)
        action.perform()

    def get_text(self, webElement):
        return webElement.text

    def get_text_in_int_format(self, webElementINT):
        return int(webElementINT.text)










