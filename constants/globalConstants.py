from selenium.webdriver.common.by import By

BASE_URL = "https://letterboxd.com/"

#succesful login
SIGN_IN_XPATH = (By.XPATH,"//html[@id='html']//header[@id='header']//nav[@class='main-nav']/ul[@class='navitems']//a[@href='/sign-in/']/span[@class='label']")
USERNAME_INPUT = (By.XPATH,"//html[@id='html']//input[@id='username']")
PASSWORD_INPUT = (By.XPATH, "//html[@id='html']//input[@id='password']")
SIGN_IN_BUTTON = (By.XPATH, "//html[@id='html']//form[@id='signin']/fieldset[@class='fieldset']//input[@value='Sign in']")
USERNAME = "testerhesabim"
PASSWORD = "Receprecep123."


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

OTHER = (By.XPATH, "//html[@id='html']//div[@id='content']//section[@class='browse-by']/ul[@class='bar-nav']/li[6]/section[@class='smenu-wrapper']/div[@class='smenu']/label")
COUNTRY_LANGUAGE = (By.XPATH, "//html[@id='html']/body/ul[6]//a[@href='/countries/']")
TURKIYE = (By.ID, "film-world-map-map-country-TR")

BROWSE_BY_GENRE2 = (By.XPATH, "//html[@id='html']//div[@id='content-nav']/div[1]/section[5]/div[@class='smenu']/label")
GENRE_DRAMA2 = (By.XPATH, "//html[@id='html']/body/ul[4]/li[@class='divider-line']/ul//a[@href='/films/popular/year/2024/genre/drama/']")
PICK_FIRST = (By.CSS_SELECTOR, ".film-poster-842301 .overlay")
MOVIE_YEAR2 = (By.XPATH, "//html[@id='html']//div[@id='film-page-wrapper']//section[@class='film-header-group']//a[@href='/films/year/2024/']")
GENRES2 = (By.XPATH, "//html[@id='html']//div[@id='tabbed-content']//a[@href='/film/challengers/genres/']")
GENRE_CHECK2 = (By.CSS_SELECTOR, "div#tab-genres > div:nth-of-type(1) > p > a:nth-of-type(1)")

#SO4
SEARCHBAR_XPATH2 = (By.XPATH,"//html[@id='html']//header[@id='header']//nav[@class='main-nav']/ul[@class='navitems']/li[7]/a[@href='#']")
SEARCHBAR_INPUT = (By.XPATH, "//html[@id='html']//input[@id='search-q']")
CREW = (By.XPATH, "//html[@id='html']//a[@id='crew']")
DETAILS = (By.XPATH, "//html[@id='html']//div[@id='tabbed-content']//a[@href='/film/inside-out-2-2024/details/']")
LEAVE_COMMENT = (By.XPATH, "//html[@id='html']//section[@id='userpanel']//a[@href='#add-this-film']")
COMMENT_INPUT = (By.XPATH, "//*[@id='frm-review']")
COMMENT_INPUT_AREA = (By.XPATH, "//html[@id='html']//textarea[@id='frm-review']")
comment = "I loved it"
COMMENT_SUBMIT = (By.XPATH, "//html[@id='html']//input[@id='diary-entry-submit-button']")

MYACCOUNT = (By.XPATH, "/html/body/header/section/div[1]/div/nav/ul/li[1]")
MYREVIEWS = (By.XPATH, "//html[@id='html']//header[@id='header']//nav[@class='main-nav']/ul[@class='navitems']//ul[@class='subnav']//a[@href='/testerhesabim/films/reviews/']")

COMMENT_TEXT_AREA = (By.XPATH, "//html[@id='html']//div[@id='content']/div/section[2]/ul//p[.='I loved it']")
my_comment = "I loved it"

#SO5
MOVIE_NAME_5 = "Dune"
MOVIE5 = (By.XPATH,"//html[@id='html']//div[@id='content']/div[@class='content-wrap']/div/section/ul[@class='results']/li[1]/div[@class='film-detail-content']/h2[@class='headline-2 prettify']/span[@class='film-title-wrapper']/a[@href='/film/dune-2021/']")
comment2 = "Great movie"

SIGN_OUT = (By.XPATH, "//html[@id='html']//a[@id='sign-out']")


#SO6
comment3 = "My favorite movie"
YOUR_REVIEW = (By.XPATH,"//html[@id='html']//section[@id='my-reviews']//a[@href='/testerhesabim/film/dune-2021/reviews/']")
ACTIVITIES = (By.XPATH,"//html[@id='html']//header[@id='header']//nav[@class='main-nav']/ul[@class='navitems']//a[@href='/activity/']/span[@class='icon']")
EDIT_BUTTON = (By.XPATH,"//html[@id='html']//table[@id='diary-table']/tbody/tr[1]/td[9]//a[@href='#']/span[@class='icon']")
CLOSE_BUTTON = (By.XPATH, "//html[@id='html']//div[@id='cboxClose']")
DIARY = (By.XPATH,"//html[@id='html']//div[@id='content']/div/section//a[@href='/testerhesabim/films/diary/']")
DELETE_BUTTON = (By.XPATH,"//html[@id='html']//a[@id='diary-entry-delete-button']")


