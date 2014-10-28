#!/usr/bin/env python3
#this file create a freq dict of text

import re
import os
import sys
import uu
import operator

class FrequencyDict:

    fd =[] 

    def split_to_words(self, text):
        text = text.lower()
        text = text.strip()
        text = re.sub('\d', '', text)
        words = re.split('\W*', text)
        return words

    def find_in_dict(self, word):
        pass

    def add_word(self, word, fd):
        pass

    def create_dict(self, words):
        for word in words:
            self.add_word(word)
        return self.fd 

    def sort(self): 
        pass

class FreqDictList(FrequencyDict):
    ''' Implementation of creating a frequency dict with lists. '''

    def find_in_dict(self, word):
        for i in range(len(self.fd)):
            if word == self.fd[i][0]:
                return i
        return 0

    def add_word(self, word):
        i = self.find_in_dict(word)
        if self.find_in_dict(word) is 0:
            self.fd.append([word, 1])
        else:
            self.fd[i][1] +=1
        return self.fd
 
    def sort(self):
        self.fd = sorted(self.fd, key= lambda dict: dict[1], reverse=True)
        return self.fd


class FreqDictDict(FrequencyDict):
    ''' Implementation of creating a frequency dict with dictionaries. '''

    fd ={} 

    def find_in_dict(self, word):
        if word in self.fd:    
            return -1
        return 0

    def add_word(self, word):
        if self.find_in_dict(word) is 0:
            self.fd[word] = 1
        else:
            self.fd[word] +=1
        return self.fd

    def sort(self):
        sorted(self.fd.items(), key=operator.itemgetter(1), reverse=True)
        return [[key, item] for key, item in self.fd.items()]


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
