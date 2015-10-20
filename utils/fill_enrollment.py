# -*- coding: utf-8 -*-
import os
import json
import datetime
from model.enrollment import AddEnrollment, TableEnrollment
from datetime import date

__author__ = 'stako'


class FillEnrollment(object):

    def file_path(self, file_name):
        """
        This method makes absolute path to json file.
        :param file_name: is name of json file.
        :return: path.
        """
        project_path = os.path.dirname(os.path.realpath(__file__))
        path = os.path.normpath(os.path.abspath(project_path) + "/../resources/" + file_name)
        return path

    def parseJson(self, file_name, name_of_dict):
        """
        This method parses json file and creates dictionary.
        :param file_name: is name of json file.
        :param name_of_dict: is name one of the dictionaries in json file.
        :return: dictionary with data from json file.
        """
        fl = open(self.file_path(file_name), 'r')
        st = fl.read()
        fl.close()
        get_dict_from_json = json.loads(st)
        return get_dict_from_json[name_of_dict]

    def create_enrollment_from_json(self, file_name, name_of_dict):
        """
        This method creates the instance of AddEnrollment with data from json file.
        :param file_name: is name of json file.
        :param name_of_dict: is name one of the dictionaries in json file.
        :return: instance of AddEnrollment.
        """
        enrollment = AddEnrollment()
        enrollment_json = self.parseJson(file_name, name_of_dict)
        enrollment.person_name = enrollment_json["person_name"].encode('utf8')
        enrollment.series_of_statements = enrollment_json["series_of_statements"]
        enrollment.number_statements = enrollment_json["number_statements"]
        enrollment.radiobutton_higher_education = enrollment_json["radiobutton_higher_education"].encode('utf8')
        enrollment.radiobutton_evaluation_of_the_interview = \
            enrollment_json["radiobutton_evaluation_of_the_interview"].encode('utf8')
        enrollment.checkbox_is_state = enrollment_json["checkbox_is_state"]
        enrollment.checkbox_is_contract = enrollment_json["checkbox_is_contract"]
        enrollment.checkbox_is_privilege = enrollment_json["checkbox_is_privilege"]
        enrollment.checkbox_is_hostel = enrollment_json["checkbox_is_hostel"]
        enrollment.checkbox_document_is_original = enrollment_json["checkbox_document_is_original"]
        enrollment.offers = enrollment_json["offers"].encode('utf8')
        enrollment.form_of_education = enrollment_json["form_of_education"].encode('utf8')
        enrollment.document = enrollment_json["document"].encode('utf8')
        enrollment.grading_scale = enrollment_json["grading_scale"].encode('utf8')
        enrollment.total_score = enrollment_json["total_score"]
        enrollment.priority = enrollment_json["priority"]
        enrollment.structural_unit = enrollment_json["structural_unit"].encode('utf8')
        enrollment.type_of_entry = enrollment_json["type_of_entry"].encode('utf8')
        enrollment.detailing_start = enrollment_json["detailing_start"].encode('utf8')
        enrollment.date_of_entry = datetime.date(enrollment_json["date_of_entry"]["year"],
                                                 enrollment_json["date_of_entry"]["month"],
                                                 enrollment_json["date_of_entry"]["day"])
        enrollment.date_closing = datetime.date(enrollment_json["date_closing"]["year"],
                                                enrollment_json["date_closing"]["month"],
                                                enrollment_json["date_closing"]["day"])
        return enrollment

    def get_enrollment_from_table(self, dict_values_of_enrollment):
        """
        This methods creates the instance of TableEnrollment with data from dictionary.
        :param dict_values_of_enrollment: is dictionary for instance create.
        :return: instance of TableEnrollment.
        """
        enrollment = TableEnrollment()
        enrollment.budget = dict_values_of_enrollment["Бюджет".decode('utf8')]
        enrollment.contract = dict_values_of_enrollment["Контракт".decode('utf8')]
        enrollment.unit = dict_values_of_enrollment["Підрозділ".decode('utf8')].encode('utf8')
        enrollment.total_score = dict_values_of_enrollment["Загальний бал".decode('utf8')]
        enrollment.is_privilege = dict_values_of_enrollment["Наявність пільг".decode('utf8')]
        enrollment.doc_series = dict_values_of_enrollment["Серія док.".decode('utf8')]
        enrollment.doc_number = dict_values_of_enrollment["Номер док.".decode('utf8')]
        enrollment.is_hostel = dict_values_of_enrollment["Потреб. гуртож".decode('utf8')]
        enrollment.type_of_entry = dict_values_of_enrollment["Тип поступлення".decode('utf8')]
        enrollment.date_of_create = dict_values_of_enrollment["Дата створення".decode('utf8')]
        enrollment.date_from = dict_values_of_enrollment["Дата дії (з)".decode('utf8')]
        enrollment.date_till = dict_values_of_enrollment["Дата дії (по)".decode('utf8')]
        return enrollment

    def table_enrollment_from_json(self, name_of_json, name_of_dict):
        """
        This methods creates the instance of TableEnrollment with data from json file.
        :param name_of_json: is name of json file.
        :param name_of_dict: is name one of the dictionaries in json file.
        :return: instance of TableEnrollment.
        """
        enrollment = self.create_enrollment_from_json(name_of_json, name_of_dict)
        table_enrollment = TableEnrollment()
        table_enrollment.budget = enrollment.checkbox_is_state
        table_enrollment.contract = enrollment.checkbox_is_contract
        table_enrollment.unit = enrollment.structural_unit
        table_enrollment.total_score = enrollment.total_score
        table_enrollment.is_privilege = enrollment.checkbox_is_privilege
        table_enrollment.doc_series = enrollment.series_of_statements
        table_enrollment.doc_number = enrollment.number_statements
        table_enrollment.is_hostel = enrollment.checkbox_is_hostel
        table_enrollment.type_of_entry = enrollment.detailing_start.decode('utf8')
        table_enrollment.date_of_create = date.today()
        table_enrollment.date_from = enrollment.date_of_entry
        table_enrollment.date_till = enrollment.date_closing
        return table_enrollment
