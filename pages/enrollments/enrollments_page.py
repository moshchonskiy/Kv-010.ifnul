__author__ = 'Evgen'
from pages.internal_page import InternalPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class EnrollmentsPage(InternalPage):
    SEARCH_SELECT_DROPDOWN = (By.XPATH, "//select[contains(@class, 'form-control')]")
    SEARCH_FIELD = (By.XPATH, "//input[@ng-model='querySearchBy']")
    SUBMIT_SEARCH_BUTTON = (By.XPATH, "//button[contains(@ng-click, 'startSearch')]")

    @property
    def search_select_dropdown(self):
        return self.driver.find_element(*self.SEARCH_SELECT_DROPDOWN)

    def search_by(self, method):
        """
        Method selects value to search by
        :param method: might be
        :return:
        """
        select = self.search_select_dropdown
