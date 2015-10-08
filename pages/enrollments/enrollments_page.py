# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.expected_conditions import *
from pages.internal_page import InternalPage

__author__ = 'Evgen'


class EnrollmentsPage(InternalPage):
    # def __init__(self, driver, base_url):
    #     self.driver = webdriver.Firefox()
    #     self.base_url = base_url
    #     self.wait = WebDriverWait(driver, 15)

    SEARCH_METHOD = {"person_id": "0",
                     "document_series": "1",
                     "document_number": "2",
                     "proposal_id": "3"
                     }
    FILTER_RESULTS = {"budget": u'✓',
                      "not_budget": u'✘',
                      "privileged": u'є пільги',
                      "not_privileged": u'пільги відсутні',
                      "contract": u'✓',
                      "not_contract": u'✘',
                      "accommodation": u'потреб. гуртож.',
                      "not_accommodation": u'не потреб. гуртож.'
                      }
    SEARCH_SELECT_DROPDOWN = (By.XPATH, "//select[contains(@class, 'form-control')]")
    SEARCH_FIELD = (By.XPATH, "//input[@ng-model='querySearchBy']")
    SUBMIT_SEARCH_BUTTON = (By.XPATH, "//button[contains(@ng-click, 'startSearch')]")
    ADD_NEW_ENROLLMENT_BUTTON = (By.XPATH, "//a[@href='#/enrolment/new/main']")
    NEXT_TABLE_PAGE_BUTTON = (By.CSS_SELECTOR, "li[class='ng-scope'][title='Next Page'] span")
    NEXT_TABLE_PAGE_DISABLED_BUTTON = (By.CSS_SELECTOR, "li[class='ng-scope disabled'][title='Next Page'] span")
    NEXT_TABLE_BUTTON_COUNTER = (By.XPATH, "//li[contains(@title, 'Page')]")
    IF_NEXT_BUTTON_DISABLED = (By.CSS_SELECTOR, "li[class='ng-scope'][title='Next Page'], \
                                                li[class='ng-scope disabled'][title='Next Page']")
    TEN_BUTTON = (By.XPATH, "//div[@class='raw table-footer']//div[@class='btn-group pull-right']/button[1]")
    TWENTY_BUTTON = (By.XPATH, "//div[@class='raw table-footer']//div[@class='btn-group pull-right']/button[2]")
    FIFTY_BUTTON = (By.XPATH, "//div[@class='raw table-footer']//div[@class='btn-group pull-right']/button[3]")
    HUNDRED_BUTTON = (By.XPATH, "//div[@class='raw table-footer']//div[@class='btn-group pull-right']/button[4]")
    PERSON_ID_COLUMN = (By.XPATH, "//table/tbody/tr/td[2]")
    PROPOSAL_ID_COLUMN = (By.XPATH, "//table/tbody/tr/td[3]")
    BUDGET_COLUMN = (By.XPATH, "//table/tbody/tr/td[4]")
    PRIVILEGES_COLUMN = (By.XPATH, "//table/tbody/tr/td[9]")
    DOC_SERIES_COLUMN = (By.XPATH, "//table/tbody/tr/td[10]")
    DOC_NUMBER_COLUMN = (By.XPATH, "//table/tbody/tr/td[11]")
    ACCOMMODATION_COLUMN = (By.XPATH, "//table/tbody/tr/td[12]")
    FILTER_REFRESH_BUTTON = (By.XPATH, "//div[contains(@class,'col-md-2')]/p[1]/button")
    DELETE_FILTER_BUTTON = (By.XPATH, "//div[@class='col-md-2 col-lg-2 filter']//button[@class='close']")
    FILTER_BUDGET_HEADER = (By.XPATH, "//div[@class ='panel panel-default ng-isolate-scope'][1]/div[1]//a")
    FILTER_BUDGET = (By.XPATH, "//div[@class ='panel panel-default ng-isolate-scope'][1]/div[2]/div/div[1]/label")
    FILTER_NOT_BUDGET = (By.XPATH, "//div[@class ='panel panel-default ng-isolate-scope'][1]/div[2]/div/div[2]/label")
    FILTER_CONTRACT_HEADER = (By.XPATH, "//div[@class ='panel panel-default ng-isolate-scope'][2]/div[1]//a")
    FILTER_CONTRACT = (By.XPATH, "//div[@class ='panel panel-default ng-isolate-scope'][2]/div[2]/div/div[1]/label")
    FILTER_NOT_CONTRACT = (By.XPATH, "//div[@class ='panel panel-default ng-isolate-scope'][2]/div[2]/div/div[2]/label")
    FILTER_PRIVILEGES_HEADER = (By.XPATH, "//div[@class ='panel panel-default ng-isolate-scope'][3]/div[1]//a")
    FILTER_PRIVILEGES = (By.XPATH, "//div[@class ='panel panel-default ng-isolate-scope'][3]/div[2]/div/div[1]/label")
    FILTER_NOT_PRIVILEGES = (
        By.XPATH, "//div[@class ='panel panel-default ng-isolate-scope'][3]/div[2]/div/div[2]/label")
    FILTER_ACCOMMODATION_HEADER = (By.XPATH, "//div[@class ='panel panel-default ng-isolate-scope'][4]/div[1]//a")
    FILTER_NEED_ACCOMMODATION = (
        By.XPATH, "//div[@class ='panel panel-default ng-isolate-scope'][4]/div[2]/div/div[1]/label")
    FILTER_NOT_NEED_ACCOMMODATION = (
        By.XPATH, "//div[@class ='panel panel-default ng-isolate-scope'][4]/div[2]/div/div[2]/label")
    FILTER_ENROLL_TYPE_HEADER = (By.XPATH, "//div[@class ='panel panel-default ng-isolate-scope'][5]/div[1]//a")
    FILTER_ENR_TYPE_CERTIFICATE = (
        By.XPATH, "//div[@class ='panel panel-default ng-isolate-scope'][5]/div[2]/div/div[1]/label")
    FILTER_ENR_TYPE_EXAM = (
        By.XPATH, "//div[@class ='panel panel-default ng-isolate-scope'][5]/div[2]/div/div[2]/label")
    FILTER_ENR_TYPE_NOT_ZNO = (
        By.XPATH, "//div[@class ='panel panel-default ng-isolate-scope'][5]/div[2]/div/div[14]/label")
    FILTER_SUBDIVISION_HEADER = (By.XPATH, "//div[@class ='panel panel-default ng-isolate-scope'][6]/div[1]//a")
    COLUMN_CHOOSER_BUTTON = (By.XPATH, "//button[contains(@class,'field-chooser-button')]")
    COLUMN_BUDGET_ADD = (By.XPATH, "//li[4]//*[@id='showHideHeader']")
    COLUMN_CHOOSER_CLOSE_BUTTON = (By.XPATH, "//div[@class='modal-footer']/button")

    @property
    def is_this_page(self):
        return self.is_element_visible(self.ADD_NEW_ENROLLMENT_BUTTON)

    @property
    def search_select_dropdown(self):
        return self.driver.find_element(*self.SEARCH_SELECT_DROPDOWN)

    @property
    def search_field_enr(self):
        return self.driver.find_element(*self.SEARCH_FIELD)

    @property
    def submit_search_button_enr(self):
        return self.driver.find_element(*self.SUBMIT_SEARCH_BUTTON)

    @property
    def filter_refresh_button_enr(self):
        return self.driver.find_element(*self.FILTER_REFRESH_BUTTON)

    @property
    def filter_budget(self):
        return self.driver.find_element(*self.FILTER_BUDGET)

    @property
    def filter_not_budget(self):
        return self.driver.find_element(*self.FILTER_NOT_BUDGET)

    @property
    def column_chooser_button(self):
        return self.driver.find_element(*self.COLUMN_CHOOSER_BUTTON)

    @property
    def column_chooser_close_button(self):
        return self.driver.find_element(*self.COLUMN_CHOOSER_CLOSE_BUTTON)

    @property
    def ten_button(self):
        return self.driver.find_element(*self.TEN_BUTTON)

    @property
    def twenty_button(self):
        return self.driver.find_element(*self.TWENTY_BUTTON)

    @property
    def fifty_button(self):
        return self.driver.find_element(*self.FIFTY_BUTTON)

    @property
    def hundred_button(self):
        return self.driver.find_element(*self.HUNDRED_BUTTON)

    def execute_search(self, search_by, req):
        """
        Method chooses search method and pastes request in search field
        :param search_by:  SEARCH_METHOD["method"]
        :param req: Any wanted string request
        """
        self.is_this_page
        # self.hundred_button.click()
        self.is_element_present(self.SPINNER_OFF)
        select = Select(self.search_select_dropdown)
        select.select_by_value(search_by)
        self.search_field_enr.clear()
        self.search_field_enr.send_keys(req)
        self.submit_search_button_enr.click()
        self.is_element_present(self.SPINNER_OFF)

    def search_text_in_column(self, column, req):
        """
        Method searches for inserted in search field request in a certain column
        :param column: Column selector
        :param req: String
        :return: List with found values. It will return list with correct values if method find only correct ones.
        Opposite, it returns list with incorrect values.
        """
        req = req.lower()
        correct = list()
        incorrect = list()
        web_elem = self.wait.until(presence_of_element_located(self.IF_NEXT_BUTTON_DISABLED))
        if web_elem.get_attribute("class") == "ng-scope disabled":
            elements = self.driver.find_elements(*column)
            for element in elements:
                if element.text.lower().count(req):
                    correct.append(element.text)
                else:
                    incorrect.append(element.text)
            if len(incorrect):
                return incorrect
            else:
                return correct
        else:
            while True:
                elements = self.driver.find_elements(*column)
                for element in elements:
                    if element.text.lower().count(req):
                        correct.append(element.text)
                    else:
                        incorrect.append(element.text)
                new_elem = self.wait.until(presence_of_element_located(self.IF_NEXT_BUTTON_DISABLED))
                if new_elem.get_attribute("class") == "ng-scope disabled":
                    break
                self.driver.find_element(*self.NEXT_TABLE_PAGE_BUTTON).click()
                self.is_element_present(self.SPINNER_OFF)
            if len(incorrect):
                return incorrect
            else:
                return correct

    def search_enrollment(self, search_by, req, ):
        """
        Method performs search of enrollment. For example:
        assert "some request" in ....enrolments_page.search_enrollment(... , .....)
        :param search_by:  SEARCH_METHOD["method"]
        :param req: String. For example "46" or u'текст'
        :return: List with found values. It will return list with correct values if method find only correct ones.
        Opposite, it returns list with incorrect values.
        """
        self.execute_search(search_by, req)
        if search_by is self.SEARCH_METHOD["person_id"]:
            return self.search_text_in_column(self.PERSON_ID_COLUMN, req)
        elif search_by is self.SEARCH_METHOD["document_series"]:
            return self.search_text_in_column(self.DOC_SERIES_COLUMN, req)
        elif search_by is self.SEARCH_METHOD["document_number"]:
            return self.search_text_in_column(self.DOC_NUMBER_COLUMN, req)
        elif search_by is self.SEARCH_METHOD["proposal_id"]:
            return self.search_text_in_column(self.PROPOSAL_ID_COLUMN, req)

    def add_table_columns(self, *columns):
        """
        Method adds one or more columns in table
        :param columns: Column selectors, separated with comas
        """
        self.is_this_page
        self.column_chooser_button.click()
        for column in columns:
            self.is_element_visible(column)
            self.driver.find_element(*column).click()
        self.column_chooser_close_button.click()
        self.is_element_visible(columns[0])

    def add_filters(self, *selectors_tuple):
        """
        Method adds one or more wanted filters
        :param selectors_tuple: Selectors, separated with comas
        """
        self.is_this_page
        for selector in selectors_tuple:
            self.driver.find_element(*selector).click()
        self.filter_refresh_button_enr.click()
        self.is_element_present(self.SPINNER_OFF)

    def get_columns_text(self, *column_tuple):
        """
        Method collects info from given columns and adds it to set. So it is unique values.
        It can take several columns in arguments
        :param column_tuple: Selectors, separated with comas  (self.COLUMN_1, self.COLUMN_2)
        :return: Set with found unique values.
        """
        found = set()
        web_elem = self.wait.until(presence_of_element_located(self.IF_NEXT_BUTTON_DISABLED))
        if web_elem.get_attribute("class") == "ng-scope disabled":
            for column in column_tuple:
                elements = self.driver.find_elements(*column)
                for element in elements:
                    if element.text not in found:
                        found.add(element.text)
            return found
        else:
            while True:
                for column in column_tuple:
                    elements = self.driver.find_elements(*column)
                    for element in elements:
                        if element.text not in found:
                            found.add(element.text)
                new_elem = self.wait.until(presence_of_element_located(self.IF_NEXT_BUTTON_DISABLED))
                if new_elem.get_attribute("class") == "ng-scope disabled":
                    break
                self.driver.find_element(*self.NEXT_TABLE_PAGE_BUTTON).click()
                self.is_element_present(self.SPINNER_OFF)
            return found

    def delete_all_filters(self):
        """
        Method deletes all filters
        """
        self.is_this_page
        elements = self.driver.find_elements(*self.DELETE_FILTER_BUTTON)
        for element in elements:
            element.click()
        self.filter_refresh_button_enr.click()
        self.is_element_present(self.SPINNER_OFF)
