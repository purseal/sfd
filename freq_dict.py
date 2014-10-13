#!/usr/bin/env python3
#this file create a freq dict of text

import re
import os
import sys
import uu
import operator

class FrequencyDict:

    def split_to_words(self, text):
        text = text.lower()
        text = text.strip()
        text = re.sub('\d', '', text)
        words = re.split('\W*', text)
        return words
   

class FrequencyDict_ListImpl(FrequencyDict):
'''Implementation of creating a frequency dict with lists'''

    fd =[] 

    def find_in_dict(self ,word, fd):
        for i in range(len(fd)):
            if word == fd[i][0]:
                return i
         return None

    def add_word(self, word, fd):
        i = find_in_dict(word, fd)
        if find_in_dict(word, fd) is None:
            fd.append([word, 1])
        else:
            fd[i][1] +=1
        return fd

    def create_dict(self, words):
        for word in words:
            self.find_in_dict(word, self.fd)
            self.add_word(word, self.fd)
        return self.fd

    def sort(self, fd):
        fd = sorted(fd, key= lambda dict: dict[1], reverse=True)
        return fd


class FrequencyDict_DictImpl(FrequencyDict):
'''Implementation of creating a frequency dict with dictionaries'''

    fd ={} 

    def find_in_dict(self ,word, fd):
        if word in fd:    
            return True
        return None

    def add_word(self, word, fd):
        if self.find_in_dict(word, fd) is None:
            fd[word] = 1
        else:
            fd[word] +=1
        return fd

    def create_dict(self, words):
        for word in words:
            self.find_in_dict(word, self.fd)
            self.add_word(word, self.fd)
        return self.fd

    def sort(self, fd):
        sorted(fd.items(), key=operator.itemgetter(1), reverse=True)
        return fd


if __name__ == '__main__':
    sfd = FrequencyDict_DictImpl()
    input_file_name = sys.argv[1]
    output_file_name = sys.argv[2]
    with open(input_file_name) as text_file:
        string_of_text = text_file.read()
        words = sfd.split_to_words(string_of_text)
        fd = sfd.create_dict (words)
        fd = sfd.sort(fd)
    with open(output_file_name, 'w+') as fd_file:
        for count, word in fd:
            output = '{} {}\n'.format(word, count)
            fd_file.write(output)
