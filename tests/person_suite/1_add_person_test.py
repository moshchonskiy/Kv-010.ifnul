#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'acidroed'


def search_added_person(app, person):
    """
    Method searchs new added person
    :param person: persons model in Person format
    :param app: application context in Application format
    :return: finded persons surname
    """
    person_page = app.persons_page
    person_page.is_this_page
    person_page.try_get_choose_surname().click()
    person_page.try_get_input_group().clear()
    person_page.try_get_input_group().send_keys(person.surname_ukr)
    person_page.try_get_ok_button().click()
    return person_page.try_get_searched_surname(person.surname_ukr).text.partition(' ')[0]

def test_add_person(add_person, person):
    person_page = add_person.persons_page
    person_page.is_this_page
    person_page.add_person_link
    base_page = add_person.person_base_page

    main_page = add_person.main_page
    main_page.fill_in_main_person_page(person)
    base_page.click_next_button

    extra_page = add_person.extra_page
    extra_page.fill_in_extra_person_page(person)
    base_page.click_next_button
    base_page.click_next_button

    address_page = add_person.address_page
    address_page.fill_in_address_page(person)
    base_page.click_next_button
    base_page.click_next_button
    base_page.click_next_button

    contact_page = add_person.contact_page
    contact_page.fill_in_contact_page(person)
    base_page.click_next_button

    papers_page = add_person.papers_page
    papers_page.fill_in_document_page(person)
    base_page.save_new_person()

    assert search_added_person(add_person, person) == person.surname_ukr

