import time
import pytest
from functions.helpers import functions
from constants.globalConstants import *
from selenium.webdriver import Keys

@pytest.mark.usefixtures("setup")
class Test_Searching(functions):

#TC01
    def test_searching_with_moviename(self):
        self.waitForElementClickable(SEARCHBAR_XPATH).click()
        self.waitForElementVisible(SEARCHBAR_XPATH).send_keys(MOVIE_NAME_1, Keys.ENTER)
        result = self.waitForElementVisible(RESULT)
        assert result.text == moviename

#TC02   
    def test_searching_with_partial_moviename(self):
        searchbar = self.waitForElementClickable(SEARCHBAR_XPATH).click()
        self.waitForElementVisible(SEARCHBAR_XPATH).send_keys(MOVIE_NAME_2, Keys.ENTER)
        result = self.waitForElementVisible(RESULT)
        assert result.text == moviename
#TC03  
    def test_searching_with_invalid_moviename(self):
        self.waitForElementClickable(SEARCHBAR_XPATH).click()
        self.waitForElementVisible(SEARCHBAR_XPATH).send_keys(MOVIE_NAME_3, Keys.ENTER)
        noResult = self.waitForElementVisible(NO_RESULT)
        assert noResult.text == no_result_text

#TC04
    def test_searching_with_turkish_characters(self):
        self.waitForElementClickable(SEARCHBAR_XPATH).click()
        self.waitForElementVisible(SEARCHBAR_XPATH).send_keys(MOVIE_NAME_4, Keys.ENTER)
        result = self.waitForElementVisible(RESULT)
        assert result.text == moviename
#TC05
    def test_searching_with_directorname(self):
        self.waitForElementClickable(SEARCHBAR_XPATH).click()
        self.waitForElementVisible(SEARCHBAR_XPATH).send_keys(DIRECTORNAME1, Keys.ENTER)
        result2 = self.waitForElementVisible(RESULT2)
        assert result2.text == directorname

#TC06
    def test_searching_with_incomplete_directorname(self):
        self.waitForElementClickable(SEARCHBAR_XPATH).click()
        self.waitForElementVisible(SEARCHBAR_XPATH).send_keys(DIRECTORNAME2, Keys.ENTER)
        result3 = self.waitForElementVisible(RESULT3)
        assert result3.text == directorname

#TC07 FAIL
    def test_searching_with_both_names(self):
        self.waitForElementClickable(SEARCHBAR_XPATH).click()
        self.waitForElementVisible(SEARCHBAR_XPATH).send_keys(DIRECTOR_AND_MOVIE, Keys.ENTER)
        result4 = self.waitForElementVisible(RESULT)
        time.sleep(5)
        assert result4.text == moviename

