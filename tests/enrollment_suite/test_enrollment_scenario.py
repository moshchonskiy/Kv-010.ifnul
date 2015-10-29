from model.user import User
from utils.data_provider_from_json import DataProviderJSON
from utils.enrollment_creator import EnrollmentCreator
import pytest
from time import sleep

__author__ = 'acidroed'


class TestEnrollmentScenario(object):

    speciality_id = ""

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

    def test_add_enrollment(self, logout_login, enrollment, values):
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
        self.speciality_id = app.enrollments_main_page.find_first_specialities_id().text
        app.enrollments_main_page.choose_first_specialties.click()
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
        app.enrollments_main_page.button_save.click()
        app.internal_page.is_element_present(app.internal_page.SPINNER_OFF)
        app.ensure_logout()
        app.login(User.Admin(), True)
        app.internal_page.is_element_present(app.internal_page.SPINNER_OFF)
        app.internal_page.enrollments_page_link.click()
        app.enrollments_page.is_this_page
        actual_search = app.enrollments_page.search_enrollment(app.enrollments_page.SEARCH_METHOD["person_id"], values["search_by"]["valid_person_id"])
        assert values["search_by"]["valid_person_id"] == int(actual_search[0])

    def test_view_enrollment(self, logout_login, values, enrollment):
        # self.add_enrollment(logout_login, enrollment)
        app = logout_login
        app.internal_page.enrollments_page_link.click()
        app.enrollments_page.is_this_page
        actual_search = app.enrollments_page.search_enrollment(app.enrollments_page.SEARCH_METHOD["person_id"], values["search_by"]["valid_person_id"])
        assert values["search_by"]["valid_person_id"] == int(actual_search[0])
        app.enrollments_page.edit_button_on_first_row_click()
        assert app.enrollments_main_page.find_series_of_statements().get_attribute("value") == enrollment.series_of_statements
        assert app.enrollments_main_page.find_number_statements().get_attribute("value") == str(enrollment.number_statements)
        assert self.is_checkbox_checked(app.enrollments_main_page.find_checkbox_is_state()) == enrollment.checkbox_is_state
        assert self.is_checkbox_checked(app.enrollments_main_page.find_checkbox_is_contract()) == enrollment.checkbox_is_contract
        assert self.is_checkbox_checked(app.enrollments_main_page.find_checkbox_is_privilege()) == enrollment.checkbox_is_privilege
        assert self.is_checkbox_checked(app.enrollments_main_page.find_checkbox_is_hostel()) == enrollment.checkbox_is_hostel
        assert app.enrollments_main_page.find_total_score().get_attribute("value") == str(enrollment.total_score)

    def test_delete_enrollment(self, logout_login, values, enrollment):
        app = logout_login
        app.internal_page.enrollments_page_link.click()
        app.enrollments_page.is_this_page
        actual_search = app.enrollments_page.search_enrollment(app.enrollments_page.SEARCH_METHOD["person_id"], values["search_by"]["valid_person_id"])
        assert values["search_by"]["valid_person_id"] == int(actual_search[0])
        app.enrollments_page.delete_button_on_first_row_click()
        app.internal_page.is_element_present(app.internal_page.SPINNER_OFF)
        app.ensure_logout()
        app.login(User.Admin(), True)
        app.internal_page.is_element_present(app.internal_page.SPINNER_OFF)
        app.internal_page.enrollments_page_link.click()
        app.enrollments_page.is_this_page
        actual_search = app.enrollments_page.search_enrollment(app.enrollments_page.SEARCH_METHOD["person_id"], values["search_by"]["valid_person_id"])
        assert not values["search_by"]["valid_person_id"] == int(actual_search[0])

    def is_checkbox_checked(self, checkbox):
        if checkbox.get_attribute("checked"):
            return True
        return False
