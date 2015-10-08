# coding: utf8
from model.user import User


GIVEN_SURNAME    = u'Прізвище'
GIVEN_PERSON_ID  = '14'
GIVEN_NUM_OS     = '999999'
GIVEN_SERIES_OS  = 'ss'


def login(app):
    app.ensure_logout()
    app.login(User.Admin(), True)


def test_surname_search(app):
    login(app)
    person_page = app.persons_page
    person_page.try_get_choose_surname().click()
    person_page.try_get_input_group().clear()
    person_page.try_get_input_group().send_keys(GIVEN_SURNAME)
    person_page.try_get_ok_button().click()
    #the 1st word (surname) will be given
    assert person_page.try_get_expected_surname(GIVEN_SURNAME).text.partition(' ')[0] == GIVEN_SURNAME

def test_person_id_search(app):
    person_page = app.persons_page
    person_page.try_get_choose_person_id().click()
    person_page.try_get_input_group().clear()
    person_page.try_get_input_group().send_keys(GIVEN_PERSON_ID)
    person_page.try_get_ok_button().click()
    assert person_page.try_get_expected_person_id(GIVEN_PERSON_ID).text == GIVEN_PERSON_ID

def test_num_os_search(app):
    person_page = app.persons_page
    person_page.try_get_choose_num_os().click()
    person_page.try_get_input_group().clear()
    person_page.try_get_input_group().send_keys(GIVEN_NUM_OS)
    person_page.try_get_ok_button().click()
    assert person_page.try_get_expected_num_os(GIVEN_NUM_OS).text == GIVEN_NUM_OS

def test_series_os_search(app):
    person_page = app.persons_page
    person_page.try_get_choose_series_os().click()
    person_page.try_get_input_group().clear()
    person_page.try_get_input_group().send_keys(GIVEN_SERIES_OS)
    person_page.try_get_ok_button().click()
    assert person_page.try_get_expected_series_os(GIVEN_SERIES_OS).text == GIVEN_SERIES_OS