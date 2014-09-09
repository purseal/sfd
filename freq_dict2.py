#!/usr/bin/env python3
#this file create a freq dict of text

import re 

text1 = 'aa, bb AA ccc bb,- d'

def split_to_words(text):
    text = text.lower()
    text = text.strip()
    text = re.sub('\d', '', text)
    words = re.split('\W*', text)
    return words

if __name__ == '__main__':
    split_to_words(text1)  
