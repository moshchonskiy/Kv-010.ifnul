__author__ = 'Evgen'

from internal_page import InternalPage
from selenium.webdriver.common.by import By
from pages.ui_map import NewPersonPageMap as npm
from selenium.webdriver.remote.webelement import WebElement


class NewPersonPage(InternalPage):

    @property
    def is_this_page(self):
        return self.is_element_visible((By.XPATH, npm.ThisPageXpath))

    def add_new_person(self, person):
        pass
