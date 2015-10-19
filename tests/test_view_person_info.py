# coding=utf-8
from model.user import User
from utils.personCreator import PersonCreator

__author__ = 'Vadym'

class TestViewPersonInfo(object):

    person_creator = PersonCreator()
    person = person_creator.create_person_from_json("person_test_view.json")

    def test_global_info_about_person(self, app):
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

        personUkrFIO = self.person.surname_ukr + " " + self.person.first_name_ukr + " " + self.person.second_name_ukr
        personEngFIO = self.person.surname_eng + " " + self.person.first_name_eng
        data_main_info_person = [personUkrFIO, personEngFIO, self.person.private_case_chars, str(self.person.private_case_number)]

        assert data_main_info_person[0] == app.person_current_view_page.get_fio_ukranian().text
        assert data_main_info_person[1] == app.person_current_view_page.get_fio_english().text
        assert data_main_info_person[2] == app.person_current_view_page.get_serial_person_record()
        assert data_main_info_person[3] == app.person_current_view_page.get_number_person_record()

    def test_main_info_about_person(self, app):
        data_main_info_person = []

        data_main_info_person.append(self.person.person_type)
        data_main_info_person.append(self.get_correct_birth_view(self.person.birth_day))
        data_main_info_person.append(self.__get_specific_symbol(self.person.reservist))
        data_main_info_person.append(self.person.sex)
        data_main_info_person.append(self.person.marital_status)
        data_main_info_person.append(self.__get_specific_symbol(self.person.is_outlander))
        data_main_info_person.append(self.person.nationality)
        data_main_info_person.append(self.__get_specific_symbol(self.person.hostel_need))

        arr_main_info_from_web = app.person_current_view_page.get_arr_main_info_about_person()

        assert len(data_main_info_person) == len(arr_main_info_from_web)
        # assert array by values
        for index, value_from_web in enumerate(arr_main_info_from_web):
            assert data_main_info_person[index] == value_from_web

    def test_place_of_birth(self, app):
        data_birth_person = self.person.burn_place
        size_data_birth = len(data_birth_person)
        count_of_elements_on_web = app.person_current_view_page.get_count_elements_place_of_birth()
        assert count_of_elements_on_web == size_data_birth

        arr_main_info_from_web = app.person_current_view_page.get_arr_place_of_birth()

        for index, value_from_web in enumerate(arr_main_info_from_web):
            assert data_birth_person[index] == value_from_web

    def test_addres_of_registration(self, app):
        data_addres_registration = self.person.registration_place["area"]
        size_data_addres = len(data_addres_registration)
        count_of_elements_on_web = app.person_current_view_page.get_count_elements_addres_of_registration()
        assert count_of_elements_on_web == size_data_addres

        arr_addres_of_reg_from_web = app.person_current_view_page.get_arr_addres_of_registration()

        for index, value_from_web in enumerate(arr_addres_of_reg_from_web):
            assert data_addres_registration[index] == value_from_web

    def test_exact_address_of_registration(self, app):
        data_exact_addres = []
        data_exact_addres.append(str(self.person.registration_place["index"]))
        data_exact_addres.append(self.person.registration_place["type"])
        data_exact_addres.append(self.person.registration_place["street"])
        data_exact_addres.append(str(self.person.registration_place["house"]))
        data_exact_addres.append(str(self.person.registration_place["apartment"]))

        arr_main_info_from_web = app.person_current_view_page.get_arr_exact_addres_of_registration()

        assert len(data_exact_addres) == len(arr_main_info_from_web)
        # assert array by values
        for index, value_from_web in enumerate(arr_main_info_from_web):
            assert data_exact_addres[index] == value_from_web

    def test_post_address(self, app):
        data_post_addres = []
        if(self.person.registration_place["is_addresses_match"]):
            data_post_addres = self.person.registration_place["area"]
        else:
            data_post_addres = self.person.post_registration_place["area"]
        # Доделать else когда Леша добавит в пертону еще почтовый адресс
        size_data_addres = len(data_post_addres)
        count_of_elements_on_web = app.person_current_view_page.get_count_elements_post_addres()
        assert count_of_elements_on_web == size_data_addres

        arr_addres_of_reg_from_web = app.person_current_view_page.get_arr_post_addres()

        for index, value_from_web in enumerate(arr_addres_of_reg_from_web):
            assert data_post_addres[index] == value_from_web

    def test_exact_post_addres(self, app):
        data_exact_post_addres = []

        data_exact_post_addres.append(str(self.person.post_registration_place["index"]))
        data_exact_post_addres.append(self.person.post_registration_place["type"])
        data_exact_post_addres.append(self.person.post_registration_place["street"])
        data_exact_post_addres.append(str(self.person.post_registration_place["house"]))
        data_exact_post_addres.append(str(self.person.post_registration_place["apartment"]))

        arr_main_info_from_web = app.person_current_view_page.get_arr_exact_post_addres()

        assert len(data_exact_post_addres) == len(arr_main_info_from_web)
        # assert array by values
        for index, value_from_web in enumerate(arr_main_info_from_web):
            assert data_exact_post_addres[index] == value_from_web

    def test_document_verify(self, app):
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

    def test_enrollment_verify(self, app):
        app.person_main_view_page.person_enrollment_button().click()
        app.person_enrollment_view_page.is_element_present(app.person_enrollment_view_page.SPINNER_OFF)

        # assert app.person_enrollment_view_page.is_table_enrollment_present() == True

    # Этот тест не работает, нужно доделать датапровайдер к заяве.
    def test_verify_table_with_enrollments(self, app):
        data_table_papers = [u'33', u'7', u'пільги відсутні', u'ММ', u'957894', u'потреб. гуртож.', u'2015-09-30']

        count_documents = 1
        count_row_in_table = app.person_enrollment_view_page.get_count_row_in_table_enrollment()
        # assert count_row_in_table == count_documents

        arr_info_from_table_web = app.person_enrollment_view_page.get_data_from_table()

        data_table_papers.sort()
        arr_info_from_table_web.sort()

        # assert len(data_table_papers) == len(arr_info_from_table_web)

        # for index, value_from_web in enumerate(arr_info_from_table_web):
            # assert data_table_papers[index] == value_from_web

    # private methods
    def __get_specific_symbol(self, boolean):
        if(boolean == True):
            return u'✓'
        else:
            return u'✘'

    def get_correct_birth_view(self, birth_from_json):
        split = birth_from_json.split("-")
        if (len(split) != 3):
            raise ValueError('The date is not correct')
        year = split[0]
        month = split[1]
        day = split[2]
        return day + "." + month + "." + year + u" р."


# if(self.person.registration_place["is_addresses_match"]):
#             data_exact_post_addres.append(str(self.person.registration_place["index"]))
#             data_exact_post_addres.append(self.person.registration_place["type"])
#             data_exact_post_addres.append(self.person.registration_place["street"])
#             data_exact_post_addres.append(str(self.person.registration_place["house"]))
#             data_exact_post_addres.append(str(self.person.registration_place["apartment"]))
#         else:
#             data_exact_post_addres.append(str(self.person.post_registration_place["index"]))
#             data_exact_post_addres.append(self.person.post_registration_place["type"])
#             data_exact_post_addres.append(self.person.post_registration_place["street"])
#             data_exact_post_addres.append(str(self.person.post_registration_place["house"]))
#             data_exact_post_addres.append(str(self.person.post_registration_place["apartment"]))
