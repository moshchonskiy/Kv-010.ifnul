# -*- coding: utf-8 -*-
from pages.internal_page import *
from model.user import User
import pytest

__author__ = 'yioteh'


class TestSortingPerson():
    def test_sorting_person(self, app):
        column_number = 1
        app.ensure_logout()
        app.login(User.Admin())
        pers_page = app.persons_page
        pers_page.is_this_page
        pers_page.show_all_columns()
        pers_page.is_element_present(InternalPage.SPINNER_OFF)
        #
        # Looping over columns starts here
        # Except of person_type = 6th column
        #
        list_of_all_columns_values = []                                         # resulting list of all columns values
        pers_page.driver.find_element(*pers_page.LAST_PAGE).click()
        pers_page.is_element_present(InternalPage.SPINNER_OFF)

        # How many pages do we have in pagination
        looping_over_pagination = int(pers_page.get_number_from_selector(pers_page.LAST_NUMBERED_PAGE))
        for page_count in range(looping_over_pagination - 1):
            pers_page.is_element_present(InternalPage.SPINNER_OFF)
            pers_page.driver.find_element(*pers_page.PREVIOUS_PAGE).click()
            list_of_all_columns_values.extend(pers_page.column_as_list(column_number))

        pers_page.is_element_present(InternalPage.SPINNER_OFF)
        pers_page.driver.find_element(*pers_page.get_table_selector(column_number)).click()   # sort column

        pers_page.is_element_present(InternalPage.SPINNER_OFF)
        items_per_page = int(pers_page.get_number_from_selector(pers_page.ACTIVE_ITEMS_PER_PAGE_BUTTON))
        column_after_clicking = pers_page.column_as_list(column_number)

        assert sorted(list_of_all_columns_values, reverse=True,
                      key=unicode.lower)[:items_per_page] == column_after_clicking
