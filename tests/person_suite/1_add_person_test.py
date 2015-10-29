#!/usr/bin/env python
# -*- coding: utf-8 -*-
from utils.add_person_pattern import AddPersonPattern
import pytest
from allure.constants import AttachmentType
import allure
import sys
import traceback
__author__ = 'acidroed'

@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
def test_add_person(app, person):
    with pytest.allure.step('Authorize to the application and click add person button'):
        add_person_pattern = AddPersonPattern()
        add_person_pattern.login_and_delete_all_person_by_name(app, person)
        person_page = app.persons_page
        person_page.is_this_page
        person_page.add_person_link
        base_page = app.person_base_page
    with pytest.allure.step('Fill data on the main add person page'):
        main_page = app.main_page
        main_page.fill_in_main_person_page(person)
        base_page.click_extra_tab
    with pytest.allure.step('Fill data on the extra add person page'):
        extra_page = app.extra_page
        extra_page.fill_in_extra_person_page(person)
        base_page.click_addresses_tab
    with pytest.allure.step('Fill data on the address add person page'):
        address_page = app.address_page
        address_page.fill_in_address_page(person)
        base_page.click_contacts_tab
    with pytest.allure.step('Fill data on the contacts add person page'):
        contact_page = app.contact_page
        contact_page.fill_in_contact_page(person)
        base_page.click_papers_tab
    with pytest.allure.step('Fill data on the documents add person page'):
        papers_page = app.papers_page
        papers_page.fill_in_document_page(person)
        base_page.save_new_person()
    with pytest.allure.step('Assert surname of added person is the same as from input data'):
        try:
            assert app.persons_page.return_added_person_surname(person) == person.surname_ukr
            allure.attach('screenshot', app.papers_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
        except AssertionError:
            allure.attach('screenshot', app.papers_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
            print_simple_stacktrace()
            raise

def print_simple_stacktrace():
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        print('An error occurred on line: {}, in statement: {}. The filename is: {}, and function is: {}.'
              .format(line, text, filename, func))

