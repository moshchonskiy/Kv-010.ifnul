
__author__ = 'Evgen'

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import *

from pages.internal_page import InternalPage
from pages.login_page import LoginPage
from pages.enrollments.enrollments_page import EnrollmentsPage
from pages.enrollments.add.enrollment_main_page import EnrollmentsMainPage
from pages.enrollments.add.enrollment_base_page import EnrollmentsBasePage
from model.user import User
from pages.dictionaries_page import DictionariesPage
from pages.persons.view.person_current_view_page import PersonCurrentViewPage
from pages.persons.view.person_enrollment_view_page import PersonEnrollmentViewPage
from pages.persons.view.person_main_view_page import PersonMainViewPage
from pages.persons.view.person_papers_view_page import PersonPapersViewPage
from pages.persons.persons_page import PersonsPage
from pages.persons.add.person_main_page import *
from pages.persons.add.person_enrollments_page import PersonEnrollmentPage
from pages.persons.add.person_extra_page import *
from pages.persons.add.person_addresses_page import *
from pages.persons.add.person_contacts_page import *
from pages.persons.add.person_papers_page import *
from pages.persons.add.person_base_page import *


class Application:
    def __init__(self, driver, base_url):
        self.driver = driver
        driver.get(base_url)
        driver.maximize_window()
        self.wait = WebDriverWait(driver, 15)
        self.login_page = LoginPage(driver, base_url)

