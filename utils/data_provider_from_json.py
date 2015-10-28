# coding: utf8
import json
import os

__author__ = 'dmakstc'


class DataProviderJSON():
    def __init__(self, file_name):
        project_path = os.path.dirname(os.path.realpath(__file__))
        self.path = os.path.normpath(os.path.abspath(project_path) + "/../resources/" + file_name)
        self.json_data = self.__get_json_object()

    def __get_json_object(self):
        with open(self.path) as json_data:
            d = json.load(json_data)
        json_data.close()
        return d

    def get_value_by_ij(self, i, j):
        return self.json_data[i][j]

    def get_value_by_key(self, key):
        return self.json_data[key]

    def get_dict_value(self):
        return self.json_data
