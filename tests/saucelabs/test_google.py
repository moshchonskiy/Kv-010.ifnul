import os
import unittest
import sys
import new
from selenium import webdriver
from sauceclient import SauceClient
import json

def get_remote_saucelabs_webdriver():
    SAUCE_ONDEMAND_BROWSERS = os.environ['SAUCE_ONDEMAND_BROWSERS']
    different_settings = json.loads(SAUCE_ONDEMAND_BROWSERS)
    browsers = []
    for setting in different_settings:
        browsers.append({"platform":setting["platform"],
                       "browserName":setting["browser"],
                       "version":setting["browser-version"]
                       })
    return browsers

username = os.environ['SAUCE_USER_NAME']
access_key = os.environ['SAUCE_API_KEY']

# This decorator is required to iterate over browsers
def on_platforms(platforms):
    def decorator(base_class):
        module = sys.modules[base_class.__module__].__dict__
        for i, platform in enumerate(platforms):
            d = dict(base_class.__dict__)
            d['desired_capabilities'] = platform
            name = "%s_%s" % (base_class.__name__, i + 1)
            module[name] = new.classobj(name, (base_class,), d)
    return decorator

@on_platforms(get_remote_saucelabs_webdriver())
class FirstSampleTest(unittest.TestCase):

    # setUp runs before each test case
    def setUp(self):
        self.desired_capabilities['name'] = self.id()
        self.driver = webdriver.Remote(
           command_executor="http://%s:%s@ondemand.saucelabs.com:80/wd/hub" % (username, access_key),
           desired_capabilities=self.desired_capabilities)

    # verify google title
    def test_google(self):
        self.driver.get("http://www.google.com")
        assert ("Yahho" in self.driver.title), "Unable to load google page"

    # type 'Sauce Labs' into google search box and submit
    def test_google_search(self):
        self.driver.get("http://www.google.com")
        elem = self.driver.find_element_by_name("q")
        elem.send_keys("Sauce Labs")
        elem.submit()

    # tearDown runs after each test case
    def tearDown(self):
        self.driver.quit()
        session_id = self.driver.session_id
        job_name = self.id()
        sauce_client = SauceClient(username, access_key)
        status = (sys.exc_info() == (None, None, None))
        sauce_client.jobs.update_job(session_id, passed=status)
        print "SauceOnDemandSessionID=%s job-name=%s" % (session_id, job_name)
