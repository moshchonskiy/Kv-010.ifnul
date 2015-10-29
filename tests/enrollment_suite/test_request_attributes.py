__author__ = 'vika'

from model.user import User

def to_page(app):
    app.ensure_logout()
    app.login(User.Admin(), True)
    app.internal_page.is_element_present(app.internal_page.SPINNER_OFF)
    app.internal_page.enrollments_page_link.click()
    app.enrollments_page.is_this_page
    app.enrollments_page.add_new_enrollment_button_click
    app.enrollments_main_page.is_this_page


#both positive and negative tests
def test_request_priority(app):
    to_page(app)
    en_p = app.enrollments_main_page
    for pr in range(0,21,1):
        en_p.try_get_priority().click()
        en_p.try_get_priority().clear()
        en_p.try_get_priority().send_keys(pr)
        assert en_p.certain_priority(pr).text == en_p.try_get_priority().text


def test_reguest_number_positive(app):
    to_page(app)
    en_p = app.enrollments_main_page
    values = (1, 4567, 11, 959595);
    for x in values:
        en_p.number_statements.click()
        en_p.number_statements.clear()
        en_p.number_statements.send_keys(x)
        assert en_p.certain_positive_number_statements().text == en_p.number_statements.text


def test_reguest_number_negative(app):
    to_page(app)
    en_p = app.enrollments_main_page
    values = ('fsffrg', '1s', -1);
    for x in values:
        en_p.try_get_number_statements.click()
        en_p.try_get_number_statements.clear()
        en_p.try_get_number_statements.send_keys(x)
        assert en_p.certain_negative_number_statements().text == en_p.try_get_number_statements.text


