import allure
from allure.constants import AttachmentType
import pytest

__author__ = 'Den'


@pytest.mark.usefixtures('pre_login')
class TestOne:
    def test_00(self):
        pass

    def test_01(self):
        try:
            with pytest.allure.step():
                inter_page = self.app.internal_page
                inter_page.is_this_page()
        except AssertionError:
            allure.attach('screenshot', self.app.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
            raise

    def test_02(self):
        try:
            with pytest.allure.step():
                dict_page = self.app.dictionaries_page
                dict_page.is_this_page()
        except AssertionError:
            allure.attach('screenshot', self.app.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
            raise

    def test_03(self):
        pass
