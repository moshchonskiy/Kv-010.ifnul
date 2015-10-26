__author__ = 'Evgen'
import pytest
from selenium.webdriver.common.keys import Keys

from model.user import User


def test_invalid_login(generator_app_for_sauce):
    with pytest.allure.step('Inalid login test'):
        generator_app_for_sauce.ensure_logout()
        generator_app_for_sauce.login(User.random())
        assert generator_app_for_sauce.is_not_logged_in()


def test_valid_login(generator_app_for_sauce):
    with pytest.allure.step('Valid login test'):
        generator_app_for_sauce.ensure_logout()
        generator_app_for_sauce.login(User.Admin())
        assert generator_app_for_sauce.is_logged_in()


def test_remember_me_checkbox(generator_app_for_sauce):
    with pytest.allure.step("Remember me checkbox test"):
        generator_app_for_sauce.ensure_logout()
        generator_app_for_sauce.login(User.Admin(), True)
        ip = generator_app_for_sauce.internal_page
        main_window_handle = ip.driver.current_window_handle
        body = ip.driver.find_element_by_tag_name("body")
        body.send_keys(Keys.CONTROL + 'n')
        ip.driver.switch_to.window(main_window_handle)
        all_windows = ip.driver.window_handles
        ip.driver.close()
        ip.driver.switch_to.window(all_windows[1])
        ip.driver.get(ip.base_url + "#/person/list")
        assert generator_app_for_sauce.is_logged_in()
