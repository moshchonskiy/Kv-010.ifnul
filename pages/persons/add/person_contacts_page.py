#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Deorditsa'


from person_base_page import AddPersonPage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class AddPersonContactsPage(AddPersonPage):

    MOBILE_PHONE1_INPUT = (By.ID, "phone")
    MOBILE_PHONE2_INPUT = (By.ID, "mobilePhone")
    HOME_PHONE_INPUT = (By.ID, "homePhone")
    WORK_PHONE_INPUT = (By.ID, "workPhone")
    EMAIL_INPUT = (By.ID, "email")
    SKYPE_INPUT = (By.ID, "skype")
    SITE_INPUT = (By.ID, "site")
    ICQ_INPUT = (By.ID, "ICQ")

    @property
    def is_this_page(self):
        return self.is_element_visible(self.SKYPE_INPUT)

    def set_first_mobile_phone(self, phone):
        """
        Method sets the first mobile phone
        :param phone: String parametr. Pattern is "(xxx) xxx-xx-xx"
        :return:
        """
        self.emulation_of_input(self.MOBILE_PHONE1_INPUT, phone)

    def set_second_mobile_phone(self, phone):
        """
        Method sets the first mobile phone
        :param phone: String parametr. Pattern is "(xxx) xxx-xx-xx"
        :return:
        """
        self.emulation_of_input(self.MOBILE_PHONE2_INPUT, phone)

    def set_home_phone(self, phone):
        """
        Method sets the first mobile phone
        :param phone: String parametr. Pattern is "(xxx) xxx-xx-xx"
        :return:
        """
        self.emulation_of_input(self.HOME_PHONE_INPUT, phone)

    def set_work_phone(self, phone):
        """
        Method sets the first mobile phone
        :param phone: String parametr. Pattern is "(xxx) xxx-xx-xx"
        :return:
        """
        self.emulation_of_input(self.WORK_PHONE_INPUT, phone)

    def set_email(self, email):
        """
        Method sets the e-mail address.
        :param email: String parametr.
        :return:
        """
        self.emulation_of_input(self.EMAIL_INPUT, email)

    def set_skype(self, skype):
        """
        Method sets the persons Skype ID
        :param skype: String parametr.
        :return:
        """
        self.emulation_of_input(self.SKYPE_INPUT, skype)

    def set_site(self, site):
        """
        Method sets the persons web-site
        :param site: String parametr.
        :return:
        """
        self.emulation_of_input(self.SITE_INPUT, site)

    def set_icq(self, icq):
        """
        Method sets the persons ICQ ID
        :param icq: Integer parametr.
        :return:
        """
        self.emulation_of_input(self.ICQ_INPUT, icq)

    def fill_in_contact_page(self, person):
        """
        Method fill in data on the contact persons page
        :param person: persons model in Person format
        :return:
        """
        self.is_this_page
        self.set_first_mobile_phone(person.mobile_phone1)
        self.set_second_mobile_phone(person.mobile_phone2)
        self.set_home_phone(person.home_phone)
        self.set_work_phone(person.work_phone)
        self.set_email(person.email)
        self.set_skype(person.skype)
        self.set_site(person.web_site)
        self.set_icq(person.icq)