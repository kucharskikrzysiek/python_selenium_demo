from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from model.urlAddresses import UrlAddresses


class LandingPage(BasePage):

    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.driver = driver

    ELEMENTS = {
        "logo": (By.CSS_SELECTOR, "img[itemprop = logo]"),
        "accept terms": (By.CSS_SELECTOR, "button[data-role=close-and-accept-consent]"),
        "search box": (By.CSS_SELECTOR, "input[data-role=search-input]"),
        "button search": (By.CSS_SELECTOR, "button[data-role=search-button]"),
    }

    def open(self):
        self.driver.get(UrlAddresses().allegro_main_page)
        return self

    @property
    def search_box(self):
        return self.get_element(self.ELEMENTS["search box"])

    @property
    def accept_terms(self):
        return self.get_element(self.ELEMENTS["accept terms"])

    @property
    def logo(self):
        return self.get_element(self.ELEMENTS["logo"])

    @property
    def button_search(self):
        return self.get_element(self.ELEMENTS["button search"])
