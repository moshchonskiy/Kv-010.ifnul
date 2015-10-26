

import pytest
from model.user import User
from utils.fill_enrollment import FillEnrollment

__author__ = 'stako'


def test_add_enrollments(app):
    """
    Method creates and adds the enrollment.
    :param app:
    """
    with pytest.allure.step('Test of add enrollment.'):
        enrollment = app.enrollments_main_page.get_enrollment("fill_enrollment_main.json", "fill_data_enrollment")
        app.ensure_logout()
        app.login(User.Admin(), True)
        app.internal_page.is_element_present(app.internal_page.SPINNER_OFF)
        app.internal_page.enrollments_page_link.click()
        assert app.enrollments_page.is_this_page
        app.enrollments_page.is_this_page.click()
        app.enrollments_main_page.fill_enrollment()
        fill_enrollment = FillEnrollment()
        app.enrollments_page.search_enrollment(app.enrollments_page.SEARCH_METHOD["document_series"],
                                               enrollment.series_of_statements)
        enrollment_like_table = fill_enrollment.table_enrollment_from_json("fill_enrollment_main.json",
                                                                           "fill_data_enrollment")
        app.internal_page.is_element_present(app.internal_page.SPINNER_OFF)
        enrollment_in_table = app.enrollments_page.search_enrollment_in_table()
        assert enrollment_like_table.__eq__(enrollment_in_table)
