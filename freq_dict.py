#!/usr/bin/env python3
#this file create a freq dict of text

import re
import os
import sys
import uu
import operator

class FrequencyDict:

    fd =[]

    def create_dict(self, words):
        for word in words:
            self.add_word(word)
        return self.fd

    @staticmethod
    def split_to_words(text):
        text = text.lower()
        text = text.strip()
        text = re.sub('\d', '', text)
        words = re.split('\W*', text)
        return words

    def find_in_dict(self, word):
        raise NotImplementedError

    def add_word(self, word, fd):
        raise NotImplementedError

    def create_dict(self, words):
        raise NotImplementedError

    def sort(self):
        raise NotImplementedError

class FreqDictList(FrequencyDict):
    ''' Implementation of frequency dictionary's creating with lists. '''
    def create_dict(self, words):
        for word in words:
            self.add_word(word)
        return self.fd
    def find_in_dict(self, word):
        for i in range(len(self.fd)):
            if word == self.fd[i][0]:
                return i
        return None

    def add_word(self, word):
        i = self.find_in_dict(word)
        if i is None:
            self.fd.append([word, 1])
        else:
            self.fd[i][1] +=1
        return self.fd

    def sort(self):
        self.fd = sorted(self.fd, key=lambda dict: dict[1], reverse=True)
        return self.fd


class FreqDictDict(FrequencyDict):
    ''' Implementatio of frequency dictionary's creating with dictionaries. '''

    fd ={}
    def create_dict(self, words):
        for word in words:
            self.add_word(word)
        return self.fd

    def find_in_dict(self, word):
        if word in self.fd:
            return -1
        return None

    def add_word(self, word):
        if self.find_in_dict(word) is None:
            self.fd[word] = 1
        else:
            self.fd[word] +=1
        return self.fd

    def sort(self):
        sort_list_of_tuples = sorted(self.fd.items(), key=operator.itemgetter(1), reverse=True)
        return [[key, item] for key, item in sort_list_of_tuples]


if __name__ == '__main__':
    sfd = FreqDictList()
    input_file_name = sys.argv[1]
    output_file_name = sys.argv[2]
    with open(input_file_name) as text_file:
        string_of_text = text_file.read()
        words = sfd.split_to_words(string_of_text)
        fd = sfd.create_dict (words)
        fd = sfd.sort()
    with open(output_file_name, 'w+') as fd_file:
        for count, word in fd:
            output = '{} {}\n'.format(word, count)
            fd_file.write(output)
