import datetime

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

    def test_beginning_date_later_than_creation_date(self, logout_login):
        app = logout_login
        creation_date = self.read_creation_date(app)
        time_delta = datetime.timedelta(days=1)
        begin_date = creation_date + time_delta
        app.enrollments_main_page.set_begin_date(begin_date)
        assert not app.enrollments_main_page.find_date_of_begining().get_attribute("class").__contains__("ng-invalid")

    def test_beginning_date_earlier_than_creation_date(self, logout_login):
        app = logout_login
        creation_date = self.read_creation_date(app)
        time_delta = datetime.timedelta(days=1)
        begin_date = creation_date - time_delta
        app.enrollments_main_page.set_begin_date(begin_date)
        assert app.enrollments_main_page.find_date_of_begining().get_attribute("class").__contains__("ng-invalid")

    def test_ending_date_later_than_creation_date(self, logout_login):
        app = logout_login
        creation_date = self.read_creation_date(app)
        time_delta = datetime.timedelta(days=1)
        end_date = creation_date + time_delta
        app.enrollments_main_page.set_end_date(end_date)
        assert not app.enrollments_main_page.find_date_of_ending().get_attribute("class").__contains__("ng-invalid")

    def test_ending_date_earlier_than_creation_date(self, logout_login):
        app = logout_login
        creation_date = self.read_creation_date(app)
        time_delta = datetime.timedelta(days=1)
        end_date = creation_date - time_delta
        app.enrollments_main_page.set_end_date(end_date)
        assert app.enrollments_main_page.find_date_of_ending().get_attribute("class").__contains__("ng-invalid")

    def test_ending_date_later_than_beginning_date(self, logout_login):
        app = logout_login
        creation_date = self.read_creation_date(app)
        time_delta = datetime.timedelta(days=1)
        begin_date = creation_date + time_delta
        end_date = begin_date + time_delta
        app.enrollments_main_page.set_begin_date(begin_date)
        app.enrollments_main_page.set_end_date(end_date)
        assert not app.enrollments_main_page.find_date_of_ending().get_attribute("class").__contains__("ng-invalid")

    def test_ending_date_earlier_than_beginning_date(self, logout_login):
        app = logout_login
        creation_date = self.read_creation_date(app)
        time_delta = datetime.timedelta(days=2)
        begin_date = creation_date + time_delta
        time_delta = datetime.timedelta(days=1)
        end_date = begin_date - time_delta
        app.enrollments_main_page.set_begin_date(begin_date)
        app.enrollments_main_page.set_end_date(end_date)
        assert app.enrollments_main_page.find_date_of_ending().get_attribute("class").__contains__("ng-invalid")