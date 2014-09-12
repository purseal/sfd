#!/usr/bin/env python3
#this file create a freq dict of text

import re

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

if __name__ == '__main__':
    word = split_to_words(text1)
