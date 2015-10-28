from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from decorators.error_handling_dec import ErrorHandler

__author__ = 'Evgen'
from selenium.webdriver.common.by import By

from page import Page


class LoginPage(Page):
    USERNAME_FIELD = (By.ID, "inputLogin")
    PASSWORD_FIELD = (By.ID, "inputPassword")
    LOGIN_CHECKBOX = (By.XPATH, "//input[@type='checkbox']")
    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")
    LOGIN_PAGE = (By.NAME, "auth")

    @property
    def username_field(self):
        return self.driver.find_element(*self.USERNAME_FIELD)

    @property
    def password_field(self):
        return self.driver.find_element(*self.PASSWORD_FIELD)

    @property
    def login_checkbox(self):
        return self.driver.find_element(*self.LOGIN_CHECKBOX)

    @property
    def submit_button(self):
        return self.driver.find_element(*self.SUBMIT_BUTTON)

    @property
    def is_this_page(self):
        return self.is_element_visible(self.LOGIN_PAGE)

    @ErrorHandler("current page is not Login page")
    def is_current_page(self):
        return self.wait.until(visibility_of_element_located(self.LOGIN_PAGE))