#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'acidroed'


from utility.personCreator import PersonCreator
from model.user import User

def test_add_person(app):
    person_creator = PersonCreator()
    person = person_creator.create_person_from_json("person.json")

    app.ensure_logout()
    app.login(User.Admin(), True)

    person_page = app.persons_page
    person_page.is_this_page
    person_page.add_person_link

    main_page = app.main_page
    main_page.is_this_page
    main_page.person_type_select_click()
    main_page.choose_person_type(person.person_type)
    main_page.set_ukr_surname(person.surname_ukr)
    main_page.set_first_ukr_name(person.first_name_ukr)
    main_page.set_father_ukr_name(person.second_name_ukr)
    main_page.set_eng_surname(person.surname_eng)
    main_page.set_first_eng_name(person.first_name_eng)
    main_page.click_next_button

    extra_page = app.extra_page
    extra_page.is_this_page
    extra_page.set_persons_birth_day(person.birth_day)
    extra_page.choose_person_sex_type(person.sex)
    extra_page.choose_person_martial_status(person.marital_status)
    extra_page.choose_person_nationality(person.nationality)
    extra_page.set_private_case_chars(person.private_case_chars)
    extra_page.set_private_case_numbers(person.private_case_number)
    extra_page.check_resident_status(person.is_outlander)
    extra_page.check_reservist_status(person.reservist)
    extra_page.check_needed_hostel_status(person.hostel_need)
    extra_page.click_next_button
    extra_page.click_next_button

    address_page = app.address_page
    address_page.is_this_page
    for i in range(0, len(person.burn_place)):
        address_page.select_birth_place(person.burn_place[i], i)

    for i in range(0, len(person.registration_place["area"])):
        address_page.select_registration_address(person.registration_place["area"][i], i)

    address_page.set_zip_code(person.registration_place["index"])
    address_page.reg_address_type_select(person.registration_place["type"])
    address_page.set_street(person.registration_place["street"])
    address_page.set_house(person.registration_place["house"])
    address_page.set_apartment(person.registration_place["apartment"])
    address_page.check_is_reg_and_post_addresses_the_same(person.registration_place["is_addresses_match"])
    address_page.click_next_button
    address_page.click_next_button
    address_page.click_next_button

    contact_page = app.contact_page
    contact_page.is_this_page
    contact_page.set_first_mobile_phone(person.mobile_phone1)
    contact_page.set_second_mobile_phone(person.mobile_phone2)
    contact_page.set_home_phone(person.home_phone)
    contact_page.set_work_phone(person.work_phone)
    contact_page.set_email(person.email)
    contact_page.set_skype(person.skype)
    contact_page.set_site(person.web_site)
    contact_page.set_icq(person.icq)
    contact_page.click_next_button

    papers_page = app.papers_page
    papers_page.is_this_page
    papers_page.press_add_new_document_button
    papers_page.document_type_select(person.documents[0].category)
    papers_page.document_name_select(person.documents[0].document_name)
    papers_page.set_document_series(person.documents[0].document_case_char)
    papers_page.set_document_number(person.documents[0].document_case_number)
    papers_page.set_day_of_issue(person.documents[0].day_of_issue)
    papers_page.set_document_maker(person.documents[0].issued_by)
    papers_page.check_is_original_document(person.documents[0].document_is_original)
    papers_page.check_is_foreign_document(person.documents[0].document_is_foreign)
    papers_page.press_save_new_document_button
    papers_page.save_new_person()

    person_page.try_get_choose_surname().click()
    person_page.try_get_input_group().clear()
    person_page.try_get_input_group().send_keys(person.surname_ukr)
    person_page.try_get_ok_button().click()
    expected_person = person_page.try_get_expected_surname(person.surname_ukr).text.partition(' ')[0]
    person_page.delete_first_person_in_page

    assert expected_person == person.surname_ukr

