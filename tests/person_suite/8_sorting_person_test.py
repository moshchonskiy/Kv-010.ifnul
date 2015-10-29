# -*- coding: utf-8 -*-
import allure
from allure.constants import AttachmentType
import pytest


__author__ = 'yioteh'


@pytest.mark.usefixtures('pre_login')
class TestSortingPerson():
    def test_sorting_person(self):
        # variable list
        list_of_all_columns_values = []
        column_number = 1
        try:

            with pytest.allure.step("Prepare TestSortingPerson"):
                pers_page = self.app.persons_page
                pers_page.is_current_page()
            with pytest.allure.step("Check all checkbox"):
                pers_page.show_all_columns()
            # Looping over columns starts here
            # Except of person_type = 6th column

            with pytest.allure.step("start generate test array of value"):
                # resulting list of all columns values
                pers_page.try_get_last_page_ref().click()

                pers_page.wait_until_page_generate()
                # How many pages do we have in pagination
                looping_over_pagination = int(pers_page.get_number_from_selector(pers_page.LAST_NUMBERED_PAGE))
                for page_count in range(looping_over_pagination - 1):
                    pers_page.wait_until_page_generate()
                    pers_page.driver.find_element(*pers_page.PREVIOUS_PAGE).click()
                    list_of_all_columns_values.extend(pers_page.column_as_list(column_number))

            with pytest.allure.step("start generate tested data"):
                pers_page.wait_until_page_generate()
                pers_page.driver.find_element(*pers_page.get_table_selector(column_number)).click()  # sort column
                pers_page.wait_until_page_generate()
                items_per_page = int(pers_page.get_number_from_selector(pers_page.ACTIVE_ITEMS_PER_PAGE_BUTTON))
                column_after_clicking = pers_page.column_as_list(column_number)

            assert sorted(list_of_all_columns_values, reverse=True)[:items_per_page] == column_after_clicking
        except AssertionError:
            allure.attach('screenshot', self.app.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
            raise
