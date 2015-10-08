# coding: utf8
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.internal_page import InternalPage

GIVEN_SURNAME = u'Прізвище'
GIVEN_PERSON_ID = '14'
GIVEN_NUM_OS = '999999'
GIVEN_SERIES_OS = 'ss'

TIME_TO_WAIT = 3


class PersonsPage(InternalPage):
    # TO SEARCH
    ADD_PERSON_BUTTON = (By.XPATH, "//button[contains(@class,'btn-success')]")
    CHOOSE_SURNAME_SEARCH = (By.XPATH, "//div[@class = 'col-sm-12']//option[@value = '0']")
    CHOOSE_PERSON_ID_SEARCH = (By.XPATH, "//div[@class = 'col-sm-12']//option[@value = '1']")
    CHOOSE_NUM_OS_SEARCH = (By.XPATH, "//div[@class = 'col-sm-12']//option[@value = '2']")
    CHOOSE_SERIES_OS_SEARCH = (By.XPATH, "//div[@class = 'col-sm-12']//option[@value = '3']")
    INPUT_GROUP_SEARCH_BUTTON = (By.XPATH, "//div[@class = 'input-group']/input")
    OK_GROUP_SEARCH_BUTTON = (By.XPATH, "//div[@class = 'input-group']/span/button")
    EXPECTED_SURNAME = (By.XPATH, "//tbody[@class='pointer']/tr[@class='ng-scope']/td[2]")
    EXPECTED_PERSON_ID = (By.XPATH, "//tbody[@class='pointer']/tr[@class='ng-scope']/td[1]")
    EXPECTED_NUM_OS = (By.XPATH, "//tbody[@class='pointer']/tr[@class='ng-scope']/td[11]")
    EXPECTED_SERIES_OS = (By.XPATH, "//tbody[@class='pointer']/tr[@class='ng-scope']/td[10]")

    # TO FILTER
    # There would be absolute passes. It is awful, it may be changed.
    # But classes in XML file are named all the same, and stuff like div[1] doesn't work.
    # REFRESH_UPPER_BUTTON            = (By.XPATH, "")
    # REFRESH_BOTTOM_BUTTON           = (By.XPATH, "")

    # SEX_MALE_CHECKBOX               = (By.XPATH, "html/body/div[1]/div[2]/div/div[2]/div[1]/accordion/div/div[1]/div[2]/div/div[1]/label")
    # SEX_FEMALE_CHECKBOX             = (By.XPATH, "")
    # SEX_NOT_DEFINED_CHECKBOX        = (By.XPATH, "")

    # TYPE_APPLICANT_CHECKBOX         = (By.XPATH, "")
    # TYPE_STUDENT_CHECKBOX           = (By.XPATH, "")
    # TYPE_SCIENTIST_CHECKBOX         = (By.XPATH, "")
    # TYPE_EMPLOYEE_CHECKBOX          = (By.XPATH, "")
    # TYPE_GRADUATE_CHECKBOX          = (By.XPATH, "")
    # TYPE_OUTSIDER_CHECKBOX          = (By.XPATH, "")

    # NEED_HOSTEL_CHECKBOX            = (By.XPATH, "")
    # DONT_NEED_HOSTEL_CHECKBOX       = (By.XPATH, "")

    # BOUND_TO_MILITARY_CHECKBOX      = (By.XPATH, "")
    # NOT_BOUND_TO_MILITARY_CHECKBOX  = (By.XPATH, "")

    # RESIDENT_FOREIGNER_CHECKBOX     = (By.XPATH, "")
    # RESIDENT_NOT_FOREIGNER_CHECKBOX = (By.XPATH, "")



    @property
    def is_this_page(self):
        return self.is_element_visible(self.ADD_PERSON_BUTTON)

    @property
    def add_person_link(self):
        return self.driver.find_element_by_xpath(*self.ADD_PERSON_BUTTON)

    # to all filters


    # sex (male, female, not defined)


    # type (applicant, student, scientist, employee, graduate, outsider)


    # need for hostel (need, doesn`t need)


    # bound to military service(bound, isn`t bound)


    # resident(foreigner, isn`t foreigner)



    # to all searches
    def try_get_input_group(self):
        return self.is_element_visible(self.INPUT_GROUP_SEARCH_BUTTON)

    def try_get_ok_button(self):
        return self.is_element_visible(self.OK_GROUP_SEARCH_BUTTON)

    # surname search
    def try_get_choose_surname(self):
        return self.is_element_visible(self.CHOOSE_SURNAME_SEARCH)

    def try_get_expected_surname(self):
        WebDriverWait(self.driver, TIME_TO_WAIT).until(
            EC.text_to_be_present_in_element(self.EXPECTED_SURNAME, GIVEN_SURNAME))
        return self.is_element_visible(self.EXPECTED_SURNAME)

    # persone_id search
    def try_get_choose_person_id(self):
        return self.is_element_visible(self.CHOOSE_PERSON_ID_SEARCH)

    def try_get_expected_person_id(self):
        WebDriverWait(self.driver, TIME_TO_WAIT).until(
            EC.text_to_be_present_in_element(self.EXPECTED_PERSON_ID, GIVEN_PERSON_ID))
        return self.driver.find_element(*self.EXPECTED_PERSON_ID)

    # num_os search
    def try_get_choose_num_os(self):
        return self.is_element_visible(self.CHOOSE_NUM_OS_SEARCH)

    def try_get_expected_num_os(self):
        WebDriverWait(self.driver, TIME_TO_WAIT).until(
            EC.text_to_be_present_in_element(self.EXPECTED_NUM_OS, GIVEN_NUM_OS))
        return self.driver.find_element(*self.EXPECTED_NUM_OS)

    # series_os search
    def try_get_choose_series_os(self):
        return self.is_element_visible(self.CHOOSE_SERIES_OS_SEARCH)

    def try_get_expected_series_os(self):
        WebDriverWait(self.driver, TIME_TO_WAIT).until(
            EC.text_to_be_present_in_element(self.EXPECTED_SERIES_OS, GIVEN_SERIES_OS))
        return self.driver.find_element(*self.EXPECTED_SERIES_OS)
