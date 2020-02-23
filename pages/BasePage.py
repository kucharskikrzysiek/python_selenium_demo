from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def get_element(self, element_tuple):
        self.wait_for_page_loaded()
        self.wait.until(EC.presence_of_element_located(element_tuple))
        return self.driver.find_element(element_tuple[0], element_tuple[1])

    def wait_for_page_loaded(self):
        self.wait.until(lambda d: d.execute_script("return document.readyState=='complete'"))

    def get_elements(self, element_tuple):
        self.wait.until(EC.presence_of_element_located(element_tuple))
        return self.driver.find_elements(element_tuple[0], element_tuple[1])
