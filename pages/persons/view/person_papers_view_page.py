# coding=utf-8
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.persons.view.person_main_view_page import PersonMainViewPage

__author__ = 'Vadym'

class PersonPapersViewPage(PersonMainViewPage):

    FOR_COUNT_DOCUMENTS_IN_PERSON = (By.XPATH, "//table[@class='table table-hover']/tbody/tr")
    FOR_COUNT_VISIBLE_COLUMN = (By.XPATH, "//table[@class='table table-hover']"
                                          "/thead/tr/td[not(@class='ng-binding ng-hide')]")
    TEXT_CORRECT_PAGE_PERSON_PROFILE = (By.CSS_SELECTOR, ".content-header-title")
    TABLE = (By.XPATH, "//table[@class='table table-hover']")
    ROW = "/tbody/tr[./td[not(@class='ng-binding ng-hide')]]"
    CELL = "/td[not(@class='editing')]"
    TEXT_DOES_NOT_HAVE_PAPERS = (By.XPATH, "//div[@class='col-xs-10']/h4")

    def get_text_not_have_papers(self):
        return self.driver.find_element(*self.TEXT_DOES_NOT_HAVE_PAPERS)

    def get_data_from_table(self):
        result = []
        # add locators to the array
        count_of_row = self.get_count_row_in_table_documents()
        count_of_column = self.get_count_column_in_table_documents()
        for row in range(count_of_row):
            for column in range(count_of_column):
                result.append(self.__get_locators_values_from_table(row, column))

        for index, locator in enumerate(result):
            element_by_locator = self.driver.find_element(*locator).text
            result[index] = element_by_locator # replace locator by value found by this locator
        return result

    def get_text_person_profile(self):
        return self.driver.find_element(*self.TEXT_CORRECT_PAGE_PERSON_PROFILE).text

    def get_count_row_in_table_documents(self):
        elements_documents = self.driver.find_elements(*self.FOR_COUNT_DOCUMENTS_IN_PERSON)
        return len(elements_documents)

    def get_count_column_in_table_documents(self):
        elements_documents = self.driver.find_elements(*self.FOR_COUNT_VISIBLE_COLUMN)
        return len(elements_documents)

    def is_table_present(self):
        try:
            self.driver.find_element(*self.TABLE)
        except NoSuchElementException:
            return False
        return True

    # private methods
    def __get_locators_values_from_table(self, row, column):
        return (By.XPATH, "//table[@class='table table-hover']/tbody/tr[" + str(row + 1) + "]/td[" + str(column + 1) + "]")
