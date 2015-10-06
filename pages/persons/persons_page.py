# -*- coding: utf-8 -*-
__author__ = 'Evgen'
from pages.internal_page import InternalPage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class PersonsPage(InternalPage):

    ADD_PERSON_BUTTON = (By.XPATH, "//button[contains(@class,'btn-success')]")
    SHOW_HIDE_FILTERS_BUTTON = (By.XPATH, "//button[contains(@ng-click,'hideFilterFunc')]")
    FIELD_CHOOSER_BUTTON = (By.XPATH, "//button[contains(@class, 'field-chooser-button')]")
    FIELD_CHOOSER_RED_CLOSE_BUTTON = (By.XPATH, "//button[parent::div[contains(@class, 'modal-footer')]]")
    # Columns dictionary binding number of column to it's name
    COLUMNS_DICT = {
        1: '№',
        2: 'ПІБ',
        3: 'Ім’я',
        4: 'По-батькові',
        5: 'Прізвище',
        6: 'Тип персони',
        7: 'Стать',
        8: 'Сімейний стан',
        9: 'Громад-во',
        10: 'Серія ОС',
        11: 'Номер ОС',
        12: 'Резидент',
        13: 'Місце народж.',
        14: 'Дата народж.',
        15: 'ВЗ',
        16: 'Гуртожиток',
        17: 'Мат. відп'
    }
    # Column headers in selection popup
    NUMERATION_COLUMN_MODAL             = (By.XPATH, "//span[contains(., '" + COLUMNS_DICT.get(1) + "')]")
    FULL_NAME_COLUMN_MODAL              = (By.XPATH, "//span[contains(., '" + COLUMNS_DICT.get(2) + "')]")
    FIRST_NAME_COLUMN_MODAL             = (By.XPATH, "//span[contains(., '" + COLUMNS_DICT.get(3) + "')]")
    MIDDLE_NAME_COLUMN_MODAL            = (By.XPATH, "//span[contains(., '" + COLUMNS_DICT.get(4) + "')]")
    LAST_NAME_COLUMN_MODAL              = (By.XPATH, "//span[contains(., '" + COLUMNS_DICT.get(5) + "')]")
    PERSON_TYPE_COLUMN_MODAL            = (By.XPATH, "//span[contains(., '" + COLUMNS_DICT.get(6) + "')]")
    SEX_COLUMN_MODAL                    = (By.XPATH, "//span[contains(., '" + COLUMNS_DICT.get(7) + "')]")
    MARITAL_STATUS_COLUMN_MODAL         = (By.XPATH, "//span[contains(., '" + COLUMNS_DICT.get(8) + "')]")
    CITIZENSHIP_COLUMN_MODAL            = (By.XPATH, "//span[contains(., '" + COLUMNS_DICT.get(9) + "')]")
    DOSSIER_SERIES_COLUMN_MODAL         = (By.XPATH, "//span[contains(., '" + COLUMNS_DICT.get(10) + "')]")  # Osobova Sprava
    DOSSIER_NUMBER_COLUMN_MODAL         = (By.XPATH, "//span[contains(., '" + COLUMNS_DICT.get(11) + "')]")  # Osobova Sprava
    RESIDENT_COLUMN_MODAL               = (By.XPATH, "//span[contains(., '" + COLUMNS_DICT.get(12) + "')]")
    PLACE_OF_BIRTH_COLUMN_MODAL         = (By.XPATH, "//span[contains(., '" + COLUMNS_DICT.get(13) + "')]")
    DATE_OF_BIRTH_COLUMN_MODAL          = (By.XPATH, "//span[contains(., '" + COLUMNS_DICT.get(14) + "')]")
    RESERVIST_COLUMN_MODAL              = (By.XPATH, "//span[contains(., '" + COLUMNS_DICT.get(15) + "')]")
    DORMITORY_COLUMN_MODAL              = (By.XPATH, "//span[contains(., '" + COLUMNS_DICT.get(16) + "')]")
    MATERIALLY_RESPONSIBLE_COLUMN_MODAL = (By.XPATH, "//span[contains(., '" + COLUMNS_DICT.get(17) + "')]")
    # Column headers in persons table
    NUMERATION_COLUMN             = (By.XPATH, "//a[contains(., '" + COLUMNS_DICT.get(1) + "')]")
    FULL_NAME_COLUMN              = (By.XPATH, "//a[contains(., '" + COLUMNS_DICT.get(2) + "')]")
    FIRST_NAME_COLUMN             = (By.XPATH, "//a[contains(., '" + COLUMNS_DICT.get(3) + "')]")
    MIDDLE_NAME_COLUMN            = (By.XPATH, "//a[contains(., '" + COLUMNS_DICT.get(4) + "')]")
    LAST_NAME_COLUMN              = (By.XPATH, "//a[contains(., '" + COLUMNS_DICT.get(5) + "')]")
    PERSON_TYPE_COLUMN            = (By.XPATH, "//a[contains(., '" + COLUMNS_DICT.get(6) + "')]")
    SEX_COLUMN                    = (By.XPATH, "//a[contains(., '" + COLUMNS_DICT.get(7) + "')]")
    MARITAL_STATUS_COLUMN         = (By.XPATH, "//a[contains(., '" + COLUMNS_DICT.get(8) + "')]")
    CITIZENSHIP_COLUMN            = (By.XPATH, "//a[contains(., '" + COLUMNS_DICT.get(9) + "')]")
    DOSSIER_SERIES_COLUMN         = (By.XPATH, "//a[contains(., '" + COLUMNS_DICT.get(10) + "')]")  # Osobova Sprava
    DOSSIER_NUMBER_COLUMN         = (By.XPATH, "//a[contains(., '" + COLUMNS_DICT.get(11) + "')]")  # Osobova Sprava
    RESIDENT_COLUMN               = (By.XPATH, "//a[contains(., '" + COLUMNS_DICT.get(12) + "')]")
    PLACE_OF_BIRTH_COLUMN         = (By.XPATH, "//a[contains(., '" + COLUMNS_DICT.get(13) + "')]")
    DATE_OF_BIRTH_COLUMN          = (By.XPATH, "//a[contains(., '" + COLUMNS_DICT.get(14) + "')]")
    RESERVIST_COLUMN              = (By.XPATH, "//a[contains(., '" + COLUMNS_DICT.get(15) + "')]")
    DORMITORY_COLUMN              = (By.XPATH, "//a[contains(., '" + COLUMNS_DICT.get(16) + "')]")
    MATERIALLY_RESPONSIBLE_COLUMN = (By.XPATH, "//a[contains(., '" + COLUMNS_DICT.get(17) + "')]")


    @property
    def is_this_page(self):
        return self.is_element_visible(self.ADD_PERSON_BUTTON)

    @property
    def add_person_link(self):
        return self.driver.find_element_by_xpath(*self.ADD_PERSON_BUTTON)

    def column_as_list(self, column_number):
        """
        Method get column number as input
        :return: list of text data in column
        """
        list_of_column_text = []
        list_of_column_elements = self.driver.find_elements_by_xpath("//tbody/tr/td[" + str(column_number) + "]")
        for element in list_of_column_elements:
            list_of_column_text.append(element.text.lower())
        return list_of_column_text

    @property
    def is_element_present(self):

        pass
