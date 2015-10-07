from time import sleep
from model.user import User


__author__ = 'stako'


def test_add_enrollments(app):
    """
    Method creates and adds the enrollment.
    :param app:
    :return:
    """
    app.ensure_logout()
    app.login(User.Admin(), True)
    sleep(3)
    app.internal_page.enrollments_page_link.click()
    assert app.enrollments_page.is_this_page
    app.enrollments_page.is_this_page.click()
    app.enrollments_main_page.fill_enrollment()
    assert app.enrollments_page.search_enrollment(app.enrollments_page.SEARCH_METHOD["document_series"], "222333") == "222333"





