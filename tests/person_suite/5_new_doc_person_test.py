__author__ = 'evgen'
from model.user import User

def login(app):
    app.ensure_logout()
    app.login(User.Admin())


def test_add_new_document(app, person):
    login(app)
    person_page = app.persons_page
    person_page.edit_first_person_in_page

    base_page = app.person_base_page
    base_page.click_next_button
    base_page.click_next_button
    base_page.click_next_button
    base_page.click_next_button
    base_page.click_next_button
    base_page.click_next_button
    base_page.click_next_button

    papers_page = app.papers_page
    papers_page.fill_in_document_page(person)
    actual = app.papers_page.try_get_searched_doc_num(person.documents[0].document_case_number).text
    expected = str(person.documents[0].document_case_number)
    assert actual == expected
    papers_page.delete_first_document_in_page
    base_page.save_new_person()


