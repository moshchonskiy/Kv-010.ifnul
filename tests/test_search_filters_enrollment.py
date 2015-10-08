# -*- coding: utf-8 -*-
__author__ = 'Evgen'
import pytest

from model.user import User


class TestSearchFilters(object):
    # driver = webdriver.Firefox()
    # base_url = "http://localhost:9000"
    # app = Application(driver, base_url)

    def test_search_by_person_id(self, app):
        with pytest.allure.step("Authorize on the site with admin credentials"):
            app.ensure_logged_in()
            app.internal_page.is_this_page
        with pytest.allure.step("Go to enrollments page"):
            app.internal_page.enrollments_page_link.click()
            app.enrollments_page.is_this_page
        en_page = app.enrollments_page
        with pytest.allure.step("Searching by person ID"):
            assert "9" in en_page.search_enrollment(en_page.SEARCH_METHOD["person_id"], "9")

    def test_search_by_document_series(self, app):
        en_page = app.enrollments_page
        with pytest.allure.step("Searching by document's series"):
            assert u'авіа' in en_page.search_enrollment(en_page.SEARCH_METHOD["document_series"], u'аві')

    def test_search_by_document_number(self, app):
        en_page = app.enrollments_page
        with pytest.allure.step("Searching by document's number"):
            assert "3333" in en_page.search_enrollment(en_page.SEARCH_METHOD["document_number"], "3333")

    def test_search_by_proposal_id(self, app):
        en_page = app.enrollments_page
        with pytest.allure.step("Searching by proposal ID"):
            assert "5" in en_page.search_enrollment(en_page.SEARCH_METHOD["proposal_id"], "5")

    def test_filter_by_budget(self, app):
        with pytest.allure.step("Authorize on the site with admin credentials"):
            app.ensure_logout()
            app.login(User.Admin())
            app.internal_page.is_this_page
        with pytest.allure.step("Go to enrollments page"):
            app.internal_page.enrollments_page_link.click()
            app.enrollments_page.is_this_page
        with pytest.allure.step("Add budget column"):
            enr_page = app.enrollments_page
            enr_page.add_table_columns(enr_page.COLUMN_BUDGET_ADD)
        with pytest.allure.step("In the filters section click on budget filter"):
            enr_page.add_filters(enr_page.FILTER_BUDGET)
        with pytest.allure.step("Check the results"):
            actual = enr_page.get_columns_text(enr_page.BUDGET_COLUMN)
            expected = {enr_page.FILTER_RESULTS["budget"]}
            assert actual == expected

    def test_filter_by_not_budget(self, app):
        with pytest.allure.step("Authorize on the site with admin credentials"):
            app.ensure_logout()
            app.login(User.Admin())
            app.internal_page.is_this_page
        with pytest.allure.step("Go to enrollments page"):
            app.internal_page.enrollments_page_link.click()
            app.enrollments_page.is_this_page
        with pytest.allure.step("In the filters section add not budget filter"):
            enr_page = app.enrollments_page
            enr_page.add_filters(enr_page.FILTER_NOT_BUDGET)
        with pytest.allure.step("Check the results"):
            actual = enr_page.get_columns_text(enr_page.BUDGET_COLUMN)
            expected = {enr_page.FILTER_RESULTS["not_budget"]}
            assert actual == expected

    def test_filter_by_privileges(self, app):
        with pytest.allure.step("Authorize on the site with admin credentials"):
            app.ensure_logout()
            app.login(User.Admin())
            app.internal_page.is_this_page
        with pytest.allure.step("Go to enrollments page"):
            app.internal_page.enrollments_page_link.click()
            app.enrollments_page.is_this_page
        with pytest.allure.step("In the filters section add privileges filter"):
            enr_page = app.enrollments_page
            enr_page.add_filters(enr_page.FILTER_PRIVILEGES)
        with pytest.allure.step("Check the results"):
            actual = enr_page.get_columns_text(enr_page.PRIVILEGES_COLUMN)
            expected = {enr_page.FILTER_RESULTS["privileged"]}
            assert actual == expected

    def test_filter_by_not_privileges(self, app):
        with pytest.allure.step("Authorize on the site with admin credentials"):
            app.ensure_logout()
            app.login(User.Admin())
            app.internal_page.is_this_page
        with pytest.allure.step("Go to enrollments page"):
            app.internal_page.enrollments_page_link.click()
            app.enrollments_page.is_this_page
        with pytest.allure.step("In the filters section add not privileges filter"):
            enr_page = app.enrollments_page
            enr_page.add_filters(enr_page.FILTER_NOT_PRIVILEGES)
        with pytest.allure.step("Check the results"):
            actual = enr_page.get_columns_text(enr_page.PRIVILEGES_COLUMN)
            expected = {enr_page.FILTER_RESULTS["not_privileged"]}
            assert actual == expected

    def test_filter_mix(self, app):
        with pytest.allure.step("Authorize on the site with admin credentials"):
            app.ensure_logout()
            app.login(User.Admin())
            app.internal_page.is_this_page
        with pytest.allure.step("Go to enrollments page"):
            app.internal_page.enrollments_page_link.click()
            app.enrollments_page.is_this_page
        with pytest.allure.step("In the filters section add necessary filters"):
            enr_page = app.enrollments_page
            enr_page.add_filters(enr_page.FILTER_NOT_PRIVILEGES, enr_page.FILTER_BUDGET,
                                 enr_page.FILTER_NEED_ACCOMMODATION)
        with pytest.allure.step("Check the results"):
            actual = enr_page.get_columns_text(enr_page.PRIVILEGES_COLUMN, enr_page.BUDGET_COLUMN,
                                               enr_page.ACCOMMODATION_COLUMN)
            expected = {enr_page.FILTER_RESULTS["not_privileged"], enr_page.FILTER_RESULTS["budget"],
                        enr_page.FILTER_RESULTS["accommodation"]}
            assert actual == expected

    def test_delete_filters(self, app):
        with pytest.allure.step("Authorize on the site with admin credentials"):
            app.ensure_logout()
            app.login(User.Admin())
            app.internal_page.is_this_page
        with pytest.allure.step("Go to enrollments page"):
            app.internal_page.enrollments_page_link.click()
            app.enrollments_page.is_this_page
        with pytest.allure.step("In the filters section add necessary filters"):
            enr = app.enrollments_page
            enr.add_filters(enr.FILTER_NEED_ACCOMMODATION, enr.FILTER_BUDGET, enr.FILTER_CONTRACT)
        with pytest.allure.step("Delete all the filters"):
            enr.delete_all_filters()
        with pytest.allure.step("Check the results"):
            assert len(enr.driver.find_elements(*enr.DELETE_FILTER_BUTTON)) == 0
