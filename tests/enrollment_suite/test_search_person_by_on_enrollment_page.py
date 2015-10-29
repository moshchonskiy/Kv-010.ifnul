#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import pytest
from utils.data_provider_from_json import DataProviderJSON
from utils.personCreator import PersonCreator

__author__ = 'odeortc'


class TestSearchPersonBy(object):

    @pytest.fixture
    def real_person(request, dictionary_with_json_files):
        """
        Fixture create model of person which already exists in the system
        :return: Model of Person
        """
        create_person = PersonCreator(dictionary_with_json_files["existing_person"])
        return create_person.create_person_from_json()

    @pytest.fixture
    def values(request):
        return DataProviderJSON("values_for_enrollment_test.json").get_dict_value()

    def search_by(self, app, searched_value, searched_by_option):
        """
        Method performes searching by value and searching type
        :param searched_value: Value which need to find
        :param searched_by_option: Searching type in Integer. 0 - by PIB, 1 - by surname, 2 - by person id, 3 - by documents number
        :param app: application context in Application format
        :return:
        """
        app.internal_page.enrollments_page_link.click()
        app.enrollments_page.is_this_page
        app.enrollments_page.add_new_enrollment_button_click
        app.enrollments_main_page.is_this_page
        app.enrollments_main_page.select_person_by(searched_by_option)
        app.enrollments_main_page.set_search_person_by(searched_value)
        app.enrollments_main_page.ok_for_input_field

    def search_by_pib_and_surname(self, app, searched_value, searched_by_option, is_valid_value):
        """
        Method performes searching by PIB or surname
        :param searched_value: Value which need to find
        :param searched_by_option: Searching type in Integer. 0 - by PIB, 1 - by surname, 2 - by person id, 3 - by documents number
        :param is_valid_value: Boolean format. If searched_value is valid - True, else - False
        :param app: application context in Application format
        :return:
        """
        self.search_by(app, searched_value, searched_by_option)
        all_found_persons_pib = app.enrollments_main_page.get_all_found_persons_pib()
        check = False
        if is_valid_value and len(all_found_persons_pib) > 0:
            for pib in all_found_persons_pib:
                if pib.text.__contains__(searched_value):
                    check = True
                else:
                    check = False
                    break
        elif not is_valid_value and len(all_found_persons_pib) == 0:
            check = True
        app.enrollments_main_page.cancel_click
        return check

    def search_by_person_id(self, app, searched_value, searched_by_option, is_valid_value):
        """
        Method performes searching by person ID
        :param searched_value: Value which need to find
        :param searched_by_option: Searching type in Integer. 0 - by PIB, 1 - by surname, 2 - by person id, 3 - by documents number
        :param is_valid_value: Boolean format. If searched_value is valid - True, else - False
        :param app: application context in Application format
        :return:
        """
        self.search_by(app, searched_value, searched_by_option)
        all_found_persons_id = app.enrollments_main_page.get_all_found_persons_id()
        check = False
        if is_valid_value and len(all_found_persons_id) == 1 and all_found_persons_id[0].text == str(searched_value):
            check = True
        elif not is_valid_value and len(all_found_persons_id) == 0:
            check = True
        app.enrollments_main_page.cancel_click
        return check

    def search_by_doc_number(self, app, searched_value, persons_surname, searched_by_option, is_valid_value):
        """
        Method performes searching by documents number
        :param searched_value: Value which need to find
        :param searched_by_option: Searching type in Integer. 0 - by PIB, 1 - by surname, 2 - by person id, 3 - by documents number
        :param is_valid_value: Boolean format. If searched_value is valid - True, else - False
        :param app: application context in Application format
        :return:
        """
        self.search_by(app, searched_value, searched_by_option)
        all_found_persons_pib = app.enrollments_main_page.get_all_found_persons_pib()
        check = False
        if is_valid_value and len(all_found_persons_pib) > 0:
            for pib in all_found_persons_pib:
                if pib.text.__contains__(persons_surname):
                    check = True
                else:
                    check = False
                    break
        elif not is_valid_value and len(all_found_persons_pib) == 0:
            check = True
        app.enrollments_main_page.cancel_click
        return check

    def test_search_by_pib_valid(self, logout_login, real_person):
        assert self.search_by_pib_and_surname(logout_login, real_person.second_name_ukr, 0, True)

    def test_search_by_pib_invalid(self, logout_login, values):
        assert self.search_by_pib_and_surname(logout_login, values["search_by"]["invalid_pib"], 0, False)

    def test_search_by_surname_valid(self, logout_login, real_person):
        assert self.search_by_pib_and_surname(logout_login, real_person.surname_ukr, 1, True)

    def test_search_by_surname_invalid(self, logout_login, real_person):
        assert self.search_by_pib_and_surname(logout_login, real_person.second_name_ukr, 1, False)

    def test_search_by_person_id_valid(self, logout_login, values):
        assert self.search_by_person_id(logout_login, values["search_by"]["valid_person_id"], 2, True)

    def test_search_by_person_id_invalid(self, logout_login, values):
        assert self.search_by_person_id(logout_login, values["search_by"]["invalid_person_id"], 2, False)

    def test_search_by_doc_number_valid(self, logout_login, real_person):
        assert self.search_by_doc_number(logout_login, real_person.documents[0].document_case_number,
                                         real_person.surname_ukr, 3, True)

    def test_search_by_doc_number_invalid(self, logout_login, values):
        assert self.search_by_doc_number(logout_login, int(values["search_by"]["invalid_document_number"]),
                                         values["search_by"]["invalid_pib"], 3, False)