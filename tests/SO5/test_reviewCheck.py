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
        sign_out = self.waitForElementVisible(SIGN_OUT)
        actions = ActionChains(self.driver)
        actions.move_to_element(my_account).perform()
        actions.click(sign_out).perform()
        # self.waitForElementVisible(MYACCOUNT).click()
        # self.waitForElementVisible(SIGN_OUT).click()
        self.driver.refresh()