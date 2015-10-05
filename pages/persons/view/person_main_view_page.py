# coding=utf-8
from selenium.webdriver.common.by import By
from pages.internal_page import InternalPage

__author__ = 'Administrator'

class PersonMainViewPage(InternalPage):

    PERSON_DOCUMENTS_BUTTON = (By.XPATH, "//a[contains(.,'Документи')]")
    PERSON_ENROLLMENT_BUTTON = (By.XPATH, "//a[contains(.,'Заяви')]")
    PERSON_BUTTON = (By.XPATH, "//a[contains(.,'Персона')]")

    def person_document_button(self):
        return self.driver.find_element(*self.PERSON_ENROLLMENT_BUTTON)

    def person_enrollment_button(self):
        return self.driver.find_element(*self.PERSON_DOCUMENTS_BUTTON)

    def person_current_button(self):
        return self.driver.find_element(*self.PERSON_BUTTON)