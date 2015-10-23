# coding=utf-8
from model.user import User
from utils.fill_enrollment import FillEnrollment
from utils.table_ease_access import TestTable

__author__ = 'Vadym'

def test_global_info_about_person(app, person):
    app.ensure_logout()
    app.login(User.Admin())
    app.internal_page.is_this_page

    # Find new person by surname (Alexey test 'add person')
    person_page = app.persons_page
    person_page.try_get_choose_surname().click()
    person_page.try_get_input_group().clear()
    person_page.try_get_input_group().send_keys(person.surname_ukr)
    person_page.try_get_ok_button().click()
    app.person_current_view_page.is_element_present(app.person_current_view_page.SPINNER_OFF)
    person_page.view_first_person_in_page

    # Is it current view person page?
    app.person_current_view_page.is_element_present(app.person_current_view_page.SPINNER_OFF)
    assert app.person_papers_view_page.get_text_person_profile() == u"Перегляд персони"

    personUkrFIO = person.surname_ukr + " " + person.first_name_ukr + " " + person.second_name_ukr
    personEngFIO = person.surname_eng + " " + person.first_name_eng
    private_case_chars = person.private_case_chars
    private_case_number = str(person.private_case_number)

    actual_person = app.person_current_view_page

    assert personUkrFIO == actual_person.get_fio_ukranian().text
    assert personEngFIO == actual_person.get_fio_english().text
    assert private_case_chars == actual_person.get_serial_person_record()
    assert private_case_number == actual_person.get_number_person_record()

def test_main_info_about_person(app, person):
    expected_main_info_person = []

    expected_main_info_person.append(person.person_type)
    expected_main_info_person.append(person.get_birthday_str_for_view())
    expected_main_info_person.append(person.get_specific_symbol_for_view(person.reservist))
    expected_main_info_person.append(person.sex)
    expected_main_info_person.append(person.marital_status)
    expected_main_info_person.append(person.get_specific_symbol_for_view(person.is_outlander))
    expected_main_info_person.append(person.nationality)
    expected_main_info_person.append(person.get_specific_symbol_for_view(person.hostel_need))

    actual_main_info = app.person_current_view_page.get_arr_main_info_about_person()

    assert len(expected_main_info_person) == len(actual_main_info)
    # assert array by values
    for index, actual_value_from_web in enumerate(actual_main_info):
        assert expected_main_info_person[index] == actual_value_from_web

def test_place_of_birth(app, person):
    expected_place_birth_person = person.burn_place
    expected_size_data_birth = len(expected_place_birth_person)
    actual_count_of_elements_on_web = app.person_current_view_page.get_count_elements_place_of_birth()
    assert actual_count_of_elements_on_web == expected_size_data_birth

    actual_place_of_birth = app.person_current_view_page.get_arr_place_of_birth()

    for index, actual_value_from_web in enumerate(actual_place_of_birth):
        assert expected_place_birth_person[index] == actual_value_from_web

def test_addres_of_registration(app, person):
    expected_addres_registration = person.registration_place["area"]
    expected_size_data_addres = len(expected_addres_registration)
    actual_count_of_elements = app.person_current_view_page.get_count_elements_addres_of_registration()
    assert actual_count_of_elements == expected_size_data_addres

    actual_addres_of_reg = app.person_current_view_page.get_arr_addres_of_registration()

    for index, actual_value_from_web in enumerate(actual_addres_of_reg):
        assert expected_addres_registration[index] == actual_value_from_web

def test_exact_address_of_registration(app, person):
    expected_exact_addres = []
    expected_exact_addres.append(str(person.registration_place["index"]))
    expected_exact_addres.append(person.registration_place["type"])
    expected_exact_addres.append(person.registration_place["street"])
    expected_exact_addres.append(str(person.registration_place["house"]))
    expected_exact_addres.append(str(person.registration_place["apartment"]))

    actual_exact_addresses = app.person_current_view_page.get_arr_exact_addres_of_registration()

    assert len(expected_exact_addres) == len(actual_exact_addresses)
    # assert array by values
    for index, actual_value_from_web in enumerate(actual_exact_addresses):
        assert expected_exact_addres[index] == actual_value_from_web

def test_post_address(app, person):
    expected_post_addres = []
    if(person.registration_place["is_addresses_match"]):
        expected_post_addres = person.registration_place["area"]
    else:
        expected_post_addres = person.post_registration_place["area"]
    expected_size_post_addres = len(expected_post_addres)
    actual_size_post_addres = app.person_current_view_page.get_count_elements_post_addres()
    assert actual_size_post_addres == expected_size_post_addres

    actual_addres_of_reg = app.person_current_view_page.get_arr_post_addres()

    for index, value_from_web in enumerate(actual_addres_of_reg):
        assert expected_post_addres[index] == value_from_web

def test_exact_post_addres(app, person):
    expected_exact_post_addres = []

    expected_exact_post_addres.append(str(person.post_registration_place["index"]))
    expected_exact_post_addres.append(person.post_registration_place["type"])
    expected_exact_post_addres.append(person.post_registration_place["street"])
    expected_exact_post_addres.append(str(person.post_registration_place["house"]))
    expected_exact_post_addres.append(str(person.post_registration_place["apartment"]))

    actual_exact_post_addres = app.person_current_view_page.get_arr_exact_post_addres()

    assert len(expected_exact_post_addres) == len(actual_exact_post_addres)
    # assert array by values
    for index, actual_value_from_web in enumerate(actual_exact_post_addres):
        assert expected_exact_post_addres[index] == actual_value_from_web

def test_document_verify(app, person):
    app.person_main_view_page.person_document_button().click()
    app.person_papers_view_page.is_element_present(app.person_papers_view_page.SPINNER_OFF)

    if(len(person.documents) > 0):
        assert app.person_papers_view_page.is_table_present() == True
    else:
        assert app.person_papers_view_page.is_table_present() == False

def test_verify_table_with_documents(app, person):
    person_papers = app.person_papers_view_page
    if(len(person.documents) == 0):
        assert person_papers.get_text_not_have_papers().text == u"У даної персони немає документів"
        return
    expected_table_documents = []
    for document in person.documents:
        doc_row = []
        doc_row.append(document.document_name)
        doc_row.append(document.document_case_char)
        doc_row.append(str(document.document_case_number))
        doc_row.append(document.get_day_of_issue_str_for_view())
        doc_row.append(document.issued_by)
        doc_row.append(person.get_specific_symbol_for_view(document.document_is_original))
        doc_row.append(person.get_specific_symbol_for_view(document.document_is_foreign))
        doc_row.append(document.category_reward)
        doc_row.append(document.reward)
        doc_row.append(document.type_of_reward)
        doc_row.append(str(document.average_rate))
        doc_row.append(str(document.pincode))
        expected_table_documents.append(doc_row)

    expected_count_documents = len(person.documents)
    actual_count_row_in_table = app.person_papers_view_page.get_count_row_in_table_documents()
    assert actual_count_row_in_table == expected_count_documents

    actual_table = TestTable(person_papers.driver, person_papers.TABLE, row_xpath=person_papers.ROW, cell_xpath=person_papers.CELL)

    for i in range(1, actual_table.try_get_table_data_height() + 1):
        for j in range(1, actual_table.try_get_table_data_width() + 1):
            assert actual_table.try_get_cell_ij(i, j).text == expected_table_documents[i - 1][j - 1]

def test_enrollment_verify(app):
    person_enrollment = app.person_enrollment_view_page

    app.person_main_view_page.person_enrollment_button().click()
    person_enrollment.is_element_present(app.person_enrollment_view_page.SPINNER_OFF)

    # Валера должен сделать json который в себе хранит множество заявок
    enrollments = FillEnrollment()
    expected_enrollment = enrollments.create_enrollment_from_json("fill_enrollment_main_test_view.json", "1")

    # if(len(person.documents) > 0):
    assert person_enrollment.is_table_enrollment_present() == True
    # else:
    #     assert app.person_papers_view_page.is_table_present() == False
    if(expected_enrollment is None):
        assert person_enrollment.get_text_not_have_enrollment().text == u"У даної персони немає заяв"
        return

    expected_enrollments = []
    for enrollment in range(1):
        row = []
        row.append(expected_enrollment.get_text_privilege_for_view(expected_enrollment.checkbox_is_privilege))
        row.append(expected_enrollment.series_of_statements)
        row.append(expected_enrollment.number_statements)
        row.append(expected_enrollment.get_text_hostel_for_view(expected_enrollment.checkbox_is_hostel))
        row.append(expected_enrollment.get_day_of_entry_str_for_view())
        expected_enrollments.append(row)

    expected_count_documents = len(expected_enrollments)
    actual_count_row_in_table = person_enrollment.get_count_row_in_table_enrollment()
    assert actual_count_row_in_table == expected_count_documents

    actual_table = TestTable(person_enrollment.driver, person_enrollment.TABLE, row_xpath=person_enrollment.ROW, cell_xpath=person_enrollment.CELL)

    for i in range(1, actual_table.try_get_table_data_height() + 1):
        # 3 - We begin from "Наявність пільг" because number and id we did't type when created enrollment
        for j in range(3, actual_table.try_get_table_data_width() + 1):
            assert actual_table.try_get_cell_ij(i, j).text == expected_enrollments[i - 1][j - 3]

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
