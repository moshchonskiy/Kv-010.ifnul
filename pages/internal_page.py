#!/usr/bin/env python
# -*- coding: utf-8 -*-
from decorators.error_handling_dec import  ErrorHandlerPO

__author__ = 'Evgen'

from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import *
from page import Page
from time import sleep


class InternalPage(Page):
    INTERNAL_PAGE = (By.CSS_SELECTOR, "nav")
    USER_DROPDOWN = (By.XPATH, "//i[@class='fa fa-user fa-fw']")
    LOGOUT_BUTTON = (By.XPATH, "//li[@class='dropdown open']//a[@ng-click='header.logout()']")
    PERSON_PAGE_LINK = (By.XPATH, "//a[@ui-sref='root.person.list']")
    ENROLLMENTS_PAGE_LINK = (By.XPATH, "//a[@ui-sref='root.enrolment.list']")
    DICTIONARIES_PAGE_LINK = (By.XPATH, "//a[@ui-sref='root.dictionaries']")

    SELECT_FIRST_SHOWED_YEAR = (By.XPATH, "//div//ul[@ng-model='date']//tbody//tr[1]//td[1]//button//span")
    # SELECT_ALL_VISIBLE_YEARS_MONTHS_OR_DAYS = (By.XPATH, "//ul[@ng-model='date']//tbody//tr//td//button//span[@class='ng-binding']")
    SELECT_ALL_VISIBLE_YEARS_MONTHS_OR_DAYS = (By.XPATH, "//ul[@ng-model='date']//tbody//tr//td//button//span")
    GO_TO_LEFT_BUTTON_IN_DATE_PICKER = (By.CSS_SELECTOR, "button.btn.btn-default.btn-sm.pull-left")
    GO_TO_RIGHT_BUTTON_IN_DATE_PICKER = (By.CSS_SELECTOR, "button.btn.btn-default.btn-sm.pull-right")
    ACTIVATE_MONTH_OR_YEAR_CHANGE_BUTTON = (By.CSS_SELECTOR, "button[id*='-title']")

    @ErrorHandlerPO("current page is not internal page")
    def is_current_page(self):
        return self.wait.until(visibility_of_element_located(self.INTERNAL_PAGE))

    @property
    def user_dropdown(self):
        self.is_element_visible(self.USER_DROPDOWN)
        return self.driver.find_element(*self.USER_DROPDOWN)

    @property
    def logout_button(self):
        self.is_element_visible(self.LOGOUT_BUTTON)
        return self.driver.find_element(*self.LOGOUT_BUTTON)

    @property
    def is_this_page(self):
        return self.is_element_visible(self.INTERNAL_PAGE)

    @property
    def persons_page_link(self):
        return self.driver.find_element(*self.PERSON_PAGE_LINK)

    @property
    def enrollments_page_link(self):
        return self.driver.find_element(*self.ENROLLMENTS_PAGE_LINK)

    @property
    def dictionaries_page_link(self):
        return self.driver.find_element(*self.DICTIONARIES_PAGE_LINK)

    def is_element_present(self, locator):
        try:
            return self.wait.until(presence_of_element_located(locator))
        except WebDriverException:
            return False

    def emulation_of_input(self, locator, value):
        """
        Method emulates one by one symbols input into input form
        :param locator: Selector for element, which activate input field
        :param value: Value, which need to fill in in input form. Can be String or int format.
        :return:
        """
        elem = self.driver.find_element(*locator)
        elem.clear()
        if type(value) == int:
            value = str(value)
        for i in value:
            elem.send_keys(i)

    def choose_year(self, date, el):
        """
        Method sets year in date picker
        :param date: Date, which need to set up in datetime format
        :return:
        """
        is_choosed = False
        while not is_choosed:
            self.is_element_present(self.SELECT_FIRST_SHOWED_YEAR)
            first_showed_year = el.find_element(*self.SELECT_FIRST_SHOWED_YEAR)
            year_delta = date.year - int(first_showed_year.text)
            if year_delta > 19:
                self.is_element_present(self.GO_TO_RIGHT_BUTTON_IN_DATE_PICKER)
                el.find_element(*self.GO_TO_RIGHT_BUTTON_IN_DATE_PICKER).click()
            elif year_delta < 0:
                self.is_element_present(self.GO_TO_LEFT_BUTTON_IN_DATE_PICKER)
                el.find_element(*self.GO_TO_LEFT_BUTTON_IN_DATE_PICKER).click()
            elif year_delta == 0:
                first_showed_year.click()
                is_choosed = True
            else:
                is_choosed = True
                self.is_element_present(self.SELECT_FIRST_SHOWED_YEAR)
                all_years = el.find_elements(*self.SELECT_ALL_VISIBLE_YEARS_MONTHS_OR_DAYS)
                for year in all_years:
                    if year.text != "" and int(year.text) == date.year:
                        year.click()
                        break

    def choose_month(self, date, el):
        """
        Method sets month in date picker
        :param date: Date, which need to set up in datetime format
        :return:
        """
        self.is_element_present(self.SELECT_ALL_VISIBLE_YEARS_MONTHS_OR_DAYS)
        all_months = el.find_elements(*self.SELECT_ALL_VISIBLE_YEARS_MONTHS_OR_DAYS)
        for month in all_months:
            if month.text != "" and month.text == date.strftime('%B'):
                month.click()
                break

    def choose_day(self, date, el):
        """
        Method sets day in date picker
        :param date: Date, which need to set up in datetime format
        :return:
        """
        self.is_element_present(self.SELECT_ALL_VISIBLE_YEARS_MONTHS_OR_DAYS)
        all_days = el.find_elements(*self.SELECT_ALL_VISIBLE_YEARS_MONTHS_OR_DAYS)
        for day in all_days:
            if day.text != "" and int(day.text) == date.day:
                day.click()
                break


    def set_date(self, date_picker_locator, date):
        """
        Method sets date in date picker
        :param date_picker_locator: Selector for element, which activate date picker
        :param date: Date, which need to set up in datetime format
        :return:
        """
        self.is_element_visible(date_picker_locator)
        elem = self.driver.find_element(*date_picker_locator)
        elem.click()
        el = elem.find_element_by_xpath("..")
        self.is_element_present(self.ACTIVATE_MONTH_OR_YEAR_CHANGE_BUTTON)
        el.find_element(*self.ACTIVATE_MONTH_OR_YEAR_CHANGE_BUTTON).click()
        self.is_element_present(self.ACTIVATE_MONTH_OR_YEAR_CHANGE_BUTTON)
        el.find_element(*self.ACTIVATE_MONTH_OR_YEAR_CHANGE_BUTTON).click()
        self.choose_year(date, el)
        self.choose_month(date, el)
        self.choose_day(date, el)
