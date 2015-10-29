from selenium.webdriver.common.by import By
from pages.internal_page import InternalPage

__author__ = 'Evgen'


class PersonEnrollmentPage(InternalPage):
    ADD_ENROLLMENT = (By.XPATH, ".//*[@ng-click='newEnrolment()']")
    ENROLLMENT_DOC_NUMBER_IN_PERSON = (By.XPATH, ".//*[@class='pointer']/tr/td[11]")

    @property
    def add_enrollment(self):
        return self.is_element_visible(self.ADD_ENROLLMENT)

    @property
    def enrollment_doc_number(self):
        self.is_element_visible(self.ENROLLMENT_DOC_NUMBER_IN_PERSON)
        return self.driver.find_elements(*self.ENROLLMENT_DOC_NUMBER_IN_PERSON)
