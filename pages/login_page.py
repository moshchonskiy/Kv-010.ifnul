__author__ = 'Evgen'
from page import Page
from selenium.webdriver.common.by import By


class LoginPage(Page):
    USERNAME_FIELD = (By.ID, "inputLogin")
    PASSWORD_FIELD = (By.ID, "inputPassword")
    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")
    LOGIN_PAGE = (By.NAME, "auth")

    @property
    def username_field(self):
        return self.driver.find_element(*self.USERNAME_FIELD)

    @property
    def password_field(self):
        return self.driver.find_element(*self.PASSWORD_FIELD)

    @property
    def submit_button(self):
        return self.driver.find_element(*self.SUBMIT_BUTTON)

    @property
    def is_this_page(self):
        return self.is_element_visible(self.LOGIN_PAGE)
