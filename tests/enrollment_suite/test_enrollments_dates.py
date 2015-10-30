import datetime
import pytest

__author__ = 'acidroed'

class TestEnrollmentsDates(object):

    def convert_string_to_datetime(self, str_date):
        return datetime.datetime.strptime(str_date, '%Y-%m-%d')

    def read_creation_date(self, app):
        """
        Method read date of creation on add enrollment page
        :param app: application context in Application format
        :return: Creation date in Datetime format
        """
        app.internal_page.enrollments_page_link.click()
        app.enrollments_page.is_this_page
        app.enrollments_page.add_new_enrollment_button_click
        app.enrollments_main_page.is_this_page
        return self.convert_string_to_datetime(app.enrollments_main_page.find_date_of_creation().get_attribute("value"))

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_beginning_date_later_than_creation_date(self, logout_login):
        with pytest.allure.step('Authorize to the application, click add enrollment button and read date of creation'):
            app = logout_login
            creation_date = self.read_creation_date(app)
            time_delta = datetime.timedelta(days=1)
            begin_date = creation_date + time_delta
        with pytest.allure.step('Set begining date later than creation date'):
            app.enrollments_main_page.set_begin_date(begin_date)
        with pytest.allure.step('Asert that the beginning date input field is not red'):
            assert not app.enrollments_main_page.find_date_of_begining().get_attribute("class").__contains__("ng-invalid")

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_beginning_date_earlier_than_creation_date(self, logout_login):
        with pytest.allure.step('Authorize to the application, click add enrollment button and read date of creation'):
            app = logout_login
            creation_date = self.read_creation_date(app)
            time_delta = datetime.timedelta(days=1)
            begin_date = creation_date - time_delta
        with pytest.allure.step('Set begining date earlier than creation date'):
            app.enrollments_main_page.set_begin_date(begin_date)
        with pytest.allure.step('Asert that the beginning date input field is red'):
            assert app.enrollments_main_page.find_date_of_begining().get_attribute("class").__contains__("ng-invalid")

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_ending_date_later_than_creation_date(self, logout_login):
        with pytest.allure.step('Authorize to the application, click add enrollment button and read date of creation'):
            app = logout_login
            creation_date = self.read_creation_date(app)
            time_delta = datetime.timedelta(days=1)
            end_date = creation_date + time_delta
        with pytest.allure.step('Set ending date earlier than creation date'):
            app.enrollments_main_page.set_end_date(end_date)
        with pytest.allure.step('Asert that the ending date input field is not red'):
            assert not app.enrollments_main_page.find_date_of_ending().get_attribute("class").__contains__("ng-invalid")

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_ending_date_earlier_than_creation_date(self, logout_login):
        with pytest.allure.step('Authorize to the application, click add enrollment button and read date of creation'):
            app = logout_login
            creation_date = self.read_creation_date(app)
            time_delta = datetime.timedelta(days=1)
            end_date = creation_date - time_delta
        with pytest.allure.step('Set ending date earlier than creation date'):
            app.enrollments_main_page.set_end_date(end_date)
        with pytest.allure.step('Asert that the ending date input field is red'):
            assert app.enrollments_main_page.find_date_of_ending().get_attribute("class").__contains__("ng-invalid")

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_ending_date_later_than_beginning_date(self, logout_login):
        with pytest.allure.step('Authorize to the application, click add enrollment button and read date of creation'):
            app = logout_login
            creation_date = self.read_creation_date(app)
            time_delta = datetime.timedelta(days=1)
            begin_date = creation_date + time_delta
            end_date = begin_date + time_delta
        with pytest.allure.step('Set beginning date and ending date later than beginning date'):
            app.enrollments_main_page.set_begin_date(begin_date)
            app.enrollments_main_page.set_end_date(end_date)
        with pytest.allure.step('Asert that the ending date input field is not red'):
            assert not app.enrollments_main_page.find_date_of_ending().get_attribute("class").__contains__("ng-invalid")

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_ending_date_earlier_than_beginning_date(self, logout_login):
        with pytest.allure.step('Authorize to the application, click add enrollment button and read date of creation'):
            app = logout_login
            creation_date = self.read_creation_date(app)
            time_delta = datetime.timedelta(days=2)
            begin_date = creation_date + time_delta
            time_delta = datetime.timedelta(days=1)
            end_date = begin_date - time_delta
        with pytest.allure.step('Set beginning date and ending date earlier than beginning date'):
            app.enrollments_main_page.set_begin_date(begin_date)
            app.enrollments_main_page.set_end_date(end_date)
        with pytest.allure.step('Asert that the ending date input field is red'):
            assert app.enrollments_main_page.find_date_of_ending().get_attribute("class").__contains__("ng-invalid")