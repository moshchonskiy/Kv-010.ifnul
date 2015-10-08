# coding=utf-8
from selenium.webdriver.common.by import By
from pages.persons.view.person_main_view_page import PersonMainViewPage

__author__ = 'Vadym'

class PersonPapersViewPage(PersonMainViewPage):

    FOR_COUNT_DOCUMENTS_IN_PERSON = (By.XPATH, "//table[@class='table table-hover']/tbody/tr")
    TEXT_CORRECT_PAGE_PERSON_PROFILE = (By.CSS_SELECTOR, ".content-header-title")
    TABLE = (By.XPATH, "//table[@class='table table-hover']")

    def get_data_from_table(self):
        result = []
        # add locators to the array
        count_of_row = self.get_count_row_in_table_documents()
        count_of_column = 12 # from 1 to 12. In table 13 column but last are buttons 'editing', don't need validate this
        for row in range(count_of_row):
            for column in range(count_of_column):
                result.append(self.__get_locators_values_from_table(row, column))

        for index, locator in enumerate(result):
            element_by_locator = self.driver.find_element(*locator).text
            # возможно стоит проверить, не пустое ли тут значение
            result[index] = element_by_locator # replace locator by value found by this locator
        return result

    def get_text_person_profile(self):
        return self.driver.find_element(*self.TEXT_CORRECT_PAGE_PERSON_PROFILE).text

    def get_count_row_in_table_documents(self):
        elements_documents = self.driver.find_elements(*self.FOR_COUNT_DOCUMENTS_IN_PERSON)
        return len(elements_documents)

    def is_table_present(self):
        return self.driver.find_element(*self.TABLE).is_displayed()

    # private methods
    def __get_locators_values_from_table(self, row, column):
        return (By.XPATH, "//table[@class='table table-hover']/tbody/tr[" + str(row + 1) + "]/td[" + str(column + 1) + "]")
