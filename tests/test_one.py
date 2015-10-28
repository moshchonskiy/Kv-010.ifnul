
import allure
from allure.constants import AttachmentType
import pytest


__author__ = 'Den'





@pytest.mark.usefixtures('pre_login')
class TestOne:

    def _decorator(self, func):
        def wr(*args):
            try:
                return func(*args)
            except AssertionError:
                 allure.attach('screenshot', self.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
        return wr

    def test_00(self):
        pass

    @_decorator
    def test_01(self):
        inter_page = self.app.internal_page
        inter_page.is_this_page()


    def test_02(self):
        dict_page = self.app.dictionaries_page
        dict_page.is_this_page()

    def test_03(self):
        pass


