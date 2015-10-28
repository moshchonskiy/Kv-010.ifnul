from utils.add_person_pattern import AddPersonPattern
from utils.personCreator import PersonCreator

__author__ = 'stako'

def test_delete_person(app, dictionary_with_json_files):
    create_person = PersonCreator(dictionary_with_json_files["person"])
    person = create_person.create_person_from_json()
    add_person_pattern = AddPersonPattern()
    add_person_pattern.add_person(app, person)
    assert len(app.persons_page.rows_in_body) == 0