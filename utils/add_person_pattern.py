from model.user import User

__author__ = 'stako'


class AddPersonPattern(object):

    def add_person(self, app, person):
        app.ensure_logout()
        app.login(User.Admin(), True)
        # Check that the added person doesn't exist
        is_person_already_exists = True
        while is_person_already_exists:
            self.search_person_by_surname(app, person.surname_ukr)
            if app.persons_page.searching_person_by_surname(person.surname_ukr) is not None:
                app.persons_page.delete_first_person_in_page
            else:
                is_person_already_exists = False

    def del_created_person(self, app, person):
        #Delete new added person
        person_page = app.persons_page
        person_page.is_this_page
        expected_person = person_page.try_get_searched_surname(person.surname_ukr).text.partition(' ')[0]
        if expected_person:
            person_page.delete_first_person_in_page

    def search_person_by_surname(self, app, surname):
        person_page = app.persons_page
        person_page.try_get_choose_surname().click()
        person_page.try_get_input_group().clear()
        person_page.try_get_input_group().send_keys(surname)
        person_page.try_get_ok_button().click()
