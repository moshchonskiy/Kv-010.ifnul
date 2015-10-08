from model.user import User

__author__ = 'stako'


def test_view_enrollment(app):
    """
    Method creates and adds the enrollment.
    :param app:
    """
    app.ensure_logout()
    app.login(User.Admin(), True)
    app.internal_page.is_element_present(app.internal_page.SPINNER_OFF)
    app.internal_page.enrollments_page_link.click()
    assert app.enrollments_page.is_this_page