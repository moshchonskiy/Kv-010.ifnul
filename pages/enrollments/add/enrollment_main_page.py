# -*- coding: utf-8 -*-
from time import sleep
from pages.internal_page import InternalPage
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import Select

__author__ = 'Stako'


class EnrollmentsMainPage(InternalPage):
    # SEARCH_PERSON_BY_ID = (
    #     By.CSS_SELECTOR, "select[class='form-control ng-pristine ng-valid ng-touched'] option[value='1']")
    # INPUT_FIELD_FOR_SEARCH = (By.CLASS_NAME, "form-control ng-valid ng-touched ng-dirty ng-valid-parse")
    OK_FOR_INPUT_FIELD = (By.CSS_SELECTOR, "div[class='input-group'] * button[class='btn btn-primary']")
    SECOND_PERSON = (By.XPATH, "html/body/div[5]/div/div/div[2]/div[2]/table/tbody/tr[2]/td[2]")
    # SEARCH_FIELD_IN_ALERT_CHOOSE_PERSON = (
    #     By.CSS_SELECTOR, "input[class='form-control ng-pristine ng-valid ng-touched']")
    # CHOOSE_PERSON_IN_ALERT_CHOOSE_PERSON = (By.CSS_SELECTOR, "tbody[class='pointer'] tr")
    SERIES_OF_STATEMENTS = (By.XPATH, "//*[@id='inputDocSeries']")
    NUMBER_STATEMENTS = (By.XPATH, ".//*[@id='inputdocNum']")
    CHECKBOX_IS_STATE = (By.XPATH, ".//input[@ng-model='enrolment.isState']")
    CHECKBOX_IS_CONTRACT = (By.XPATH, ".//input[@ng-model='enrolment.isContract']")
    CHECKBOX_IS_PRIVILEGE = (By.XPATH, ".//input[@ng-model='enrolment.isPrivilege']")
    RADIOBUTTON_GETTING_EDUCATION = (By.CSS_SELECTOR, "input[name='isedustate'][value='11']")
    RADIOBUTTON_IS_INTERVIEW = (By.CSS_SELECTOR, "input[value='11'][ng-model='enrolment.isInterview']")
    CHECKBOX_IS_HOSTEL = (By.XPATH, ".//*[@ng-init='enrolment.isHostel = 0']")
    SEARCH_OFFERS_FIELD = (
        By.XPATH, "input[class='form-control ui-select-search ng-valid ng-touched ng-dirty ng-valid-parse']")
    #CHOOSE_OFFER = (By.XPATH, "//div[@id='ui-select-choices-row-3-12']/a")
    CHOOSE_FORM_OF_EDUCATION = (By.XPATH, "input[class='form-control ui-select-search ng-pristine ng-valid ng-touched']")
    #CHOOSE_SPECIALTIES_FORM = (By.XPATH, ".//*[@id='ui-select-choices-row-8-17']/a")
    BUTTON_CHOOSE_SPECIALTIES = (By.CSS_SELECTOR, "button[class='btn btn-primary'] >i")
    # DOCUMENT = (By.XPATH, ".//*[@id='inputStructure']/div/span")
    # ADD_NEW_DOCUMENT = (By.XPATH, ".//*[@id='subjPlus']/a/button")
    # ATESTAT = (By.XPATH, ".//*[@id='ui-select-choices-row-9-0']/a/div")
    TOTAL_SCORE = (By.ID, "inputMark")
    # GRADING_SCALE = (By.XPATH, ".//*[@id='markScale']//span[@class='btn btn-default form-control ui-select-toggle']")
    # SCALE = (By.XPATH, ".//*[@id='ui-select-choices-row-5-3']/a")
    CHECKBOX_DOCUMENT_IS_ORIGINAL = (By.XPATH, ".//*[@class='ng-pristine ng-untouched ng-valid']")
    PRIORITY = (By.XPATH, ".//*[@id='inputPriority']")
    STRUCTURAL_UNIT = (
        By.XPATH, ".//*[@id='inputStructure']//input[@aria-activedescendant='ui-select-choices-row-6-0']")
    TYPE_OF_ENTRY_MENU = (By.ID, "inputChiefEnrolTypes")
    TYPE_OF_ENTRY = (By.XPATH, "//*[@id='inputChiefEnrolTypes']/option[@value='1']")
    DETAILING_START_MENU = (By.ID, "inputEnrolmentTypeId")
    DETAILING_START = (By.XPATH, ".//*[@id='inputEnrolmentTypeId']/option[@value='13']")
    DATE_CLOSING_STATEMENTS = (By.XPATH, ".//*[@id='endDate']")
    BUTTON_YEARS_AND_MONTH = (By.XPATH, ".//*[@id='datepicker-17627-159-title']")
    BUTTON_YEARS = (By.XPATH, ".//*[@id='datepicker-17627-159-title']")
    BUTTON_YEAR_2018 = (By.XPATH, ".//*[@id='datepicker-17627-159-17']/button")
    BUTTON_MONTH_APRIL = (By.XPATH, ".//*[@id='datepicker-17627-159-3']/button")
    BUTTON_DATE_FORTH = (By.XPATH, ".//*[@id='datepicker-17627-159-9']/button")
    BUTTON_SAVE = (By.XPATH, ".//*[@class='btn btn-primary'][@ng-click='sendToServer()']")


    POP = (By.XPATH, ".//*[@id='movieForm']/div[9]/div[1]/div[1]/div/div/div/span/i")
    LIST = (By.XPATH, "//div[contains(@id, 'ui-select-choices-row-16')]/a/div")
    PIP = (By.XPATH, ".//*[@id='ui-select-choices-row-7-0']/a/div")

    @property
    def pop(self):
        return self.is_element_visible(self.POP)


    def list(self):
        lst = self.driver.find_elements(*self.LIST)
        return lst

    @property
    def pip(self):
        return self.is_element_visible(self.PIP)


    @property
    def second_person(self):
        return self.is_element_visible(self.SECOND_PERSON)

    @property
    def input_field_for_search(self):
        return self.is_element_visible(self.INPUT_FIELD_FOR_SEARCH)

    @property
    def ok_for_input_field(self):
        return self.is_element_visible(self.OK_FOR_INPUT_FIELD)

    @property
    def search_field_in_alert_choose_person(self):
        return self.is_element_visible(self.SEARCH_FIELD_IN_ALERT_CHOOSE_PERSON)

    @property
    def choose_person_in_alert_choose_person(self):
        return self.is_element_visible(self.CHOOSE_PERSON_IN_ALERT_CHOOSE_PERSON)

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
    def search_offers_field(self):
        return self.is_element_visible(self.SEARCH_OFFERS_FIELD)

    @property
    def choose_offer(self):
        return self.is_element_visible(self.CHOOSE_OFFER)

    @property
    def choose_form_of_education(self):
        return self.is_element_visible(self.CHOOSE_FORM_OF_EDUCATION)

    @property
    def choose_specialties_form(self):
        return self.is_element_visible(self.CHOOSE_SPECIALTIES_FORM)

    @property
    def button_choose_specialties(self):
        return self.is_element_visible(self.BUTTON_CHOOSE_SPECIALTIES)

    @property
    def document(self):
        return self.is_element_visible(self.DOCUMENT)

    @property
    def add_new_document(self):
        return self.is_element_visible(self.ADD_NEW_DOCUMENT)

    @property
    def atestat(self):
        return self.is_element_visible(self.ATESTAT)

    @property
    def total_score(self):
        return self.is_element_visible(self.TOTAL_SCORE)

    @property
    def grading_scale(self):
        return self.is_element_visible(self.GRADING_SCALE)

    @property
    def scale(self):
        return self.is_element_visible(self.SCALE)

    @property
    def checkbox_document_is_original(self):
        return self.is_element_visible(self.CHECKBOX_DOCUMENT_IS_ORIGINAL)

    @property
    def priority(self):
        return self.is_element_visible(self.PRIORITY)

    @property
    def structural_init(self):
        return self.is_element_visible(self.STRUCTURAL_UNIT)

    @property
    def type_of_entry_menu(self):
        return self.is_element_visible(self.TYPE_OF_ENTRY_MENU)

    @property
    def type_of_entry(self):
        return self.is_element_visible(self.TYPE_OF_ENTRY)

    @property
    def detailing_start_menu(self):
        return self.is_element_visible(self.DETAILING_START_MENU)

    @property
    def detailing_start(self):
        return self.is_element_visible(self.DETAILING_START)

    @property
    def date_closing_statements(self):
        return self.is_element_visible(self.DATE_CLOSING_STATEMENTS)

    @property
    def button_years_and_month(self):
        return self.is_element_visible(self.BUTTON_YEARS_AND_MONTH)

    @property
    def button_years(self):
        return self.is_element_visible(self.BUTTON_YEARS)

    @property
    def button_year_2018(self):
        return self.is_element_visible(self.BUTTON_YEAR_2018)

    @property
    def button_month_april(self):
        return self.is_element_visible(self.BUTTON_MONTH_APRIL)

    @property
    def button_date_forth(self):
        return self.is_element_visible(self.BUTTON_DATE_FORTH)

    @property
    def button_save(self):
        return self.is_element_visible(self.BUTTON_SAVE)

    def find_element_in_select(self, elements, sss):
        for el in elements:
            if el.text == sss:
                print el.text
                return el

    def fill_enrollment(self):
        sleep(1)
        self.ok_for_input_field.click()
        sleep(1)
        self.second_person.click()
        sleep(1)
        self.series_of_statements.send_keys("222333")
        self.number_statements.send_keys("7778777")
        self.checkbox_is_state.click()
        self.checkbox_is_contract.click()
        self.checkbox_is_privilege.click()
        self.radiobutton_getting_education.click()
        self.radiobutton_is_interview.click()
        self.checkbox_is_hostel.click()
        sleep(2)
        self.pop.click()    #u'Фізичний'
        lst = self.list()
        self.find_element_in_select(self.list(), "Фізичний").click()
        sleep(2)
        # self.choose_form_of_education.click()  #u'Бакалавр'
        # self.choose_form_of_education.send_keys(u'Бакалавр')  #u'Бакалавр'
        sleep(2)
        # self.button_choose_specialties.click()
        sleep(5)


