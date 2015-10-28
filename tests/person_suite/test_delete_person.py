from utils.add_person_pattern import AddPersonPattern

__author__ = 'stako'

def test_delete_person(app, ):
    create_person = PersonCreator(dictionary_with_json_files["person"])
    person = create_person.create_person_from_json()
    add_person_pattern = AddPersonPattern()
    add_person_pattern.add_person(app, person)