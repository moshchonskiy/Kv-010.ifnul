from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import *

from fixtures.decorators import ErrorHandler

__author__ = 'Evgen'


class Page(object):
    SPINNER_OFF = (By.XPATH, "//div[@id='spinnerDiv' and @style='display: none;']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def is_element_visible(self, locator):
        return self.wait.until(visibility_of_element_located(locator))

    def is_element_present(self, locator):
        try:
            return self.wait.until(presence_of_element_located(locator))
        except WebDriverException:
            return False

    @ErrorHandler("page generation is failed")
    def wait_until_page_generate(self):
        return self.wait.until(presence_of_element_located(self.SPINNER_OFF))
