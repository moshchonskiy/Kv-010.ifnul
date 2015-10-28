import pytest

__author__ = 'dmakstc'


@pytest.mark.usefixtures('login')
class TestAddTwo:
    def test_01(self):
        print "TestAddTwo_test_01"
        print self.app

    def test_02(self):
        print "TestAddTwo_test_02"
        print self.app
