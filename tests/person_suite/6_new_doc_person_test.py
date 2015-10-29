__author__ = 'evgen'
from model.user import User
import pytest
import allure
from allure.constants import AttachmentType
import sys
import traceback

@pytest.allure.severity(pytest.allure.severity_level.NORMAL)  #BLOCKER, CRITICAL, NORMAL, MINOR, TRIVIAL. py.test my_tests/ --allure_severities=critical,blocker
def test_add_new_document(app, person):

    app.ensure_logged_in()

    with pytest.allure.step("Search person by surname before adding"):
        person_page = app.persons_page
        person_page.search_person_by_surname(person.surname_ukr)
    with pytest.allure.step("Open editing of person with clicking edit button"):
        person_page.edit_first_person_in_page.click()
    with pytest.allure.step("Go to documents page"):
        base_page = app.person_base_page
        base_page.click_extra_tab
        base_page.is_element_present(base_page.SPINNER_OFF)
        base_page.click_addresses_tab
        base_page.is_element_present(base_page.SPINNER_OFF)
        base_page.click_contacts_tab
        base_page.is_element_present(base_page.SPINNER_OFF)
        base_page.click_papers_tab
        base_page.is_element_present(base_page.SPINNER_OFF)
    with pytest.allure.step("Adding new document to the person"):
        app.papers_page.fill_in_document_page(person)
        base_page.save_new_person()

    with pytest.allure.step("Search person by surname after adding"):
        person_page.search_person_by_surname(person.surname_ukr)
    with pytest.allure.step("Open editing of person with clicking edit button"):
        person_page.edit_first_person_in_page.click()
        base_page = app.person_base_page
        base_page.click_extra_tab
        base_page.is_element_present(base_page.SPINNER_OFF)
        base_page.click_addresses_tab
        base_page.is_element_present(base_page.SPINNER_OFF)
        base_page.click_contacts_tab
        base_page.is_element_present(base_page.SPINNER_OFF)
        base_page.click_papers_tab
    with pytest.allure.step("Checking that new person document is added "):
        try:
            actual = app.papers_page.try_get_searched_doc_num(person.documents[0].document_case_number).text
            expected = str(person.documents[0].document_case_number)
            assert actual == expected
            allure.attach('screenshot', app.papers_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
        except AssertionError:
            allure.attach('screenshot', app.papers_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
            print_simple_stacktrace()
            raise

        app.papers_page.delete_all_person_documents()
        base_page.save_new_person()


def print_simple_stacktrace():
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        print('An error occurred on line: {}, in statement: {}. The filename is: {}, and function is: {}.'
              .format(line, text, filename, func))

