# coding: utf8
from model.user import User


def login(app):
    app.ensure_logout()
    app.login(User.Admin(), True)


def test_gender_filter(app):
    login(app)
    person_page = app.persons_page

    person_page.try_get_gender_male_checkbox().click()
    person_page.try_get_refresh_upper_button().click()
    cells_texts = person_page.try_get_filtered_gender_column(u'Чоловіча')
    for text in cells_texts:
        assert text == u'Чоловіча'

    person_page.try_get_close_filter().click()

    person_page.try_get_gender_female_checkbox().click()
    person_page.try_get_refresh_upper_button().click()
    cells_texts = person_page.try_get_filtered_gender_column(u'Жіноча')
    for text in cells_texts:
        assert text == u'Жіноча'


def test_type_filter(app):
    login(app)
    person_page = app.persons_page

    person_page.try_get_type_applicant_checkbox().click()
    person_page.try_get_refresh_upper_button().click()
    cells_texts = person_page.try_get_filtered_type_column(u'абітурієнт')
    for text in cells_texts:
        assert text == u'абітурієнт'

    person_page.try_get_close_filter().click()

    person_page.try_get_type_student_checkbox().click()
    person_page.try_get_refresh_upper_button().click()
    cells_texts = person_page.try_get_filtered_type_column(u'студент')
    for text in cells_texts:
        assert text == u'студент'

    person_page.try_get_close_filter().click()

    person_page.try_get_type_scientist_checkbox().click()
    person_page.try_get_refresh_upper_button().click()
    cells_texts = person_page.try_get_filtered_type_column(u'науковець')
    for text in cells_texts:
        assert text == u'науковець'

    person_page.try_get_close_filter().click()

    person_page.try_get_type_employee_checkbox().click()
    person_page.try_get_refresh_upper_button().click()
    cells_texts = person_page.try_get_filtered_type_column(u'працівник')
    for text in cells_texts:
        assert text == u'працівник'

    person_page.try_get_close_filter().click()

    person_page.try_get_type_graduate_checkbox().click()
    person_page.try_get_refresh_upper_button().click()
    cells_texts = person_page.try_get_filtered_type_column(u'випускник')
    for text in cells_texts:
        assert text == u'випускник'

    person_page.try_get_close_filter().click()

    person_page.try_get_type_outsider_checkbox().click()
    person_page.try_get_refresh_upper_button().click()
    cells_texts = person_page.try_get_filtered_type_column(u'сторонній')
    for text in cells_texts:
        assert text == u'сторонній'


# only for need hostel
def test_need_hostel_filter(app):
    login(app)
    person_page = app.persons_page

    person_page.try_get_need_hostel_checkbox().click()
    person_page.try_get_refresh_upper_button().click()
    cells_texts = person_page.try_get_filtered_need_hostel_column(u'потреб. гуртож.')
    for text in cells_texts:
        assert text == u'потреб. гуртож.'


# only for bound to military person
def test_bound_to_military_filter(app):
    login(app)
    person_page = app.persons_page

    person_page.try_get_burger_button().click()
    person_page.try_get_add_to_table_military_checkbox().click()
    person_page.try_get_close_after_addition_button().click()

    person_page.try_get_bound_to_military_checkbox().click()
    person_page.try_get_refresh_upper_button().click()

    cells_texts = person_page.try_get_filtered_military_column(u'ВЗ')
    for text in cells_texts:
        assert text == u'ВЗ'


# only for foreigner resident
def test_resident_filter(app):
    login(app)
    person_page = app.persons_page
    person_page.try_get_burger_button().click()
    person_page.try_get_add_to_table_resident_checkbox().click()
    person_page.try_get_close_after_addition_button().click()
    person_page.try_get_resident_foreigner_checkbox().click()
    person_page.try_get_refresh_upper_button().click()

    cells_texts = person_page.try_get_filtered_resident_column(u'інозем.')
    for text in cells_texts:
        assert text == u'інозем.'
