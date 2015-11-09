__author__ = 'Evgen'
import pytest

class TestGoogle:

    def test_valid_login(self, app_for_sauce):
        with pytest.allure.step('Valid login test'):
            assert app_for_sauce.login_page.is_this_page

    def test_invalid(self, app_for_sauce):
        assert app_for_sauce.login_page.is_this_page