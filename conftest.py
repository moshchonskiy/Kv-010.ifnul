__author__ = 'Evgen'

import pytest
from selenium import webdriver
from model.application import Application


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--base_url", action="store", default="http://194.44.198.221/")


@pytest.fixture(scope="session")
def browser_type(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--base_url")


@pytest.fixture(scope="session")
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
