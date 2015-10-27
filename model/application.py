from pages.dictionaries_page import DictionariesPage
from pages.persons.view.person_current_view_page import PersonCurrentViewPage
from pages.persons.view.person_enrollment_view_page import PersonEnrollmentViewPage
from pages.persons.view.person_main_view_page import PersonMainViewPage
from pages.persons.view.person_papers_view_page import PersonPapersViewPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import *
from pages.login_page import LoginPage
from pages.enrollments.enrollments_page import EnrollmentsPage
from pages.enrollments.add.enrollment_main_page import EnrollmentsMainPage
from pages.enrollments.add.enrollment_base_page import EnrollmentsBasePage
from model.user import User
from pages.persons.add.person_main_page import *
from pages.persons.persons_page import PersonsPage
from pages.persons.add.person_extra_page import *
from pages.persons.add.person_addresses_page import *
from pages.persons.add.person_contacts_page import *
from pages.persons.add.person_papers_page import *
from pages.persons.add.person_base_page import *

__author__ = 'Evgen'


class Application:
    def __init__(self, driver, base_url):
        """

        :type self: object
        """
        self.base_url = base_url
        self.driver = driver
        self.driver.get(base_url)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 15)
        self.login_page = LoginPage(self.driver)
        self.persons_page = PersonsPage(self.driver)
        self.internal_page = InternalPage(self.driver)
        self.person_main_page = AddPersonMainPage(self.driver)
        self.enrollments_page = EnrollmentsPage(self.driver)
        self.dictionaries_page = DictionariesPage(self.driver)
        self.person_current_view_page = PersonCurrentViewPage(self.driver)
        self.person_main_view_page = PersonMainViewPage(self.driver)
        self.person_papers_view_page = PersonPapersViewPage(self.driver)
        self.person_enrollment_view_page = PersonEnrollmentViewPage(self.driver)
        self.enrollments_main_page = EnrollmentsMainPage(self.driver)
        self.enrollments_base_page = EnrollmentsBasePage(self.driver)
        self.main_page = AddPersonMainPage(self.driver)
        self.extra_page = AddPersonExtraPage(self.driver)
        self.address_page = AddPersonAddressesPage(self.driver)
        self.contact_page = AddPersonContactsPage(self.driver)
        self.papers_page = AddPersonPapersPage(self.driver)
        self.person_base_page = AddPersonPage(self.driver)

    def login(self, user, checkbox=False):
        """
        Method performs login to the application. Use app.login(User.Admin) in tests
        :param user: User.Admin or User.random at the moment
        :param checkbox: True with checkbox remember me and False without it. Default value is False
        """
        lp = self.login_page
        lp.is_this_page()
        lp.username_field.clear()
        lp.username_field.send_keys(user.username)
        lp.password_field.clear()
        lp.password_field.send_keys(user.password)
        if checkbox:
            lp.login_checkbox.click()
            lp.submit_button.click()
            self.internal_page.is_element_present(self.internal_page.SPINNER_OFF)
        else:
            lp.submit_button.click()
            self.internal_page.is_element_present(self.internal_page.SPINNER_OFF)

    def ensure_logged_in(self):
        """
        Method ensures you are logged in, if not it enters as Admin
        """
        element = self.wait.until(presence_of_element_located((By.CSS_SELECTOR, "nav, input[id='inputLogin']")))
        if element.tag_name == "input":
            self.login(User.Admin())

    def logout(self):
        """
        Method performs logout from application
        """
        ip = self.internal_page
        ip.is_this_page()
        ip.user_dropdown.click()
        ip.logout_button.click()

    def ensure_logout(self):
        """
        Method ensures you are logged out from application, if not it performs logout
        """
        element = self.wait.until(presence_of_element_located((By.CSS_SELECTOR, "nav, input[id='inputLogin']")))
        if element.tag_name == "nav":
            self.logout()

    def is_logged_in(self):
        """
        Method checks you are logged in
        :return True or False
        """
        return self.internal_page.is_this_page

    def is_not_logged_in(self):
        """
        Method checks you are not logged in
        :return: True or False
        """
        return self.login_page.is_this_page
