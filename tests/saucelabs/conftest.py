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

sauce_user_name = os.environ['SAUCE_USER_NAME']
sauce_api_key = os.environ['SAUCE_API_KEY']

def get_remote_browsers():
    SAUCE_ONDEMAND_BROWSERS = os.environ['SAUCE_ONDEMAND_BROWSERS']
    different_settings = json.loads(SAUCE_ONDEMAND_BROWSERS)
    browsers = []
    for setting in different_settings:
        browsers.append({"platform":setting["platform"],
                       "browserName":setting["browser"],
                       "version":setting["browser-version"]
                       })
    return browsers

@pytest.yield_fixture(scope="module", params=get_remote_browsers())
def app_for_sauce(request, base_url):
    sauce_url = "http://%s:%s@ondemand.saucelabs.com:80/wd/hub"
    selenium_platform = request.param["platform"]
    selenium_version = request.param["browser-version"]
    selenium_browser = request.param["browser"]
    desired_cap = {'browserName': selenium_browser, 'platform': selenium_platform, 'version': selenium_version}
    driver = webdriver.Remote(
            command_executor=sauce_url % (sauce_user_name, sauce_api_key),
            desired_capabilities=desired_cap)
    print('SauceOnDemandSessionID={} job-name={}'.format(str(driver.session_id), request.param.name))
    yield Application(driver, base_url)
    driver.quit()
    test_result = sauceclient.SauceClient(sauce_user_name, sauce_api_key)
    status = (sys.exc_info() == (None, None, None))
    test_result.jobs.update_job(driver.session_id, passed=status)






