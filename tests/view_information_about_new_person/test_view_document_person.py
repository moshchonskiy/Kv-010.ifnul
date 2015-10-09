# coding=utf-8
from model.user import User
from utility.personCreator import PersonCreator

__author__ = 'Vadym'

class TestViewDocumentPerson(object):

    person_creator = PersonCreator()
    person = person_creator.create_person_from_json("person_test_view.json")

    def test_login_page_document_verify(self, app):
        app.ensure_logout()
        app.login(User.Admin())
        app.internal_page.is_this_page

        person_page = app.persons_page
        person_page.try_get_choose_surname().click()
        person_page.try_get_input_group().clear()
        person_page.try_get_input_group().send_keys(self.person.surname_ukr)
        person_page.try_get_ok_button().click()
        app.person_current_view_page.is_element_present(app.person_current_view_page.SPINNER_OFF)
        person_page.view_first_person_in_page

        app.person_current_view_page.is_element_present(app.person_current_view_page.SPINNER_OFF)
        assert app.person_papers_view_page.get_text_person_profile() == u"Перегляд персони"

        app.person_main_view_page.person_document_button().click()
        app.person_papers_view_page.is_element_present(app.person_papers_view_page.SPINNER_OFF)

        if(len(self.person.documents) > 0):
            assert app.person_papers_view_page.is_table_present() == True

    # Нужно переделать логику, что бы ассерт был не по сортировке всех данных в таблице, а по строке.
    # Так как есть вероятность что данные с разных строк пересекуться, но тест пройдет все равно
    def test_verify_table_with_papers(self, app):
        if(len(self.person.documents) == 0):
            return
        data_table_papers = []
        for document in self.person.documents:
            data_table_papers.append(document.document_name)
            data_table_papers.append(document.document_case_char)
            data_table_papers.append(str(document.document_case_number))
            data_table_papers.append(document.day_of_issue)
            data_table_papers.append(document.issued_by)
            data_table_papers.append(self.__get_specific_symbol(document.document_is_original))
            data_table_papers.append(self.__get_specific_symbol(document.document_is_foreign))

        count_documents = len(self.person.documents)
        count_row_in_table = app.person_papers_view_page.get_count_row_in_table_documents()
        assert count_row_in_table == count_documents

        arr_info_from_table_web = app.person_papers_view_page.get_data_from_table()

        data_table_papers.sort()
        arr_info_from_table_web.sort()

        assert len(data_table_papers) == len(arr_info_from_table_web)

        for index, value_from_web in enumerate(arr_info_from_table_web):
            assert data_table_papers[index] == value_from_web

    # private methods
    def __get_specific_symbol(self, boolean):
        if(boolean == True):
            return u'✓'
        else:
            return u'✘'