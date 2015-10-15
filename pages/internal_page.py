#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Evgen'

from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import *

from page import Page
import sys


class InternalPage(Page):
    INTERNAL_PAGE = (By.CSS_SELECTOR, "nav")
    USER_DROPDOWN = (By.XPATH, "//i[@class='fa fa-user fa-fw']")
    LOGOUT_BUTTON = (By.XPATH, "//li[@class='dropdown open']//a[@ng-click='header.logout()']")
    PERSON_PAGE_LINK = (By.XPATH, "//a[@ui-sref='root.person.list']")
    ENROLLMENTS_PAGE_LINK = (By.XPATH, "//a[@ui-sref='root.enrolment.list']")
    DICTIONARIES_PAGE_LINK = (By.XPATH, "//a[@ui-sref='root.dictionaries']")
    SPINNER_OFF = (By.XPATH, "//div[@id='spinnerDiv' and @style='display: none;']")
    SELECT_FIRST_SHOWED_YEAR = (By.XPATH, "//div//ul[@ng-model='date']//tbody//tr[1]//td[1]//button//span")
    # SELECT_FIRST_SHOWED_YEAR_IN_PERSONS_BIRTH_DAY_CHOOSER = (By.CSS_SELECTOR, "div ul[ng-model='date'] tbody tr:nth-child(1) td:nth-child(1) button span")
    SELECT_ALL_VISIBLE_YEARS_MONTHS_OR_DAYS = (By.XPATH, "//div//ul[@ng-model='date']//tbody//tr//td//span[@class='ng-binding']")
    GO_TO_LEFT_BUTTON_IN_DATE_PICKER = (By.CSS_SELECTOR, "button.btn.btn-default.btn-sm.pull-left")
    GO_TO_RIGHT_BUTTON_IN_DATE_PICKER = (By.CSS_SELECTOR, "button.btn.btn-default.btn-sm.pull-right")
    ACTIVATE_MONTH_OR_YEAR_CHANGE_BUTTON = (By.CSS_SELECTOR, "button[id*='-title']")

    @property
    def user_dropdown(self):
        return self.driver.find_element(*self.USER_DROPDOWN)

    @property
    def logout_button(self):
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
        elem = self.driver.find_element(*locator)
        elem.clear()
        val = str(value)

        # unicode(value, 'utf-8')
        print type(val)
        for i in len(val):
            elem.send_keys(val[i])

    def choose_year(self, date):
        """
        Method sets year in date picker
        :param date: Date, which need to set up in datetime format
        :return:
        """
        is_choosed = False
        while not is_choosed:
            self.is_element_present(self.SELECT_FIRST_SHOWED_YEAR)
            first_showed_year = self.driver.find_element(*self.SELECT_FIRST_SHOWED_YEAR)
            year_delta = date.year - int(first_showed_year.text)
            if year_delta > 19:
                self.is_element_present(self.GO_TO_RIGHT_BUTTON_IN_DATE_PICKER)
                self.driver.find_element(*self.GO_TO_RIGHT_BUTTON_IN_DATE_PICKER).click()
            elif year_delta < 0:
                self.is_element_present(self.GO_TO_LEFT_BUTTON_IN_DATE_PICKER)
                self.driver.find_element(*self.GO_TO_LEFT_BUTTON_IN_DATE_PICKER).click()
            elif year_delta == 0:
                first_showed_year.click()
                is_choosed = True
            else:
                is_choosed = True
                self.is_element_present(self.SELECT_FIRST_SHOWED_YEAR)
                all_years = self.driver.find_elements(*self.SELECT_ALL_VISIBLE_YEARS_MONTHS_OR_DAYS)
                for year in all_years:
                    if int(year.text) == date.year:
                        year.click()
                        break

    def choose_month(self, date):
        """
        Method sets month in date picker
        :param date: Date, which need to set up in datetime format
        :return:
        """
        self.is_element_present(self.SELECT_ALL_VISIBLE_YEARS_MONTHS_OR_DAYS)
        all_months = self.driver.find_elements(*self.SELECT_ALL_VISIBLE_YEARS_MONTHS_OR_DAYS)
        for month in all_months:
            if month.text == date.strftime('%B'):
                month.click()
                break

    def choose_day(self, date):
        """
        Method sets day in date picker
        :param date: Date, which need to set up in datetime format
        :return:
        """
        self.is_element_present(self.SELECT_ALL_VISIBLE_YEARS_MONTHS_OR_DAYS)
        all_days = self.driver.find_elements(*self.SELECT_ALL_VISIBLE_YEARS_MONTHS_OR_DAYS)
        for day in all_days:
            if int(day.text) == date.day:
                day.click()
                break


    def set_date(self, date_picker_locator, date):
        """
        Method sets date in date picker
        :param date_picker_locator: Selector for element, which activate date picker
        :param date: Date, which need to set up in datetime format
        :return:
        """
        self.is_element_present(date_picker_locator)
        self.driver.find_element(*date_picker_locator).click()
        self.is_element_present(self.ACTIVATE_MONTH_OR_YEAR_CHANGE_BUTTON)
        self.driver.find_element(*self.ACTIVATE_MONTH_OR_YEAR_CHANGE_BUTTON).click()
        self.is_element_present(self.ACTIVATE_MONTH_OR_YEAR_CHANGE_BUTTON)
        self.driver.find_element(*self.ACTIVATE_MONTH_OR_YEAR_CHANGE_BUTTON).click()
        self.choose_year(date)
        self.choose_month(date)
        self.choose_day(date)
