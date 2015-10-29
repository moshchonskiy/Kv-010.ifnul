__author__ = 'evgen'
from model.user import User
import pytest
import allure

@pytest.allure.severity(pytest.allure.severity_level.NORMAL)  #BLOCKER, CRITICAL, NORMAL, MINOR, TRIVIAL. py.test my_tests/ --allure_severities=critical,blocker
def test_add_new_document(app, person):

    app.ensure_logged_in()

    with pytest.allure.step("Search person by surname before adding"):
        person_page = app.persons_page
        person_page.search_person_by_surname(person.surname_ukr)
    with pytest.allure.step("Open editing of person with clicking edit button"):
        person_page.edit_first_person_in_page
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
        person_page.edit_first_person_in_page
        base_page = app.person_base_page
        base_page.click_extra_tab
        base_page.is_element_present(base_page.SPINNER_OFF)
        base_page.click_addresses_tab
        base_page.is_element_present(base_page.SPINNER_OFF)
        base_page.click_contacts_tab
        base_page.is_element_present(base_page.SPINNER_OFF)
        base_page.click_papers_tab
    with pytest.allure.step("Checking that new person document is added "):
        actual = app.papers_page.try_get_searched_doc_num(person.documents[0].document_case_number).text
        expected = str(person.documents[0].document_case_number)
        assert actual == expected
        app.papers_page.delete_all_person_documents()
        base_page.save_new_person()


