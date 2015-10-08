# coding: utf8
import json

__author__ = 'dmakstc'


class DataProviderJSON():
    def __init__(self, file_path):
        self.path = file_path
        self.json_data = self.__get_json_object()

    def __get_json_object(self):
        with open(self.path) as json_data:
            d = json.load(json_data)
        json_data.close()
        return d

    def get_value_by_ij(self, i, j):
        return self.json_data[i][j]
