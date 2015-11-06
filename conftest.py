#!/usr/bin/env python
# -*- coding: utf-8 -*-
from model.user import User

__author__ = 'Evgen'

import pytest
from selenium import webdriver
from pyvirtualdisplay import Display
from model.application import Application
from utils.data_provider_from_json import DataProviderJSON
from utils.configuration import Configuration

# def pytest_addoption(parser):
#     parser.addoption("--browser", action="store", default="firefox")
#     parser.addoption("--base_url", action="store", default="http://192.168.96.134:9000/")
#     # parser.addoption("--base_url", action="store", default="http://194.44.198.221/")
#     parser.addoption("--jenkins_display", action="store_true")


@pytest.fixture(scope="session")
def browser_type(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--base_url")


@pytest.fixture(scope="session")
def dictionary_with_json_files():
    data_provider = DataProviderJSON("properties.json")
    return data_provider.get_value_by_key("json_files")


@pytest.fixture(scope="session")
def jenkins_display(request):
    return request.config.getoption("--jenkins_display")


@pytest.fixture(scope="session")
def app(request, browser_type, base_url, jenkins_display):
    """
    Fixture is used to perform all tests, use it in your tests like >>>  def test_method(app)
    It performs all tests in one browser, because of (scope="session")
    If it needs to perform tests in another browser,
    you can write in the console something like >>> py.test --browser "chrome"
    :return: new Application with chosen or default params
    """
    if jenkins_display:
        display = Display(visible=0, size=(1366, 768))
        display.start()
    if browser_type == "firefox":
        driver = webdriver.Firefox()
    elif browser_type == "chrome":
        driver = webdriver.Chrome()
    elif browser_type == "ie":
        driver = webdriver.Ie()
    request.addfinalizer(driver.quit)
    return Application(driver, base_url)


@pytest.yield_fixture(scope="function")
def logout_login(app):
    app.ensure_logout()
    app.login(User.Admin(), True)
    app.internal_page.wait_until_page_generate()
    yield app


@pytest.fixture(scope="class")
def pre_login(request, app):
    app.ensure_logout()
    app.login(User.Admin(), True)
    request.cls.app = app

@pytest.fixture(scope="session")
def screenshot():
    return Configuration()
