# -*- coding: utf-8 -*-
__author__ = 'Evgen'
from pages.internal_page import InternalPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver


class PersonsPage(InternalPage):

    ADD_PERSON_BUTTON = (By.XPATH, "//a[@ui-sref='root.person.new.main']")
    SHOW_HIDE_FILTERS_BUTTON = (By.XPATH, "//button[contains(@ng-click,'hideFilterFunc')]")
    ACTIVE_ITEMS_PER_PAGE_BUTTON = (By.XPATH, "//button[contains(@class, 'active')]")
    PREVIOUS_PAGE = (By.XPATH, "//li[contains(@title, 'Previous Page')]")
    LAST_NUMBERED_PAGE = (By.XPATH, "//li[contains(@title, 'Last Page')]/preceding-sibling::li[2]/span")
    LAST_PAGE = (By.XPATH, "//li[contains(@title, 'Last Page')]")
    FIELD_CHOOSER_BUTTON = (By.XPATH, "//button[contains(@class, 'field-chooser-button')]")
    FIELD_CHOOSER_RED_CLOSE_BUTTON = (By.XPATH, "//button[parent::div[contains(@class, 'modal-footer')]]")
    INACTIVE_COLUMNS_MODAL = (By.XPATH, "//ul[@class='list-group']/li/label/input[not(@checked)]")
    # Columns dictionary binding number of column to it's name
    COLUMNS_DICT = {
        1: '№',
        2: 'ПІБ',
        3: 'Ім’я',
        4: 'По-батькові',
        5: 'Прізвище',
        6: 'Тип персони',
        7: 'Стать',
        8: 'Сімейний стан',
        9: 'Громад-во',
        10: 'Серія ОС',
        11: 'Номер ОС',
        12: 'Резидент',
        13: 'Місце народж.',
        14: 'Дата народж.',
        15: 'ВЗ',
        16: 'Гуртожиток',
        17: 'Мат. відп'
    }
          
    # TO SEARCH    
    CHOOSE_SURNAME_SEARCH = (By.XPATH, "//div[@class = 'col-sm-12']//option[@value = '0']")
    CHOOSE_PERSON_ID_SEARCH = (By.XPATH, "//div[@class = 'col-sm-12']//option[@value = '1']")
    CHOOSE_NUM_OS_SEARCH = (By.XPATH, "//div[@class = 'col-sm-12']//option[@value = '2']")
    CHOOSE_SERIES_OS_SEARCH = (By.XPATH, "//div[@class = 'col-sm-12']//option[@value = '3']")
    INPUT_GROUP_SEARCH_BUTTON = (By.XPATH, "//div[@class = 'input-group']/input")
    OK_GROUP_SEARCH_BUTTON = (By.XPATH, "//div[@class = 'input-group']/span/button")
    EXPECTED_SURNAME = (By.XPATH, "//tbody[@class='pointer']/tr[@class='ng-scope'][1]/td[2]")
    EXPECTED_PERSON_ID = (By.XPATH, "//tbody[@class='pointer']/tr[@class='ng-scope']/td[1]")
    EXPECTED_NUM_OS = (By.XPATH, "//tbody[@class='pointer']/tr[@class='ng-scope']/td[11]")
    EXPECTED_SERIES_OS = (By.XPATH, "//tbody[@class='pointer']/tr[@class='ng-scope']/td[10]")
    DELETE_FIRST_PERSON_IN_TABLE = (By.XPATH, "//tbody[@class='pointer']/tr[@class='ng-scope'][1]/td[18]//button[3]")

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
    #
    # !!! Important
    #
    # To get selectors on table headers (sorting after click on it)
    # or modal window column selection (which columns display)
    # use methods get_table_selector(N) and get_modal_selector(N)
    # where N is the key of COLUMN_DICT

    def get_modal_selector(self, column_number):
        return By.XPATH, "//span[contains(., '" + PersonsPage.COLUMNS_DICT.get(column_number) + "')]"

    def get_table_selector(self, column_number):
        return By.XPATH, "//a[contains(., '" + PersonsPage.COLUMNS_DICT.get(column_number) + "')]"

    #
    # END OF SELECTORS SECTION
    #


    @property
    def is_this_page(self):
        return self.is_element_visible(self.ADD_PERSON_BUTTON)

    @property
    def add_person_link(self):
        return self.driver.find_element(*self.ADD_PERSON_BUTTON).click()

    @property
    def delete_first_person_in_page(self):
        if self.is_element_visible(self.DELETE_FIRST_PERSON_IN_TABLE):
            self.driver.find_element(*self.DELETE_FIRST_PERSON_IN_TABLE).click()
            self.is_element_present(self.SPINNER_OFF)

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

    def try_get_expected_surname(self, given_surname):
        WebDriverWait(self.driver, 15).until(
            EC.text_to_be_present_in_element(self.EXPECTED_SURNAME, given_surname))
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

    def column_as_list(self, column_number):
        """
        Method get column number as input
        :return: list of text data in column
        """
        list_of_column_text = []
        list_of_column_elements = self.driver.find_elements_by_xpath("//tbody/tr/td[" + str(column_number) + "]")
        for element in list_of_column_elements:
            list_of_column_text.append(element.text)
        return list_of_column_text

    def get_all_hidden_columns(self):
        """
        Method get all columns with class attribute "ng-scope ng-hide"
        :return: list of visible columns number according to COLUMNS_DICT
        """
        visible_columns_list = []
        column_headers = self.driver.find_elements_by_xpath('//thead/tr/th')
        for i in range(len(column_headers)):
            if column_headers[i].get_attribute('class') == 'ng-scope ng-hide':
                visible_columns_list.append(i+1)
        return visible_columns_list

    def show_all_columns(self):
        self.driver.find_element(*PersonsPage.FIELD_CHOOSER_BUTTON).click()
        not_selected_columns =\
            self.driver.find_elements(*PersonsPage.INACTIVE_COLUMNS_MODAL)
        for column_name in not_selected_columns:
            column_name.click()
        self.driver.find_element(*PersonsPage.FIELD_CHOOSER_RED_CLOSE_BUTTON).click()

    def get_number_from_selector(self, selector):
        return self.driver.find_element(*selector).text
