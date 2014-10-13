#!/usr/bin/env python3

import freq_dict
import unittest

class TestFreqDict(unittest.TestCase):

    def setUp(self):
        pass

    def check_split(self):
        text = ['aa bb', 'aa - bb', 'aa,- bb', 'aa bb cc ']
        list_of_words = [['aa','bb'], ['aa','bb'], ['aa','bb'], ['aa','bb','cc']]
        for (t,l) in zip(text, list_of_words):
            self.assertTrue(dictionary.split_to_words(t) == l, 'split to words test: [false]')

    def check_find_dict(self):
        word = 'dd'
        fd1 = {'aa': 2, 'dd': 1, 'd': 4}
        fd2 = {'aa': 2, 'cc': 1, 'd': 4}
        self.assertTrue(dictionary.find_in_dict(word, fd1) == True, 'find word in freq dict test1: [false]')
        self.assertTrue(dictionary.find_in_dict(word, fd2) == None, 'find word in freq dict test2: [false]')

    def check_add_word(self):
        word = 'dd'
        fd = [{'aa': 1, 'dd': 2}, {'aa': 1, 'bb': 3}]
        new_fd = [{'aa': 1, 'dd': 3}, {'aa': 1, 'bb': 3, 'dd': 1}]
        for (f,n) in zip(fd, new_fd):
            self.assertTrue(dictionary.add_word(word, f) == n, 'add word in freq dict test1: [false]')

    def check_create_dict(self):
        words = ['aa', 'bb', 'cc', 'aa', 'bb', 'bb']
        fd = {'aa': 2, 'bb': 3, 'cc': 1}
        self.assertTrue(dictionary.create_dict(words) == fd, 'create dict test: [false]')

    def check_sort(self):
        fd = {'ff': 2, 'bb': 3, 'cc': 1, 'aa': 2}
        sort_fd = {'bb': 3, 'ff': 2, 'aa': 2, 'cc': 1}
        self.assertTrue(dictionary.sort(fd) == sort_fd, 'sort test: [false]')

    def test_list_impl(self):


    def test_dict_impl(self):


if __name__ == '__main__':
    dictionary = freq_dict.FrequencyDict_DictImpl() 
    unittest.main()
