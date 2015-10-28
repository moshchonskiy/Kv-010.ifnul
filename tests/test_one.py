import pytest as pytest
from fixtures.decorators import ErrorHandler, dec

__author__ = 'Den'


@pytest.mark.usefixtures('pre_login')
class TestOne:
    def test_00(self):
        pass

    def test_01(self):
        inter_page = self.app.internal_page
        inter_page.is_this_page()


    def test_02(self):
        dict_page = self.app.dictionaries_page
        dict_page.is_this_page()

    def test_03(self):
        pass
