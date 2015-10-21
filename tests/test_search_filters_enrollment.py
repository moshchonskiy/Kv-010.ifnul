# -*- coding: utf-8 -*-
from model.user import User
from allure.constants import AttachmentType
import pytest
import allure
import sys
import traceback

__author__ = 'Evgen'


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
        with pytest.allure.step("Searching by person ID"):
            en_page = app.enrollments_page
            expected_id = "9"
            actual_search = en_page.search_enrollment(en_page.SEARCH_METHOD["person_id"], "9")
            try:
                assert expected_id in actual_search
                allure.attach('screenshot', en_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
            except AssertionError:
                allure.attach('screenshot', en_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
                self.print_simple_stacktrace()
                raise

    def test_search_by_document_series(self, app):
        en_page = app.enrollments_page
        with pytest.allure.step("Searching by document's series"):
            expected_document_series = u'авіа'
            actual_search = en_page.search_enrollment(en_page.SEARCH_METHOD["document_series"], u'аві')
            try:
                assert expected_document_series in actual_search
                allure.attach('screenshot', en_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
            except AssertionError:
                allure.attach('screenshot', en_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
                self.print_simple_stacktrace()
                raise

    def test_search_by_document_number(self, app):
        en_page = app.enrollments_page
        with pytest.allure.step("Searching by document's number"):
            expected_number = "3333"
            actual_search = en_page.search_enrollment(en_page.SEARCH_METHOD["document_number"], "3333")
            try:
                assert expected_number in actual_search
                allure.attach('screenshot', en_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
            except AssertionError:
                allure.attach('screenshot', en_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
                self.print_simple_stacktrace()
                raise

    def test_search_by_proposal_id(self, app):
        en_page = app.enrollments_page
        with pytest.allure.step("Searching by proposal ID"):
            expected_id = "5"
            actual_search_results = en_page.search_enrollment(en_page.SEARCH_METHOD["proposal_id"], "5")
            try:
                assert expected_id in actual_search_results
            except AssertionError:
                allure.attach('screenshot', en_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
                self.print_simple_stacktrace()
                raise

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
            try:
                assert actual == expected
                allure.attach('screenshot', enr_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
            except AssertionError:
                allure.attach('screenshot', enr_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
                self.print_simple_stacktrace()
                raise



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
            try:
                assert actual == expected
                allure.attach('screenshot', enr_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
            except AssertionError:
                allure.attach('screenshot', enr_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
                self.print_simple_stacktrace()
                raise

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
            try:
                assert actual == expected
                allure.attach('screenshot', enr_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
            except AssertionError:
                allure.attach('screenshot', enr_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
                self.print_simple_stacktrace()
                raise

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
            try:
                assert actual == expected
                allure.attach('screenshot', enr_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
            except AssertionError:
                allure.attach('screenshot', enr_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
                self.print_simple_stacktrace()
                raise

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
            try:
                assert actual == expected
                allure.attach('screenshot', enr_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
            except AssertionError:
                allure.attach('screenshot', enr_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
                self.print_simple_stacktrace()
                raise

    def test_delete_filters(self, app):
        with pytest.allure.step("Authorize on the site with admin credentials"):
            app.ensure_logout()
            app.login(User.Admin())
            app.internal_page.is_this_page
        with pytest.allure.step("Go to enrollments page"):
            app.internal_page.enrollments_page_link.click()
            app.enrollments_page.is_this_page
        with pytest.allure.step("In the filters section add necessary filters"):
            enr_page = app.enrollments_page
            enr_page.add_filters(enr_page.FILTER_NEED_ACCOMMODATION, enr_page.FILTER_BUDGET, enr_page.FILTER_CONTRACT)
        with pytest.allure.step("Delete all the filters"):
            enr_page.delete_all_filters()
        with pytest.allure.step("Check the results"):
            actual = len(enr_page.driver.find_elements(*enr_page.DELETE_FILTER_BUTTON))
            expected = 0
            try:
                assert actual == expected
                allure.attach('screenshot', enr_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
            except AssertionError:
                allure.attach('screenshot', enr_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
                self.print_simple_stacktrace()
                raise


    def print_simple_stacktrace(self):
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        print('An error occurred on line: {}, in statement: {}. The filename is: {}, and function is: {}.'
              .format(line, text, filename, func))
