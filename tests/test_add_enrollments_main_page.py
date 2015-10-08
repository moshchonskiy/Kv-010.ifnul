from model.user import User
import pytest

__author__ = 'stako'


def test_add_enrollments(app):
    """
    Method creates and adds the enrollment.
    :param app:
    """
    with pytest.allure.step('Test of add enrollment.'):
        app.ensure_logout()
        app.login(User.Admin(), True)
        app.internal_page.is_element_present(app.internal_page.SPINNER_OFF)
        app.internal_page.enrollments_page_link.click()
        assert app.enrollments_page.is_this_page
        app.enrollments_page.is_this_page.click()
        app.enrollments_main_page.fill_enrollment()
        assert app.enrollments_page.search_enrollment(app.enrollments_page.SEARCH_METHOD["document_series"],
                                                      app.enrollments_main_page.res_dict["series_of_statements"]) == \
               app.enrollments_main_page.res_dict["series_of_statements"]
