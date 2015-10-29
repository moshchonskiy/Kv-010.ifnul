# -*- coding: utf-8 -*-
import pytest

__author__ = 'Vadym'

# OFFER = "Біологічний"
# FORM_OF_EDUCATION = "Спеціаліст"

data_provider_offers = ["Біологічний", "Економічний", "Історичний", "Фізичний",
                        "Хімічний", "Механіко-математичний", "Іноземних мов"]
data_provider_forms_of_education = ["Молодший спеціаліст на основі повної загальної середньої освіти",
                                    "Бакалавр",
                                    "Магістр на основі повної загальної середньої освіти",
                                    "Кваліфікований робітник 2 ступеня на основі БЗСО БЕЗ права отримання ПЗСО",
                                    "Магістр (зі скороченим терміном навчання)",
                                    "Бакалавр (з нормативним терміном навчання, на 2 курс)",
                                    "Спеціаліст на основі повної загальної середньої освіти",
                                    "Магістр (зі скороченим терміном навчання)"
                                    ]

@pytest.fixture(params=data_provider_offers)
def offers(request):
    return request.param

@pytest.fixture(params=data_provider_forms_of_education)
def forms_of_education(request):
    return request.param

def test_open_add_enrollment(app):
    app.ensure_logged_in()
    app.internal_page.is_this_page
    app.internal_page.enrollments_page_link.click()
    app.enrollments_page.is_this_page
    app.enrollments_page.is_this_page.click()

def test_check_correct_structural_subdivision(app, offers):
    enr_page = app.enrollments_main_page
    enr_page.search_offers(offers, "Молодший спеціаліст на основі базової загальної середньої освіти")
    actual_data_structural_subdivision = enr_page.get_arr_structural_subdivision_from_choose_offer()
    enr_page.button_close_choose_offer.click()
    for actual_data in actual_data_structural_subdivision:
        assert offers == actual_data.encode("utf-8")

def test_check_correct_type_of_offer(app, forms_of_education):
    enr_page = app.enrollments_main_page
    enr_page.search_offers("Біологічний", forms_of_education)
    actual_data_type_offer = enr_page.get_arr_type_offer_from_choose_offer()
    enr_page.button_close_choose_offer.click()
    for actual_data in actual_data_type_offer:
        assert forms_of_education == actual_data.encode("utf-8")