__author__ = 'acidroed'



class TestEnrollmentsDates(object):

    def read_creation_date(self, app):
        app.internal_page.enrollments_page_link.click()
        app.enrollments_page.is_this_page
        app.enrollments_page.add_new_enrollment_button_click
        app.enrollments_main_page.is_this_page
        creation_date = app.enrollments_main_page.find_date_of_creation.text
        print creation_date

    def test_date(self, logout_login):
        self.read_creation_date(logout_login)
        assert True
