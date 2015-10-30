# coding: utf8
import allure
from allure.constants import AttachmentType
import pytest
from utils.add_person_pattern import AddPersonPattern

__author__ = 'Denys'

GIVEN_SURNAME = u'Прізвище'
GIVEN_PERSON_ID = '14'
GIVEN_NUM_OS = '999999'
GIVEN_SERIES_OS = 'ss'


@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
@pytest.mark.usefixtures('pre_login')
class TestSearchPerson:
    def test_surname_search(self):
        try:
            add_person_pattern = AddPersonPattern()
            add_person_pattern.search_person_by_surname(self.app, GIVEN_SURNAME)
            # the 1st word (surname) will be given
            assert self.app.persons_page.try_get_searched_surname(GIVEN_SURNAME).text.partition(' ')[0] == GIVEN_SURNAME
        except Exception:
            allure.attach('screenshot', self.app.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
            raise

    def test_person_id_search(self):
        try:
            person_page = self.app.persons_page
            person_page.try_get_choose_person_id().click()
            person_page.try_get_input_group().clear()
            person_page.try_get_input_group().send_keys(GIVEN_PERSON_ID)
            person_page.try_get_ok_button().click()
            assert person_page.try_get_searched_person_id(GIVEN_PERSON_ID).text == GIVEN_PERSON_ID
        except Exception:
            allure.attach('screenshot', self.app.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
            raise

    def test_num_os_search(self):
        try:
            person_page = self.app.persons_page
            person_page.try_get_choose_num_os().click()
            person_page.try_get_input_group().clear()
            person_page.try_get_input_group().send_keys(GIVEN_NUM_OS)
            person_page.try_get_ok_button().click()
            assert person_page.try_get_searched_num_os(GIVEN_NUM_OS).text == GIVEN_NUM_OS
        except Exception:
            allure.attach('screenshot', self.app.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
            raise

    def test_series_os_search(self):
        try:
            person_page = self.app.persons_page
            person_page.try_get_choose_series_os().click()
            person_page.try_get_input_group().clear()
            person_page.try_get_input_group().send_keys(GIVEN_SERIES_OS)
            person_page.try_get_ok_button().click()
            assert person_page.try_get_searched_series_os(GIVEN_SERIES_OS).text == GIVEN_SERIES_OS
        except Exception:
            allure.attach('screenshot', self.app.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
            raise
