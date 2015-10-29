from utils.add_person_pattern import AddPersonPattern

__author__ = 'stako'


def test_delete_person(app, person):
    add_person_pattern = AddPersonPattern()
    add_person_pattern.add_person(app, person)
    assert len(app.persons_page.rows_in_body) == 0
