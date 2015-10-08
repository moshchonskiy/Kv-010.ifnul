# coding=utf-8
import time
from selenium.webdriver.common.by import By
from model.user import User

__author__ = 'Vadym'

def test_global_info_about_person(app):
    app.ensure_logout()
    app.login(User.Admin())
    app.internal_page.is_this_page
    app.internal_page.driver.get('http://194.44.198.221/#/person/view/68/main')
    app.person_current_view_page.is_element_present(app.person_current_view_page.SPINNER_OFF)
    assert app.person_papers_view_page.get_text_person_profile() == u"Перегляд персони"
    data_main_info_person = [u'Малкович Малкович Малкович', u'Malkovich Malkovich', u'MA', u'19531209']

    assert data_main_info_person[0] == app.person_current_view_page.get_fio_ukranian().text
    assert data_main_info_person[1] == app.person_current_view_page.get_fio_english().text
    assert data_main_info_person[2] == app.person_current_view_page.get_serial_person_record()
    assert data_main_info_person[3] == app.person_current_view_page.get_number_person_record()


def test_main_info_about_person(app):
    data_main_info_person = [u'абітурієнт', u'09.12.1953 р.', u'✘', u'Чоловіча',
                             u'одружений', u'✘', u'Україна', u'3', u'✘']
    arr_main_info_from_web = app.person_current_view_page.get_arr_main_info_about_person()

    data_main_info_person.sort()
    arr_main_info_from_web.sort()

    assert len(data_main_info_person) == len(arr_main_info_from_web)
    # assert array by values
    for index, value_from_web in enumerate(arr_main_info_from_web):
        assert data_main_info_person[index] == value_from_web

def test_place_of_birth(app):
    data_birth_person = [u'М.КИЇВ', u'РАЙОНИ М. КИЇВ', u'ДЕСНЯНСЬКИЙ']
    size_data_birth = len(data_birth_person)
    count_of_elements_on_web = app.person_current_view_page.get_count_elements_place_of_birth()
    assert count_of_elements_on_web == size_data_birth

    arr_main_info_from_web = app.person_current_view_page.get_arr_place_of_birth()

    data_birth_person.sort()
    arr_main_info_from_web.sort()

    for index, value_from_web in enumerate(arr_main_info_from_web):
        assert data_birth_person[index] == value_from_web


def test_addres_of_registration(app):
    data_addres_registration = [u'М.КИЇВ', u'РАЙОНИ М. КИЇВ', u'ДЕСНЯНСЬКИЙ']
    size_data_addres = len(data_addres_registration)
    count_of_elements_on_web = app.person_current_view_page.get_count_elements_addres_of_registration()
    assert count_of_elements_on_web == size_data_addres

    arr_addres_of_reg_from_web = app.person_current_view_page.get_arr_addres_of_registration()

    data_addres_registration.sort()
    arr_addres_of_reg_from_web.sort()

    for index, value_from_web in enumerate(arr_addres_of_reg_from_web):
        assert data_addres_registration[index] == value_from_web

def test_exact_address_of_registration(app):
    data_exact_addres = [u'591209', u'бульвар', u'Малкович', u'12', u'9']
    arr_main_info_from_web = app.person_current_view_page.get_arr_exact_addres_of_registration()

    data_exact_addres.sort()
    arr_main_info_from_web.sort()

    assert len(data_exact_addres) == len(arr_main_info_from_web)
    # assert array by values
    for index, value_from_web in enumerate(arr_main_info_from_web):
        assert data_exact_addres[index] == value_from_web

def test_post_address(app):
    data_post_addres = [u'М.КИЇВ', u'РАЙОНИ М. КИЇВ', u'ДЕСНЯНСЬКИЙ']
    size_data_addres = len(data_post_addres)
    count_of_elements_on_web = app.person_current_view_page.get_count_elements_post_addres()
    assert count_of_elements_on_web == size_data_addres

    arr_addres_of_reg_from_web = app.person_current_view_page.get_arr_post_addres()

    data_post_addres.sort()
    arr_addres_of_reg_from_web.sort()

    for index, value_from_web in enumerate(arr_addres_of_reg_from_web):
        assert data_post_addres[index] == value_from_web

def test_exact_post_addres(app):
    data_exact_post_addres = [u'591209', u'бульвар', u'Малкович', u'12', u'9']
    arr_main_info_from_web = app.person_current_view_page.get_arr_exact_post_addres()

    data_exact_post_addres.sort()
    arr_main_info_from_web.sort()

    assert len(data_exact_post_addres) == len(arr_main_info_from_web)
    # assert array by values
    for index, value_from_web in enumerate(arr_main_info_from_web):
        assert data_exact_post_addres[index] == value_from_web
