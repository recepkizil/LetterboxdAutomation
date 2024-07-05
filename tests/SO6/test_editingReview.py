import time
import pytest
from functions.helpers import functions
from constants.globalConstants import *
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains


@pytest.mark.usefixtures("setup")
class Test_Editing_Review(functions):
#TC01
    def test_edit_review(self):
        self.succesful_login()
        self.waitForElementClickable(SEARCHBAR_XPATH2).click()
        self.waitForElementVisible(SEARCHBAR_INPUT).send_keys(MOVIE_NAME_5, Keys.ENTER)
        self.waitForElementVisible(MOVIE5).click()
        self.waitForElementVisible(LEAVE_COMMENT).click()
        self.waitForElementVisible(COMMENT_INPUT).click()
        self.waitForElementVisible(COMMENT_INPUT_AREA).send_keys(comment3)
        self.waitForElementVisible(COMMENT_SUBMIT).click()
        time.sleep(2)
        self.driver.refresh()
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,2350)")
        time.sleep(2)
        your_review = self.waitForElementVisible(YOUR_REVIEW)
        assert your_review.text == "YOUR REVIEWS"
        time.sleep(2)

#TC02
    def test_cancel_edit_review(self):
        self.succesful_login()
        self.waitForElementClickable(SEARCHBAR_XPATH2).click()
        self.waitForElementVisible(SEARCHBAR_INPUT).send_keys(MOVIE_NAME_5, Keys.ENTER)
        self.waitForElementVisible(MOVIE5).click()
        self.waitForElementVisible(LEAVE_COMMENT).click()
        self.waitForElementVisible(COMMENT_INPUT).click()
        self.waitForElementVisible(COMMENT_INPUT_AREA).send_keys(comment3)
        time.sleep(2)
        self.waitForElementVisible(COMMENT_SUBMIT).click()
        time.sleep(2)
        self.waitForElementVisible(ACTIVITIES).click()
        self.waitForElementVisible(DIARY).click()
        self.waitForElementVisible(EDIT_BUTTON).click()
        self.waitForElementVisible(CLOSE_BUTTON).click()
        time.sleep(2)
        assert "/testerhesabim/films/diary/" in self.driver.current_url
        time.sleep(2)

#TC03
    def test_delete_review(self):
        self.succesful_login()
        self.waitForElementClickable(SEARCHBAR_XPATH2).click()
        self.waitForElementVisible(SEARCHBAR_INPUT).send_keys(MOVIE_NAME_5, Keys.ENTER)
        self.waitForElementVisible(MOVIE5).click()
        self.waitForElementVisible(LEAVE_COMMENT).click()
        self.waitForElementVisible(COMMENT_INPUT).click()
        self.waitForElementVisible(COMMENT_INPUT_AREA).send_keys(comment3)
        time.sleep(2)
        self.waitForElementVisible(COMMENT_SUBMIT).click()
        time.sleep(2)
        self.waitForElementVisible(ACTIVITIES).click()
        self.waitForElementVisible(DIARY).click()
        self.waitForElementVisible(EDIT_BUTTON).click()
        self.waitForElementVisible(DELETE_BUTTON).click()
        time.sleep(2)
        assert "/testerhesabim/films/diary/" in self.driver.current_url
        time.sleep(2)
        





