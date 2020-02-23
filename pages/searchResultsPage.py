from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class SearchResultsPage(BasePage):

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    ELEMENTS = {
        "searching phrase label": (By.XPATH, "//h1/span[.='toster']"),
        "articles": (By.XPATH, "//article//h2/a"),
    }

    @property
    def searching_phrase_label(self):
        return self.get_element(self.ELEMENTS["searching phrase label"])

    @property
    def articles(self):
        return self.get_elements(self.ELEMENTS["articles"])

