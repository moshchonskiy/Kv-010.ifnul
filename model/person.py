__author__ = 'odeortc'
import datetime

class Person(object):

    def __init__(self):
        self.person_type = ""
        self.surname_ukr = ""
        self.first_name_ukr = ""
        self.second_name_ukr = ""
        self.surname_eng = ""
        self.first_name_eng = ""
        self.birth_day = datetime.date(1, 1, 1)
        self.sex = ""
        self.marital_status = ""
        self.nationality = ""
        self.private_case_chars = ""
        self.private_case_number = 0
        self.is_outlander =	False
        self.reservist = False
        self.hostel_need = False
        self.burn_place = []
        self.registration_place = {"area": [], "index": 0, "type": "", "street": "", "house": 0, "apartment": 0, "is_addresses_match": True}
        self.post_registration_place = {"area": [], "index": 0, "type": "", "street": "", "house": 0, "apartment": 0}
        self.photo = ""
        self.mobile_phone1 = ""
        self.mobile_phone2 = ""
        self.home_phone = ""
        self.work_phone = ""
        self.email = ""
        self.skype = ""
        self.web_site = ""
        self.icq = 0
        self.documents = []

class Document(object):

    def __init__(self):
        self.category = ""
        self.document_name = ""
        self.document_case_char = ""
        self.document_case_number = ""
        self.day_of_issue = datetime.date(1, 1, 1)
        self.issued_by = ""
        self.average_rate = 0.0
        self.type_of_reward = ""
        self.document_is_original = False
        self.document_is_foreign = False


