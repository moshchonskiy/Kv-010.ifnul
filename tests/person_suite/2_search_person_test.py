# coding: utf8
from model.user import User

# GIVEN_SURNAME    = u'Прізвище'
GIVEN_PERSON_ID  = '14'
# GIVEN_NUM_OS     = '999999'
# GIVEN_SERIES_OS  = 'ss'
#
def login(app):
    app.ensure_logout()
    app.login(User.Admin(), True)


def test_surname_search(app, person):
    login(app)
    person_page = app.persons_page
    person_page.try_get_choose_surname().click()
    person_page.try_get_input_group().clear()
    person_page.try_get_input_group().send_keys(person.surname_ukr)
    person_page.try_get_ok_button().click()
    #the 1st word (surname) will be given
    assert person_page.try_get_searched_surname(person.surname_ukr).text.partition(' ')[0] == person.surname_ukr

def test_person_id_search(app):
    person_page = app.persons_page
    person_page.try_get_choose_person_id().click()
    person_page.try_get_input_group().clear()
    person_page.try_get_input_group().send_keys(GIVEN_PERSON_ID)
    person_page.try_get_ok_button().click()
    assert person_page.try_get_searched_person_id(GIVEN_PERSON_ID).text == GIVEN_PERSON_ID

def test_num_os_search(app, person):
    person_page = app.persons_page
    person_page.try_get_choose_num_os().click()
    person_page.try_get_input_group().clear()
    person_page.try_get_input_group().send_keys(person.private_case_number)
    person_page.try_get_ok_button().click()
    assert person_page.try_get_searched_num_os(person.private_case_number).text == str(person.private_case_number)

def test_series_os_search(app, person):
    person_page = app.persons_page
    person_page.try_get_choose_series_os().click()
    person_page.try_get_input_group().clear()
    person_page.try_get_input_group().send_keys(person.private_case_chars)
    person_page.try_get_ok_button().click()
    assert person_page.try_get_searched_series_os(person.private_case_chars).text == person.private_case_chars