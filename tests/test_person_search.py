# coding: utf8
from model.user import User
from pages.persons.persons_page import GIVEN_SURNAME, GIVEN_PERSON_ID, GIVEN_NUM_OS, GIVEN_SERIES_OS


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
    # the 1st word (surname) will be given
    assert person_page.try_get_expected_surname().text.partition(' ')[0] == GIVEN_SURNAME


def test_person_id_search(app):
    person_page = app.persons_page
    person_page.try_get_choose_person_id().click()
    person_page.try_get_input_group().clear()
    person_page.try_get_input_group().send_keys(GIVEN_PERSON_ID)
    person_page.try_get_ok_button().click()
    assert person_page.try_get_expected_person_id().text == GIVEN_PERSON_ID


def test_num_os_search(app):
    person_page = app.persons_page
    person_page.try_get_choose_num_os().click()
    person_page.try_get_input_group().clear()
    person_page.try_get_input_group().send_keys(GIVEN_NUM_OS)
    person_page.try_get_ok_button().click()
    assert person_page.try_get_expected_num_os().text == GIVEN_NUM_OS


def test_series_os_search(app):
    person_page = app.persons_page
    person_page.try_get_choose_series_os().click()
    person_page.try_get_input_group().clear()
    person_page.try_get_input_group().send_keys(GIVEN_SERIES_OS)
    person_page.try_get_ok_button().click()
    assert person_page.try_get_expected_series_os().text == GIVEN_SERIES_OS
