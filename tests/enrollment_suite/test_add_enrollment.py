from utils.data_provider_from_json import DataProviderJSON
from utils.enrollment_creator import EnrollmentCreator
import pytest
from time import sleep

__author__ = 'acidroed'


class TestAddEnrollment(object):

    @pytest.fixture
    def enrollment(request):
        """
        Fixture create model of enrollment
        :return: Model of Enrollment
        """
        return EnrollmentCreator("enrollment_valid.json").get_enrollment()

    @pytest.fixture
    def values(request):
        return DataProviderJSON("values_for_enrollment_test.json").get_dict_value()

    def add_enrollment(self, logout_login, enrollment):
        app = logout_login
        app.internal_page.enrollments_page_link.click()
        app.enrollments_page.is_this_page
        app.enrollments_page.add_new_enrollment_button_click
        app.enrollments_main_page.is_this_page
        app.enrollments_main_page
        app.enrollments_main_page.add_person_in_enrollment(enrollment.person_name)
        app.enrollments_main_page.emulation_of_input(app.enrollments_main_page.SERIES_OF_STATEMENTS, enrollment.series_of_statements)
        app.enrollments_main_page.emulation_of_input(app.enrollments_main_page.NUMBER_STATEMENTS, enrollment.number_statements)
        app.enrollments_main_page.click_all_checkbox(enrollment.checkbox_is_state,
                                enrollment.checkbox_is_contract,
                                enrollment.checkbox_is_privilege,
                                enrollment.checkbox_is_hostel,
                                enrollment.checkbox_document_is_original)
        app.enrollments_main_page.radiobutton_higher_education(enrollment.radiobutton_higher_education)
        app.enrollments_main_page.radiobutton_evaluation_of_the_interview(enrollment.radiobutton_evaluation_of_the_interview)
        app.enrollments_main_page.search_offers(enrollment.offers, enrollment.form_of_education)
        app.enrollments_main_page.choose_document(enrollment.document)
        app.enrollments_main_page.choose_grading_scale(enrollment.grading_scale)
        app.enrollments_main_page.add_total_score(app.enrollments_main_page.TOTAL_SCORE, enrollment.total_score)
        app.enrollments_main_page.add_priority(app.enrollments_main_page.PRIORITY, enrollment.priority)
        app.enrollments_main_page.choose_structural_unit(enrollment.structural_unit)
        app.enrollments_main_page.type_of_entry(enrollment.type_of_entry)
        app.enrollments_main_page.specification_of_entry(enrollment.detailing_start)
        app.enrollments_main_page.set_date(app.enrollments_main_page.DATE_OF_ENTRY_STATEMENTS, enrollment.date_of_entry)
        app.enrollments_main_page.set_date(app.enrollments_main_page.DATE_CLOSING_STATEMENTS, enrollment.date_closing)
        app.enrollments_main_page.is_element_present(app.enrollments_main_page.SPINNER_OFF)
        # sleep(10)
        app.enrollments_main_page.button_save.click()

    def test_view_person(self, logout_login, values):
        app = logout_login
        app.internal_page.enrollments_page_link.click()
        app.enrollments_page.is_this_page
        en_page = app.enrollments_page
        expected_id = "9"
        actual_search = en_page.search_enrollment(en_page.SEARCH_METHOD["person_id"], values["valid_person_id"])

