import time
import pytest
from functions.helpers import functions
from constants.globalConstants import *
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import Select


@pytest.mark.usefixtures("setup")
class Test_Filtering(functions):

#TC01
    def test_filter_by_year(self):
        self.waitForElementClickable(FILMS_XPATH).click()
        self.waitForElementClickable(BROWSE_BY_YEAR).click()
        self.waitForElementClickable(DECADE_2020S).click()
        self.waitForElementClickable(YEAR_2024).click()
        assert "films/popular/year/2024/" in self.driver.current_url
        self.waitForElementClickable(FIRST_RESULT).click()
        movie_year = self.waitForElementVisible(MOVIE_YEAR)
        assert movie_year.text == "2024"

#TC02
    def test_filter_by_genre(self):
        self.waitForElementClickable(FILMS_XPATH).click()
        self.waitForElementClickable(BROWSE_BY_GENRE).click()
        self.waitForElementClickable(GENRE_DRAMA).click()
        assert "https://letterboxd.com/films/genre/drama/" in self.driver.current_url
        time.sleep(2)
        self.waitForElementClickable(SECOND_RESULT).click()
        self.waitForElementClickable(GENRES).click()
        genre = self.waitForElementVisible(GENRE_CHECK)
        assert genre.text == "Drama"

#TC03
    def test_filter_by_service(self):
        self.waitForElementClickable(FILMS_XPATH).click()
        self.waitForElementClickable(SERVICE).click()
        self.waitForElementClickable(AMAZON_US).click()
        assert "/films/on/amazon-usa/" in self.driver.current_url 
        service = self.waitForElementVisible(SERVICE_CHECK)
        assert "films available on Amazon US." in service.text 

#TC04 
    def test_filter_by_rating(self):
        self.waitForElementClickable(FILMS_XPATH).click()
        time.sleep(2)
        self.waitForElementVisible(RATING).click()
        time.sleep(2)
        self.waitForElementClickable(TOP250).click()
        time.sleep(2)
        assert "/jack/list/official-top-250-documentary-films/" in self.driver.current_url
        header = self.waitForElementVisible(TOP250_HEADER)
        assert header.text == header_text

#TC05
    def test_filter_by_popularity(self):
        self.waitForElementClickable(FILMS_XPATH).click()
        self.waitForElementVisible(POPULAR).click()
        self.waitForElementVisible(THIS_YEAR).click()
        self.waitForElementVisible(FIRST_FILM).click()
        movie_year = self.waitForElementVisible(MOVIE_YEAR)
        assert movie_year.text == "2024"
    
# #TC06
    def test_filter_by_other(self):
        self.waitForElementClickable(FILMS_XPATH).click()
        time.sleep(2)
        other = self.waitForElementClickable(OTHER)
        self.moveToElement(other)
        self.waitForElementClickable(COUNTRY_LANGUAGE).click()
        self.waitForElementClickable(TURKIYE).click()
        time.sleep(2) 
        self.newTab() 
        assert "/films/country/turkey/" in self.driver.current_url

#TC07
    def test_multiple_filtering(self):
        self.waitForElementClickable(FILMS_XPATH).click()
        self.waitForElementClickable(BROWSE_BY_YEAR).click()
        self.waitForElementClickable(DECADE_2020S).click()
        self.waitForElementClickable(YEAR_2024).click()
        assert "films/popular/year/2024/" in self.driver.current_url
        self.waitForElementClickable(BROWSE_BY_GENRE2).click()
        self.waitForElementClickable(GENRE_DRAMA2).click()
        self.waitForElementClickable(PICK_FIRST).click()
        movie_year2 = self.waitForElementVisible(MOVIE_YEAR2)
        assert movie_year2.text == "2024"
        time.sleep(3)
        self.driver.execute_script("window.scrollBy(0,150)")
        self.waitForElementClickable(GENRES2).click()
        genre2 = self.waitForElementVisible(GENRE_CHECK2)
        assert genre2.text == "Drama" 

    


