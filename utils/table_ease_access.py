from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

__author__ = 'dmakstc'


class TestTable:
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator
        self.wait = WebDriverWait(driver, 15)

    def try_get_table(self):
        try:
            return self.wait.until(visibility_of_element_located(self.locator))
        except WebDriverException:
            return False

    def try_get_cell_ij(self, i, j):
        tmp_path = self.locator[1] + "/tbody/tr[./td][%d]/td[%d]" % (i, j)
        return self.driver.find_element(self.locator[0], tmp_path)

    def try_get_table_data_height(self):
        return len(self.driver.find_elements(self.locator[0], self.locator[1] + "/tbody/tr[./td]"))

    def try_get_table_data_width(self):
        if self.try_get_table_data_height() > 0:
            return len(self.driver.find_elements(self.locator[0], self.locator[1] + "/tbody/tr[./td][1]/td"))
        return 0
