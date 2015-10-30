import pytest
from utils.add_person_pattern import AddPersonPattern
from utils.configuration import Configuration

__author__ = 'stako'


@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
def test_delete_person(app, person):
    with pytest.allure.step('Test delete the created person.'):
        add_person_pattern = AddPersonPattern()
        add_person_pattern.login_and_delete_all_person_by_name(app, person)
        assert_expression = len(app.persons_page.rows_in_body) == 0
        configuration = Configuration()
        configuration.assert_and_get_screenshot(app, assert_expression)
