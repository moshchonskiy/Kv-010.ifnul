# coding=utf-8
from selenium.webdriver.common.by import By
from pages.persons.view.person_main_view_page import PersonMainViewPage

__author__ = 'Vadym'

class PersonCurrentViewPage(PersonMainViewPage):

    # >>>>>>>>>>>>>>>>>>>>>>>>>>> Global locators for information about person <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    FIO_PERSON_UKRANIAN = (By.XPATH, "//h2[@class='text-primary ng-binding']")
    FIO_PERSON_ENGLISH = (By.XPATH, "//h4[@class='ng-binding']")
    SERIAL_PERSONAL_RECORD = (By.XPATH, "//p[contains(.,'Серія')]")
    NUMBER_PERSONAL_RECORD = (By.XPATH, "//p[contains(.,'Номер')]")

    # >>>>>>>>>>>>>>>>>>>>>>>>>>> Main locators for information about person <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
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
    FOR_COUNT_ELEMENTS_DATE_OF_BIRTH = (By.CSS_SELECTOR, ".form-group.col-md-10>label+div .form-group.ng-scope")

    # >>>>>>>>>>>>>>>>>>>>>>>>>>> Addreses <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    # Address of registration
    FOR_COUNT_ELEMENTS_ADDRES_OF_REGISTRATION = (By.CSS_SELECTOR, ".row.form-group.ng-scope>div>label+div"
                                    "[ng-model='entirePerson.addresses.regAddresses.adminUnitId'] .form-group.ng-scope")
    # Exact addresses
    REGISTRATION_ZIPCODE = (By.ID, "inputZipCodeReg")
    REGISTRATION_STREET_TYPE = (By.ID, "inputStreetTypeReg")
    REGISTRATION_STREET = (By.ID, "inputStreetReg")
    REGISTRATION_HOME = (By.ID, "inputHouseReg")
    REGISTRATION_APARTMENT = (By.ID, "inputApartmentReg")
    # Post addres
    FOR_COUNT_ELEMENTS_POST_ADDRES = (By.CSS_SELECTOR, ".row.form-group.ng-scope>div>label+div"
                                "[ng-model='entirePerson.addresses.postAddresses.adminUnitId'] .form-group.ng-scope")
    # Exact post addresses
    POST_ZIPCODE = (By.ID, "inputZipCodePost")
    POST_STREET_TYPE = (By.ID, "inputStreetTypePost")
    POST_STREET = (By.ID, "inputStreetPost")
    POST_HOME = (By.ID, "inputHousePost")
    POST_APARTMENT = (By.ID, "inputApartmentPost")

    # >>>>>>>>>>>>>>>>>>>>>>>>>>> Global information about person <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    def get_fio_ukranian(self):
        return self.driver.find_element(*self.FIO_PERSON_UKRANIAN)

    def get_fio_english(self):
        return self.driver.find_element(*self.FIO_PERSON_ENGLISH)

    def get_serial_person_record(self):
        text_with_colon = self.driver.find_element(*self.SERIAL_PERSONAL_RECORD).text
        value_without_spaces = self.__get_text_splited_by_colon(text_with_colon)
        return value_without_spaces

    def get_number_person_record(self):
        text_with_colon = self.driver.find_element(*self.NUMBER_PERSONAL_RECORD).text
        value_without_spaces = self.__get_text_splited_by_colon(text_with_colon)
        return value_without_spaces

    # >>>>>>>>>>>>>>>>>>>>>>>>>>> Main information about person <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    def get_arr_main_info_about_person(self):
        result = []
        # add locators to the array
        result.extend((self.TYPE_OF_PERSON, self.DATE_OF_BIRTH, self.RESIDENT, self.SEX, self.MARITAL_STATUS,
                       self.MILITARY_SERVICE, self.CITIZENSHIP, self.INDEX_MATERIAL_RESPONSIBLE, self.HOSTEL))
        for index, locator in enumerate(result):
            element_by_locator = self.driver.find_element(*locator)
            # возможно стоит проверить, не пустое ли тут значение
            text_with_colon = element_by_locator.text
            value_without_spaces = self.__get_text_splited_by_colon(text_with_colon)
            result[index] = value_without_spaces #replace locator by value found by this locator
        return result

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>> Place of birth <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    def get_arr_place_of_birth(self):
        result = []
        # add locators to the array
        count_of_elements = self.get_count_elements_place_of_birth()
        for x in range(count_of_elements):
            result.append(self.__get_locator_date_of_birth_by_level(x))

        for index, locator in enumerate(result):
            element_by_locator = self.driver.find_element(*locator).text
            # возможно стоит проверить, не пустое ли тут значение
            result[index] = element_by_locator #replace locator by value found by this locator
        return result

    def get_count_elements_place_of_birth(self):
        elements_place_of_birth = self.driver.find_elements(*self.FOR_COUNT_ELEMENTS_DATE_OF_BIRTH)
        return len(elements_place_of_birth)

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>> Address of registration <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    # Address of registration
    def get_arr_addres_of_registration(self):
        result = []
        # add locators to the array
        count_of_elements = self.get_count_elements_addres_of_registration()
        for x in range(count_of_elements):
            result.append(self.__get_locator_addres_of_registration_by_level(x))

        for index, locator in enumerate(result):
            element_by_locator = self.driver.find_element(*locator).text
            # возможно стоит проверить, не пустое ли тут значение
            result[index] = element_by_locator #replace locator by value found by this locator
        return result

    def get_count_elements_addres_of_registration(self):
        elements_addres_of_registration = self.driver.find_elements(*self.FOR_COUNT_ELEMENTS_ADDRES_OF_REGISTRATION)
        return len(elements_addres_of_registration)

    # Exact address
    def get_arr_exact_addres_of_registration(self):
        result = []
        # add locators to the array
        result.extend((self.REGISTRATION_ZIPCODE, self.REGISTRATION_STREET_TYPE, self.REGISTRATION_STREET,
                      self.REGISTRATION_HOME, self.REGISTRATION_APARTMENT))
        for index, locator in enumerate(result):
            element_by_locator = self.driver.find_element(*locator).text
            # возможно стоит проверить, не пустое ли тут значение
            result[index] = element_by_locator #replace locator by value found by this locator
        return result

    # Post addres
    def get_arr_post_addres(self):
        result = []
        # add locators to the array
        count_of_elements = self.get_count_elements_addres_of_registration()
        for x in range(count_of_elements):
            result.append(self.__get_post_addres_of_registration_by_level(x))

        for index, locator in enumerate(result):
            element_by_locator = self.driver.find_element(*locator).text
            # возможно стоит проверить, не пустое ли тут значение
            result[index] = element_by_locator #replace locator by value found by this locator
        return result

    def get_count_elements_post_addres(self):
        elements_post_addres = self.driver.find_elements(*self.FOR_COUNT_ELEMENTS_POST_ADDRES)
        return len(elements_post_addres)

    # Exact post address
    def get_arr_exact_post_addres(self):
        result = []
        # add locators to the array
        result.extend((self.POST_ZIPCODE, self.POST_STREET_TYPE, self.POST_STREET,
                      self.POST_HOME, self.POST_APARTMENT))
        for index, locator in enumerate(result):
            element_by_locator = self.driver.find_element(*locator).text
            # возможно стоит проверить, не пустое ли тут значение
            result[index] = element_by_locator #replace locator by value found by this locator
        return result

    # Private methods (it uses only in this class)
    def __get_locator_date_of_birth_by_level(self, level_int):
        return (By.CSS_SELECTOR, ".form-group.col-md-10>label+div>div:nth-child"
                                 "(" + str(level_int + 1) + ") span:nth-child(2) span")

    def __get_locator_addres_of_registration_by_level(self, level_int):
        return (By.CSS_SELECTOR, ".row.form-group.ng-scope>div>label+div[ng-model='entirePerson.addresses"
                        ".regAddresses.adminUnitId']>div:nth-child(" + str(level_int + 1) + ") span:nth-child(2) span")

    def __get_post_addres_of_registration_by_level(self, level_int):
        return (By.CSS_SELECTOR, ".row.form-group.ng-scope>div>label+div[ng-model='entirePerson.addresses"
                        ".postAddresses.adminUnitId']>div:nth-child(" + str(level_int + 1) + ") span:nth-child(2) span")

    # split value by ':' like 'Стать: Чоловіча' we must get just dynamic properties 'Чоловіча'
    def __get_text_splited_by_colon(self, text_with_colon):
        split = text_with_colon.split(":")
        value_of_text = split[1]
        value_of_text_without_spaces = value_of_text.strip(' ')
        return value_of_text_without_spaces

