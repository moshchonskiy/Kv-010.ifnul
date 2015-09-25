__author__ = 'Evgen'
from model.user import User
from model.application import Application
from pages.persons_page import PersonsPage


def test_go_to_new_person(app):
    app.login(User.Admin())
    app.go_to_persons_page()
    assert app.persons_page.is_this_page
