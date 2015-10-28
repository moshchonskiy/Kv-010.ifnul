from selenium.webdriver.common.by import By
from fixtures.decorators import ErrorHandler

from pages.internal_page import InternalPage

__author__ = 'Denys'


class DictionariesPage(InternalPage):
    DICTIONARIES_PAGE = (By.XPATH, "//i[@class ='fa fa-book text-danger']")
    DICTIONARIES_DROPDOWN = (By.XPATH, "//select[@ng-click ='pickDictionary()']")
    DICTIONARIES_PAGE_TABLE = (By.XPATH, "//table")
    BUTTON_DISPLAY_BY_10 = (By.XPATH, "//div[contains(@class,'ng-table-counts')]/button[1]")
    BUTTON_DISPLAY_BY_25 = (By.XPATH, "//div[contains(@class,'ng-table-counts')]/button[2]")
    BUTTON_DISPLAY_BY_50 = (By.XPATH, "//div[contains(@class,'ng-table-counts')]/button[3]")
    BUTTON_DISPLAY_BY_100 = (By.XPATH, "//div[contains(@class,'ng-table-counts')]/button[4]")
    PAGE_BUTTON_NEXT = (By.XPATH, "//ul[@class='pagination ng-table-pagination']/li/a[@ng-switch-when='next']")
    PAGE_BUTTON_PREV = (By.XPATH, "//ul[@class='pagination ng-table-pagination']/li/a[@ng-switch-when='prev']")

    TABLE_HEAD_CELL = "//table/thead/tr/td[%d]"
    TABLE_HEAD_LAST_CELL = "//table/thead/tr/td[last()]"

    TABLE_BODY_CELL = ("//table/tbody/tr[%d]/td[%d]")
    TABLE_BODY_LAST_CELL_IN_I_ROW = ("//table/tbody/tr[%d]/td[last()]")
    TABLE_BODY_LAST_CELL_IN_LAST_ROW = ("//table/tbody/tr[last()]/td[last()]")

    @ErrorHandler("Dictionary page is not current")
    def is_this_page(self):
        return self.is_element_visible(self.DICTIONARIES_PAGE)

    def try_get_table(self):
        return self.is_element_visible(self.DICTIONARIES_PAGE_TABLE)

    def try_get_dictionaries_select_elem(self):
        return self.is_element_visible(self.DICTIONARIES_DROPDOWN)

    def try_get_button_10(self):
        return self.driver.find_element(*self.BUTTON_DISPLAY_BY_10)

    def try_get_button_25(self):
        return self.driver.find_element(*self.BUTTON_DISPLAY_BY_25)

    def try_get_button_50(self):
        return self.driver.find_element(*self.BUTTON_DISPLAY_BY_50)

    def try_get_button_100(self):
        return self.driver.find_element(*self.BUTTON_DISPLAY_BY_100)

    def try_get_page_button_next(self):
        return self.is_element_visible(self.PAGE_BUTTON_NEXT)

    def try_get_page_button_prev(self):
        return self.is_element_visible(self.PAGE_BUTTON_PREV)

    def try_get_table_head_cell_i(self, i):
        return self.is_element_visible((By.XPATH, self.TABLE_HEAD_CELL % i))

    def try_get_table_head_cell_last(self):
        return self.is_element_visible((By.XPATH, self.TABLE_HEAD_LAST_CELL))

    def try_get_table_body_cell_i_j(self, i, j):
        return self.is_element_visible((By.XPATH, self.TABLE_BODY_CELL % (i, j)))

    def try_get_table_body_last_cell_in_i_row(self, i):
        return self.is_element_visible((By.XPATH, self.TABLE_BODY_LAST_CELL_IN_I_ROW % i))

    def try_get_table_body_last_cell_in_last_row(self):
        return self.is_element_visible((By.XPATH, self.TABLE_BODY_LAST_CELL_IN_LAST_ROW))
