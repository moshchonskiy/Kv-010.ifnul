# -*- coding: utf-8 -*-
from pages.internal_page import InternalPage
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import Select

__author__ = 'Stako'


class EnrollmentsMainPage(InternalPage):
    OK_FOR_INPUT_FIELD = (By.CSS_SELECTOR, "div[class='input-group'] * button[class='btn btn-primary']")
    SECOND_PERSON = (By.XPATH, "html/body/div[5]/div/div/div[2]/div[2]/table/tbody/tr[6]/td[2]")
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
    STRUCTURAL_UNIT = (By.XPATH,
                       ".//*[@class='col-xs-3']/*[@id='inputStructure']//i[@class='caret pull-right']")
    TYPE_OF_ENTRY_MENU = (By.ID, "inputChiefEnrolTypes")
    DETAILING_START_MENU = (By.ID, "inputEnrolmentTypeId")
    DATE_CLOSING_STATEMENTS = (By.XPATH, ".//*[@id='endDate']")
    BUTTON_YEARS_AND_MONTH = (By.XPATH,
                              ".//ul[@class='dropdown-menu ng-valid ng-valid-date-disabled ng-dirty ng-valid-parse ng-valid-date']//button[contains(@id, 'datepicker-')]")
    BUTTON_YEARS = (By.XPATH,
                    ".//ul[@class='dropdown-menu ng-valid ng-valid-date-disabled ng-dirty ng-valid-parse ng-valid-date']//button[contains(@id, 'datepicker-')]")
    BUTTON_YEAR_2018 = (By.XPATH, ".//*[@id=contains(@id, ''datepicker-')]/button")
    BUTTON_MONTH_APRIL = (By.XPATH, ".//*[@id=contains(@id, ''datepicker-')]/button")
    BUTTON_DATE_FORTH = (By.XPATH, ".//*[@id=contains(@id, ''datepicker-')]/button")
    BUTTON_SAVE = (By.XPATH, ".//*[@class='btn btn-primary'][@ng-click='sendToServer()']")

    POP = (By.XPATH, ".//*[@class='btn btn-default btn-sm pull-right']")

    @property
    def pop(self):
        return self.is_element_visible(self.POP)

    @property
    def search_offers_field(self):
        return self.is_element_visible(self.SEARCH_OFFERS_FIELD)

    @property
    def choose_first_specialties(self):
        return self.is_element_visible(self.CHOOSE_FIRST_SPECIALTIES)

    def list_form_ui_select(self):
        return self.driver.find_elements(*self.LIST_FROM_UI_SELECT)

    @property
    def choose_form_of_education(self):
        return self.is_element_visible(self.CHOOSE_FORM_OF_EDUCATION)

    @property
    def second_person(self):
        return self.is_element_visible(self.SECOND_PERSON)

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

    def find_element_in_ui_select(self, elements, string):
        for el in elements:
            if el.text.encode('utf8') == string:
                return el

    def find_element_in_select(self, elements, string):
        for sel in elements:
            if sel.text.encode('utf8') == string:
                sel.click()
                break

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
        self.search_offers_field.click()
        self.find_element_in_ui_select(self.list_form_ui_select(), "Фізичний").click()
        self.choose_form_of_education.click()
        self.find_element_in_ui_select(self.list_form_ui_select(), "Бакалавр").click()
        self.button_choose_specialties.click()
        sleep(3)
        self.choose_first_specialties.click()
        self.document.click()
        self.find_element_in_ui_select(self.list_form_ui_select(), "Атестат про повну загальну середню освіту").click()
        self.grading_scale.click()
        self.find_element_in_ui_select(self.list_form_ui_select(), "стобальна").click()
        self.total_score.send_keys("77")
        self.checkbox_document_is_original.click()
        self.priority.send_keys("3")
        self.structural_unit.click()
        self.find_element_in_ui_select(self.list_form_ui_select(), "Фізичний").click()
        self.find_element_in_select(
            Select(self.driver.find_element_by_id("inputChiefEnrolTypes")).options, "За результатами іспитів")
        self.find_element_in_select(
            Select(self.driver.find_element_by_id("inputEnrolmentTypeId")).options, "Учасник міжнародної олімпіади")
        self.date_closing_statements.send_keys("2016-04-04")
        sleep(1)

        #//tbody[@class='pointer']//td[contains (@class, 'ng-binding ng-scope')]
        # enroll_user = {
        #     "number": "",
        #     "person_id": "",
        #     "propose_id": "",
        #     "isBudget": "",
        #     "isContract": "",
        #     "unit": "",
        #     "documents_personification": "",
        #     "total_score": "",
        #     "isPrivileges": "",
        #     "series_doc": "",
        #     "number_doc": "",
        #     "isHostel": "",
        #     "type_of_admission": "",
        #     "date_of_create": "",
        #     "date_start": "",
        #     "date_end": "",
        #     "hierarchy": ""
        #     }