# coding=utf-8
from selenium.webdriver.common.by import By
from pages.internal_page import InternalPage

__author__ = 'Administrator'

class PersonMainViewPage(InternalPage):

    PERSON_DOCUMENTS_BUTTON = (By.XPATH, "//a[contains(.,'Документи')]")
    PERSON_ENROLLMENT_BUTTON = (By.XPATH, "//a[contains(.,'Заяви')]")
    PERSON_BUTTON = (By.XPATH, "//a[contains(.,'Персона')]")