#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Deorditsa'

from pages.internal_page import InternalPage
from selenium.webdriver.common.by import By


class AddPersonPage(InternalPage):

    NEXT_BUTTON = (By.XPATH, "//button[@ng-click='goToNextTab(1)']")
    SAVE_NEW_PERSON_BUTTON = (By.XPATH, "//button[@ng-click='sendToServerPerson()']")
    BACK_BUTTON = (By.XPATH, "//button[@ng-click='goToNextTab(-1)']")
    PERSON_MAIN_TAB = (By.XPATH, "//li//a[contains(., 'ПІБ')]")
    PERSON_PASSPORT_TAB = (By.XPATH, "//li//a[contains(., 'Посвідчення')]")
    PERSON_EXTRA_INFO_TAB = (By.XPATH, "//li//a[contains(., 'Додаткова інформація')]")
    PERSON_ADDRESSES_TAB = (By.XPATH, "//li//a[contains(., 'Адреси')]")
    PERSON_CERTIFICATE_TAB = (By.XPATH, "//li//a[contains(., 'Атестати')]")
    PERSON_PHOTO_TAB = (By.XPATH, "//li//a[contains(., 'Фото')]")
    PERSON_CONTACTS_TAB = (By.XPATH, "//li//a[contains(., 'Контакти')]")
    PERSON_PAPERS_TAB = (By.XPATH, "//li//a[contains(., 'Документи')]")
    PERSON_ENROLLMENTS_TAB = (By.XPATH, "//li//a[contains(., 'Заяви')][@ng-click='select()']")

    @property
    def is_this_page(self):
        return self.is_element_visible(self.SAVE_NEW_PERSON_BUTTON)

    @property
    def click_next_button(self):
        self.driver.find_element(*self.NEXT_BUTTON).click()
        self.wait_until_page_generate()

    @property
    def click_back_button(self):
        return self.driver.find_element(*self.BACK_BUTTON).click()

    @property
    def click_main_tab(self):
        return self.driver.find_element(*self.PERSON_MAIN_TAB).click()

    @property
    def click_extra_tab(self):
        return self.driver.find_element(*self.PERSON_EXTRA_INFO_TAB).click()

    @property
    def click_contacts_tab(self):
        return self.driver.find_element(*self.PERSON_CONTACTS_TAB).click()

    @property
    def click_addresses_tab(self):
        return self.driver.find_element(*self.PERSON_ADDRESSES_TAB).click()

    @property
    def click_papers_tab(self):
        return self.driver.find_element(*self.PERSON_PAPERS_TAB).click()

    @property
    def enrollments_tab(self):
        return self.is_element_visible(self.PERSON_ENROLLMENTS_TAB)

    def find_element_in_select(self, elements, value):
        """
        Method performs choosing concrete value in select element and click on it
        :param elements: list of WebDriver elements from select menu
        :param value: String parameter which is searched in select menu
        :return:
        """
        for el in elements:
            if el.text == value:
                return el

    def checkbox_manager(self, checkbox_element, needed_value):
        """
        Method checks or unchecks checkbox. It depends on current checkbox element status and needed value.
        :param checkbox_element: WebDriver (checkbox) element
        :param needed_value: Boolean parameter. If need that element was checked, the needed_value must be True
        :return:
        """
        if not checkbox_element.get_attribute("checked") and needed_value:
            checkbox_element.click()
        elif checkbox_element.get_attribute("checked") and not needed_value:
            checkbox_element.click()

    def save_new_person(self):
        """
        Method saves new person
        :return:
        """
        self.driver.find_element(*self.SAVE_NEW_PERSON_BUTTON).click()
        self.wait_until_page_generate()
