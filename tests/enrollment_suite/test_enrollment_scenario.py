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

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_add_enrollment(self, logout_login, enrollment, values, screenshot):
        with pytest.allure.step('Authorize to the application and click add enrollment button'):
            app = logout_login
            app.internal_page.enrollments_page_link.click()
            app.enrollments_page.is_this_page
            app.enrollments_page.add_new_enrollment_button_click
            app.enrollments_main_page.is_this_page
        with pytest.allure.step('Search person to add enrollment'):
            app.enrollments_main_page.add_person_in_enrollment(enrollment.person_name)
        with pytest.allure.step('Fill data on the add enrollment page'):
            app.enrollments_main_page.emulation_of_input(app.enrollments_main_page.SERIES_OF_STATEMENTS, enrollment.series_of_statements)
            app.enrollments_main_page.emulation_of_input(app.enrollments_main_page.NUMBER_STATEMENTS, enrollment.number_statements)
            app.enrollments_main_page.click_all_checkbox(enrollment.checkbox_is_state,
                                    enrollment.checkbox_is_contract,
                                    enrollment.checkbox_is_privilege,
                                    enrollment.checkbox_is_hostel,
                                    enrollment.checkbox_document_is_original)
            app.enrollments_main_page.radiobutton_higher_education(enrollment.radiobutton_higher_education)
            app.enrollments_main_page.radiobutton_evaluation_of_the_interview(enrollment.radiobutton_evaluation_of_the_interview)
        with pytest.allure.step('Search and choose proposition of speciality for person'):
            app.enrollments_main_page.search_offers(enrollment.offers, enrollment.form_of_education)
            self.speciality_id = app.enrollments_main_page.find_first_specialities_id().text
            app.enrollments_main_page.choose_first_specialties.click()
        with pytest.allure.step('Choose document to attach to the enrollment'):
            app.enrollments_main_page.choose_document(enrollment.document)
        with pytest.allure.step('Fill other data after choose document on the add enrollment page'):
            app.enrollments_main_page.choose_grading_scale(enrollment.grading_scale)
            app.enrollments_main_page.add_total_score(app.enrollments_main_page.TOTAL_SCORE, enrollment.total_score)
            app.enrollments_main_page.add_priority(app.enrollments_main_page.PRIORITY, enrollment.priority)
            app.enrollments_main_page.choose_structural_unit(enrollment.structural_unit)
            app.enrollments_main_page.type_of_entry(enrollment.type_of_entry)
            app.enrollments_main_page.specification_of_entry(enrollment.detailing_start)
        with pytest.allure.step('Choose beginning and closing dates on the add enrollment page'):
            app.enrollments_main_page.set_date(app.enrollments_main_page.DATE_OF_ENTRY_STATEMENTS, enrollment.date_of_entry)
            app.enrollments_main_page.set_date(app.enrollments_main_page.DATE_CLOSING_STATEMENTS, enrollment.date_closing)
            app.enrollments_main_page.iwait_until_page_generate()
        with pytest.allure.step('Save data on the add enrollment page'):
            app.enrollments_main_page.button_save.click()
        with pytest.allure.step('Logout, login after adding enrollment'):
            app.internal_page.wait_until_page_generate()
            app.ensure_logout()
            app.login(User.Admin(), True)
        with pytest.allure.step('Search person which enrollment was added to on the enrollment page'):
            app.internal_page.wait_until_page_generate()
            app.internal_page.enrollments_page_link.click()
            app.enrollments_page.is_this_page
            actual_search = app.enrollments_page.search_enrollment(app.enrollments_page.SEARCH_METHOD["person_id"], values["search_by"]["valid_person_id"])
        with pytest.allure.step('Assert person ID is the same person ID which enrollment was added to'):
            screenshot.assert_and_get_screenshot(app, values["search_by"]["valid_person_id"] == int(actual_search[0]))
            # assert values["search_by"]["valid_person_id"] == int(actual_search[0])

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_view_enrollment(self, logout_login, values, enrollment, screenshot):
        with pytest.allure.step('Authorize to the application and view enrollment page'):
            app = logout_login
            app.internal_page.enrollments_page_link.click()
            app.enrollments_page.is_this_page
        with pytest.allure.step('Search person which enrollment was added to on the enrollment page'):
            actual_search = app.enrollments_page.search_enrollment(app.enrollments_page.SEARCH_METHOD["person_id"], values["search_by"]["valid_person_id"])
        with pytest.allure.step('Assert person ID is the same person ID which enrollment was added to'):
            screenshot.assert_and_get_screenshot(app, values["search_by"]["valid_person_id"] == int(actual_search[0]))
            # assert values["search_by"]["valid_person_id"] == int(actual_search[0])
        with pytest.allure.step('View added enrollment'):
            app.enrollments_page.edit_button_on_first_row_click()
        with pytest.allure.step('Assert series of enrollment is the same as from input data'):
            screenshot.assert_and_get_screenshot(app, app.enrollments_main_page.find_series_of_statements().get_attribute("value") == enrollment.series_of_statements)
            # assert app.enrollments_main_page.find_series_of_statements().get_attribute("value") == enrollment.series_of_statements
        with pytest.allure.step('Assert number of enrollment is the same as from input data'):
            screenshot.assert_and_get_screenshot(app, app.enrollments_main_page.find_number_statements().get_attribute("value") == str(enrollment.number_statements))
            # assert app.enrollments_main_page.find_number_statements().get_attribute("value") == str(enrollment.number_statements)
        with pytest.allure.step('Assert "is state" checkbox of enrollment is the same as from input data'):
            screenshot.assert_and_get_screenshot(app, self.is_checkbox_checked(app.enrollments_main_page.find_checkbox_is_state()) == enrollment.checkbox_is_state)
            # assert self.is_checkbox_checked(app.enrollments_main_page.find_checkbox_is_state()) == enrollment.checkbox_is_state
        with pytest.allure.step('Assert "is contract" checkbox is the same as from input data'):
            screenshot.assert_and_get_screenshot(app, self.is_checkbox_checked(app.enrollments_main_page.find_checkbox_is_contract()) == enrollment.checkbox_is_contract)
            assert self.is_checkbox_checked(app.enrollments_main_page.find_checkbox_is_contract()) == enrollment.checkbox_is_contract
        with pytest.allure.step('Assert "is privilege" checkbox is the same as from input data'):
            screenshot.assert_and_get_screenshot(app, self.is_checkbox_checked(app.enrollments_main_page.find_checkbox_is_contract()) == enrollment.checkbox_is_contract)
            # assert self.is_checkbox_checked(app.enrollments_main_page.find_checkbox_is_privilege()) == enrollment.checkbox_is_privilege
        with pytest.allure.step('Assert "is hostel" checkbox is the same as from input data'):
            screenshot.assert_and_get_screenshot(app, self.is_checkbox_checked(app.enrollments_main_page.find_checkbox_is_hostel()) == enrollment.checkbox_is_hostel)
            assert self.is_checkbox_checked(app.enrollments_main_page.find_checkbox_is_hostel()) == enrollment.checkbox_is_hostel
        with pytest.allure.step('Assert total score is the same as from input data'):
            screenshot.assert_and_get_screenshot(app, app.enrollments_main_page.find_total_score().get_attribute("value") == str(enrollment.total_score))
            # assert app.enrollments_main_page.find_total_score().get_attribute("value") == str(enrollment.total_score)

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_delete_enrollment(self, logout_login, values, enrollment, screenshot):
        with pytest.allure.step('Authorize to the application and view enrollment page'):
            app = logout_login
            app.internal_page.enrollments_page_link.click()
            app.enrollments_page.is_this_page
        with pytest.allure.step('Search person which enrollment was added to on the enrollment page'):
            actual_search = app.enrollments_page.search_enrollment(app.enrollments_page.SEARCH_METHOD["person_id"], values["search_by"]["valid_person_id"])
        with pytest.allure.step('Assert person ID is the same person ID which enrollment was added to'):
            screenshot.assert_and_get_screenshot(app, values["search_by"]["valid_person_id"] == int(actual_search[0]))
            # assert values["search_by"]["valid_person_id"] == int(actual_search[0])
        with pytest.allure.step('Delete enrollment button click'):
            app.enrollments_page.delete_button_on_first_row_click()
            app.internal_page.wait_until_page_generate()
        with pytest.allure.step('Logout, login after deleting enrollment'):
            app.ensure_logout()
            app.login(User.Admin(), True)
        with pytest.allure.step('Search person which enrollment was added to on the enrollment page'):
            app.internal_page.wait_until_page_generate()
            app.internal_page.enrollments_page_link.click()
            app.enrollments_page.is_this_page
            actual_search = app.enrollments_page.search_enrollment(app.enrollments_page.SEARCH_METHOD["person_id"], values["search_by"]["valid_person_id"])
        with pytest.allure.step('Assert that the person id is not exist in searching result'):
            screenshot.assert_and_get_screenshot(app, not values["search_by"]["valid_person_id"] == int(actual_search[0]))
            # assert not values["search_by"]["valid_person_id"] == int(actual_search[0])

    def is_checkbox_checked(self, checkbox):
        if checkbox.get_attribute("checked"):
            return True
        return False
