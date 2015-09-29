__author__ = 'Evgen'

from selenium.webdriver.remote.webelement import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import *

from pages.login_page import LoginPage
from pages.persons_page import PersonsPage
from pages.internal_page import InternalPage
from pages.person.add_person_page import AddPersonPage
from model.user import User


class Application:
    def __init__(self, driver, base_url):
        driver.get(base_url)
        self.wait = WebDriverWait(driver, 15)
        self.login_page = LoginPage(driver, base_url)
        self.persons_page = PersonsPage(driver, base_url)
        self.internal_page = InternalPage(driver, base_url)
        self.new_person_page = AddPersonPage(driver, base_url)

    def login(self, user):
        lp = self.login_page
        lp.is_this_page
        lp.username_field.send_keys(user.username)
        lp.password_field.send_keys(user.password)
        lp.submit_button.click()

    def ensure_logged_in(self):
        element = self.wait.until(presence_of_element_located((By.CSS_SELECTOR, "nav, input[id='inputLogin']")))
        if element.tag_name == "input[id='inputLogin']":
            self.login(User.Admin())

    def logout(self):
        ip = self.internal_page
        ip.is_this_page
        ip.user_dropdown.click()
        ip.logout_button.click()

    def ensure_logout(self):
        element = self.wait.until(presence_of_element_located((By.CSS_SELECTOR, "nav, input[id='inputLogin']")))
        if element.tag_name == "nav":
            self.logout()

    def is_logged_in(self):
        return self.internal_page.is_this_page

    def is_not_logged_in(self):
        return self.login_page.is_this_page
