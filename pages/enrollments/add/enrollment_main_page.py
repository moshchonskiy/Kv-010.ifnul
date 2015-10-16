# -*- coding: utf-8 -*-
import os
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.internal_page import InternalPage
from utils.data_provider_from_json import DataProviderJSON

__author__ = 'Stako'


class EnrollmentsMainPage(InternalPage):
    OK_FOR_INPUT_FIELD = (By.CSS_SELECTOR, "div[class='input-group'] * button[class='btn btn-primary']")
    SEARCH_NAME_FIELD = (By.XPATH, "//div[@class='modal-body ng-scope']//input[contains (@type, 'search')]")
    FIRST_PERSON = (By.XPATH, "//*[@class='table-responsive']//tbody[@class='pointer']//tr[1]/td[2]")
    SERIES_OF_STATEMENTS = (By.ID, "inputDocSeries")
    NUMBER_STATEMENTS = (By.ID, "inputdocNum")
    CHECKBOX_IS_STATE = (By.XPATH, ".//input[@ng-model='enrolment.isState']")
    CHECKBOX_IS_CONTRACT = (By.XPATH, ".//input[@ng-model='enrolment.isContract']")
    CHECKBOX_IS_PRIVILEGE = (By.XPATH, ".//input[@ng-model='enrolment.isPrivilege']")
    RADIOBUTTON_DONT_GETTING_EDUCATION = (By.CSS_SELECTOR, "input[name='isedustate'][value='0']")
    RADIOBUTTON_GETTING_EDUCATION = (By.CSS_SELECTOR, "input[name='isedustate'][value='1']")
    RADIOBUTTON_IS_EDUCATION = (By.CSS_SELECTOR, "input[name='isedustate'][value='11']")
    RADIOBUTTON_NOT_PASSED_INTERVIEW = (By.CSS_SELECTOR, "input[ng-model='enrolment.isInterview'][value='-1']")
    RADIOBUTTON_DONT_NEED_INTERVIEW = (By.CSS_SELECTOR, "input[ng-model='enrolment.isInterview'][value='0']")
    RADIOBUTTON_NEED_INTERVIEW = (By.CSS_SELECTOR, "input[ng-model='enrolment.isInterview'][value='1']")
    RADIOBUTTON_INTERVIEW_PASSED = (By.CSS_SELECTOR, "input[ng-model='enrolment.isInterview'][value='11']")
    CHECKBOX_IS_HOSTEL = (By.XPATH, ".//*[@ng-init='enrolment.isHostel = 0']")
    SEARCH_OFFERS_FIELD = (By.XPATH, "//*[@ng-model='searchBy.departmentId']//*[@class='caret pull-right']")
    CHOOSE_FORM_OF_EDUCATION = (By.XPATH, "//*[@ng-model='searchBy.specOfferTypeId']//*[@class='caret pull-right']")
    LIST_FROM_UI_SELECT = (By.XPATH, "//div[contains(@id, 'ui-select-choices-row')]/a/div")
    BUTTON_CHOOSE_SPECIALTIES = (By.CSS_SELECTOR, "button[class='btn btn-primary'] >i")
    CHOOSE_FIRST_SPECIALTIES = (By.XPATH, "//div[@class='table-responsive']//tbody[@class='pointer']/tr[1]/td[2]")
    DOCUMENT = (By.XPATH, ".//*[@class='col-xs-5']/*[@id='inputStructure']//i[@class='caret pull-right']")
    TOTAL_SCORE = (By.ID, "inputMark")
    GRADING_SCALE = (By.XPATH, ".//*[@id='markScale']//i[@class='caret pull-right']")
    CHECKBOX_DOCUMENT_IS_ORIGINAL = (By.XPATH, ".//*[@class='ng-pristine ng-untouched ng-valid']")
    PRIORITY = (By.ID, "inputPriority")
    STRUCTURAL_UNIT = (By.XPATH, ".//*[@class='col-xs-3']/*[@id='inputStructure']//i[@class='caret pull-right']")
    DATE_OF_ENTRY_STATEMENTS = (By.ID, "begDate")
    DATE_CLOSING_STATEMENTS = (By.ID, "endDate")
    BUTTON_SAVE = (By.XPATH, ".//*[@class='btn btn-primary'][@ng-click='sendToServer()']")
    ID_DETAILING_START_MENU = "inputEnrolmentTypeId"
    ID_TYPE_OF_ENTRY_MENU = "inputChiefEnrolTypes"

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
    def radiobutton_dont_getting_education(self):
        return self.is_element_visible(self.RADIOBUTTON_DONT_GETTING_EDUCATION)

    @property
    def radiobutton_is_education(self):
        return self.is_element_visible(self.RADIOBUTTON_IS_EDUCATION)

    @property
    def radiobutton_not_passed_interview(self):
        return self.is_element_visible(self.RADIOBUTTON_NOT_PASSED_INTERVIEW)

    @property
    def radiobutton_dont_need_interview(self):
        return self.is_element_visible(self.RADIOBUTTON_DONT_NEED_INTERVIEW)

    @property
    def radiobutton_need_interview(self):
        return self.is_element_visible(self.RADIOBUTTON_NEED_INTERVIEW)

    @property
    def radiobutton_interview_passed(self):
        return self.is_element_visible(self.RADIOBUTTON_INTERVIEW_PASSED)

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
        self.add_person_in_enrollment(self.from_enrollment_json("person_name"))
        self.series_of_statements.send_keys(self.from_enrollment_json("series_of_statements"))
        self.number_statements.send_keys(self.from_enrollment_json("number_statements"))
        self.click_all_checkbox(self.from_enrollment_json("checkbox_is_state"),
                                self.from_enrollment_json("checkbox_is_contract"),
                                self.from_enrollment_json("checkbox_is_privilege"),
                                self.from_enrollment_json("checkbox_is_hostel"),
                                self.from_enrollment_json("checkbox_document_is_original"))
        self.radiobutton_higher_education("radiobutton_higher_education")
        self.radiobutton_evaluation_of_the_interview("radiobutton_evaluation_of_the_interview")
        self.search_offers(self.from_enrollment_json("offers"), self.from_enrollment_json("form_of_education"))
        self.choose_document(self.from_enrollment_json("document"))
        self.choose_grading_scale(self.from_enrollment_json("grading_scale"))
        self.add_total_score(self.from_enrollment_json("total_score"))
        self.add_priority(self.from_enrollment_json("priority"))
        self.choose_structural_unit(self.from_enrollment_json("structural_unit"))
        self.type_of_entry(self.from_enrollment_json("type_of_entry"))
        self.specification_of_entry(self.from_enrollment_json("detailing_start"))
        date_of_entry = datetime.date(2015, 10, 17)
        date_closing = datetime.date(2017, 11, 21)
        self.set_date(self.DATE_OF_ENTRY_STATEMENTS, date_of_entry)
        self.set_date(self.DATE_CLOSING_STATEMENTS, date_closing)
        self.is_element_present(self.SPINNER_OFF)
        self.button_save.click()

    def add_person_in_enrollment(self, name):
        self.is_element_present(self.SPINNER_OFF)
        self.ok_for_input_field.click()
        self.is_element_present(self.SPINNER_OFF)
        self.search_name_field.send_keys(name.decode('utf8'))
        self.first_person.click()
        self.is_element_present(self.SPINNER_OFF)

    def radiobutton_higher_education(self, education):
        if education == "Не отримую освіти":
            self.radiobutton_dont_getting_education.click()
        elif education == "Отримую освіту":
            self.radiobutton_getting_education.click()
        elif education == "Є вища освіта":
            self.radiobutton_is_education.click()

    def radiobutton_evaluation_of_the_interview(self, evaluation):
        if evaluation == "Не пройшов співбесіду":
            self.radiobutton_not_passed_interview.click()
        elif evaluation == "Не потрібно співбесіди":
            self.radiobutton_dont_need_interview.click()
        elif evaluation == "Потрібна співбесіда":
            self.radiobutton_need_interview.click()
        elif evaluation == "Співпебісда пройдена":
            self.radiobutton_interview_passed.click()

    def search_offers(self, offer, form_of_education):
        self.search_offers_field.click()
        self.find_element_in_ui_select(self.list_form_ui_select(), offer).click()
        self.choose_form_of_education.click()
        self.find_element_in_ui_select(self.list_form_ui_select(), form_of_education).click()
        self.button_choose_specialties.click()
        self.is_element_present(self.SPINNER_OFF)
        self.choose_first_specialties.click()

    def choose_document(self, document):
        self.document.click()
        self.find_element_in_ui_select(self.list_form_ui_select(), document).click()

    def choose_grading_scale(self, scale):
        self.grading_scale.click()
        self.find_element_in_ui_select(self.list_form_ui_select(), scale).click()

    def add_total_score(self, score):
        self.total_score.send_keys(score)

    def add_priority(self, priority):
        self.priority.send_keys(priority)

    def choose_structural_unit(self, unit):
        self.structural_unit.click()
        self.find_element_in_ui_select(self.list_form_ui_select(), unit).click()

    def type_of_entry(self, type_of_entry):
        self.find_element_in_select(
            Select(self.driver.find_element_by_id(self.ID_TYPE_OF_ENTRY_MENU)).options, type_of_entry)

    def specification_of_entry(self, specification):
        self.find_element_in_select(
            Select(self.driver.find_element_by_id(self.ID_DETAILING_START_MENU)).options, specification)

    def click_all_checkbox(self, state, contract, privilege, hostel, document):
        if state == "False":
            self.checkbox_is_state.click()
        if contract == "False":
            self.checkbox_is_contract.click()
        if privilege == "True":
            self.checkbox_is_privilege.click()
        if hostel == "True":
            self.checkbox_is_hostel.click()
        if document == "True":
            self.checkbox_document_is_original.click()
