# coding=utf-8
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox import webdriver
from pages.persons.view.person_main_view_page import PersonMainViewPage

__author__ = 'Administrator'

class PersonCurrentViewPage(PersonMainViewPage):

    # >>>>>>>>>>>>>>>>>>>>>>>>>>> Global locators for information about person <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    FIO_PERSON_UKRANIAN = (By.XPATH, "//h2[@class='text-primary ng-binding']")
    FIO_PERSON_ENGLISH = (By.XPATH, "//h4[@class='ng-binding']")

    SERIAL_PERSONAL_RECORD = (By.XPATH, "//p[contains(.,'Серія')]")
    NUMBER_PERSONAL_RECORD = (By.XPATH, "//p[contains(.,'Номер')]")

    # >>>>>>>>>>>>>>>>>>>>>>>>>>> Main locators for information about person <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    # This titles for use in tests
    arr_titles_main = ["TYPE_OF_PERSON", "DATE_OF_BIRTH", "RESIDENT", "SEX", "MARITAL_STATUS", "MILITARY_SERVICE",
                      "CITIZENSHIP", "INDEX_MATERIAL_RESPONSIBLE", "HOSTEL"]
    TYPE_OF_PERSON = (By.XPATH, "//p[contains(.,'Тип персони')]")
    DATE_OF_BIRTH = (By.XPATH, "//p[contains(.,'Дата народження')]")
    RESIDENT = (By.XPATH, "//p[contains(.,'Резидент')]")
    SEX = (By.XPATH, "//p[contains(.,'Стать')]")
    MARITAL_STATUS = (By.XPATH, "//p[contains(.,'Сімейний стан')]")
    MILITARY_SERVICE = (By.XPATH, "//p[contains(.,'Військовозобовязаний')]")
    CITIZENSHIP = (By.XPATH, "//p[contains(.,'Громадянство')]")
    INDEX_MATERIAL_RESPONSIBLE = (By.XPATH, "//p[contains(.,'Індекс матеріально відповідального')]")
    HOSTEL = (By.XPATH, "//p[contains(.,'Гуртожиток')]")

    # Date of birth
    arr_titles_birth = ["PLACE_OF_BIRTH_LEVEL_1", "PLACE_OF_BIRTH_LEVEL_2", "PLACE_OF_BIRTH_LEVEL_3",
                "PLACE_OF_BIRTH_LEVEL_4", "PLACE_OF_BIRTH_LEVEL_5", "PLACE_OF_BIRTH_LEVEL_6", "PLACE_OF_BIRTH_LEVEL_7"]
    FOR_COUNT_ELEMENTS_DATE_OF_BIRTH = (By.CSS_SELECTOR, ".form-group.col-md-10>label+div .form-group.ng-scope")
    PLACE_OF_BIRTH_LEVEL_1 = (By.CSS_SELECTOR, ".form-group.col-md-10>label+div>div:nth-child(1) span:nth-child(2) span")
    PLACE_OF_BIRTH_LEVEL_2 = (By.CSS_SELECTOR, ".form-group.col-md-10>label+div>div:nth-child(2) span:nth-child(2) span")
    PLACE_OF_BIRTH_LEVEL_3 = (By.CSS_SELECTOR, ".form-group.col-md-10>label+div>div:nth-child(3) span:nth-child(2) span")
    PLACE_OF_BIRTH_LEVEL_4 = (By.CSS_SELECTOR, ".form-group.col-md-10>label+div>div:nth-child(4) span:nth-child(2) span")
    PLACE_OF_BIRTH_LEVEL_5 = (By.CSS_SELECTOR, ".form-group.col-md-10>label+div>div:nth-child(5) span:nth-child(2) span")
    PLACE_OF_BIRTH_LEVEL_6 = (By.CSS_SELECTOR, ".form-group.col-md-10>label+div>div:nth-child(6) span:nth-child(2) span")
    PLACE_OF_BIRTH_LEVEL_7 = (By.CSS_SELECTOR, ".form-group.col-md-10>label+div>div:nth-child(7) span:nth-child(2) span")

    # >>>>>>>>>>>>>>>>>>>>>>>>>>> Addreses <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    # Address of registration
    arr_titles_registration = ["REGISTRATION_ADRESS_LEVEL_1", "REGISTRATION_ADRESS_LEVEL_2", "REGISTRATION_ADRESS_LEVEL_3",
                "REGISTRATION_ADRESS_LEVEL_4", "REGISTRATION_ADRESS_LEVEL_5", "REGISTRATION_ADRESS_LEVEL_6", "REGISTRATION_ADRESS_LEVEL_7"]
    FOR_COUNT_ELEMENTS_ADDRES_OF_REGISTRATION = (By.CSS_SELECTOR, ".row.form-group.ng-scope>div>label+div"
                                    "[ng-model='entirePerson.addresses.regAddresses.adminUnitId'] .form-group.ng-scope")
    REGISTRATION_ADRESS_LEVEL_1 = (By.CSS_SELECTOR, ".row.form-group.ng-scope>div>label+div"
                "[ng-model='entirePerson.addresses.regAddresses.adminUnitId']>div:nth-child(1) span:nth-child(2) span")
    REGISTRATION_ADRESS_LEVEL_2 = (By.CSS_SELECTOR, ".row.form-group.ng-scope>div>label+div"
                "[ng-model='entirePerson.addresses.regAddresses.adminUnitId']>div:nth-child(2) span:nth-child(2) span")
    REGISTRATION_ADRESS_LEVEL_3 = (By.CSS_SELECTOR, ".row.form-group.ng-scope>div>label+div"
                "[ng-model='entirePerson.addresses.regAddresses.adminUnitId']>div:nth-child(3) span:nth-child(2) span")
    REGISTRATION_ADRESS_LEVEL_4 = (By.CSS_SELECTOR, ".row.form-group.ng-scope>div>label+div"
                "[ng-model='entirePerson.addresses.regAddresses.adminUnitId']>div:nth-child(4) span:nth-child(2) span")
    REGISTRATION_ADRESS_LEVEL_5 = (By.CSS_SELECTOR, ".row.form-group.ng-scope>div>label+div"
                "[ng-model='entirePerson.addresses.regAddresses.adminUnitId']>div:nth-child(5) span:nth-child(2) span")
    REGISTRATION_ADRESS_LEVEL_6 = (By.CSS_SELECTOR, ".row.form-group.ng-scope>div>label+div"
                "[ng-model='entirePerson.addresses.regAddresses.adminUnitId']>div:nth-child(6) span:nth-child(2) span")
    REGISTRATION_ADRESS_LEVEL_7 = (By.CSS_SELECTOR, ".row.form-group.ng-scope>div>label+div"
                "[ng-model='entirePerson.addresses.regAddresses.adminUnitId']>div:nth-child(7) span:nth-child(2) span")

    # Exact addresses
    arr_titles_exact_reg = ["REGISTRATION_ZIPCODE", "REGISTRATION_STREET_TYPE", "REGISTRATION_STREET",
                            "REGISTRATION_HOME", "REGISTRATION_APARTMENT"]
    REGISTRATION_ZIPCODE = (By.ID, "inputZipCodeReg")
    REGISTRATION_STREET_TYPE = (By.ID, "inputStreetTypeReg")
    REGISTRATION_STREET = (By.ID, "inputStreetReg")
    REGISTRATION_HOME = (By.ID, "inputHouseReg")
    REGISTRATION_APARTMENT = (By.ID, "inputApartmentReg")

    # Post addres
    arr_titles_post_addres = ["POST_ADRESS_LEVEL_1", "POST_ADRESS_LEVEL_2", "POST_ADRESS_LEVEL_3",
                "POST_ADRESS_LEVEL_4", "POST_ADRESS_LEVEL_5", "POST_ADRESS_LEVEL_6", "POST_ADRESS_LEVEL_7"]
    FOR_COUNT_ELEMENTS_POST_ADDRES = (By.CSS_SELECTOR, ".row.form-group.ng-scope>div>label+div"
                                "[ng-model='entirePerson.addresses.postAddresses.adminUnitId'] .form-group.ng-scope")
    POST_ADRESS_LEVEL_1 = (By.CSS_SELECTOR, ".row.form-group.ng-scope>div>label+div"
                "[ng-model='entirePerson.addresses.postAddresses.adminUnitId']>div:nth-child(1) span:nth-child(2) span")
    POST_ADRESS_LEVEL_2 = (By.CSS_SELECTOR, ".row.form-group.ng-scope>div>label+div"
                "[ng-model='entirePerson.addresses.postAddresses.adminUnitId']>div:nth-child(2) span:nth-child(2) span")
    POST_ADRESS_LEVEL_3 = (By.CSS_SELECTOR, ".row.form-group.ng-scope>div>label+div"
                "[ng-model='entirePerson.addresses.postAddresses.adminUnitId']>div:nth-child(3) span:nth-child(2) span")
    POST_ADRESS_LEVEL_4 = (By.CSS_SELECTOR, ".row.form-group.ng-scope>div>label+div"
                "[ng-model='entirePerson.addresses.postAddresses.adminUnitId']>div:nth-child(4) span:nth-child(2) span")
    POST_ADRESS_LEVEL_5 = (By.CSS_SELECTOR, ".row.form-group.ng-scope>div>label+div"
                "[ng-model='entirePerson.addresses.postAddresses.adminUnitId']>div:nth-child(5) span:nth-child(2) span")
    POST_ADRESS_LEVEL_6 = (By.CSS_SELECTOR, ".row.form-group.ng-scope>div>label+div"
                "[ng-model='entirePerson.addresses.postAddresses.adminUnitId']>div:nth-child(6) span:nth-child(2) span")
    POST_ADRESS_LEVEL_7 = (By.CSS_SELECTOR, ".row.form-group.ng-scope>div>label+div"
                "[ng-model='entirePerson.addresses.postAddresses.adminUnitId']>div:nth-child(7) span:nth-child(2) span")

    # Exact post addresses
    arr_titles_post_exact = ["POST_ZIPCODE", "POST_STREET_TYPE", "POST_STREET",
                            "POST_HOME", "POST_APARTMENT"]
    POST_ZIPCODE = (By.ID, "inputZipCodePost")
    POST_STREET_TYPE = (By.ID, "inputStreetTypePost")
    POST_STREET = (By.ID, "inputStreetPost")
    POST_HOME = (By.ID, "inputHousePost")
    POST_APARTMENT = (By.ID, "inputApartmentPost")

    # >>>>>>>>>>>>>>>>>>>>>>>>>>> Global information about person <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    @property
    def get_fio_ukranian(self):
        return self.driver.find_element(*self.FIO_PERSON_UKRANIAN)

    @property
    def get_fio_english(self):
        return self.driver.find_element(*self.FIO_PERSON_ENGLISH)

    def get_serial_person_record(self):
        text_with_colon = self.driver.find_element(*self.SERIAL_PERSONAL_RECORD).text.encode("cp1251")
        value_without_spaces = self.__get_text_splited_by_colon(text_with_colon)
        return value_without_spaces

    def get_number_person_record(self):
        text_with_colon = self.driver.find_element(*self.NUMBER_PERSONAL_RECORD).text.encode("cp1251")
        value_without_spaces = self.__get_text_splited_by_colon(text_with_colon)
        return value_without_spaces

    # >>>>>>>>>>>>>>>>>>>>>>>>>>> Main information about person <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    def get_dict_main_info_about_person(self):
        arr_values = [self.TYPE_OF_PERSON, self.DATE_OF_BIRTH, self.RESIDENT, self.SEX, self.MARITAL_STATUS,
                      self.MILITARY_SERVICE, self.CITIZENSHIP, self.INDEX_MATERIAL_RESPONSIBLE, self.HOSTEL]
        dict_main_info = {}
        count = 0
        for locator in arr_values:
            element_by_locator = self.driver.find_element(*locator)
            text_with_colon = element_by_locator.text
            value_without_spaces = self.__get_text_splited_by_colon(text_with_colon)
            if value_without_spaces != u'✘':
                value_without_spaces = value_without_spaces.encode("cp1251")
            dict_main_info[self.arr_titles_main[count]] = value_without_spaces
            count += 1
        return dict_main_info

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>> Place of birth <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    def get_dict_place_of_birth(self):
        arr_values = [self.PLACE_OF_BIRTH_LEVEL_1, self.PLACE_OF_BIRTH_LEVEL_2, self.PLACE_OF_BIRTH_LEVEL_3,
                      self.PLACE_OF_BIRTH_LEVEL_4, self.PLACE_OF_BIRTH_LEVEL_5, self.PLACE_OF_BIRTH_LEVEL_6,
                      self.PLACE_OF_BIRTH_LEVEL_7]
        dict_birth = {}
        count = 0
        for locator in arr_values:
            element_by_locator = self.driver.find_element(*locator).text.encode("cp1251")
            dict_birth[self.arr_titles_birth[count]] = element_by_locator
            count += 1
            if (count == self.get_count_elements_place_of_birth()):
                break
        return dict_birth

    def get_count_elements_place_of_birth(self):
        elements_place_of_birth = self.driver.find_elements(*self.FOR_COUNT_ELEMENTS_DATE_OF_BIRTH)
        return len(elements_place_of_birth)

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>> Address of registration <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    # Address of registration
    def get_dict_addres_of_registration(self):
        arr_values = [self.REGISTRATION_ADRESS_LEVEL_1, self.REGISTRATION_ADRESS_LEVEL_2, self.REGISTRATION_ADRESS_LEVEL_3,
                      self.REGISTRATION_ADRESS_LEVEL_4, self.REGISTRATION_ADRESS_LEVEL_5, self.REGISTRATION_ADRESS_LEVEL_6,
                      self.REGISTRATION_ADRESS_LEVEL_7]
        dict_registration = {}
        count = 0
        for locator in arr_values:
            element_by_locator = self.driver.find_element(*locator).text.encode("cp1251")
            dict_registration[self.arr_titles_registration[count]] = element_by_locator
            count += 1
            if (count == self.get_count_elements_place_of_birth()):
                break
        return dict_registration

    def get_count_elements_addres_of_registration(self):
        elements_addres_of_registration = self.driver.find_elements(*self.FOR_COUNT_ELEMENTS_ADDRES_OF_REGISTRATION)
        return len(elements_addres_of_registration)

    # Exact address
    def get_dict_exact_addres_of_registration(self):
        arr_values = [self.REGISTRATION_ZIPCODE, self.REGISTRATION_STREET_TYPE, self.REGISTRATION_STREET,
                      self.REGISTRATION_HOME, self.REGISTRATION_APARTMENT]
        dict_exact_registration = {}
        count = 0
        for locator in arr_values:
            element_by_locator = self.driver.find_element(*locator).text.encode("cp1251")
            element_without_spaces = element_by_locator.strip(' ')
            dict_exact_registration[self.arr_titles_exact_reg[count]] = element_without_spaces
            count += 1
        return dict_exact_registration

    # Post addres
    def get_dict_post_addres(self):
        arr_values = [self.POST_ADRESS_LEVEL_1, self.POST_ADRESS_LEVEL_2, self.POST_ADRESS_LEVEL_3,
                      self.POST_ADRESS_LEVEL_4, self.POST_ADRESS_LEVEL_5, self.POST_ADRESS_LEVEL_6,
                      self.POST_ADRESS_LEVEL_7]
        dict_post_registration = {}
        count = 0
        for locator in arr_values:
            element_by_locator = self.driver.find_element(*locator).text.encode("cp1251")
            dict_post_registration[self.arr_titles_post_addres[count]] = element_by_locator
            count += 1
            if (count == self.get_count_elements_post_addres()):
                break
        return dict_post_registration

    def get_count_elements_post_addres(self):
        elements_post_addres = self.driver.find_elements(*self.FOR_COUNT_ELEMENTS_POST_ADDRES)
        return len(elements_post_addres)

    # Exact address
    def get_dict_exact_post_addres(self):
        arr_values = [self.POST_ZIPCODE, self.POST_STREET_TYPE, self.POST_STREET,
                      self.POST_HOME, self.POST_APARTMENT]
        dict_exact_post = {}
        count = 0
        for locator in arr_values:
            element_by_locator = self.driver.find_element(*locator).text.encode("cp1251")
            element_without_spaces = element_by_locator.strip(' ')
            dict_exact_post[self.arr_titles_post_exact[count]] = element_without_spaces
            count += 1
        return dict_exact_post

    # Private methods (it uses only in this class)
    def __get_text_splited_by_colon(self, text_with_colon):
        split = text_with_colon.split(":")
        value_of_text = split[1]
        value_of_text_without_spaces = value_of_text.strip(' ')
        return value_of_text_without_spaces

