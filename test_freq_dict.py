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
            self.assertTrue(self.dictionary.split_to_words(t) == l, 'split to words test: [false]')

    def check_find_dict(self):
        word = 'dd'
        list_fd1 = [['aa', 2], ['dd', 1], ['d', 4]]
        list_fd2 = [['aa', 2], ['cc', 1], ['d', 4]]
        dict_fd1 = {'aa': 2, 'dd': 1, 'd': 4}
        dict_fd2 = {'aa': 2, 'cc': 1, 'd': 4}
        if isinstance(self.dictionary, freq_dict.FreqDictList):
            self.dictionary.fd = list_fd1
            self.assertTrue(self.dictionary.find_in_dict(word) == 1, 'find word in freq dict test1 list: [false]')
            self.dictionary.fd = list_fd2
            self.assertTrue(self.dictionary.find_in_dict(word) == 0, 'find word in freq dict test2 list: [false]')
        else:
            self.dictionary.fd = dict_fd1
            self.assertTrue(self.dictionary.find_in_dict(word) == -1, 'find word in freq dict test1 dict: [false]')
            self.dictionary.fd = dict_fd2
            self.assertTrue(self.dictionary.find_in_dict(word) == 0, 'find word in freq dict test2 dict: [false]')

    def check_add_word(self):
        word = 'dd'
        list_fd = [[['aa', 1], ['dd', 2]], [['aa', 1], ['bb', 3]]]
        list_new_fd = [[['aa', 1], ['dd', 3]], [['aa', 1], ['bb', 3], ['dd', 1]]]
        dict_fd = [{'aa': 1, 'dd': 2}, {'aa': 1, 'bb': 3}]
        new_fd = [{'aa': 1, 'dd': 3}, {'aa': 1, 'bb': 3, 'dd': 1}]
        if isinstance(self.dictionary, freq_dict.FreqDictList):
            for (f,n) in zip(list_fd, list_new_fd):
                self.dictionary.fd = f
                self.assertTrue(self.dictionary.add_word(word) == n, 'add word in freq dict test1 list: [false]')
        else:
            for (f,n) in zip(dict_fd, list_new_fd):
                self.dictionary.fd = f
                self.assertTrue(self.dictionary.add_word(word) == n, 'add word in freq dict test1 dict: [false]')

    def check_create_dict(self):
        words = ['aa', 'bb', 'cc', 'aa', 'bb', 'bb']
        list_fd = [['aa', 2], ['bb', 3], ['cc', 1]]
        dict_fd = {'aa': 2, 'bb': 3, 'cc': 1} 
        if isinstance(self.dictionary, freq_dict.FreqDictList):
            self.dictionary.fd = []
            self.assertTrue(self.dictionary.create_dict(words) == list_fd, 'create dict test: [false]')
        else:
            self.dictionary.fd = {}
            self.assertTrue(self.dictionary.create_dict(words) == dict_fd, 'create dict test: [false]')

    def check_sort(self):
        list_fd = [['aa', 2], ['bb', 3], ['cc', 1]]
        dict_fd = {'aa': 2, 'bb': 3, 'cc': 1}
        sort_fd = [['bb', 3], ['aa', 2], ['cc', 2]]
        if isinstance(self.dictionary, freq_dict.FreqDictList):
            self.dictionary.fd = list_fd
            self.assertTrue(self.dictionary.sort() == sort_fd, 'sort test: [false]')
        else: 
            self.dictionary.fd = dict_fd
            self.assertTrue(self.dictionary.sort() == sort_fd, 'sort test: [false]')

    def check_realisation(self, chosen_implementation):
        self.dictionary = chosen_implementation
        self.check_split()
        self.check_find_dict()
        self.check_add_word()
        self.check_create_dict()
        self.check_sort()      

    def test_list_impl(self):
        self.check_realisation(freq_dict.FreqDictList)

    def test_dict_impl(self):
        self.check_realisation(freq_dict.FreqDictDict)

if __name__ == '__main__':
    unittest.main()
