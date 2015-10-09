# coding=utf-8
from model.user import User
from utility.personCreator import PersonCreator

__author__ = 'Vadym'

class TestCurrentViewPersonInfo(object):

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
        data_main_info_person.append(self.person.birth_day_for_view.replace('-', '.') + u" р.")
        data_main_info_person.append(self.__get_specific_symbol(self.person.reservist))
        data_main_info_person.append(self.person.sex)
        data_main_info_person.append(self.person.marital_status)
        data_main_info_person.append(self.__get_specific_symbol(self.person.is_outlander))
        data_main_info_person.append(self.person.nationality)
        data_main_info_person.append("") #Індекс матеріально відповідального
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

    # private methods
    def __get_specific_symbol(self, boolean):
        if(boolean == True):
            return u'✓'
        else:
            return u'✘'


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
