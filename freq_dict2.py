#!/usr/bin/env python3
#this file create a freq dict of text

import re 

text1 = 'aa, bb AA ccc bb,- d'

def split_to_words(text):
    text = text.lower()
    text = text.strip()
    text = re.sub('\d', '', text)
    words = re.split('\W*', text)
    return word
    
    def find_in_dict(words):
    fd = []
    i = 0
    for word in words:
        i +=1
        if word == fd[i][0]:    
            fd[i][1] +=1
            print ('case is true')
        else:
            fd.append([word, 1])
            print ([word, 1])
    return fd


if __name__ == '__main__':
    split_to_words(text1)  
