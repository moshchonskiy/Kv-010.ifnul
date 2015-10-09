__author__ = 'Evgen'

from person_base_page import AddPersonPage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class AddPersonMainPage(AddPersonPage):

    PERSON_TYPE_SELECT = (By.XPATH, "//div[@id='personTypeId']//span")
    ALL_PERSON_TYPES_SELECT = (By.XPATH, "//a[@class='ui-select-choices-row-inner']//div[@class='ng-binding ng-scope']")
    PERSON_SURNAME_UKR_INPUT = (By.XPATH, "//input[@id='surname']")
    PERSON_SURNAME_ENG_INPUT = (By.XPATH, "//input[@id='surnameEng']")
    PERSON_FARTHER_NAME_UKR_INPUT = (By.XPATH, "//input[@id='fatherName']")
    PERSON_FIRST_NAME_UKR_INPUT = (By.XPATH, "//input[@id='firstName']")
    PERSON_FIRST_NAME_ENG_INPUT = (By.XPATH, "//input[@id='firstNameEng']")


    @property
    def is_this_page(self):
        return self.is_element_visible(self.PERSON_TYPE_SELECT)

    def person_type_select_click(self):
        """
        Method performs clicking on person type select field
        :return:
        """
        self.is_element_present(self.PERSON_TYPE_SELECT)
        self.driver.find_element(*self.PERSON_TYPE_SELECT).click()

    def choose_person_type(self, person_type):
        """
        Method performs choosing concrete person type
        :param person_type: if person_type exists in select menu, then method will click on it, else will leave default value
        :return:
        """
        self.is_element_present(self.ALL_PERSON_TYPES_SELECT)
        self.find_element_in_select(self.driver.find_elements(*self.ALL_PERSON_TYPES_SELECT), person_type).click()

    def set_first_ukr_name(self, first_ukr_name):
        """
        Method sets the first person name on Ukranian language
        :param first_ukr_name: first person name on Ukranian language
        :return:
        """
        self.is_element_present(self.PERSON_FIRST_NAME_UKR_INPUT)
        self.driver.find_element(*self.PERSON_FIRST_NAME_UKR_INPUT).send_keys(first_ukr_name)

    def set_ukr_surname(self, ukr_surname):
        """
        Method sets the persons surname on Ukranian language
        :param ukr_surname: persons surname on Ukranian language
        :return:
        """
        self.driver.find_element(*self.PERSON_SURNAME_UKR_INPUT).send_keys(ukr_surname)

    def set_father_ukr_name(self, father_ukr_name):
        """
        Method sets the fathers person name on Ukranian language
        :param father_ukr_name: fathers person name on Ukranian language
        :return:
        """
        self.driver.find_element(*self.PERSON_FARTHER_NAME_UKR_INPUT).send_keys(father_ukr_name)

    def set_eng_surname(self, eng_surname):
        """
        Method sets the persons surname on English language
        :param ukr_surname: persons surname on English language
        :return:
        """
        self.driver.find_element(*self.PERSON_SURNAME_ENG_INPUT).send_keys(eng_surname)

    def set_first_eng_name(self, first_eng_name):
        """
        Method sets the first person name on English language
        :param first_eng_name: first person name on English language
        :return:
        """
        self.driver.find_element(*self.PERSON_FIRST_NAME_ENG_INPUT).send_keys(first_eng_name)

