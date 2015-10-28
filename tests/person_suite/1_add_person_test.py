#!/usr/bin/env python
# -*- coding: utf-8 -*-
from utils.add_person_pattern import AddPersonPattern

__author__ = 'acidroed'


def test_add_person(app, person):
    add_person_pattern = AddPersonPattern()
    add_person_pattern.add_person(app, person)
    person_page = app.persons_page
    person_page.is_this_page
    person_page.add_person_link
    base_page = app.person_base_page

    main_page = app.main_page
    main_page.fill_in_main_person_page(person)
    base_page.click_extra_tab

    extra_page = app.extra_page
    extra_page.fill_in_extra_person_page(person)
    base_page.click_addresses_tab

    address_page = app.address_page
    address_page.fill_in_address_page(person)
    base_page.click_contacts_tab

    contact_page = app.contact_page
    contact_page.fill_in_contact_page(person)
    base_page.click_papers_tab

    papers_page = app.papers_page
    papers_page.fill_in_document_page(person)
    base_page.save_new_person()

    assert app.persons_page.return_added_person_surname(person) == person.surname_ukr



