from model.user import User
from utils.personCreator import PersonCreator

__author__ = 'Evgen'

import pytest
from selenium import webdriver
from model.application import Application
import os
from model.person import Person


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    # parser.addoption("--base_url", action="store", default="http://localhost:9000/")
    parser.addoption("--base_url", action="store", default="http://194.44.198.221/")
    parser.addoption("--person_file", action="store", default="person.json")


@pytest.fixture(scope="module")
def browser_type(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="module")
def base_url(request):
    return request.config.getoption("--base_url")

@pytest.fixture(scope="module")
def person_file(request):
    project_path = os.path.dirname(os.path.realpath(__file__))
    path = os.path.normpath(os.path.abspath(project_path) + "/resources/" + request.config.getoption("--person_file"))
    return path

@pytest.fixture(scope="module")
def person(request, person_file):
    person_creator = PersonCreator(person_file)
    return person_creator.create_person_from_json()

@pytest.yield_fixture()
def add_person(app):
    app.ensure_logout()
    app.login(User.Admin(), True)


@pytest.fixture(scope="module")
def app(request, browser_type, base_url):
    """
    Fixture is used to perform all tests, use it in your tests like >>>  def test_method(app)
    It performs all tests in one browser, because of (scope="session")
    If it needs to perform tests in another browser,
    you can write in the console something like >>> py.test --browser "chrome"
    :return: new Application with chosen or default params
    """
    if browser_type == "firefox":
        driver = webdriver.Firefox()
    elif browser_type == "chrome":
        driver = webdriver.Chrome()
    elif browser_type == "ie":
        driver = webdriver.Ie()
    request.addfinalizer(driver.quit)
    return Application(driver, base_url)
