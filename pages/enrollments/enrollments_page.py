# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep
from pages.internal_page import InternalPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from exceptions import AssertionError

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
    SEARCH_SELECT_DROPDOWN = (By.XPATH, "//select[contains(@class, 'form-control')]")
    SEARCH_FIELD = (By.XPATH, "//input[@ng-model='querySearchBy']")
    SUBMIT_SEARCH_BUTTON = (By.XPATH, "//button[contains(@ng-click, 'startSearch')]")
    ADD_NEW_ENROLLMENT_BUTTON = (By.XPATH, "//a[@href='#/enrolment/new/main']")
    NEXT_TABLE_PAGE_BUTTON = (By.XPATH, "//div[@class='raw table-footer']/paging/ul/li[@title='Next Page']/span")
    NEXT_TABLE_PAGE_DISABLED_BUTTON = (
        By.XPATH, "//div[@class='raw table-footer']/paging/ul/li[@class='ng-scope disabled' and @title='Next Page']/span")
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
    NEW_ROW_WAITER = (By.XPATH, "//table/tbody/tr[11]")

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
        Method perform choosing of search method and clicking of submit button
        :param search_by:  person_id,  document_series, document_number, proposal_id
        :param req: Request sends to search field
        :return:
        """
        self.is_this_page
        select = Select(self.search_select_dropdown)
        select.select_by_value(search_by)
        self.search_field_enr.clear()
        self.search_field_enr.send_keys(req)
        self.submit_search_button_enr.click()
        self.is_element_present(self.SPINNER_OFF)

    def search_text_in_column(self, column, text):
        """
        Method searches in wanted column for requested text
        :param column: Column selector
        :param text: String
        :return: List with founded text
        """
        elements = self.driver.find_elements(*column)
        lst = [element.text for element in elements if element.text != text]
        if len(lst) > 0:
            return lst[0]
        else:
            return text

    def search_enrollment(self, search_by, req):
        """
        Method perform choosing of search method and clicking of submit button
        :param search_by:  person_id,  document_series, document_number, proposal_id
        :param req: Request sends to search field
        :return: List with founded text
        """
        self.is_this_page
        select = Select(self.search_select_dropdown)
        select.select_by_value(search_by)
        self.search_field_enr.clear()
        self.search_field_enr.send_keys(req)
        self.submit_search_button_enr.click()
        self.is_element_present(self.SPINNER_OFF)
        # while self.is_element_present(self.NEXT_TABLE_PAGE_BUTTON):
        if search_by is self.SEARCH_METHOD["person_id"]:
            self.search_text_in_column(self.PERSON_ID_COLUMN, req)
        elif search_by is self.SEARCH_METHOD["document_series"]:
            self.search_text_in_column(self.DOC_SERIES_COLUMN, req)
        elif search_by is self.SEARCH_METHOD["document_number"]:
            self.search_text_in_column(self.DOC_NUMBER_COLUMN, req)
        elif search_by is self.SEARCH_METHOD["proposal_id"]:
            self.search_text_in_column(self.PROPOSAL_ID_COLUMN, req)

    def search_enrollment_by_person_id(self, person_id):
        """
        Method perform search of enrollment by person ID
        :param person_id: The person ID in string
        :return:
        """
        self.hundred_button.click()
        self.is_element_present(self.SPINNER_OFF)
        return self.search_enrollment(self.SEARCH_METHOD["person_id"], person_id)

    def search_enrollment_by_doc_series(self, doc_series):
        """
        Method perform search of enrollment by document's series
        :param doc_series: String
        :return:
        """
        self.hundred_button.click()
        self.is_element_present(self.SPINNER_OFF)
        return self.search_enrollment(self.SEARCH_METHOD["document_series"], doc_series)

    def search_enrollment_by_doc_number(self, doc_number):
        """
        Method perform search of enrollment by document's number
        :param doc_number: String
        :return:
        """
        self.hundred_button.click()
        self.is_element_present(self.SPINNER_OFF)
        return self.search_enrollment(self.SEARCH_METHOD["document_number"], doc_number)

    def search_enrollment_by_proposal_id(self, proposal_id):
        """
        Method perform search of enrollment by proposal id
        :param proposal_id: String
        :return:
        """
        self.hundred_button.click()
        self.is_element_present(self.SPINNER_OFF)
        return self.search_enrollment(self.SEARCH_METHOD["proposal_id"], proposal_id)

    def table_column_chooser(self, column):
        """
        Method adds column from column chooser
        :param column: constant with column
        :return:
        """
        self.is_this_page
        self.column_chooser_button.click()
        self.is_element_visible(column)
        self.driver.find_element(*column).click()
        self.column_chooser_close_button.click()
        sleep(1)

    def filter_add(self, f_add):
        """
        Method adds a wanted filter
        :param f_add: self.FILTER_WANTED
        :return:
        """
        self.driver.find_element(*f_add).click()

    def filter_by_budget(self, budget=True):
        """
        Method performs filter by budget. Don't use in one test
        :param budget: True is budget, False is not budget
        :return:
        """
        yes_budget = u'✓'
        not_budget = u'✘'
        self.hundred_button.click()
        self.is_element_present(self.SPINNER_OFF)
        self.table_column_chooser(self.COLUMN_BUDGET_ADD)
        if budget:
            self.filter_budget.click()
        else:
            self.filter_not_budget.click()
        self.filter_refresh_button_enr.click()
        self.is_element_present(self.SPINNER_OFF)
        elements = self.driver.find_elements(*self.BUDGET_COLUMN)
        lst = [element.text for element in elements]
        if budget:
            if not_budget in lst:
                return not_budget
            else:
                return yes_budget
        else:
            if yes_budget in lst:
                return yes_budget
            else:
                return not_budget

    def filter_by_privileges(self):
        """
        Method perform a filtering by privileges
        :return:
        """
        priv = u'є пільги'
        self.hundred_button.click()
        self.is_element_present(self.SPINNER_OFF)
        self.filter_add(self.FILTER_PRIVILEGES)
        self.filter_refresh_button_enr.click()
        self.is_element_present(self.SPINNER_OFF)
        elements = self.driver.find_elements(*self.PRIVILEGES_COLUMN)
        lst = [element.text for element in elements if element.text != priv]
        if len(lst) > 0:
            return lst[0]
        else:
            return priv

    def filter_by_not_privileges(self):
        priv = u'пільги відсутні'
        self.hundred_button.click()
        self.is_element_present(self.SPINNER_OFF)
        self.filter_add(self.FILTER_NOT_PRIVILEGES)
        self.filter_refresh_button_enr.click()
        self.is_element_present(self.SPINNER_OFF)
        elements = self.driver.find_elements(*self.PRIVILEGES_COLUMN)
        lst = [element.text for element in elements if element.text != priv]
        if len(lst) > 0:
            return lst[0]
        else:
            return priv

    def filter_mixer(self):
        """
        Method performs mix of different filters
        :return: List of unique values of filtered columns
        """
        self.hundred_button.click()
        self.is_element_present(self.SPINNER_OFF)
        self.table_column_chooser(self.COLUMN_BUDGET_ADD)
        self.filter_add(self.FILTER_BUDGET)
        self.filter_add(self.FILTER_NOT_PRIVILEGES)
        self.filter_add(self.FILTER_NEED_ACCOMMODATION)
        self.filter_refresh_button_enr.click()
        self.is_element_present(self.SPINNER_OFF)
        elements = self.driver.find_elements(*self.BUDGET_COLUMN)
        elements1 = self.driver.find_elements(*self.PRIVILEGES_COLUMN)
        elements2 = self.driver.find_elements(*self.ACCOMMODATION_COLUMN)
        lst = list()
        for element in elements:
            if element.text not in lst:
                lst.append(element.text)
        for element in elements1:
            if element.text not in lst:
                lst.append(element.text)
        for element in elements2:
            if element.text not in lst:
                lst.append(element.text)
        return lst
