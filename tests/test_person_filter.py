# coding: utf8
from model.user import User

GIVEN_GENDER            = u'Чоловіча'
GIVEN_TYPE              = u'абітурієнт'
GIVEN_NEED_OF_HOSTEL    = u'потреб. гуртож.'
GIVEN_BOUND_TO_MILITARY = u'ВЗ'
GIVEN_RESIDENT          = u'інозем.'


def login(app):
    app.ensure_logout()
    app.login(User.Admin(), True)

#only for males
def test_gender_filter(app):
    login(app)
    person_page = app.persons_page
    person_page.try_get_gender_male_checkbox().click()
    person_page.try_get_refresh_upper_button().click()
    assert person_page.try_get_filtered_gender(GIVEN_GENDER).text == GIVEN_GENDER

#only for applicant
def test_type_filter(app):
    login(app)
    person_page = app.persons_page
    person_page.try_get_type_applicant_checkbox().click()
    person_page.try_get_refresh_upper_button().click()
    assert person_page.try_get_filtered_type(GIVEN_TYPE).text == GIVEN_TYPE

#only for need hostel
def test_neet_hostel_filter(app):
    login(app)
    person_page = app.persons_page
    person_page.try_get_need_hostel_checkbox().click()
    person_page.try_get_refresh_upper_button().click()
    assert person_page.try_get_filtered_need_of_hostel(GIVEN_NEED_OF_HOSTEL).text == GIVEN_NEED_OF_HOSTEL

#only for bound to military person
def test_bound_to_military_filter(app):
    login(app)
    person_page = app.persons_page
    person_page.try_get_burger_button().click()
    person_page.try_get_add_to_table_military_checkbox().click()
    person_page.try_get_close_after_addition_button().click()
    person_page.try_get_bound_to_military_checkbox().click()
    person_page.try_get_refresh_upper_button().click()
    assert person_page.try_get_filtered_bound_to_military(GIVEN_BOUND_TO_MILITARY).text == GIVEN_BOUND_TO_MILITARY

#only for foreigner resident
def test_bound_to_military_filter(app):
    login(app)
    person_page = app.persons_page
    person_page.try_get_burger_button().click()
    person_page.try_get_add_to_table_resident_checkbox().click()
    person_page.try_get_close_after_addition_button().click()
    person_page.try_get_resident_foreigner_checkbox().click()
    person_page.try_get_refresh_upper_button().click()
    assert person_page.try_get_filtered_resident(GIVEN_RESIDENT).text == GIVEN_RESIDENT