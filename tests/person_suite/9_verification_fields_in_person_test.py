#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
from model.user import User

__author__ = 'stako'


def fill_main_person_page_with_invalid_data(app, invalid_person):
    """
    Method fill in the main persons page with invalid data.
    :param invalid_person: persons model in Person format with invalid data
    :param app: application context in Application format
    :return:
    """
    main_page = app.main_page
    main_page.is_this_page
    main_page.set_ukr_surname(invalid_person.surname_ukr)
    main_page.set_first_ukr_name(invalid_person.first_name_ukr)
    main_page.set_father_ukr_name(invalid_person.second_name_ukr)
    main_page.set_eng_surname(invalid_person.surname_eng)
    main_page.set_first_eng_name(invalid_person.first_name_eng)


def fill_extra_person_page_with_invalid_data(app, invalid_person):
    """
    Method fill in the extra persons page with invalid data.
    :param invalid_person: persons model in Person format
    :param app: application context in Application format
    :return:
    """
    extra_page = app.extra_page
    extra_page.is_this_page
    app.extra_page.set_private_case_numbers(invalid_person.private_case_number)


@pytest.allure.severity(pytest.allure.severity_level.MINOR)
def test_verification_fields_in_person(app, invalid_person, screenshot):
    with pytest.allure.step('The test verifies the correct operation of inspection fields.'):
        # login and follow up to person's page
        app.ensure_logout()
        app.login(User.Admin(), True)
        assert_expression = app.persons_page.is_this_page
        screenshot.assert_and_get_screenshot(app, assert_expression)

    with pytest.allure.step('Verification of fields in main page.'):
        app.persons_page.add_person_link
        fill_main_person_page_with_invalid_data(app, invalid_person)
        assert_expression = app.main_page.person_surname_ukr_input_incorrect
        screenshot.assert_and_get_screenshot(app, assert_expression)

        assert_expression = app.main_page.person_surname_eng_input_incorrect
        screenshot.assert_and_get_screenshot(app, assert_expression)

        assert_expression = app.main_page.person_father_name_input_incorrect
        screenshot.assert_and_get_screenshot(app, assert_expression)

        assert_expression = app.main_page.person_first_name_ukr_input_incorrect
        screenshot.assert_and_get_screenshot(app, assert_expression)

        assert_expression = app.main_page.person_first_name_eng_input_incorrect
        screenshot.assert_and_get_screenshot(app, assert_expression)

    with pytest.allure.step('Verification of fields in extra page.'):
        app.person_base_page.click_extra_tab
        fill_extra_person_page_with_invalid_data(app, invalid_person)
        assert_expression = app.extra_page.private_case_number_input_incorrect
        screenshot.assert_and_get_screenshot(app, assert_expression)

