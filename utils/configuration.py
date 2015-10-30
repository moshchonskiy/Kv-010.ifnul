import sys
import traceback
import allure
from allure.constants import AttachmentType

__author__ = 'stako'


class Configuration():
    @staticmethod
    def print_simple_stacktrace():
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        print('An error occurred on line: {}, in statement: {}. The filename is: {}, and function is: {}.'
              .format(line, text, filename, func))

    def assert_and_get_screenshot(self, app, expression):
        try:
            assert expression
            allure.attach('screenshot', app.persons_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
        except AssertionError:
            allure.attach('screenshot', app.persons_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
            self.print_simple_stacktrace()
            raise
