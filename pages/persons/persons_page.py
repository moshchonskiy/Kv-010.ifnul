__author__ = 'Evgen'
from pages.internal_page import InternalPage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class PersonsPage(InternalPage):

    ADD_PERSON_BUTTON = (By.XPATH, "//button[contains(@class,'btn-success')]")


    @property
    def is_this_page(self):
        return self.is_element_visible(self.ADD_PERSON_BUTTON)

    @property
    def add_person_link(self):
        return self.driver.find_element_by_xpath(*self.ADD_PERSON_BUTTON)