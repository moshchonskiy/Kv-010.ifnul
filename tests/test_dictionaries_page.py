# coding: utf8

from selenium.webdriver.support.select import Select

from model.user import User
from utils.data_provider_from_json import DataProviderJSON
from utils.table_ease_access import TestTable

__author__ = 'Den'

def goto_dictionaries_page(app):
    assert app.internal_page.is_this_page
    app.internal_page.dictionaries_page_link.click()
    assert app.dictionaries_page.is_this_page


def test_public_activity_dict(logout_login):
    app = logout_login
    dict_page = app.dictionaries_page
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
    data_provider = DataProviderJSON('public_activity.json')
    for i in range(1, table.try_get_table_data_height() + 1):
        for j in range(1, table.try_get_table_data_width() + 1):
            assert table.try_get_cell_ij(i, j).text == data_provider.get_value_by_ij(str(i), str(j))


def test_inform_about_unit_dict_check_all_value(app):
    dict_page = app.dictionaries_page
    goto_dictionaries_page(app)
    select_value = dict_page.try_get_dictionaries_select_elem
    assert select_value
    case_value = Select(select_value)
    case_value.select_by_visible_text(u'Інформація про підрозділи')
    data_provider = DataProviderJSON('info_about_unit.json')
    table = TestTable(dict_page.driver, dict_page.DICTIONARIES_PAGE_TABLE)
    assert dict_page.wait_until_page_generate()
    for i in range(1, table.try_get_table_data_height() + 1):
        for j in range(1, table.try_get_table_data_width() + 1):
            assert table.try_get_cell_ij(i, j).text == data_provider.get_value_by_ij(str(i), str(j))
    dict_page.try_get_button_25().click()
    for i in range(1, table.try_get_table_data_height() + 1):
        for j in range(1, table.try_get_table_data_width() + 1):
            assert table.try_get_cell_ij(i, j).text == data_provider.get_value_by_ij(str(i), str(j))


def test_click_on_all_dictionary(app):
    dict_page = app.dictionaries_page
    goto_dictionaries_page(app)
    select_value = dict_page.try_get_dictionaries_select_elem
    assert select_value
    case_value = Select(select_value)
    dp = DataProviderJSON('dictionaries_page_selecting_name.json')
    for s in dp.get_dict_value()["value"]:
        if s != u"Адміністративно-територіальні одиниці":
            case_value.select_by_visible_text(s)
            assert dict_page.wait_until_page_generate()
            dict_page.try_get_button_10().click()
            table = TestTable(dict_page.driver, dict_page.DICTIONARIES_PAGE_TABLE)
            assert table.try_get_table_data_height() <= 10
