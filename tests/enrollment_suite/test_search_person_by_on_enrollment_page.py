#!/usr/bin/env python
# -*- coding: utf-8 -*-
from model.user import User
from time import sleep

__author__ = 'odeortc'


class TestSearchPersonBy(object):
    # BY_PIB = u"по ПІБ"
    # BY_SURNAME = u"по призвіщу"
    # BY_PERSON_ID = u"по id персони"
    # BY_DOCUMENT_NUMBER = u"по номеру документу"
    #
    # def __init__(self, app):
    #     self.app = app

    def test_search_by_pib(self, app):
        app.ensure_logout()
        app.login(User.Admin(), True)
        app.internal_page.is_element_present(app.internal_page.SPINNER_OFF)
        app.internal_page.enrollments_page_link.click()
        app.enrollments_page.is_this_page
        app.enrollments_page.add_new_enrollment_button_click
        app.enrollments_main_page.is_this_page
        app.enrollments_main_page.search_person_by(0)
        searched_pib = u"Gdfg"
        app.enrollments_main_page.set_search_person_by(searched_pib)
        app.enrollments_main_page.ok_for_input_field
        # app.enrollments_main_page.is_element_present(app.internal_page.SPINNER_OFF)
        all_found_persons_pib = app.enrollments_main_page.get_all_found_persons_pib()
        assert len(all_found_persons_pib) > 0
        check = False
        for pib in all_found_persons_pib:
            if pib.text.__contains__(searched_pib):
                check = True
            else:
                check = False
                break
        assert check
        sleep(5)