#!/usr/bin/env python3
#this file create a freq dict of text

import re
import os
import sys
import uu

text1 = 'aa, bb AA ccc bb,- d ffff'

def split_to_words(text):
    text = text.lower()
    text = text.strip()
    text = re.sub('\d', '', text)
    words = re.split('\W*', text)
    return words

def find_in_dict(word, fd):
    for i in range(len(fd)):
        if word == fd[i][0]:    
            return i
    return None

def add_word(word, fd):
    i = find_in_dict(word, fd)
    if find_in_dict(word, fd) is None:
        fd.append([word, 1])
    else:
        fd[i][1] +=1
    return fd

def create_dict(words):
    fd = []
    for word in words:
        find_in_dict(word, fd)
        add_word(word, fd)
    return fd

def sort(fd):
    return sorted(fd, key= lambda dict: dict[1], reverse=True)

if __name__ == '__main__':
    file = open (os.path.join('/home/maria/', sys.argv[1]))
    #uu.decode (file)
    text1 = file.read()
    words = split_to_words(text1)
    fd = create_dict (words)
    fd = sort(fd)
    print(fd)
