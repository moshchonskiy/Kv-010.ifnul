# coding: utf8
from selenium.webdriver.support.select import Select
from model.user import User

__author__ = 'Den'


def test_is_login(app):
    app.ensure_logout()
    app.login(User.Admin(), True)
    assert app.internal_page.is_this_page


def test_public_activity_dict(app):
    app.internal_page.dictionaries_page_link.click()
    assert app.dictionaries_page.is_this_page
    dict_page = app.dictionaries_page
    select = dict_page.try_get_dictionaries_select_elem
    assert select
    case = Select(select)
    case.select_by_visible_text(u'Публічні активності')
    table = dict_page.try_get_table
    assert table
    assert dict_page.try_get_table_body_cell_i_j(1, 1).text == \
           u'Всеукраїнські учнівські олімпіади із базових предметів (IV етап)'
    assert dict_page.try_get_table_head_cell_i(1).text == u'Назва активності'
    assert dict_page.try_get_button_10 and dict_page.try_get_button_25 and dict_page.try_get_button_50 \
           and dict_page.try_get_button_100
