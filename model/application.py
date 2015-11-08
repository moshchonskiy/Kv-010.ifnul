
__author__ = 'Evgen'

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import *

from pages.login_page import LoginPage



class Application:
    def __init__(self, driver, base_url):
        self.driver = driver
        driver.get(base_url)
        driver.maximize_window()
        self.wait = WebDriverWait(driver, 15)
        self.login_page = LoginPage(driver, base_url)

