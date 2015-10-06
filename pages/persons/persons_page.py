__author__ = 'Evgen'
from pages.internal_page import InternalPage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class PersonsPage(InternalPage):

    ADD_PERSON_BUTTON          = (By.XPATH, "//button[contains(@class,'btn-success')]")

    CHOOSE_SURNAME_SEARCH      = (By.XPATH, "//div[@class = 'col-sm-12']//option[@value = '0']")
    CHOOSE_PERSON_ID_SEARCH    = (By.XPATH, "//div[@class = 'col-sm-12']//option[@value = '1']")
    CHOOSE_NUM_OS_SEARCH       = (By.XPATH, "//div[@class = 'col-sm-12']//option[@value = '2']")
    CHOOSE_SERIES_OS_SEARCH    = (By.XPATH, "//div[@class = 'col-sm-12']//option[@value = '3']")

    INPUT_GROUP_SEARCH_BUTTON  = (By.XPATH, "//div[@class = 'input-group']/input")
    OK_GROUP_SEARCH_BUTTON     = (By.XPATH, "//div[@class = 'input-group']/span/button")

    EXPECTED_SURNAME           = (By.XPATH, "//tbody[@class='pointer']/tr[@class='ng-scope']/td[2]")
    EXPECTED_PERSON_ID         = (By.XPATH, "//tbody[@class='pointer']/tr[@class='ng-scope']/td[1]")
    EXPECTED_NUM_OS            = (By.XPATH, "//tbody[@class='pointer']/tr[@class='ng-scope']/td[11]")
    EXPECTED_SERIES_OS         = (By.XPATH, "//tbody[@class='pointer']/tr[@class='ng-scope']/td[10]")


    @property
    def is_this_page(self):
        return self.is_element_visible(self.ADD_PERSON_BUTTON)

    @property
    def add_person_link(self):
        return self.driver.find_element_by_xpath(*self.ADD_PERSON_BUTTON)

    #to all searches
    def try_get_input_group(self):
        return self.is_element_visible(self.INPUT_GROUP_SEARCH_BUTTON)

    def try_get_ok_button(self):
        return self.is_element_visible(self.OK_GROUP_SEARCH_BUTTON)

    #surname search
    def try_get_choose_surname(self):
        return self.is_element_visible(self.CHOOSE_SURNAME_SEARCH)

    def try_get_expected_surname(self):
        return self.driver.find_element(*self.EXPECTED_SURNAME)

    #persone_id search
    def try_get_choose_person_id(self):
        return self.is_element_visible(self.CHOOSE_PERSON_ID_SEARCH)

    def try_get_expected_person_id(self):
        return self.driver.find_element(*self.EXPECTED_PERSON_ID)

    #num_os search
    def try_get_choose_num_os(self):
        return self.is_element_visible(self.CHOOSE_NUM_OS_SEARCH)

    def try_get_expected_num_os(self):
        return self.driver.find_element(*self.EXPECTED_NUM_OS)

    #series_os search
    def try_get_choose_series_os(self):
        return self.is_element_visible(self.CHOOSE_SERIES_OS_SEARCH)

    def try_get_expected_series_os(self):
        return self.driver.find_element(*self.EXPECTED_SERIES_OS)

