#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
from model.user import User
from utils.add_person_pattern import AddPersonPattern


@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
def test_add_enrollment_in_new_person(app, person, dictionary_with_json_files):
    with pytest.allure.step('Test of add enrollment in new person.'):
        add_person = AddPersonPattern()
        if app.is_not_logged_in():
            app.ensure_logout()
            app.login(User.Admin(), True)
            app.internal_page.is_element_present(app.internal_page.SPINNER_OFF)
        assert app.persons_page.is_this_page
        add_person.search_person_by_surname(app, person.surname_ukr)
        app.internal_page.is_element_present(app.internal_page.SPINNER_OFF)
        app.persons_page.edit_first_person_in_page.click()
        app.person_base_page.enrollments_tab.click()
        expected_number = fill_enrollment_in_person(app, dictionary_with_json_files["fill_enrollment_main"])
        app.internal_page.is_element_present(app.internal_page.SPINNER_OFF)
        list_with_actual_numbers = app.person_enrollment.enrollment_doc_number
        assert is_doc_number_in_list_of_numbers(expected_number, list_with_actual_numbers)
        app.persons_page.return_to_persons_main_page(app)


def is_doc_number_in_list_of_numbers(expected, list_with_actual_numbers):
    for numbers in list_with_actual_numbers:
        if numbers.text == expected:
            return True
    return False


def fill_enrollment_in_person(app, name_of_json_file):
    app.person_enrollment.add_enrollment.click()
    enrollment = app.enrollments_main_page.fill_enrollment(name_of_json_file, "fill_data_enrollment")
    return enrollment.number_statements
