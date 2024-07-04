import time
import pytest
from functions.helpers import functions
from constants.globalConstants import *
from selenium.webdriver import Keys

@pytest.mark.usefixtures("setup")
class Test_EmptySearch(functions):

#TC01
    def test_empty_searching(self):
        self.waitForElementClickable(SEARCHBAR_XPATH).click()
        self.waitForElementVisible(SEARCHBAR_XPATH).send_keys(EMPTY_SEARCH, Keys.ENTER)
        noResult = self.waitForElementVisible(NO_RESULT)
        assert noResult.text == no_result_text
