__author__ = 'Evgen'
from internal_page import InternalPage
from selenium.webdriver.common.by import By
from ui_map import PersonsPageMap as ppm
from selenium.webdriver.remote.webdriver import WebDriver


class PersonsPage(InternalPage):


   # driver= WebDriver  # using for development purpose, comment this line after finish

    @property
    def is_this_page(self):
        return self.is_element_visible((By.XPATH, ppm.AddPersonButtonXPATH))

    @property
    def add_person_link(self):
        return self.driver.find_element_by_xpath(ppm.AddPersonButtonXPATH)
