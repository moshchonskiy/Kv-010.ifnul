# -*- coding: utf-8 -*-
from pages.internal_page import *
from model.application import Application
from model.user import User
from selenium import webdriver
from pytest import *

__author__ = 'yioteh'


class TestSortingPerson():
    driver = webdriver.Firefox()
    base_url = 'http://194.44.198.221/'
    app = Application(driver, base_url)

    def test_sorting_person(self):
        column_number = 3
        self.app.ensure_logout()
        self.app.login(User.Admin())
        pers_page = self.app.persons_page
        pers_page.is_this_page
        pers_page.show_all_columns()
        pers_page.is_element_present(InternalPage.SPINNER_OFF)
        #
        # Looping over columns starts here
        # Except of person_type = 6th column
        #
        list_of_all_columns_values = []         # resulting list of all columns values
        pers_page.driver.find_element(*pers_page.LAST_PAGE).click()
        pers_page.is_element_present(InternalPage.SPINNER_OFF)
        looping_over_pagination = int(pers_page.get_number_from_selector(pers_page.LAST_NUMBERED_PAGE))
        # list_of_all_columns_values.extend(pers_page.column_as_list(column_number))
        print '.'.join(sorted(list_of_all_columns_values, reverse=True, key=unicode.lower))
        for page_count in range(looping_over_pagination - 1):
            pers_page.is_element_present(InternalPage.SPINNER_OFF)
            pers_page.driver.find_element(*pers_page.PREVIOUS_PAGE).click()
            list_of_all_columns_values.extend(pers_page.column_as_list(column_number))
            print '.'.join(sorted(list_of_all_columns_values, reverse=True, key=unicode.lower))
        pers_page.is_element_present(InternalPage.SPINNER_OFF)
        pers_page.driver.find_element(*pers_page.get_table_selector(column_number)).click()   # sort column
        pers_page.is_element_present(InternalPage.SPINNER_OFF)
        items_per_page = int(pers_page.get_number_from_selector(pers_page.ACTIVE_ITEMS_PER_PAGE_BUTTON))
        column_after_clicking = pers_page.column_as_list(column_number)
        print
        print sorted(list_of_all_columns_values, reverse=True, key=unicode.lower)[:items_per_page]
        print column_after_clicking
        assert sorted(list_of_all_columns_values, reverse=True,
                      key=unicode.lower)[:items_per_page] == column_after_clicking
