__author__ = 'Evgen'
from page import Page
from selenium.webdriver.common.by import By
from ui_map import LoginPageMap as lpm


class LoginPage(Page):
    @property
    def username_field(self):
        return self.driver.find_element_by_id(lpm.UsernameFieldID)

    @property
    def password_field(self):
        return self.driver.find_element_by_id(lpm.PasswordFieldID)

    @property
    def submit_button(self):
        return self.driver.find_element_by_xpath(lpm.SubmitButtonXPATH)

    @property
    def is_this_page(self):
        return self.is_element_visible((By.NAME, lpm.ThisPageNAME))
