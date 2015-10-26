#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import threading
from model.user import User
from utils.personCreator import PersonCreator
from pyvirtualdisplay import Display

__author__ = 'Evgen'

import pytest
from selenium import webdriver
from model.application import Application
import os
import sys
import sauceclient
from sys import stdout

# SAUCE_USER_NAME = os.environ['SAUCE_USER_NAME']
# SAUCE_API_KEY = os.environ['SAUCE_API_KEY']

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    # parser.addoption("--base_url", action="store", default="http://localhost:9000/")
    parser.addoption("--base_url", action="store", default="http://194.44.198.221/")
    parser.addoption("--person_file", action="store", default="person_test_view.json")
    parser.addoption("--jenkins_display", action="store_true")

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
def add_person(app, person):
    app.ensure_logout()
    app.login(User.Admin(), True)
    # Check that the added person doesn't exist
    person_page = app.persons_page
    is_person_already_exists = True
    while is_person_already_exists:
        person_page.is_this_page
        person_page.try_get_choose_surname().click()
        person_page.try_get_input_group().clear()
        person_page.try_get_input_group().send_keys(person.surname_ukr)
        person_page.try_get_ok_button().click()
        if person_page.searching_person_by_surname(person.surname_ukr) != None:
            person_page.delete_first_person_in_page
        else:
            is_person_already_exists = False

    yield app
    # Delete new added person
    person_page.is_this_page
    expected_person = person_page.try_get_expected_surname(person.surname_ukr).text.partition(' ')[0]
    if expected_person:
        person_page.delete_first_person_in_page

@pytest.fixture(scope="module")
def jenkins_display(request):
    return request.config.getoption("--jenkins_display")


@pytest.fixture(scope="module")
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


def get_remote_saucelabs_webdriver():
    # SAUCE_ONDEMAND_BROWSERS = os.environ['SAUCE_ONDEMAND_BROWSERS']
    # different_settings = json.loads(SAUCE_ONDEMAND_BROWSERS)
    # SAUCE_URL = "http://%s:%s@ondemand.saucelabs.com:80/wd/hub"
    drivers = []
    # for setting in different_settings:
    #     SELENIUM_PLATFORM = setting["platform"]
    #     SELENIUM_VERSION = setting["browser-version"]
    #     SELENIUM_BROWSER = setting["browser"]
    #     desired_cap = {'browserName': SELENIUM_BROWSER, 'platform': SELENIUM_PLATFORM, 'version': SELENIUM_VERSION, 'name': "Kv-010.ifnul"}
    #     driver = webdriver.Remote(
    #         command_executor=SAUCE_URL % (SAUCE_USER_NAME, SAUCE_API_KEY),
    #         desired_capabilities=desired_cap)
    #     drivers.append(driver)
    return drivers


@pytest.yield_fixture(scope="module", params=get_remote_saucelabs_webdriver())
def generator_app_for_sauce(request, base_url):
    # test_result = sauceclient.SauceClient(SAUCE_USER_NAME, SAUCE_API_KEY)
    driver = request.param
    yield Application(driver, base_url)
    print("Link to your job: https://saucelabs.com/jobs/%s" % driver.session_id)
    try:
        if sys.exc_info() == (None, None, None):
            test_result.jobs.update_job(driver.session_id, passed=True)
        else:
            test_result.jobs.update_job(driver.session_id, passed=False)
    finally:
        driver.quit()




