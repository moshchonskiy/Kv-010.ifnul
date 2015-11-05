

import pytest
from model.user import User
from utils.fill_enrollment import FillEnrollment

__author__ = 'stako'


# def test_add_enrollments(app):
def add_enrollments(logout_login):
    """
    Method creates and adds the enrollment.
    :param logout_login:
    """
    with pytest.allure.step('Test of add enrollment.'):
        name_of_json_file = "fill_enrollment_main.json"
        name_of_dictionary = "fill_data_enrollment"
        enrollment = logout_login.enrollments_main_page.get_enrollment(name_of_json_file, name_of_dictionary)
        logout_login.internal_page.enrollments_page_link.click()
        assert logout_login.enrollments_page.is_this_page
        logout_login.enrollments_page.is_this_page.click()
        logout_login.enrollments_main_page.fill_enrollment(name_of_json_file, name_of_dictionary)
        fill_enrollment = FillEnrollment()
        logout_login.enrollments_page.search_enrollment(logout_login.enrollments_page.SEARCH_METHOD["document_series"],
                                               enrollment.series_of_statements)
        enrollment_like_table = fill_enrollment.table_enrollment_from_json(name_of_json_file,
                                                                           name_of_dictionary)
        logout_login.internal_page.is_element_present(logout_login.internal_page.SPINNER_OFF)
        enrollment_in_table = logout_login.enrollments_page.search_enrollment_in_table()
        assert enrollment_like_table == enrollment_in_table
