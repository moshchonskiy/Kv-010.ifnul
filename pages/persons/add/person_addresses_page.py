#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Deorditsa'


from person_base_page import AddPersonPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class AddPersonAddressesPage(AddPersonPage):

    BIRTH_PLACE_SELECTOR = "div[ng-model='person.birthPlace']>div:nth-child(%s) ul a div"
    BIRTH_PLACE_LEVEL_SELECTOR = "div[ng-model='person.birthPlace']>div:nth-child(%s) label+div span"
    REG_ADDRESS_PLACE_SELECTOR = "div[ng-model='addresses.regAddresses.adminUnitId']>div:nth-child(%s) ul a div"
    REG_ADDRESS_LEVEL_SELECTOR = "div[ng-model='addresses.regAddresses.adminUnitId']>div:nth-child(%s) label+div span"
    POST_PLACE_LABEL = "РњiСЃС†Рµ РїСЂРѕР¶РёРІР°РЅРЅСЏ"
    ALL_REGISTRATION_PLACES_SELECT = (By.XPATH, "//a[@class='ui-select-choices-row-inner']//div[@class='ng-binding ng-scope']")
    INDEX_INPUT = (By.ID, "inputZipCodeReg")
    ADDRESS_TYPE_CHOOSER = (By.ID, "inputStreetTypeReg")
    ALL_ADDRESS_TYPE_SELECT = (By.XPATH, "//select[@id='inputStreetTypeReg']//option")
    STREET_INPUT = (By.XPATH, "//input[@id='inputStreetReg']")
    HOUSE_INPUT = (By.XPATH, "//input[@id='inputHouseReg']")
    APARTMENT_INPUT = (By.XPATH, "//input[@id='inputApartmentReg']")
    IS_ADDRESSES_MATCH = (By.XPATH, "//input[@ng-model='addresses.isAdressesMatch']")
    ALL_POST_PLACES_SELECT = (By.XPATH, "//a[@class='ui-select-choices-row-inner']//div[@class='ng-binding ng-scope']")
    INDEX_POST_INPUT = (By.XPATH, "//input[@id='inputZipCodePost']")
    ADDRESS_TYPE_POST_CHOOSER = (By.XPATH, "//select[@id='inputStreetTypePost']")
    ALL_ADDRESS_TYPE_POST_SELECT = (By.XPATH, "//select[@id='inputStreetTypePost']//option")
    STREET_POST_INPUT = (By.XPATH, "//input[@id='inputStreetPost']")
    HOUSE_POST_INPUT = (By.XPATH, "//input[@id='inputHousePost']")
    APARTMENT_POST_INPUT = (By.XPATH, "//input[@id='inputApartmentPost']")

    @property
    def is_this_page(self):
        return self.is_element_visible(self.INDEX_INPUT)

    def get_selector_for_current_block_and_level(self, selector, level):
        """
        Method makes selector for current block and drop-down current level
        :param selector: Selector which points to current block
        :param level: Integer number which means level in current block
        :return:
        """
        return (By.CSS_SELECTOR, selector % str(level))

    def select_birth_place(self, address, address_level):
        """
        Method select address in drop-down menu in birth place block on the current level
        :param address: String address. If address exists in select menu, then method will click on it, else will leave default value
        :param address_level: Integer number which means level in current block
        :return:
        """
        self.is_element_present(self.get_selector_for_current_block_and_level(self.BIRTH_PLACE_LEVEL_SELECTOR, address_level+1))
        self.driver.find_element(*self.get_selector_for_current_block_and_level(self.BIRTH_PLACE_LEVEL_SELECTOR, address_level+1)).click()
        all_level_addresses = self.driver.find_elements(*self.get_selector_for_current_block_and_level(self.BIRTH_PLACE_SELECTOR, address_level+1))
        self.find_element_in_select(all_level_addresses, address).click()
        self.is_element_present(self.SPINNER_OFF)

    def select_registration_address(self, address, address_level):
        """
        Method select address in drop-down menu in registration adress block on the current level
        :param address: String address. If address exists in select menu, then method will click on it, else will leave default value
        :param address_level: Integer number which means level in current block
        :return:
        """
        self.is_element_present(self.get_selector_for_current_block_and_level(self.REG_ADDRESS_LEVEL_SELECTOR, address_level+1))
        self.driver.find_element(*self.get_selector_for_current_block_and_level(self.REG_ADDRESS_LEVEL_SELECTOR, address_level+1)).click()
        all_level_addresses = self.driver.find_elements(*self.get_selector_for_current_block_and_level(self.REG_ADDRESS_PLACE_SELECTOR, address_level+1))
        self.find_element_in_select(all_level_addresses, address).click()
        self.is_element_present(self.SPINNER_OFF)

    def set_zip_code(self, index):
        """
        Method sets the zip code
        :param index: Integer parametr.
        :return:
        """
        self.driver.find_element(*self.INDEX_INPUT).send_keys(index)

    def reg_address_type_select(self, address_type):
        """
        Method select type of address in select menu
        :param address_type: String address type. If type exists in select menu, then method will click on it, else will leave default value
        :return:
        """
        self.is_element_present(self.ADDRESS_TYPE_CHOOSER)
        Select(self.driver.find_element(*self.ADDRESS_TYPE_CHOOSER)).select_by_visible_text(address_type)

    def set_street(self, street):
        """
        Method sets the street
        :param street: String parametr.
        :return:
        """
        self.driver.find_element(*self.STREET_INPUT).send_keys(street)

    def set_house(self, house):
        """
        Method sets the house
        :param house: Integer parametr.
        :return:
        """
        self.driver.find_element(*self.HOUSE_INPUT).send_keys(house)

    def set_apartment(self, apartment):
        """
        Method sets the apartment
        :param apartment: Integer parametr.
        :return:
        """
        self.driver.find_element(*self.APARTMENT_INPUT).send_keys(apartment)

    def check_is_reg_and_post_addresses_the_same(self, is_addresses_match):
        """
        Method checks or unchecks "Is registration address and post address the same?" checkbox
        :param is_addresses_match: Boolean format. Must be True, if registration address and post address are the same.
        :return:
        """
        self.checkbox_manager(self.driver.find_element(*self.IS_ADDRESSES_MATCH), is_addresses_match)

