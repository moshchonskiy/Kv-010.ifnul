__author__ = 'Evgen'

from internal_page import InternalPage
from selenium.webdriver.common.by import By


class NewPersonPage(InternalPage):

    @property
    def is_this_page(self):
        return self.is_element_visible((By.XPATH, "//label[@for='inputDocSeries']"))
