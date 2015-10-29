# coding=utf-8
from datetime import date

__author__ = 'stako'

class Enrollment():
    def __init__(self):
        self.person_name = ""
        self.series_of_statements = ""
        self.number_statements = 0
        self.radiobutton_higher_education = ""
        self.radiobutton_evaluation_of_the_interview = ""
        self.checkbox_is_state = False
        self.checkbox_is_contract = False
        self.checkbox_is_privilege = False
        self.checkbox_is_hostel = False
        self.checkbox_document_is_original = False
        self.offers = ""
        self.form_of_education = ""
        self.document = ""
        self.grading_scale = ""
        self.total_score = 0
        self.priority = 1
        self.structural_unit = ""
        self.type_of_entry = ""
        self.detailing_start = ""
        self.date_of_entry = date(1, 1, 1)
        self.date_closing = date(1, 1, 1)

class AddEnrollment(object):
    def __init__(self):
        self.person_name = ""
        self.series_of_statements = ""
        self.number_statements = ""
        self.radiobutton_higher_education = ""
        self.radiobutton_evaluation_of_the_interview = ""
        self.checkbox_is_state = ""
        self.checkbox_is_contract = ""
        self.checkbox_is_privilege = ""
        self.checkbox_is_hostel = ""
        self.checkbox_document_is_original = ""
        self.offers = ""
        self.form_of_education = ""
        self.document = ""
        self.grading_scale = ""
        self.total_score = ""
        self.priority = ""
        self.structural_unit = ""
        self.type_of_entry = ""
        self.detailing_start = ""
        self.date_of_entry = date(1, 1, 1)
        self.date_closing = date(1, 1, 1)

    def get_day_of_entry_str_for_view(self):
        return self.date_of_entry.strftime("%Y-%m-%d")

    def get_text_hostel_for_view(self, boolean):
        if(boolean == "True"):
            return u'потреб. гуртож.'
        else:
            return u'не потреб. гуртож.'

    def get_text_privilege_for_view(self, boolean):
        if(boolean == "True"):
            return u'є пільги'
        else:
            return u'немає пільг'


class TableEnrollment(object):
    def __init__(self):
        self.number = ""
        self.person_id = ""
        self.enrollment_id = ""
        self.budget = ""
        self.contract = ""
        self.unit = ""
        self.person_document = ""
        self.total_score = ""
        self.is_privilege = ""
        self.doc_series = ""
        self.doc_number = ""
        self.is_hostel = ""
        self.type_of_entry = ""
        self.date_of_create = date(1, 1, 1)
        self.date_from = date(1, 1, 1)
        self.date_till = date(1, 1, 1)
        self.hierarchy = ""

    def __eq__(self, other):
        return self.budget == other.budget and \
               self.contract == other.contract and \
               self.unit == other.unit and \
               self.total_score == other.total_score and \
               self.doc_series == other.doc_series and \
               self.doc_number == other.doc_number and \
               self.is_hostel == other.is_hostel and \
               self.is_privilege == other.is_privilege and \
               self.type_of_entry == other.type_of_entry and \
               self.date_of_create.__eq__(other.date_of_create) and \
               self.date_from.__eq__(other.date_from) and \
               self.date_till.__eq__(other.date_till)
