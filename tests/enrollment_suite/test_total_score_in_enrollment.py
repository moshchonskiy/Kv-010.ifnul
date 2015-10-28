# /coding=utf-8
import pytest

author = "Vadym"

data_provider_numbers = [1, 3, 5, 6, 11, 12, 13, 50, 60, 61, 75, 100, 101, 154, 200, 201, 1024, 0, -1,
                         -3, -5, -6, -11, -12, -13, -50, -60, -61, -75, -100, -154, -200, -201, -1024]
data_provider_character = ['A', 'B', 'C', 'D', 'E', 'Fx', 'F', 'l', 'o', 'q', 'dsf', 'a']

@pytest.fixture(params=data_provider_numbers)
def number(request):
    return request.param

@pytest.fixture(params=data_provider_character)
def character(request):
    return request.param

def union_arr():
    return data_provider_numbers + data_provider_character

@pytest.fixture(params=union_arr())
def number_and_character(request):
    return request.param

def test_open_add_enrollment(app):
    app.ensure_logged_in()
    app.internal_page.is_this_page
    app.internal_page.enrollments_page_link.click()
    app.enrollments_page.is_this_page
    app.enrollments_page.is_this_page.click()
    enr_page = app.enrollments_main_page

    enr_page.is_element_present(app.person_current_view_page.SPINNER_OFF)
    assert app.enrollments_main_page.get_text_add_enrollment().text == u"Додавання заяви"

def test_field_total_score_on_numbers(app, number):
    enr_page = app.enrollments_main_page

    enr_page.add_total_score(enr_page.TOTAL_SCORE, number)
    element = enr_page.get_form_input_total_score()
    status_form_right_now = enr_page.get_atrribute_of_element_by(element, "class").split(' ')
    enr_page.clear_form_input_total_score()
    assert 'ng-valid' in status_form_right_now

def test_field_total_score_on_characters(app, character):
    enr_page = app.enrollments_main_page

    enr_page.add_total_score(enr_page.TOTAL_SCORE, character)
    element = enr_page.get_form_input_total_score()
    status_form_right_now = enr_page.get_atrribute_of_element_by(element, "class").split(' ')
    enr_page.clear_form_input_total_score()
    assert 'ng-invalid' in status_form_right_now

def test_twelve_scale(app, number_and_character):
    enr_page = app.enrollments_main_page

    if(enr_page.get_text_choose_grading_scale().text != u"дванадцятибальна"):
        enr_page.choose_grading_scale("дванадцятибальна")

    enr_page.add_total_score(enr_page.TOTAL_SCORE, number_and_character)
    element = enr_page.get_form_input_total_score()
    status_form_right_now = enr_page.get_atrribute_of_element_by(element, "class").split(' ')
    enr_page.clear_form_input_total_score()
    if(type(number_and_character) == int and (number_and_character > 0 and number_and_character < 13)):
        # check form is not red when type correct value by scale assessment
        assert 'ng-valid' in status_form_right_now
    else:
        # check form is red when type correct value by scale assessment
        assert 'ng-invalid' in status_form_right_now

def test_sixty_scale(app, number_and_character):
    enr_page = app.enrollments_main_page

    if(enr_page.get_text_choose_grading_scale().text != u"шестидесятибальна"):
        enr_page.choose_grading_scale("шестидесятибальна")

    enr_page.add_total_score(enr_page.TOTAL_SCORE, number_and_character)
    element = enr_page.get_form_input_total_score()
    status_form_right_now = enr_page.get_atrribute_of_element_by(element, "class").split(' ')
    enr_page.clear_form_input_total_score()
    if(type(number_and_character) == int and (number_and_character > 0 and number_and_character < 61)):
        # check form is not red when type correct value by scale assessment
        assert 'ng-valid' in status_form_right_now
    else:
        # check form is red when type correct value by scale assessment
        assert 'ng-invalid' in status_form_right_now

def test_one_hundred_scale(app, number_and_character):
    enr_page = app.enrollments_main_page

    if(enr_page.get_text_choose_grading_scale().text != u"стобальна"):
        enr_page.choose_grading_scale("стобальна")

    enr_page.add_total_score(enr_page.TOTAL_SCORE, number_and_character)
    element = enr_page.get_form_input_total_score()
    status_form_right_now = enr_page.get_atrribute_of_element_by(element, "class").split(' ')
    enr_page.clear_form_input_total_score()
    if(type(number_and_character) == int and (number_and_character > 0 and number_and_character < 101)):
        # check form is not red when type correct value by scale assessment
        assert 'ng-valid' in status_form_right_now
    else:
        # check form is red when type correct value by scale assessment
        assert 'ng-invalid' in status_form_right_now

def test_two_hundred_scale(app, number_and_character):
    enr_page = app.enrollments_main_page

    if(enr_page.get_text_choose_grading_scale().text != u"двохсотбальна"):
        enr_page.choose_grading_scale("двохсотбальна")

    enr_page.add_total_score(enr_page.TOTAL_SCORE, number_and_character)
    element = enr_page.get_form_input_total_score()
    status_form_right_now = enr_page.get_atrribute_of_element_by(element, "class").split(' ')
    enr_page.clear_form_input_total_score()
    if(type(number_and_character) == int and (number_and_character > 0 and number_and_character < 201)):
        # check form is not red when type correct value by scale assessment
        assert 'ng-valid' in status_form_right_now
    else:
        # check form is red when type correct value by scale assessment
        assert 'ng-invalid' in status_form_right_now

def test_ECTS_scale(app, number_and_character):
    enr_page = app.enrollments_main_page

    if(enr_page.get_text_choose_grading_scale().text != "ECTS"):
        enr_page.choose_grading_scale("ECTS")
    ECTS_DATA = ['A', 'B', 'C', 'D', 'E', 'Fx', 'F']

    enr_page.add_total_score(enr_page.TOTAL_SCORE, number_and_character)
    element = enr_page.get_form_input_total_score()
    status_form_right_now = enr_page.get_atrribute_of_element_by(element, "class").split(' ')
    enr_page.clear_form_input_total_score()
    if(number_and_character in ECTS_DATA):
        # check form is not red when type correct value by scale assessment
        assert 'ng-valid' in status_form_right_now
    else:
        # check form is red when type correct value by scale assessment
        assert 'ng-invalid' in status_form_right_now

def test_five_point_scale(app, number_and_character):
    enr_page = app.enrollments_main_page

    if(enr_page.get_text_choose_grading_scale().text != u"п'ятибальна"):
        enr_page.choose_grading_scale("п'ятибальна")

    enr_page.add_total_score(enr_page.TOTAL_SCORE, number_and_character)
    element = enr_page.get_form_input_total_score()
    status_form_right_now = enr_page.get_atrribute_of_element_by(element, "class").split(' ')
    enr_page.clear_form_input_total_score()
    if(type(number_and_character) == int and (number_and_character > 0 and number_and_character < 6)):
        # check form is not red when type correct value by scale assessment
        assert 'ng-valid' in status_form_right_now
    else:
        # check form is red when type correct value by scale assessment
        assert 'ng-invalid' in status_form_right_now

def test_interview_scale(app, number_and_character):
    enr_page = app.enrollments_main_page
    if(enr_page.get_text_choose_grading_scale().text != u"співбесіда"):
        enr_page.choose_grading_scale("співбесіда")
    enr_page.add_total_score(enr_page.TOTAL_SCORE, number_and_character)
    element = enr_page.get_form_input_total_score()
    status_form_right_now = enr_page.get_atrribute_of_element_by(element, "class").split(' ')
    enr_page.clear_form_input_total_score()
    assert 'ng-valid' in status_form_right_now # == поле не красное
