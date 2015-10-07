# -*- coding: utf-8 -*-
__author__ = 'Evgen'
import pytest
from model.user import User
from selenium import webdriver
from model.application import Application


class TestSearchFilters(object):
    # driver = webdriver.Firefox()
    # base_url = "http://localhost:9000"
    # app = Application(driver, base_url)

    def test_search_by_person_id(self, app):

        app.ensure_logged_in()
        app.internal_page.is_this_page
        app.internal_page.enrollments_page_link.click()
        app.enrollments_page.is_this_page
        en_page = app.enrollments_page
        with pytest.allure.step("Searching by person ID"):
            assert en_page.search_enrollment(en_page.SEARCH_METHOD["person_id"], "9") == "9"

    def test_search_by_document_series(self, app):
        en_page = app.enrollments_page
        with pytest.allure.step("Searching by document's series"):
            assert en_page.search_enrollment(en_page.SEARCH_METHOD["document_series"], "232") == "232"

    def test_search_by_document_number(self, app):
        en_page = app.enrollments_page
        with pytest.allure.step("Searching by document's number"):
            assert en_page.search_enrollment(en_page.SEARCH_METHOD["document_number"], "3333") == "3333"

    def test_search_by_proposal_id(self, app):
        en_page = app.enrollments_page
        with pytest.allure.step("Searching by proposal ID"):
            assert en_page.search_enrollment(en_page.SEARCH_METHOD["proposal_id"], "5") == "5"

    def test_filter_by_budget(self, app):

        app.ensure_logout()
        app.login(User.Admin())
        app.internal_page.is_this_page
        app.internal_page.enrollments_page_link.click()
        app.enrollments_page.is_this_page
        enr_page = app.enrollments_page
        enr_page.add_table_columns(enr_page.COLUMN_BUDGET_ADD)
        enr_page.add_filters(enr_page.FILTER_BUDGET)
        actual = enr_page.get_columns_text(enr_page.BUDGET_COLUMN)
        expected = enr_page.FILTER_RESULTS["budget"]
        assert actual == expected

    def test_filter_by_not_budget(self, app):

        app.ensure_logout()
        app.login(User.Admin())
        app.internal_page.is_this_page
        app.internal_page.enrollments_page_link.click()
        app.enrollments_page.is_this_page
        enr_page = app.enrollments_page
        enr_page.add_filters(enr_page.FILTER_NOT_BUDGET)
        actual = enr_page.get_columns_text(enr_page.BUDGET_COLUMN)
        expected = enr_page.FILTER_RESULTS["not_budget"]
        assert actual == expected

    def test_filter_by_privileges(self, app):
        app.ensure_logout()
        app.login(User.Admin())
        app.internal_page.is_this_page
        app.internal_page.enrollments_page_link.click()
        app.enrollments_page.is_this_page
        enr_page = app.enrollments_page
        enr_page.add_filters(enr_page.FILTER_PRIVILEGES)
        actual = enr_page.get_columns_text(enr_page.PRIVILEGES_COLUMN)
        expected = enr_page.FILTER_RESULTS["privileged"]
        assert actual == expected

    def test_filter_by_privileges(self, app):
        app.ensure_logout()
        app.login(User.Admin())
        app.internal_page.is_this_page
        app.internal_page.enrollments_page_link.click()
        app.enrollments_page.is_this_page
        enr_page = app.enrollments_page
        enr_page.add_filters(enr_page.FILTER_NOT_PRIVILEGES)
        actual = enr_page.get_columns_text(enr_page.PRIVILEGES_COLUMN)
        expected = enr_page.FILTER_RESULTS["not_privileged"]
        assert actual == expected

    def test_filter_mix(self, app):
        app.ensure_logout()
        app.login(User.Admin())
        app.internal_page.is_this_page
        app.internal_page.enrollments_page_link.click()
        app.enrollments_page.is_this_page
        enr_page = app.enrollments_page
        enr_page.add_filters(enr_page.FILTER_NOT_PRIVILEGES, enr_page.FILTER_BUDGET, enr_page.FILTER_NEED_ACCOMMODATION)
        actual = enr_page.get_columns_text(enr_page.PRIVILEGES_COLUMN, enr_page.BUDGET_COLUMN, enr_page.ACCOMMODATION_COLUMN)
        expected = {enr_page.FILTER_RESULTS["not_privileged"], enr_page.FILTER_RESULTS["budget"], enr_page.FILTER_RESULTS["accommodation"]}
        assert actual == expected

    def test_delete_filters(self, app):
        app.ensure_logout()
        app.login(User.Admin())
        app.internal_page.is_this_page
        app.internal_page.enrollments_page_link.click()
        app.enrollments_page.is_this_page
        enr = app.enrollments_page
        enr.add_filters(enr.FILTER_NEED_ACCOMMODATION, enr.FILTER_BUDGET, enr.FILTER_CONTRACT)
        enr.delete_all_filters()
        assert len(enr.driver.find_elements(*enr.DELETE_FILTER_BUTTON)) == 0
