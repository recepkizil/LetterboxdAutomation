from selenium.webdriver.common.by import By

BASE_URL = "https://letterboxd.com/"

#succesful login
SIGN_IN_XPATH = (By.XPATH,"//html[@id='html']//header[@id='header']//nav[@class='main-nav']/ul[@class='navitems']//a[@href='/sign-in/']/span[@class='label']")
USERNAME_INPUT = (By.XPATH,"//html[@id='html']//input[@id='username']")
PASSWORD_INPUT = (By.XPATH, "//html[@id='html']//input[@id='password']")
SIGN_IN_BUTTON = (By.XPATH, "//html[@id='html']//form[@id='signin']/fieldset[@class='fieldset']//input[@value='Sign in']")
USERNAME = "testerhesabim"
PASSWORD = "Receprecep123"


#SO1 - SEARCHING

SEARCHBAR_XPATH = (By.XPATH, "//form[@id='search']/fieldset/input")
MOVIE_NAME_1 = "Inside Out 2"
RESULT = (By.XPATH, "//a[contains(text(),'Inside Out 2')]")   
moviename = "Inside Out 2"
MOVIE_NAME_2 = "Inside Out"
MOVIE_NAME_3 = "djghkjdhgjhjdgkd"
NO_RESULT = (By.XPATH, "//html[@id='html']//div[@id='content']//div[@class='cols-3']/section/h2[@class='section-heading']")
no_result_text = "NO RESULTS"
MOVIE_NAME_4 = "İnside Out 2"
DIRECTORNAME1 = "Kelsey Mann"
RESULT2 = (By.XPATH, "//html[@id='html']//div[@id='content']//div[@class='cols-3']/section/ul[@class='results']//a[@href='/director/kelsey-mann/']")
directorname = "Kelsey Mann"
DIRECTORNAME2 = "Kelsey"
RESULT3 = (By.XPATH, "//html[@id='html']//div[@id='content']//div[@class='cols-3']/section/ul[@class='results']//a[@href='/director/kelsey-mann/']")
DIRECTOR_AND_MOVIE = "Kelsey Mann Inside Out 2"

#SO2 EMPTY SEARCH

EMPTY_SEARCH = " "

#SO3 FILTERING

FILMS_XPATH = (By.XPATH, "//html[@id='html']//header[@id='header']//nav[@class='main-nav']/ul[@class='navitems']//a[@href='/films/']/span[@class='label']")
BROWSE_BY_YEAR = (By.XPATH, "//html[@id='html']//div[@id='content']//section[@class='browse-by']/ul[@class='bar-nav']/li[1]/section[@class='smenu-wrapper']/div[@class='smenu']/label")
DECADE_2020S = (By.XPATH, "//html[@id='html']/body/ul[1]//a[@href='/films/decade/2020s/']")
YEAR_2024 = (By.XPATH, "//html[@id='html']//div[@id='content']/div/section//a[@href='/films/popular/year/2024/']")
FIRST_RESULT = (By.CSS_SELECTOR, ".film-poster-617443 .overlay")
MOVIE_YEAR = (By.XPATH, "//html[@id='html']//div[@id='film-page-wrapper']//section[@class='film-header-group']//a[@href='/films/year/2024/']")
FILTERED_RESULT = (By.XPATH, "//?/p[@innertext='There are 20,868 films released in 2024.']")
BROWSE_BY_GENRE = (By.XPATH, "//html[@id='html']//div[@id='content']//section[@class='browse-by']/ul[@class='bar-nav']/li[4]/section[@class='smenu-wrapper']/div[@class='smenu']/label")
GENRE_DRAMA = (By.XPATH, "//html[@id='html']/body/ul[4]//a[@href='/films/genre/drama/']")
SECOND_RESULT = (By.CSS_SELECTOR, ".film-poster-426406 .overlay")
GENRES = (By.XPATH,"//a[contains(@href, '/film/parasite-2019/genres/')]")
GENRE_CHECK = (By.CSS_SELECTOR, ".capitalize:nth-child(2) .text-slug:nth-child(3)")

SERVICE = (By.XPATH, "//div[@id='content']/div[3]/section/ul/li[5]/section/div/label")
AMAZON_US = (By.XPATH, "//a[contains(@href, '/films/on/amazon-usa/')]")
SERVICE_CHECK = (By.XPATH, "//div[@id='films-browser-list-container']/section/p")

RATING = (By.XPATH, "//div[@id='content']/div[3]/section/ul/li[2]/section/div/label")
TOP250 = (By.XPATH, "//a[contains(text(),'Top 250 Documentaries')]")
TOP250_HEADER = (By.XPATH, "//html[@id='html']//div[@id='content']//div[@class='cols-2']/section//h1[.='Official Top 250 Documentary Films']")
header_text= "Official Top 250 Documentary Films"

POPULAR = (By.XPATH, "//html[@id='html']//div[@id='content']//section[@class='browse-by']/ul[@class='bar-nav']/li[3]/section[@class='smenu-wrapper']/div[@class='smenu']/label")
THIS_YEAR = (By.XPATH, "//html[@id='html']/body/ul[3]//a[@href='/films/popular/this/year/']")
FIRST_FILM = (By.CSS_SELECTOR, ".film-poster-617443 .overlay")

OTHER = (By.CSS_SELECTOR, ".smenu-menu:nth-child(14) > .smenu-selected")
COUNTRY_LANGUAGE = (By.XPATH, "//html[@id='html']/body/ul[6]//a[@href='/countries/']]")

BROWSE_BY_GENRE2 = (By.XPATH, "//html[@id='html']//div[@id='content-nav']/div[1]/section[5]/div[@class='smenu']/label")
GENRE_DRAMA2 = (By.XPATH, "//html[@id='html']/body/ul[4]/li[@class='divider-line']/ul//a[@href='/films/popular/year/2024/genre/drama/']")
PICK_FIRST = (By.CSS_SELECTOR, ".film-poster-842301 .overlay")
MOVIE_YEAR2 = (By.XPATH, "//html[@id='html']//div[@id='film-page-wrapper']//section[@class='film-header-group']//a[@href='/films/year/2024/']")
GENRES2 = (By.XPATH, "//html[@id='html']//div[@id='tabbed-content']//a[@href='/film/challengers/genres/']")
GENRE_CHECK2 = (By.CSS_SELECTOR, "div#tab-genres > div:nth-of-type(1) > p > a:nth-of-type(1)")
