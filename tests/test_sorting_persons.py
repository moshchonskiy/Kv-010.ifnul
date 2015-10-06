# -*- coding: utf-8 -*-
from selenium import webdriver
from model.application import Application
from model.user import User
from selenium.webdriver.common.by import By
from pytest import *

__author__ = 'yioteh'


class TestSortingPerson():
    driver = webdriver.Firefox()
    base_url = 'http://194.44.198.221/'
    app = Application(driver, base_url)

    def test_sorting_person(self):
        SPINNER_OFF = (By.XPATH, "//div[@id='spinnerDiv' and @style='display: none;']")
        column_number = 2
        self.app.ensure_logout()
        self.app.login(User.Admin())
        pers_page = self.app.persons_page
        intern_page = self.app.internal_page
        pers_page.is_this_page
        pers_page.driver.find_element(*pers_page.FULL_NAME_COLUMN).click()
        intern_page.is_element_present(SPINNER_OFF)
        column_after_clicking = pers_page.column_as_list(column_number)
        assert sorted(column_after_clicking, reverse=True, key=unicode.lower) == column_after_clicking
