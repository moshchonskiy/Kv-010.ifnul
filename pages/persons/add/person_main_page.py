__author__ = 'Evgen'

from pages.internal_page import InternalPage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class PersonMainPage(InternalPage):

    ADD_PERSON_PAGE = (By.XPATH, "//label[@for='inputDocSeries']")
    SAVE_NEW_PERSON_BUTTON = (By.XPATH, "//button[@class='btn btn-block btn-success']")
    NEXT_BUTTON = (By.XPATH, "//button[@ng-click='goToNextTab(1)']")
    BACK_BUTTON = (By.XPATH, "//button[@ng-click='goToNextTab(-1)']")

    @property
    def is_this_page(self):
        return self.is_element_visible(self.ADD_PERSON_PAGE)

    def add_new_person(self, person):
        self
