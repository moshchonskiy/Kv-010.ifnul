# coding: utf8
from pages.internal_page import InternalPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class PersonsPage(InternalPage):
    #TO SEARCH
    ADD_PERSON_BUTTON               = (By.XPATH, "//button[contains(@class,'btn-success')]")
    CHOOSE_SURNAME_SEARCH           = (By.XPATH, "//div[@class='col-sm-12']//option[@value='0']")
    CHOOSE_PERSON_ID_SEARCH         = (By.XPATH, "//div[@class='col-sm-12']//option[@value='1']")
    CHOOSE_NUM_OS_SEARCH            = (By.XPATH, "//div[@class='col-sm-12']//option[@value='2']")
    CHOOSE_SERIES_OS_SEARCH         = (By.XPATH, "//div[@class='col-sm-12']//option[@value='3']")
    INPUT_GROUP_SEARCH_BUTTON       = (By.XPATH, "//div[@class='input-group']/input")
    OK_GROUP_SEARCH_BUTTON          = (By.XPATH, "//div[@class='input-group']/span/button")
    EXPECTED_SURNAME                = (By.XPATH, "//tbody[@class='pointer']/tr[@class='ng-scope']/td[2]")
    EXPECTED_PERSON_ID              = (By.XPATH, "//tbody[@class='pointer']/tr[@class='ng-scope']/td[1]")
    EXPECTED_NUM_OS                 = (By.XPATH, "//tbody[@class='pointer']/tr[@class='ng-scope']/td[11]")
    EXPECTED_SERIES_OS              = (By.XPATH, "//tbody[@class='pointer']/tr[@class='ng-scope']/td[10]")
    #TO FILTER
    REFRESH_UPPER_BUTTON            = (By.XPATH, "")
    REFRESH_BOTTOM_BUTTON           = (By.XPATH, "")
    GENDER_MALE_CHECKBOX            = (By.XPATH, "//div[@class='panel-group']/div[1]/div[2]/div[@class='panel-body']/div[1]/label/input")
    GENDER_FEMALE_CHECKBOX          = (By.XPATH, "//div[@class='panel-group']/div[1]/div[2]/div[@class='panel-body']/div[2]/label/input")
    GENDER_NOT_DEFINED_CHECKBOX     = (By.XPATH, "//div[@class='panel-group']/div[1]/div[2]/div[@class='panel-body']/div[3]/label/input")
    TYPE_APPLICANT_CHECKBOX         = (By.XPATH, "//div[@class='panel-group']/div[2]/div[2]/div[@class='panel-body']/div[1]/label/input")
    TYPE_STUDENT_CHECKBOX           = (By.XPATH, "//div[@class='panel-group']/div[2]/div[2]/div[@class='panel-body']/div[2]/label/input")
    TYPE_SCIENTIST_CHECKBOX         = (By.XPATH, "//div[@class='panel-group']/div[2]/div[2]/div[@class='panel-body']/div[3]/label/input")
    TYPE_EMPLOYEE_CHECKBOX          = (By.XPATH, "//div[@class='panel-group']/div[2]/div[2]/div[@class='panel-body']/div[4]/label/input")
    TYPE_GRADUATE_CHECKBOX          = (By.XPATH, "//div[@class='panel-group']/div[2]/div[2]/div[@class='panel-body']/div[5]/label/input")
    TYPE_OUTSIDER_CHECKBOX          = (By.XPATH, "//div[@class='panel-group']/div[2]/div[2]/div[@class='panel-body']/div[6]/label/input")
    NEED_HOSTEL_CHECKBOX            = (By.XPATH, "//div[@class='panel-group']/div[3]/div[2]/div[@class='panel-body']/div[1]/label/input")
    DONT_NEED_HOSTEL_CHECKBOX       = (By.XPATH, "//div[@class='panel-group']/div[3]/div[2]/div[@class='panel-body']/div[2]/label/input")
    BOUND_TO_MILITARY_CHECKBOX      = (By.XPATH, "//div[@class='panel-group']/div[4]/div[2]/div[@class='panel-body']/div[1]/label/input")
    NOT_BOUND_TO_MILITARY_CHECKBOX  = (By.XPATH, "//div[@class='panel-group']/div[4]/div[2]/div[@class='panel-body']/div[2]/label/input")
    RESIDENT_FOREIGNER_CHECKBOX     = (By.XPATH, "//div[@class='panel-group']/div[5]/div[2]/div[@class='panel-body']/div[1]/label/input")
    RESIDENT_NOT_FOREIGNER_CHECKBOX = (By.XPATH, "//div[@class='panel-group']/div[5]/div[2]/div[@class='panel-body']/div[2]/label/input")



    @property
    def is_this_page(self):
        return self.is_element_visible(self.ADD_PERSON_BUTTON)

    @property
    def add_person_link(self):
        return self.driver.find_element_by_xpath(*self.ADD_PERSON_BUTTON)

    #to all filters


    #gender (male, female, not defined)


    #type (applicant, student, scientist, employee, graduate, outsider)


    #need for hostel (need, doesn`t need)


    #bound to military service(bound, isn`t bound)


    #resident(foreigner, isn`t foreigner)



    #to all searches
    def try_get_input_group(self):
        return self.is_element_visible(self.INPUT_GROUP_SEARCH_BUTTON)

    def try_get_ok_button(self):
        return self.is_element_visible(self.OK_GROUP_SEARCH_BUTTON)

    #surname search
    def try_get_choose_surname(self):
        return self.is_element_visible(self.CHOOSE_SURNAME_SEARCH)

    def try_get_expected_surname(self, given_surname):
        self.wait.until(EC.text_to_be_present_in_element(self.EXPECTED_SURNAME, given_surname))
        return self.is_element_visible(self.EXPECTED_SURNAME)

    #persone_id search
    def try_get_choose_person_id(self):
        return self.is_element_visible(self.CHOOSE_PERSON_ID_SEARCH)

    def try_get_expected_person_id(self, given_person_id):
        self.wait.until(EC.text_to_be_present_in_element(self.EXPECTED_PERSON_ID, given_person_id))
        return self.driver.find_element(*self.EXPECTED_PERSON_ID)

    #num_os search
    def try_get_choose_num_os(self):
        return self.is_element_visible(self.CHOOSE_NUM_OS_SEARCH)

    def try_get_expected_num_os(self, given_num_os):
        self.wait.until(EC.text_to_be_present_in_element(self.EXPECTED_NUM_OS, given_num_os))
        return self.driver.find_element(*self.EXPECTED_NUM_OS)

    #series_os search
    def try_get_choose_series_os(self):
        return self.is_element_visible(self.CHOOSE_SERIES_OS_SEARCH)

    def try_get_expected_series_os(self, given_series_os):
        self.wait.until(EC.text_to_be_present_in_element(self.EXPECTED_SERIES_OS, given_series_os))
        return self.driver.find_element(*self.EXPECTED_SERIES_OS)

