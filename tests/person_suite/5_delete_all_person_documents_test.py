__author__ = 'evgen'
from model.user import User
import pytest
from allure.constants import AttachmentType
import allure
import sys
import traceback

@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
def test_delete_person_documents(app, person):
    app.ensure_logout()
    app.login(User.Admin())

    with pytest.allure.step("Search person by surname before deleting"):
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
    with pytest.allure.step("Deleting all person's document"):
        app.papers_page.delete_all_person_documents()
        base_page.save_new_person()

    with pytest.allure.step("Search person by surname after deleting"):
        person_page.search_person_by_surname(person.surname_ukr)
        person_page.edit_first_person_in_page.click()
        base_page = app.person_base_page
        base_page.click_extra_tab
        base_page.is_element_present(base_page.SPINNER_OFF)
        base_page.click_addresses_tab
        base_page.is_element_present(base_page.SPINNER_OFF)
        base_page.click_contacts_tab
        base_page.is_element_present(base_page.SPINNER_OFF)
        base_page.click_papers_tab
    with pytest.allure.step("Checking that all person's document are deleted"):
        try:
            actual = app.papers_page.get_number_of_person_documents()
            expected = 0
            assert actual == expected
            allure.attach('screenshot', app.papers_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
        except AssertionError:
            allure.attach('screenshot', app.papers_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
            print_simple_stacktrace()
            raise

    base_page.save_new_person()


def print_simple_stacktrace():
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        print('An error occurred on line: {}, in statement: {}. The filename is: {}, and function is: {}.'
              .format(line, text, filename, func))

