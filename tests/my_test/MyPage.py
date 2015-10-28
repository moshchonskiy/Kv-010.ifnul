from selenium.webdriver.common.by import By
from pages.page import Page

__author__ = 'dmakstc'


class MyPage(Page):
    INTERNAL_PAGE = (By.CSS_SELECTOR, "nav")
    PERSON_PAGE_LINK = (By.XPATH, "//a[@ui-sref='root.person.list']")
    ENROLLMENTS_PAGE_LINK = (By.XPATH, "//a[@ui-sref='root.enrolment.list']")
    DICTIONARIES_PAGE_LINK = (By.XPATH, "//a[@ui-sref='root.dictionaries']")
    SPINNER_OFF = (By.XPATH, "//div[@id='spinnerDiv' and @style='display: none;']")


    def is_this_page(self):
        return self.is_element_visible(self.INTERNAL_PAGE)