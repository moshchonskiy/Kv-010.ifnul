__author__ = 'Evgen'
import pytest
from model.user import User


def test_valid_login(app):
    app.ensure_logout()
    app.login(User.Admin())
    assert app.is_logged_in()


def test_invalid_login(app):
    app.ensure_logout()
    app.login(User.random())
    assert app.is_not_logged_in()

