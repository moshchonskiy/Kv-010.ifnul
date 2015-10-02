# -*- coding: utf-8 -*-
__author__ = 'Evgen'
from pages.internal_page import InternalPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
from exceptions import AssertionError


class EnrollmentsPage(InternalPage):
    SEARCH_SELECT_DROPDOWN = (By.XPATH, "//select[contains(@class, 'form-control')]")
    SEARCH_FIELD = (By.XPATH, "//input[@ng-model='querySearchBy']")
    SUBMIT_SEARCH_BUTTON = (By.XPATH, "//button[contains(@ng-click, 'startSearch')]")
    ADD_NEW_ENROLLMENT_BUTTON = (By.XPATH, "//a[@href='#/enrolment/new/main']")
    TEN_BUTTON = (By.XPATH, "//div[@class='btn-group pull-right']/button[1]")
    TWENTY_BUTTON = (By.XPATH, "//div[@class='btn-group pull-right']/button[2]")
    FIFTY_BUTTON = (By.XPATH, "//div[@class='btn-group pull-right']/button[3]")
    HUNDRED_BUTTON = (By.XPATH, "//div[@class='btn-group pull-right']/button[4]")
    PERSON_ID_COLUMN = (By.XPATH, "//table/tbody/tr/td[2]")
    PROPOSAL_ID_COLUMN = (By.XPATH, "//table/tbody/tr/td[3]")
    BUDGET_COLUMN = (By.XPATH, "//table/tbody/tr/td[4]")
    DOC_SERIES_COLUMN = (By.XPATH, "//table/tbody/tr/td[10]")
    DOC_NUMBER_COLUMN = (By.XPATH, "//table/tbody/tr/td[11]")
    FILTER_REFRESH_BUTTON = (By.XPATH, "//div[contains(@class,'col-md-2')]/p[1]/button")
    FILTER_BUDGET_HEADER = (By.XPATH, "//div[@class ='panel panel-default ng-isolate-scope'][1]/div[1]//a")
    FILTER_BUDGET = (By.XPATH, "//div[@class ='panel panel-default ng-isolate-scope'][1]/div[2]/div/div[1]/label")
    FILTER_NOT_BUDGET = (By.XPATH, "//div[@class ='panel panel-default ng-isolate-scope'][1]/div[2]/div/div[2]/label")
    FILTER_CONTRACT_HEADER = (By.XPATH, "//div[@class ='panel panel-default ng-isolate-scope'][2]/div[1]//a")
    FILTER_CONTRACT = (By.XPATH, "//div[@class ='panel panel-default ng-isolate-scope'][2]/div[2]/div/div[1]/label")
    FILTER_NOT_CONTRACT = (By.XPATH, "//div[@class ='panel panel-default ng-isolate-scope'][2]/div[2]/div/div[2]/label")
    FILTER_PRIVILEGES_HEADER = (By.XPATH, "//div[@class ='panel panel-default ng-isolate-scope'][3]/div[1]//a")
    FILTER_PRIVILEGES = (By.XPATH, "//div[@class ='panel panel-default ng-isolate-scope'][3]/div[2]/div/div[1]/label")
    FILTER_NOT_PRIVILEGES = (By.XPATH, "//div[@class ='panel panel-default ng-isolate-scope'][3]/div[2]/div/div[2]/label")
    FILTER_ACCOMMODATION_HEADER = (By.XPATH, "//div[@class ='panel panel-default ng-isolate-scope'][4]/div[1]//a")
    FILTER_NEED_ACCOMMODATION = (By.XPATH, "//div[@class ='panel panel-default ng-isolate-scope'][4]/div[2]/div/div[1]/label")
    FILTER_NOT_NEED_ACCOMMODATION = (By.XPATH, "//div[@class ='panel panel-default ng-isolate-scope'][4]/div[2]/div/div[2]/label")
    FILTER_ENROLL_TYPE_HEADER = (By.XPATH, "//div[@class ='panel panel-default ng-isolate-scope'][5]/div[1]//a")
    FILTER_ENR_TYPE_CERTIFICATE = (By.XPATH, "//div[@class ='panel panel-default ng-isolate-scope'][5]/div[2]/div/div[1]/label")
    FILTER_ENR_TYPE_EXAM = (By.XPATH, "//div[@class ='panel panel-default ng-isolate-scope'][5]/div[2]/div/div[2]/label")
    FILTER_ENR_TYPE_NOT_ZNO = (By.XPATH, "//div[@class ='panel panel-default ng-isolate-scope'][5]/div[2]/div/div[14]/label")
    FILTER_SUBDIVISION_HEADER = (By.XPATH, "//div[@class ='panel panel-default ng-isolate-scope'][6]/div[1]//a")
    COLUMN_CHOOSER_BUTTON = (By.XPATH, "//button[contains(@class,'field-chooser-button')]")
    BUDGET_COLUMN_ADD = (By.XPATH, "//li[4]//*[@id='showHideHeader']")
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
    def column_chooser_button(self):
        return self.driver.find_element(*self.COLUMN_CHOOSER_BUTTON)

    @property
    def budget_column_add_select(self):
        return self.driver.find_element(*self.BUDGET_COLUMN_ADD)

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

    def search_enrollment_by_person_id(self, person_id):
        """
        Method perform search of enrollment by person ID
        :param person_id: The person ID in string
        :return:
        """
        self.hundred_button.click()
        self.is_element_visible(self.NEW_ROW_WAITER)
        select = Select(self.search_select_dropdown)
        select.select_by_value("0")
        self.search_field_enr.clear()
        self.search_field_enr.send_keys(person_id)
        self.submit_search_button_enr.click()
        sleep(6)
        person_ids = self.driver.find_elements(*self.PERSON_ID_COLUMN)
        lst = list()
        for cur_id in person_ids:
            if cur_id.text != person_id:
                lst.append(cur_id.text)
        if len(lst) > 0:
            return lst[0]
        else:
            return person_id

    def search_enrollment_by_doc_series(self, doc_series):
        """
        Method perform search of enrollment by document's series
        :param doc_series:
        :return:
        """
        self.hundred_button.click()
        self.is_element_visible(self.NEW_ROW_WAITER)
        select = Select(self.search_select_dropdown)
        select.select_by_value("1")
        self.search_field_enr.clear()
        self.search_field_enr.send_keys(doc_series)
        self.submit_search_button_enr.click()
        sleep(6)
        series = self.driver.find_elements(*self.DOC_SERIES_COLUMN)
        lst = list()
        for cur_series in series:
            if cur_series.text != doc_series:
                lst.append(cur_series.text)
        if len(lst) > 0:
            return lst[0]
        else:
            return doc_series

    def search_enrollment_by_doc_number(self, doc_number):
        """
        Method perform search of enrollment by document's number
        :param doc_number:
        :return:
        """
        self.hundred_button.click()
        self.is_element_visible(self.NEW_ROW_WAITER)
        select = Select(self.search_select_dropdown)
        select.select_by_value("2")
        self.search_field_enr.clear()
        self.search_field_enr.send_keys(doc_number)
        self.submit_search_button_enr.click()
        sleep(6)
        numbers = self.driver.find_elements(*self.DOC_NUMBER_COLUMN)
        nums = list()
        for cur_num in numbers:
            if cur_num.text != doc_number:
                nums.append(cur_num.text)
        if len(nums) > 0:
            return nums[0]
        else:
            return doc_number

    def search_enrollment_by_proposal_id(self, proposal_id):
        """
        Method perform search of enrollment by proposal id
        :param proposal_id:
        :return:
        """
        self.hundred_button.click()
        self.is_element_visible(self.NEW_ROW_WAITER)
        select = Select(self.search_select_dropdown)
        select.select_by_value("3")
        self.search_field_enr.clear()
        self.search_field_enr.send_keys(proposal_id)
        self.submit_search_button_enr.click()
        sleep(6)
        pro_ids = self.driver.find_elements(*self.PROPOSAL_ID_COLUMN)
        ids = list()
        for cur_id in pro_ids:
            if cur_id.text != proposal_id:
                ids.append(cur_id.text)
        if len(ids) > 0:
            return ids[0]
        else:
            return proposal_id

    def filter_by_budget(self, budget=True):
        """
        Method performs filter by budget
        :param budget: True is budget, False is not budget
        :return:
        """
        budget = "✓"
        not_budget = "✘"
        self.hundred_button.click()
        self.is_element_visible(self.NEW_ROW_WAITER)
        self.column_chooser_button.click()
        self.is_element_visible(self.BUDGET_COLUMN_ADD)
        self.budget_column_add_select.click()
        self.column_chooser_close_button.click()
        self.filter_budget.click()
        self.filter_refresh_button_enr.click()
        sleep(5)
        elements = self.driver.find_elements(*self.BUDGET_COLUMN)
        for element in elements:
            print element.text.encode("UTF-8")

        # self.hundred_button.click()
        # sleep(6)