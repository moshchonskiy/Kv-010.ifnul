# -*- coding: utf-8 -*-

__author__ = 'Vadym'


class TestSearchOfferEnrollement(object):

    def test_search_by_person_id(self, app):
        app.ensure_logged_in()
        app.internal_page.is_this_page
        app.internal_page.enrollments_page_link.click()
        app.enrollments_page.is_this_page
        app.enrollments_page.is_this_page.click()

        enr_page = app.enrollments_main_page

        enr_page.search_offers("Біологічний", "Спеціаліст")

        enr_page.button_choose_specialties()

        actual_data_offer = enr_page.get_arr_structural_subdivision_choose_offer()
        actual_data_form_of_education = enr_page.get_arr_type_offer_from_choose_offer()