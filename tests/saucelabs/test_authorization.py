__author__ = 'Evgen'
import pytest

def test_valid_login(generator_app_for_sauce):
    with pytest.allure.step('Valid login test'):
        assert generator_app_for_sauce.login_page.is_this_page

def test_invalid(generator_app_for_sauce):
    assert generator_app_for_sauce.login_page.is_this_page