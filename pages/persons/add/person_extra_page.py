#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Deorditsa'

from person_base_page import AddPersonPage
from selenium.webdriver.common.by import By

class AddPersonExtraPage(AddPersonPage):

    ACTIVATE_BIRTH_DAY_CHOOSER = (By.XPATH, "//input[@ng-model='person.begDate']")
    SEX_TYPES_SELECT = (By.XPATH, "//div[@id='genderTypeId']//div//span")
    ALL_SEX_TYPES_SELECT = (By.XPATH, "//div[@id='genderTypeId']//a//div")
    MARITAL_STATUS_SELECT = (By.XPATH, "//div[@id='marriedTypeId']//div//span//span[@class='ui-select-placeholder text-muted ng-binding']")
    ALL_MARITAL_STATUSES_SELECT = (By.XPATH, "//div[@id='marriedTypeId']//a//div")
    NATIONALITY_SELECT = (By.XPATH, "//div[@id='citizenCountryId']//div/span//span[@class='ng-binding ng-scope']")
    ALL_NATIONALITIES_SELECT = (By.XPATH, "//div[@id='citizenCountryId']//a//div")
    PRIVATE_CASE_CHARS_INPUT = (By.XPATH, "//input[@id='docSeries']")
    PRIVATE_CASE_NUMBER_INPUT = (By.XPATH, "//input[@id='docNum']")
    IS_A_OUTLANDER_CHECKER = (By.XPATH, "//input[@ng-checked='person.resident']")
    IS_A_MILITARY_CHECKER = (By.XPATH, "//input[@ng-checked='person.isMilitary']")
    NEED_HOSTEL_CHECKER = (By.XPATH, "//input[@ng-checked='person.isHostel']")

    @property
    def is_this_page(self):
        return self.is_element_visible(self.ACTIVATE_BIRTH_DAY_CHOOSER)

    def set_persons_birth_day(self, date):
        """
        Method sets persons birth day
        :param date: Date, when person was burn in a datetime format
        :return:
        """
        self.set_date(self.ACTIVATE_BIRTH_DAY_CHOOSER, date)

    def choose_person_sex_type(self, person_sex_type):
        """
        Method performs choosing concrete person sex type
        :param person_sex_type: if person_sex_type exists in select menu, then method will click on it, else will leave default value
        :return:
        """
        self.is_element_present(self.SEX_TYPES_SELECT)
        self.driver.find_element(*self.SEX_TYPES_SELECT).click()
        self.find_element_in_select(self.driver.find_elements(*self.ALL_SEX_TYPES_SELECT), person_sex_type).click()

    def choose_person_martial_status(self, person_martial_status):
        """
        Method performs choosing concrete person martial status
        :param person_martial_status: if person_martial_status exists in select menu, then method will click on it, else will leave default value
        :return:
        """
        self.is_element_present(self.MARITAL_STATUS_SELECT)
        self.driver.find_element(*self.MARITAL_STATUS_SELECT).click()
        self.find_element_in_select(self.driver.find_elements(*self.ALL_MARITAL_STATUSES_SELECT), person_martial_status).click()

    def choose_person_nationality(self, person_nationality):
        """
        Method performs choosing concrete person sex type
        :param person_nationality: String format. If person_nationality exists in select menu, then method will click on it, else will leave default value
        :return:
        """
        self.is_element_present(self.NATIONALITY_SELECT)
        self.driver.find_element(*self.NATIONALITY_SELECT).click()
        self.find_element_in_select(self.driver.find_elements(*self.ALL_NATIONALITIES_SELECT), person_nationality).click()

    def set_private_case_chars(self, chars):
        """
        Method sets the persons private case series
        :param chars: String format. Persons private case series
        :return:
        """
        self.driver.find_element(*self.PRIVATE_CASE_CHARS_INPUT).send_keys(chars)

    def set_private_case_numbers(self, numbers):
        """
        Method sets the persons private case number
        :param numbers: String format. Persons private case number
        :return:
        """
        self.driver.find_element(*self.PRIVATE_CASE_NUMBER_INPUT).send_keys(numbers)

    def check_resident_status(self, is_outlander):
        """
        Method checks or unchecks "Is person outlander?" checkbox
        :param is_outlander: Boolean format. Must be True, if person is outlander.
        :return:
        """
        self.checkbox_manager(self.driver.find_element(*self.IS_A_OUTLANDER_CHECKER), is_outlander)

    def check_needed_hostel_status(self, is_need):
        """
        Method checks or unchecks "Is person need a hostel?" checkbox
        :param is_need: Boolean format. Must be True, if person need a hostel.
        :return:
        """
        self.checkbox_manager(self.driver.find_element(*self.NEED_HOSTEL_CHECKER), is_need)

    def check_reservist_status(self, is_reservist):
        """
        Method checks or unchecks "Is person reservist?" checkbox
        :param is_reservist: Boolean format. Must be True, if person is reservist.
        :return:
        """
        self.checkbox_manager(self.driver.find_element(*self.IS_A_MILITARY_CHECKER), is_reservist)



