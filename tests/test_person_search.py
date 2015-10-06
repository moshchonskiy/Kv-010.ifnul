# coding: utf8
import time
from model.user import User
from pages.persons.persons_page import PersonsPage
__author__ = 'vika'


GIVEN_SURNAME = u'Іваненко'
GIVEN_PERSON_ID = '14'
GIVEN_NUM_OS = '34654654'
GIVEN_SERIES_OS = '32'

SLEEP_TIME = 7

def test_is_login(app):
    app.ensure_logout()
    app.login(User.Admin(), True)
    assert app.internal_page.is_this_page

def test_surname_search(app):
    person_page = app.persons_page
    person_page.try_get_choose_surname().click()
    person_page.try_get_input_group().clear()
    person_page.try_get_input_group().send_keys(GIVEN_SURNAME)
    person_page.try_get_ok_button().click()
    time.sleep(SLEEP_TIME)
    assert GIVEN_SURNAME in person_page.try_get_expected_surname().text

def test_person_id_search(app):
    person_page = app.persons_page
    #persone_page = PersonsPage()
    person_page.try_get_choose_person_id().click()
    person_page.try_get_input_group().clear()
    person_page.try_get_input_group().send_keys(GIVEN_PERSON_ID)
    person_page.try_get_ok_button().click()
    time.sleep(SLEEP_TIME)
    assert person_page.try_get_expected_person_id().text == GIVEN_PERSON_ID

def test_num_os_search(app):
    person_page = app.persons_page
    person_page.try_get_choose_num_os().click()
    person_page.try_get_input_group().clear()
    person_page.try_get_input_group().send_keys(GIVEN_NUM_OS)
    person_page.try_get_ok_button().click()
    time.sleep(SLEEP_TIME)
    assert person_page.try_get_expected_num_os().text == GIVEN_NUM_OS

def test_series_os_search(app):
    person_page = app.persons_page
    person_page.try_get_choose_series_os().click()
    person_page.try_get_input_group().clear()
    person_page.try_get_input_group().send_keys(GIVEN_SERIES_OS)
    person_page.try_get_ok_button().click()
    time.sleep(SLEEP_TIME)
    assert person_page.try_get_expected_series_os().text == GIVEN_SERIES_OS