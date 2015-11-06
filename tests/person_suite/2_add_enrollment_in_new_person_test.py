#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
from model.user import User
from utils.add_person_pattern import AddPersonPattern


@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
def test_add_enrollment_in_new_person(logout_login, person, dictionary_with_json_files, screenshot):
    with pytest.allure.step('Test of add enrollment in new person.'):
        add_person = AddPersonPattern()
        app = logout_login
        assert app.persons_page.is_this_page
        add_person.search_person_by_surname(app, person.surname_ukr)
        app.internal_page.wait_until_page_generate()
        app.persons_page.edit_first_person_in_page.click()
        app.person_base_page.enrollments_tab.click()
        enrollment = fill_enrollment_in_person(app, dictionary_with_json_files["fill_enrollment_main"])
        expected_number = enrollment.number_statements
        app.internal_page.wait_until_page_generate()
        list_with_actual_numbers = app.person_enrollment.enrollment_doc_number
        assert_expression = is_doc_number_in_list_of_numbers(expected_number, list_with_actual_numbers)
        screenshot.assert_and_get_screenshot(app, assert_expression)
        app.persons_page.return_to_persons_main_page(app)


def is_doc_number_in_list_of_numbers(expected, list_with_actual_numbers):
    """
    This method looks for document number in the list of all document numbers of all enrollments.
    :param expected: is document number.
    :param list_with_actual_numbers: list with all document numbers.
    :return: True if this number in tje list.
    """
    for numbers in list_with_actual_numbers:
        if numbers.text == expected:
            return True
    return False


def fill_enrollment_in_person(app, name_of_json_file):
    """
    This method fills enrollment in person.
    :param app: is instance-fixture of Application().
    :param name_of_json_file: name of json for filling enrollment.
    :return: instance of enrollment.
    """
    app.person_enrollment.add_enrollment.click()
    enrollment = app.enrollments_main_page.fill_enrollment(name_of_json_file, "fill_data_enrollment")
    return enrollment
