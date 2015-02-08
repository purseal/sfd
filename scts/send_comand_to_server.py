#!/usr/bin/env python3
''' This program sends a comand to the server
    and transform its output in a readable view.
'''

import re
import os

class DataGetter:
    ''' Abstract class for any data downloader. '''

    def get_data(self, string):
        pass

    def parse_data(self, data):
        pass

class SshDataGetter(DataGetter):
    ''' Implementationt of DataGetter. '''

    def __init__(self):
        self.comand = ''
        self.username = ''
        self.ip = ''
        self.password = ''

    def split_to_values(self, given_string):
        ''' Method splits a string to list of values. '''
        given_string = given_string.strip()
        comand_begin = given_string.find("'")
        comand_end = given_string.find("'", comand_begin + 1)
        string = given_string[:comand_begin - 1] + given_string[comand_end + 1:]
        words = string.split(' ')
        for word in words:
            if word == "":
                words.remove(word)
        words.append(given_string[comand_begin + 1:comand_end])
        return words

    def get_values(self, string):
        ''' Method assigns data to specified fields. '''
        list_of_values = self.split_to_values(string)
        self.username = list_of_values[2]
        self.ip = list_of_values[3]
        self.password = list_of_values[4]
        self.comand = list_of_values[5]

    def get_data(self, address):
        pass
