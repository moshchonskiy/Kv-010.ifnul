from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

__author__ = 'dmakstc'


class TestTable:
    def __init__(self, driver, locator, row_xpath="/tbody/tr[./td]", cell_xpath="/td"):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        self.table_xpath = locator[1]
        self.by = locator[0]
        self.row_xpath = row_xpath
        self.cell_xpath = cell_xpath

    def try_get_table(self):
        try:
            return self.wait.until(visibility_of_element_located((self.by, self.table_xpath)))
        except WebDriverException:
            return False

    def try_get_cell_ij(self, i, j):
        tmp_path = self.table_xpath + (self.row_xpath + "[%d]" + self.cell_xpath + "[%d]") % (i, j)
        return self.driver.find_element(self.by, tmp_path)

    def try_get_table_data_height(self):
        return len(self.driver.find_elements(self.by, self.table_xpath + self.row_xpath))

    def try_get_table_data_width(self, i=1):
        if self.try_get_table_data_height() > 0:
            return len(self.driver.find_elements(self.by,
                                                 self.table_xpath + (self.row_xpath + "[%d]" + self.cell_xpath) % i))
