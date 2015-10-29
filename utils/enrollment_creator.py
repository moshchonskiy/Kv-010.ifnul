from model.enrollment import Enrollment
from utils.data_provider_from_json import DataProviderJSON
from datetime import date

__author__ = 'acidroed'

class EnrollmentCreator():

    __enrollment = Enrollment()

    def __init__(self, file_name):
        dict = DataProviderJSON(file_name).get_dict_value()
        print dict
        enroll_dict = dict["enrollment"]
        print enroll_dict
        self.__enrollment.person_name = enroll_dict["person_name"]
        self.__enrollment.series_of_statements = enroll_dict["series_of_statements"]
        self.__enrollment.number_statements = enroll_dict["number_statements"]
        self.__enrollment.radiobutton_higher_education = enroll_dict["radiobutton_higher_education"]
        self.__enrollment.radiobutton_evaluation_of_the_interview = enroll_dict["radiobutton_evaluation_of_the_interview"]
        self.__enrollment.checkbox_is_state = enroll_dict["checkbox_is_state"]
        self.__enrollment.checkbox_is_contract = enroll_dict["checkbox_is_contract"]
        self.__enrollment.checkbox_is_privilege = enroll_dict["checkbox_is_privilege"]
        self.__enrollment.checkbox_is_hostel = enroll_dict["checkbox_is_hostel"]
        self.__enrollment.checkbox_document_is_original = enroll_dict["checkbox_document_is_original"]
        self.__enrollment.offers = enroll_dict["offers"]
        self.__enrollment.form_of_education = enroll_dict["form_of_education"]
        self.__enrollment.document = enroll_dict["document"]
        self.__enrollment.grading_scale = enroll_dict["grading_scale"]
        self.__enrollment.total_score = enroll_dict["total_score"]
        self.__enrollment.priority = enroll_dict["priority"]
        self.__enrollment.structural_unit = enroll_dict["structural_unit"]
        self.__enrollment.type_of_entry = enroll_dict["type_of_entry"]
        self.__enrollment.detailing_start = enroll_dict["detailing_start"]
        self.__enrollment.date_of_entry = date(enroll_dict["date_of_entry"]["year"], enroll_dict["date_of_entry"]["month"], enroll_dict["date_of_entry"]["day"])
        self.__enrollment.date_closing = date(enroll_dict["date_closing"]["year"], enroll_dict["date_closing"]["month"], enroll_dict["date_closing"]["day"])

    def get_enrollment(self):
        return self.__enrollment


