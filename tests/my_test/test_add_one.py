import pytest


__author__ = 'dmakstc'





@pytest.mark.usefixtures('login')
class TestAddOne:

    @ErrorDecoder()
    def test_01(self):
        print "TestAddOne_test_01"



    @ErrorDecoder()
    def test_02(self):
        print "TestAddOne_test_02"




