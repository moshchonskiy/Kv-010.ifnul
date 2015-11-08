__author__ = 'Evgen'
import pytest
from selenium.webdriver.common.keys import Keys

from model.user import User



def test_valid_login(generator_app_for_sauce):
    with pytest.allure.step('Valid login test'):
        assert generator_app_for_sauce.login_page.is_this_page
