import pytest
from utils.add_person_pattern import AddPersonPattern

__author__ = 'stako'


@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
def test_delete_person(app, person):
    with pytest.allure.step('Test delete the created person.'):
        add_person_pattern = AddPersonPattern()
        add_person_pattern.login_and_delete_all_person_by_name(app, person)
        assert len(app.persons_page.rows_in_body) == 0
