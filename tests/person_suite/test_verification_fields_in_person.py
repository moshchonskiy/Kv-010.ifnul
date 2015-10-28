#!/usr/bin/env python
# -*- coding: utf-8 -*-
from model.user import User
from utils.personCreator import PersonCreator

__author__ = 'stako'


def fill_main_person_page_with_invalid_data(app, person):
    """
    Method fill in the main persons page with invalid data.
    :param person: persons model in Person format with invalid data
    :param app: application context in Application format
    :return:
    """
    main_page = app.main_page
    main_page.is_this_page
    main_page.set_ukr_surname(person.surname_ukr)
    main_page.set_first_ukr_name(person.first_name_ukr)
    main_page.set_father_ukr_name(person.second_name_ukr)
    main_page.set_eng_surname(person.surname_eng)
    main_page.set_first_eng_name(person.first_name_eng)


def fill_extra_person_page_with_invalid_data(app, person):
    """
    Method fill in the extra persons page with invalid data.
    :param person: persons model in Person format
    :param app: application context in Application format
    :return:
    """
    extra_page = app.extra_page
    extra_page.is_this_page
    app.extra_page.set_private_case_numbers(person.private_case_number)


def test_verification_fields_in_person(app, dictionary_with_json_files):
    # create person
    create_person = PersonCreator(dictionary_with_json_files["person_incorrect"])
    person = create_person.create_person_from_json()

    # login and follow up to person's page
    app.ensure_logout()
    app.login(User.Admin(), True)
    assert app.persons_page.is_this_page

    # filling and asserting main page
    app.persons_page.add_person_link
    fill_main_person_page_with_invalid_data(app, person)
    assert app.main_page.person_surname_ukr_input_incorrect
    assert app.main_page.person_surname_eng_input_incorrect
    assert app.main_page.person_father_name_input_incorrect
    assert app.main_page.person_first_name_ukr_input_incorrect
    assert app.main_page.person_first_name_eng_input_incorrect

    # filling and asserting extra page
    app.person_base_page.click_extra_tab
    fill_extra_person_page_with_invalid_data(app, person)
    assert app.extra_page.private_case_number_input_incorrect
