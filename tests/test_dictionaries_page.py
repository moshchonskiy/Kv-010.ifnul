# coding: utf8
from selenium.webdriver.support.select import Select
from model.user import User
from utils.data_provader_from_json import DataProviderJSON
from utils.table_ease_access import TestTable

__author__ = 'Den'


def login(app):
    app.ensure_logout()
    app.login(User.Admin(), True)


def goto_dictionaries_page(app):
    assert app.internal_page.is_this_page
    app.internal_page.dictionaries_page_link.click()
    assert app.dictionaries_page.is_this_page


def test_public_activity_dict(app):
    dict_page = app.dictionaries_page
    login(app)
    goto_dictionaries_page(app)
    select_value = dict_page.try_get_dictionaries_select_elem
    assert select_value
    case_value = Select(select_value)
    case_value.select_by_visible_text(u'Публічні активності')
    table = dict_page.try_get_table
    assert table
    assert dict_page.try_get_table_body_cell_i_j(1, 1).text == \
           u'Всеукраїнські учнівські олімпіади із базових предметів (IV етап)'
    assert dict_page.try_get_table_head_cell_i(1).text == u'Назва активності'
    assert dict_page.try_get_button_10 and dict_page.try_get_button_25 and dict_page.try_get_button_50 \
           and dict_page.try_get_button_100


def test_public_activity_dict_check_all_value(app):
    """
    check all data value in table activity dict
    """
    dict_page = app.dictionaries_page
    goto_dictionaries_page(app)
    select_value = dict_page.try_get_dictionaries_select_elem
    assert select_value
    case_value = Select(select_value)
    case_value.select_by_visible_text(u'Публічні активності')

    table = TestTable(dict_page.driver, dict_page.DICTIONARIES_PAGE_TABLE)
    assert table.try_get_table()

    data_provider = DataProviderJSON('resources\\public_activity.json')

    for i in range(1, table.try_get_table_data_height() + 1):
        for j in range(1, table.try_get_table_data_width() + 1):
            assert table.try_get_cell_ij(i, j).text == data_provider.get_value_by_ij(str(i), str(j))


def test_count(app):
    dict_page = app.dictionaries_page

    goto_dictionaries_page(app)
    select_value = dict_page.try_get_dictionaries_select_elem
    assert select_value
    case_value = Select(select_value)
    case_value.select_by_visible_text(u'Дані про пільги')
    table = dict_page.try_get_table
    assert table

    if dict_page.try_get_table_body_last_cell_in_last_row():
        i = 1
        while dict_page.try_get_table_body_last_cell_in_i_row(1) != dict_page.try_get_table_body_cell_i_j(1, i):
            i += 1
        print i





