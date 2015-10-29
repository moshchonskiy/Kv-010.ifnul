#!/usr/bin/env python
# -*- coding: utf-8 -*-
from model.user import User
from utils.add_person_pattern import AddPersonPattern
from utils.personCreator import PersonCreator


def test_add_enrollment_in_new_person(app, dictionary_with_json_files):
    create_person = PersonCreator(dictionary_with_json_files["person"])
    person = create_person.create_person_from_json()
    add_person = AddPersonPattern()

    app.ensure_logout()
    app.login(User.Admin(), True)
    app.internal_page.is_element_present(app.internal_page.SPINNER_OFF)
    # assert app.persons_page.is_this_page
    add_person.search_person_by_surname(app, person.surname_ukr)
    app.internal_page.is_element_present(app.internal_page.SPINNER_OFF)
    app.persons_page.edit_first_person_in_page.click()
    app.person_base_page.enrollments_tab.click()
    expected_number = fill_enrollment_in_person(app, "fill_enrollment_main.json")
    list_with_actual_numbers = app.person_enrollment.enrollment_doc_number
    assert is_doc_number_in_list_of_numbers(expected_number, list_with_actual_numbers)


def is_doc_number_in_list_of_numbers(expected, list_with_actual_numbers):
    for numbers in list_with_actual_numbers:
        if numbers.text == expected:
            return True
    return False


def fill_enrollment_in_person(app, name_of_json_file):
    app.person_enrollment.add_enrollment.click()
    enrollment = app.enrollments_main_page.fill_enrollment(name_of_json_file, "fill_data_enrollment")
    return enrollment.number_statements

