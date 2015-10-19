# -*- coding: utf-8 -*-
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.internal_page import InternalPage
from utils.data_provider_from_json import DataProviderJSON
import datetime

__author__ = 'Stako'


class EnrollmentsMainPage(InternalPage):
    OK_FOR_INPUT_FIELD = (By.CSS_SELECTOR, "div[class='input-group'] * button[class='btn btn-primary']")
    SEARCH_NAME_FIELD = (By.XPATH, "//div[@class='modal-body ng-scope']//input[contains (@type, 'search')]")
    FIRST_PERSON = (By.XPATH, "//*[@class='table-responsive']//tbody[@class='pointer']//tr[1]/td[2]")
    SERIES_OF_STATEMENTS = (By.XPATH, "//*[@id='inputDocSeries']")
    NUMBER_STATEMENTS = (By.XPATH, ".//*[@id='inputdocNum']")
    CHECKBOX_IS_STATE = (By.XPATH, ".//input[@ng-model='enrolment.isState']")
    CHECKBOX_IS_CONTRACT = (By.XPATH, ".//input[@ng-model='enrolment.isContract']")
    CHECKBOX_IS_PRIVILEGE = (By.XPATH, ".//input[@ng-model='enrolment.isPrivilege']")
    RADIOBUTTON_GETTING_EDUCATION = (By.CSS_SELECTOR, "input[name='isedustate'][value='11']")
    RADIOBUTTON_IS_INTERVIEW = (By.CSS_SELECTOR, "input[value='11'][ng-model='enrolment.isInterview']")
    CHECKBOX_IS_HOSTEL = (By.XPATH, ".//*[@ng-init='enrolment.isHostel = 0']")
    SEARCH_OFFERS_FIELD = (By.XPATH, ".//*[@id='movieForm']/div[9]/div[1]/div[1]/div/div/div/span/i")
    CHOOSE_FORM_OF_EDUCATION = (By.XPATH, ".//*[@id='movieForm']/div[9]/div[1]/div[2]/div/div/div/span/i")
    LIST_FROM_UI_SELECT = (By.XPATH, "//div[contains(@id, 'ui-select-choices-row')]/a/div")
    BUTTON_CHOOSE_SPECIALTIES = (By.CSS_SELECTOR, "button[class='btn btn-primary'] >i")
    CHOOSE_FIRST_SPECIALTIES = (By.XPATH, "//div[@class='table-responsive']//tbody[@class='pointer']/tr[1]/td[2]")
    DOCUMENT = (By.XPATH, ".//*[@class='col-xs-5']/*[@id='inputStructure']//i[@class='caret pull-right']")
    TOTAL_SCORE = (By.ID, "inputMark")
    GRADING_SCALE = (By.XPATH, ".//*[@id='markScale']//i[@class='caret pull-right']")
    CHECKBOX_DOCUMENT_IS_ORIGINAL = (By.XPATH, ".//*[@class='ng-pristine ng-untouched ng-valid']")
    PRIORITY = (By.XPATH, ".//*[@id='inputPriority']")
    STRUCTURAL_UNIT = (By.XPATH, ".//*[@class='col-xs-3']/*[@id='inputStructure']//i[@class='caret pull-right']")
    TYPE_OF_ENTRY_MENU = (By.ID, "inputChiefEnrolTypes")
    DETAILING_START_MENU = (By.ID, "inputEnrolmentTypeId")
    DATE_CLOSING_STATEMENTS = (By.XPATH, ".//*[@id='endDate']")
    DATE_BEGINING_STATEMENTS = (By.XPATH, ".//*[@id='begDate']")
    BUTTON_SAVE = (By.XPATH, ".//*[@class='btn btn-primary'][@ng-click='sendToServer()']")

    @property
    def search_offers_field(self):
        return self.is_element_visible(self.SEARCH_OFFERS_FIELD)

    @property
    def choose_first_specialties(self):
        return self.is_element_visible(self.CHOOSE_FIRST_SPECIALTIES)

    @property
    def search_name_field(self):
        return self.is_element_visible(self.SEARCH_NAME_FIELD)

    def list_form_ui_select(self):
        self.is_element_visible(self.LIST_FROM_UI_SELECT)
        return self.driver.find_elements(*self.LIST_FROM_UI_SELECT)

    @property
    def choose_form_of_education(self):
        return self.is_element_visible(self.CHOOSE_FORM_OF_EDUCATION)

    @property
    def first_person(self):
        return self.is_element_visible(self.FIRST_PERSON)

    @property
    def ok_for_input_field(self):
        return self.is_element_visible(self.OK_FOR_INPUT_FIELD)

    @property
    def series_of_statements(self):
        return self.is_element_visible(self.SERIES_OF_STATEMENTS)

    @property
    def number_statements(self):
        return self.is_element_visible(self.NUMBER_STATEMENTS)

    @property
    def checkbox_is_state(self):
        return self.is_element_visible(self.CHECKBOX_IS_STATE)

    @property
    def checkbox_is_contract(self):
        return self.is_element_visible(self.CHECKBOX_IS_CONTRACT)

    @property
    def checkbox_is_privilege(self):
        return self.is_element_visible(self.CHECKBOX_IS_PRIVILEGE)

    @property
    def radiobutton_getting_education(self):
        return self.is_element_visible(self.RADIOBUTTON_GETTING_EDUCATION)

    @property
    def radiobutton_is_interview(self):
        return self.is_element_visible(self.RADIOBUTTON_IS_INTERVIEW)

    @property
    def checkbox_is_hostel(self):
        return self.is_element_visible(self.CHECKBOX_IS_HOSTEL)

    @property
    def button_choose_specialties(self):
        return self.is_element_visible(self.BUTTON_CHOOSE_SPECIALTIES)

    @property
    def document(self):
        return self.is_element_visible(self.DOCUMENT)

    @property
    def total_score(self):
        return self.is_element_visible(self.TOTAL_SCORE)

    @property
    def grading_scale(self):
        return self.is_element_visible(self.GRADING_SCALE)

    @property
    def checkbox_document_is_original(self):
        return self.is_element_visible(self.CHECKBOX_DOCUMENT_IS_ORIGINAL)

    @property
    def priority(self):
        return self.is_element_visible(self.PRIORITY)

    @property
    def structural_unit(self):
        return self.is_element_visible(self.STRUCTURAL_UNIT)

    def type_of_entry_menu(self):
        return self.driver.find_element_by_id(self.TYPE_OF_ENTRY_MENU)

    def detailing_start_menu(self):
        return self.driver.find_element_by_id(self.DETAILING_START_MENU)

    @property
    def date_closing_statements(self):
        return self.is_element_visible(self.DATE_CLOSING_STATEMENTS)

    @property
    def button_save(self):
        return self.is_element_visible(self.BUTTON_SAVE)

    def find_element_in_ui_select(self, elements, string):
        """
        This method looks for WebElement in ui-select by name.
        :param elements: is list of WebElements in ui-select.
        :param string: is name of elements.
        :return: looked for WebElement.
        """
        for el in elements:
            if el.text.encode('utf8') == string:
                return el

    def find_element_in_select(self, elements, string):
        """
        This method looks for options in select by name and click one.
        :param elements: is list of options in select.
        :param string: is name of elements.
        """
        for sel in elements:
            if sel.text.encode('utf8') == string:
                sel.click()
                break

    def from_enrollment_json(self, key):
        """
        This method returns value by key from json file according to UTF-8 encoding.
        """
        db = DataProviderJSON("fill_enrollment_main.json")
        return db.get_value_by_ij("fill_data_enrollment", key).encode('utf8')

    def fill_enrollment(self):
        """
        This method fill enrollment and save one.
        """
        self.is_element_present(self.SPINNER_OFF)
        self.ok_for_input_field.click()
        self.is_element_present(self.SPINNER_OFF)
        self.search_name_field.send_keys(self.from_enrollment_json("person_name").decode('utf8'))
        self.first_person.click()
        self.is_element_present(self.SPINNER_OFF)
        self.series_of_statements.send_keys(self.from_enrollment_json("series_of_statements"))
        self.number_statements.send_keys(self.from_enrollment_json("number_statements"))
        self.checkbox_is_state.click()
        self.checkbox_is_contract.click()
        self.checkbox_is_privilege.click()
        self.radiobutton_getting_education.click()
        self.radiobutton_is_interview.click()
        self.checkbox_is_hostel.click()
        self.search_offers_field.click()
        self.find_element_in_ui_select(self.list_form_ui_select(), self.from_enrollment_json("offers")).click()
        self.choose_form_of_education.click()
        self.find_element_in_ui_select(self.list_form_ui_select(),
                                       self.from_enrollment_json("form_of_education")).click()
        self.button_choose_specialties.click()
        self.is_element_present(self.SPINNER_OFF)
        self.choose_first_specialties.click()
        self.document.click()
        self.find_element_in_ui_select(self.list_form_ui_select(), self.from_enrollment_json("document")).click()
        self.grading_scale.click()
        self.find_element_in_ui_select(self.list_form_ui_select(), self.from_enrollment_json("grading_scale")).click()
        self.total_score.send_keys(self.from_enrollment_json("total_score"))
        self.checkbox_document_is_original.click()
        self.priority.send_keys(self.from_enrollment_json("priority"))
        self.structural_unit.click()
        self.find_element_in_ui_select(self.list_form_ui_select(), self.from_enrollment_json("structural_unit")).click()
        self.find_element_in_select(
            Select(self.driver.find_element_by_id("inputChiefEnrolTypes")).options,
            self.from_enrollment_json("type_of_entry"))
        self.find_element_in_select(
            Select(self.driver.find_element_by_id("inputEnrolmentTypeId")).options,
            self.from_enrollment_json("detailing_start"))
        # self.date_closing_statements.send_keys(self.from_enrollment_json("date_closing"))
        d = datetime.date(1951, 2, 5)
        self.set_date(self.DATE_CLOSING_STATEMENTS, d)
        self.set_date(self.DATE_BEGINING_STATEMENTS, d)
        self.is_element_present(self.SPINNER_OFF)
        self.button_save.click()
