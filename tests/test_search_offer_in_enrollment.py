# -*- coding: utf-8 -*-
__author__ = 'Vadym'


class TestSearchOfferEnrollement(object):

    OFFER = "Біологічний"
    FORM_OF_EDUCATION = "Спеціаліст"

    def test_search_offer_in_enrollements(self, app):
        app.ensure_logged_in()
        app.internal_page.is_this_page
        app.internal_page.enrollments_page_link.click()
        app.enrollments_page.is_this_page
        app.enrollments_page.is_this_page.click()
        app.enrollments_main_page.search_offers(self.OFFER, self.FORM_OF_EDUCATION)

    def test_check_correct_structural_subdivision(self, app):
        enr_page = app.enrollments_main_page
        actual_data_structural_subdivision = enr_page.get_arr_structural_subdivision_from_choose_offer()
        for actual_data in actual_data_structural_subdivision:
            assert u"Біологічний" == actual_data

    def test_check_correct_type_of_offer(self, app):
        enr_page = app.enrollments_main_page
        actual_data_type_offer = enr_page.get_arr_type_offer_from_choose_offer()
        for actual_data in actual_data_type_offer:
            assert u"Спеціаліст" == actual_data

    # def test_correct_added_offer(self, app):
    #     enr_page = app.enrollments_page
    #     enr_page.choose_first_specialties.click()

