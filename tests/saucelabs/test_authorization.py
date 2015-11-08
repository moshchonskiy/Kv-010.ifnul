__author__ = 'Evgen'
import pytest

def test_valid_login(generator_app_for_sauce):
    with pytest.allure.step('Valid login test'):
        print('SauceOnDemandSessionID={} job-name={}'.format(str(generator_app_for_sauce.login_page.driver.session_id),
                                                             test_valid_login.__name__))
        assert generator_app_for_sauce.login_page.is_this_page
