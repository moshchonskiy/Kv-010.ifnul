# coding=utf-8
from selenium.webdriver.common.by import By
from pages.persons.view.person_main_view_page import PersonMainViewPage

__author__ = 'Vadym'

class PersonEnrollmentViewPage(PersonMainViewPage):

    FOR_COUNT_ENROLLMENT_IN_PERSON = (By.XPATH, "//tbody[@class='pointer']/tr")
    FOR_COUNT_VISIBLE_COLUMN = (By.XPATH, "//table/thead/tr/th[not(@class='ng-scope ng-hide')]")
    TEXT_CORRECT_PAGE_PERSON_PROFILE = (By.CSS_SELECTOR, ".content-header-title")
    TABLE_ON_THE_PAGE_ENROLLMENT = (By.CSS_SELECTOR, ".table.table-bordered")

    def get_data_from_table(self):
        result = []
        # add locators to the array
        count_of_row = self.get_count_row_in_table_enrollment()
        count_of_column = self.get_count_column_in_table_enrollment()
        for row in range(count_of_row):
            for column in range(count_of_column):
                result.append(self.__get_locators_values_from_table(row, column))

        for index, locator in enumerate(result):
            element_by_locator = self.driver.find_element(*locator).text
            result[index] = element_by_locator # replace locator by value found by this locator
        return result

    def is_table_enrollment_present(self):
        return self.driver.find_element(*self.TABLE_ON_THE_PAGE_ENROLLMENT).is_displayed()

    def get_text_person_profile(self):
        return self.driver.find_element(*self.TEXT_CORRECT_PAGE_PERSON_PROFILE).text

    def get_count_row_in_table_enrollment(self):
        elements_documents = self.driver.find_elements(*self.FOR_COUNT_ENROLLMENT_IN_PERSON)
        return len(elements_documents)

    def get_count_column_in_table_enrollment(self):
        elements_documents = self.driver.find_elements(*self.FOR_COUNT_VISIBLE_COLUMN)
        return len(elements_documents)

    # private methods
    def __get_locators_values_from_table(self, row, column):
        return (By.XPATH, "//tbody/tr[" + str(row + 1) + "]/"
                            "td[not(@class='ng-binding ng-scope ng-hide')][" + str(column + 1) + "]")
