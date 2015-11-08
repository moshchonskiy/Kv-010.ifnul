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
import traceback

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
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    driver = request.param
    print('SauceOnDemandSessionID={} job-name={}'.format(str(driver.session_id), request.param.name))
    yield Application(driver, base_url)

    driver.quit()
    test_result = sauceclient.SauceClient(SAUCE_USER_NAME, SAUCE_API_KEY)
    status = (sys.exc_info() == (None, None, None))
    test_result.jobs.update_job(driver.session_id, passed=status)






