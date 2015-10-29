# coding: utf8
from model.user import User
import pytest
from allure.constants import AttachmentType
import allure
import sys
import traceback

def login(app):
    app.ensure_logout()
    app.login(User.Admin(), True)

@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
def test_gender_filter(app):
    with pytest.allure.step('Authorize to the application'):
        login(app)
        person_page = app.persons_page
        person_page.try_get_gender_male_checkbox().click()
        person_page.try_get_refresh_upper_button().click()
    with pytest.allure.step('Assert the gender in column is male'):
        try:
            cells_texts = person_page.try_get_filtered_gender_column(u'Чоловіча')
            for text in cells_texts:
                assert text == u'Чоловіча'
            allure.attach('screenshot', person_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
        except AssertionError:
            allure.attach('screenshot', person_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
            print_simple_stacktrace()
            raise

    person_page.try_get_close_filter().click()
    person_page.try_get_gender_female_checkbox().click()
    person_page.try_get_refresh_upper_button().click()
    with pytest.allure.step('Assert the gender in column is female'):
        try:
            cells_texts = person_page.try_get_filtered_gender_column(u'Жіноча')
            for text in cells_texts:
                assert text == u'Жіноча'
            allure.attach('screenshot', person_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
        except AssertionError:
            allure.attach('screenshot', person_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
            print_simple_stacktrace()
            raise


@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
def test_type_filter(app):
    login(app)
    person_page = app.persons_page
    person_page.try_get_type_applicant_checkbox().click()
    person_page.try_get_refresh_upper_button().click()
    with pytest.allure.step('Assert the filtered information in column is applicant'):
        try:
            cells_texts = person_page.try_get_filtered_type_column(u'абітурієнт')
            for text in cells_texts:
                assert text == u'абітурієнт'
            allure.attach('screenshot', person_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
        except AssertionError:
            allure.attach('screenshot', person_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
            print_simple_stacktrace()
            raise

    person_page.try_get_close_filter().click()
    person_page.try_get_type_student_checkbox().click()
    person_page.try_get_refresh_upper_button().click()
    with pytest.allure.step('Assert the filtered information in column is student'):
        try:
            cells_texts = person_page.try_get_filtered_type_column(u'студент')
            for text in cells_texts:
                assert text == u'студент'
            allure.attach('screenshot', person_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
        except AssertionError:
            allure.attach('screenshot', person_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
            print_simple_stacktrace()
            raise

    person_page.try_get_close_filter().click()
    person_page.try_get_type_scientist_checkbox().click()
    person_page.try_get_refresh_upper_button().click()
    with pytest.allure.step('Assert the filtered information in column is scientist'):
        try:
            cells_texts = person_page.try_get_filtered_type_column(u'науковець')
            for text in cells_texts:
                assert text == u'науковець'
            allure.attach('screenshot', person_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
        except AssertionError:
            allure.attach('screenshot', person_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
            print_simple_stacktrace()
            raise

    person_page.try_get_close_filter().click()
    person_page.try_get_type_employee_checkbox().click()
    person_page.try_get_refresh_upper_button().click()
    with pytest.allure.step('Assert the filtered information in column is employee'):
        try:
            cells_texts = person_page.try_get_filtered_type_column(u'працівник')
            for text in cells_texts:
                assert text == u'працівник'
            allure.attach('screenshot', person_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
        except AssertionError:
            allure.attach('screenshot', person_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
            print_simple_stacktrace()
            raise

    person_page.try_get_close_filter().click()
    person_page.try_get_type_graduate_checkbox().click()
    person_page.try_get_refresh_upper_button().click()
    with pytest.allure.step('Assert the filtered information in column is graduate'):
        try:
            cells_texts = person_page.try_get_filtered_type_column(u'випускник')
            for text in cells_texts:
                assert text == u'випускник'
            allure.attach('screenshot', person_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
        except AssertionError:
            allure.attach('screenshot', person_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
            print_simple_stacktrace()
            raise

    person_page.try_get_close_filter().click()
    person_page.try_get_type_outsider_checkbox().click()
    person_page.try_get_refresh_upper_button().click()
    with pytest.allure.step('Assert the filtered information in column is outsider'):
        try:
            cells_texts = person_page.try_get_filtered_type_column(u'сторонній')
            for text in cells_texts:
                assert text == u'сторонній'
            allure.attach('screenshot', person_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
        except AssertionError:
            allure.attach('screenshot', person_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
            print_simple_stacktrace()
            raise


@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
def test_need_hostel_filter(app):
    login(app)
    person_page = app.persons_page
    person_page.try_get_need_hostel_checkbox().click()
    person_page.try_get_refresh_upper_button().click()
    with pytest.allure.step('Assert the filtered information in column is need accommodation'):
        try:
            cells_texts = person_page.try_get_filtered_need_hostel_column(u'потреб. гуртож.')
            for text in cells_texts:
                assert text == u'потреб. гуртож.'
            allure.attach('screenshot', person_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
        except AssertionError:
            allure.attach('screenshot', person_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
            print_simple_stacktrace()
            raise


@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
def test_bound_to_military_filter(app):
    login(app)
    person_page = app.persons_page

    person_page.try_get_burger_button().click()
    person_page.try_get_add_to_table_military_checkbox().click()
    person_page.try_get_close_after_addition_button().click()

    person_page.try_get_bound_to_military_checkbox().click()
    person_page.try_get_refresh_upper_button().click()
    with pytest.allure.step('Assert the filtered information in column is military'):
        try:
            cells_texts = person_page.try_get_filtered_military_column(u'ВЗ')
            for text in cells_texts:
                assert text == u'ВЗ'
            allure.attach('screenshot', person_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
        except AssertionError:
            allure.attach('screenshot', person_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
            print_simple_stacktrace()
            raise


@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
def test_resident_filter(app):
    login(app)
    person_page = app.persons_page
    person_page.try_get_burger_button().click()
    person_page.try_get_add_to_table_resident_checkbox().click()
    person_page.try_get_close_after_addition_button().click()
    person_page.try_get_resident_foreigner_checkbox().click()
    person_page.try_get_refresh_upper_button().click()
    with pytest.allure.step('Assert the filtered information in column is foreigner'):
        try:
            cells_texts = person_page.try_get_filtered_resident_column(u'інозем.')
            for text in cells_texts:
                assert text == u'інозем.'
            allure.attach('screenshot', person_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
        except AssertionError:
            allure.attach('screenshot', person_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
            print_simple_stacktrace()
            raise


def print_simple_stacktrace():
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        print('An error occurred on line: {}, in statement: {}. The filename is: {}, and function is: {}.'
              .format(line, text, filename, func))
