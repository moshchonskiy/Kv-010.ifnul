# coding=utf-8
import time

__author__ = 'Vadym'

from model.user import User

def test_global_info_about_person(app):
    app.ensure_logout()
    app.login(User.Admin())
    app.internal_page.is_this_page
    app.internal_page.driver.get('http://194.44.198.221/#/person/view/68/main')
    time.sleep(8)

    fio_ukranian = app.person_current_view_page.get_fio_ukranian
    assert fio_ukranian
    assert u'Малкович Малкович Малкович'.encode("cp1251") == fio_ukranian.text.encode("cp1251")

    fio_english = app.person_current_view_page.get_fio_english
    assert fio_english
    assert 'Malkovich Malkovich' == fio_english.text

    assert 'MA' == app.person_current_view_page.get_serial_person_record()

    assert '19531209' == app.person_current_view_page.get_number_person_record()


def test_main_info_about_person(app):
    data_main_info_person = [u'абітурієнт', u'09.12.1953 р.', u'✘', u'Чоловіча',
                             u'одружений', u'✘', u'Україна', u'3', u'✘']
    titles = app.person_current_view_page.arr_titles_main
    dict_data_info_person = {}
    count = 0
    for value in data_main_info_person:
        if value != u'✘':
            value = value.encode("cp1251")
        dict_data_info_person[titles[count]] = value
        count += 1

    dict_main_info_from_web = app.person_current_view_page.get_dict_main_info_about_person()

    for number in range(len(dict_main_info_from_web)):
        assert dict_data_info_person[titles[number]] == dict_main_info_from_web[titles[number]]

def test_place_of_birth(app):
    data_birth_person = [u'М.КИЇВ', u'РАЙОНИ М. КИЇВ', u'ДЕСНЯНСЬКИЙ']
    titles = app.person_current_view_page.arr_titles_birth
    size_data_birth = len(data_birth_person)
    dict_birth_person = {}
    count = 0
    for value in data_birth_person:
        dict_birth_person[titles[count]] = value.encode("cp1251")
        count += 1

    count_of_elements_on_web = app.person_current_view_page.get_count_elements_place_of_birth()
    assert count_of_elements_on_web == size_data_birth

    dict_main_info_from_web = app.person_current_view_page.get_dict_place_of_birth()
    for number in range(len(dict_main_info_from_web)):
        assert dict_birth_person[titles[number]] == dict_main_info_from_web[titles[number]]

def test_address_of_registration(app):
    data_addres_registration = [u'М.КИЇВ', u'РАЙОНИ М. КИЇВ', u'ДЕСНЯНСЬКИЙ']
    titles = app.person_current_view_page.arr_titles_registration
    size_data_addres_registration = len(data_addres_registration)
    dict_addres_person = {}
    count = 0
    for value in data_addres_registration:
        dict_addres_person[titles[count]] = value.encode("cp1251")
        count += 1

    count_of_elements_on_web = app.person_current_view_page.get_count_elements_addres_of_registration()
    assert count_of_elements_on_web == size_data_addres_registration

    dict_main_info_from_web = app.person_current_view_page.get_dict_addres_of_registration()
    for number in range(len(dict_main_info_from_web)):
        assert dict_addres_person[titles[number]] == dict_main_info_from_web[titles[number]]

def test_exact_address_of_registration(app):
    data_exact_addres_registration = [u'591209', u'бульвар ', u'Малкович', u'12', u'9']
    titles = app.person_current_view_page.arr_titles_exact_reg
    dict_exact_addres_person = {}
    count = 0
    for value in data_exact_addres_registration:
        value = value.encode("cp1251")
        value = value.strip(" ")
        dict_exact_addres_person[titles[count]] = value
        count += 1

    dict_main_info_from_web = app.person_current_view_page.get_dict_exact_addres_of_registration()
    for number in range(len(dict_main_info_from_web)):
        assert dict_exact_addres_person[titles[number]] == dict_main_info_from_web[titles[number]]

def test_post_address(app):
    data_post_addres = [u'М.КИЇВ', u'РАЙОНИ М. КИЇВ', u'ДЕСНЯНСЬКИЙ']
    titles = app.person_current_view_page.arr_titles_post_addres
    size_data_post_addres = len(data_post_addres)
    dict_post_addres = {}
    count = 0
    for value in data_post_addres:
        dict_post_addres[titles[count]] = value.encode("cp1251")
        count += 1

    count_of_elements_on_web = app.person_current_view_page.get_count_elements_post_addres()
    assert count_of_elements_on_web == size_data_post_addres

    dict_main_info_from_web = app.person_current_view_page.get_dict_post_addres()
    for number in range(len(dict_main_info_from_web)):
        assert dict_post_addres[titles[number]] == dict_main_info_from_web[titles[number]]

def test_exact_post_addres(app):
    data_exact_post_addres = [u'591209', u'бульвар ', u'Малкович', u'12', u'9']
    titles = app.person_current_view_page.arr_titles_post_exact
    dict_exact_post_addres_person = {}
    count = 0
    for value in data_exact_post_addres:
        value = value.encode("cp1251")
        value = value.strip(" ")
        dict_exact_post_addres_person[titles[count]] = value
        count += 1

    dict_main_info_from_web = app.person_current_view_page.get_dict_exact_post_addres()
    for number in range(len(dict_main_info_from_web)):
        assert dict_exact_post_addres_person[titles[number]] == dict_main_info_from_web[titles[number]]
