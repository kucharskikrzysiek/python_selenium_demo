from selenium import webdriver
import os
from pages.landingPage import LandingPage
from pages.searchResultsPage import SearchResultsPage


class Application:

    def __init__(self):
        import os
        self.driver = webdriver.Chrome(os.path.join(os.path.dirname(os.path.realpath(__file__)), "chromedriver.exe"))
        self.landing_page = LandingPage(self.driver)
        self.search_results_page = SearchResultsPage(self.driver)

    def quit(self):
        self.driver.quit()

    def search_toster(self):
        self.landing_page.open()
        assert self.landing_page.logo.is_displayed()
        try:
            self.landing_page.accept_terms.click()
        except TimeoutError:
            pass
        self.landing_page.search_box.send_keys("toster")
        self.landing_page.button_search.click()
        assert self.search_results_page.searching_phrase_label.text.lower().__contains__("toster")
        articles = self.search_results_page.articles
        for article in articles:
            article_title = article.text.lower()
            assert article_title.__contains__("toster"), f"Article '{article_title}' does not contain word 'toster'"
