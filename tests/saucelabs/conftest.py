#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

__author__ = 'Evgen'

import pytest
from selenium import webdriver
from model.application import Application
import os
import sys
import sauceclient

SAUCE_USER_NAME = os.environ['SAUCE_USER_NAME']
SAUCE_API_KEY = os.environ['SAUCE_API_KEY']


def get_remote_saucelabs_webdriver():
    SAUCE_ONDEMAND_BROWSERS = os.environ['SAUCE_ONDEMAND_BROWSERS']
    different_settings = json.loads(SAUCE_ONDEMAND_BROWSERS)
    SAUCE_URL = "http://%s:%s@ondemand.saucelabs.com:80/wd/hub"
    drivers = []
    for setting in different_settings:
        SELENIUM_PLATFORM = setting["platform"]
        SELENIUM_VERSION = setting["browser-version"]
        SELENIUM_BROWSER = setting["browser"]
        desired_cap = {'browserName': SELENIUM_BROWSER, 'platform': SELENIUM_PLATFORM, 'version': SELENIUM_VERSION, 'name': "Kv-010.ifnul"}
        driver = webdriver.Remote(
            command_executor=SAUCE_URL % (SAUCE_USER_NAME, SAUCE_API_KEY),
            desired_capabilities=desired_cap)
        drivers.append(driver)
    return drivers


@pytest.yield_fixture(scope="module", params=get_remote_saucelabs_webdriver())
def generator_app_for_sauce(request, base_url):
    test_result = sauceclient.SauceClient(SAUCE_USER_NAME, SAUCE_API_KEY)
    driver = request.param
    yield Application(driver, base_url)
    print('SauceOnDemandSessionID={} job-name={}'.format(str(driver.session_id), "my_job"))
    driver.quit()

    status = sys.exc_info() == (None, None, None)
    test_result.jobs.update_job(driver.session_id, passed=status)
    # try:
    #     if sys.exc_info() == (None, None, None):
    #         test_result.jobs.update_job(driver.session_id, passed=True)
    #     else:
    #         test_result.jobs.update_job(driver.session_id, passed=False)
    # finally:
    #     driver.quit()






