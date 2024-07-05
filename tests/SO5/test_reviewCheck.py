import time
import pytest
from functions.helpers import functions
from constants.globalConstants import *
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains


@pytest.mark.usefixtures("setup")
class Test_Filtering(functions):
#TC01
    def test_checking_review(self):
        self.succesful_login()
        self.waitForElementClickable(SEARCHBAR_XPATH2).click()
        self.waitForElementVisible(SEARCHBAR_INPUT).send_keys(MOVIE_NAME_5, Keys.ENTER)
        self.waitForElementVisible(MOVIE5).click()
        self.waitForElementVisible(LEAVE_COMMENT).click()
        self.waitForElementVisible(COMMENT_INPUT).click()
        self.waitForElementVisible(COMMENT_INPUT_AREA).send_keys(comment2)
        self.waitForElementVisible(COMMENT_SUBMIT).click()
        my_account = self.waitForElementVisible(MYACCOUNT)
        self.moveToElement(my_account)
        self.waitForElementVisible(SIGN_OUT).click()
        self.driver.refresh()
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,2000)")
        time.sleep(2)
        self.take_screenshot("screenshots/mycomment.png")

