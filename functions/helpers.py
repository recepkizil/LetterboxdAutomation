import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from constants.globalConstants import *

class functions:

    def waitForElementVisible(self, locator, timeout=30):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
    
    def waitForElementsVisible(self, locator, timeout=30):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))
    
    def waitForElementClickable(self, locator, timeout=30):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
    
    def waitForURLChange(self, previous_url, timeout=20):
        try:
            WebDriverWait(self.driver, timeout).until(EC.url_changes(previous_url))
            return True
        except:
            return False
    
    def take_screenshot(self, filename):
        self.driver.get_screenshot_as_file(filename)
    
    def newTab(self):
        window_after = self.driver.window_handles[-1]
        self.driver.switch_to.window(window_after)

    def succesful_login(self):
        self.waitForElementsVisible(SIGN_IN_XPATH).click()
        self.waitForElementVisible(USERNAME_INPUT).send_keys(USERNAME)
        self.waitForElementVisible(PASSWORD_INPUT).send_keys(PASSWORD)
        self.waitForElementsVisible(SIGN_IN_BUTTON).click()



