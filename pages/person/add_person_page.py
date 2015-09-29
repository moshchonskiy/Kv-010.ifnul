__author__ = 'Evgen'

from pages.internal_page import InternalPage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class AddPersonPage(InternalPage):

    ADD_PERSON_PAGE = (By.XPATH, "//label[@for='inputDocSeries']")

    @property
    def is_this_page(self):
        return self.is_element_visible(self.ADD_PERSON_PAGE)

    def add_new_person(self, person):
        self
