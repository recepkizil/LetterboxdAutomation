import time
import pytest
from functions.helpers import functions
from constants.globalConstants import *
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import Select


@pytest.mark.usefixtures("setup")
class Test_Filtering(functions):

#TC01
    def test_film_details(self):
        self.succesful_login()
        self.waitForElementClickable(SEARCHBAR_XPATH2).click()
        self.waitForElementVisible(SEARCHBAR_INPUT).send_keys(MOVIE_NAME_1, Keys.ENTER)
        result = self.waitForElementVisible(RESULT)
        assert result.text == moviename
        self.waitForElementVisible(RESULT).click()
        self.waitForElementVisible(CREW).click()
        self.waitForElementVisible(DETAILS).click()

#TC02
    def test_leaving_comments(self):
        self.succesful_login()
        self.waitForElementClickable(SEARCHBAR_XPATH2).click()
        self.waitForElementVisible(SEARCHBAR_INPUT).send_keys(MOVIE_NAME_1, Keys.ENTER)
        result = self.waitForElementVisible(RESULT)
        assert result.text == moviename
        self.waitForElementVisible(RESULT).click()
        self.waitForElementVisible(LEAVE_COMMENT).click()
        self.waitForElementVisible(COMMENT_INPUT).click()
        self.waitForElementVisible(COMMENT_INPUT_AREA).send_keys(comment)
        self.waitForElementVisible(COMMENT_SUBMIT).click()

#TC03
    def test_checking_comments(self):
        self.succesful_login()
        self.waitForElementVisible(ACTIVITIES).click()
        self.waitForElementVisible(DIARY).click()
        self.take_screenshot("screenshots/latest_reviews.png")
        
