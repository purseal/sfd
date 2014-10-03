#!/usr/bin/env python3
#this file create a freq dict of text

import re
import os
import sys
import uu

class dict():

    def split_to_words(self, text):
        text = text.lower()
        text = text.strip()
        text = re.sub('\d', '', text)
        words = re.split('\W*', text)
        return words

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
        fd ={} 
        for word in words:
            self.find_in_dict(word, fd)
            self.add_word(word, fd)
        return fd

    def sort(self, fd):
        sorted(fd.values(), reverse=True)
        return fd

if __name__ == '__main__':
    sfd = dict()
    with open(sys.argv[1]) as text_file:
        string_of_text = text_file.read()
        words = sfd.split_to_words(string_of_text)
        fd = sfd.create_dict (words)
        fd = sfd.sort(fd)
        with open(sys.argv[2], 'w+') as fd_file:
            for item in fd:
                fd_file.write(str(item))
