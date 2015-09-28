__author__ = 'Evgen'
from page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class InternalPage(Page):

    @property
    def user_dropdown(self):
        return self.driver.find_element_by_xpath("//i[@class='fa fa-user fa-fw']")

    @property
    def logout_button(self):
        return self.driver.find_element_by_xpath("//li[@class='dropdown open']//a[@ng-click='header.logout()']")

    @property
    def is_this_page(self):
        return self.is_element_visible((By.CSS_SELECTOR, "nav"))

    @property
    def person_page_link(self):
        return self.driver.find_element_by_xpath("//a[@ui-sref='root.person.list']")

    @property
    def enrollment_page_link(self):
        return self.driver.find_element_by_xpath("//a[@ui-sref='root.enrolment.list']")

    @property
    def dictionaries_page_link(self):
        return self.driver.find_element_by_xpath("//a[@ui-sref='root.dictionaries']")
