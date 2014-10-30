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
            self.assertTrue(self.dictionary.find_in_dict(word) is None, 'find word in freq dict test2 list: [false]')
        else:
            self.dictionary.fd = dict_fd1
            self.assertTrue(self.dictionary.find_in_dict(word) == -1, 'find word in freq dict test1 dict: [false]')
            self.dictionary.fd = dict_fd2
            self.assertTrue(self.dictionary.find_in_dict(word) is None, 'find word in freq dict test2 dict: [false]')

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
            for (f,n) in zip(dict_fd, new_fd):
                self.dictionary.fd = f
                res = self.dictionary.add_word(word)
                self.assertTrue(res == n, 'add word in freq dict test1 dict: [false] {} {}'.format(res, n))

    def check_create_dict(self):
        words = ['aa', 'bb', 'cc', 'aa', 'bb', 'bb']
        list_fd = [['aa', 2], ['bb', 3], ['cc', 1]]
        dict_fd = {'aa': 2, 'bb': 3, 'cc': 1}
        print('x1: ', type(self.dictionary))
        # TODO: when there is more than 2 implementations - error here))
        expected_out = list_fd if isinstance(self.dictionary, freq_dict.FreqDictList) else dict_fd 
        self.dictionary.fd = []
        res = self.dictionary.create_dict(words)
        self.assertTrue(res == expected_out, 'create dict test: [false] implementation:{}, was:{} should:{} '.format(type(self.dictionary), res, expected_out))

    def check_sort(self):
        list_fd = [['aa', 2], ['bb', 3], ['cc', 2]]
        dict_fd = {'aa': 2, 'bb': 3, 'cc': 2}
        sort_fd = [['bb', 3], ['aa', 2], ['cc', 2]]
        if isinstance(self.dictionary, freq_dict.FreqDictList):
            self.dictionary.fd = list_fd
            res = self.dictionary.sort()
            self.assertTrue(res == sort_fd, 'sort test: [false] was: {} should:{}'.format(res, sort_fd))
        else: 
            self.dictionary.fd = dict_fd
            self.assertTrue(self.dictionary.sort() == sort_fd, 'sort test: [false]')

    def check_implementation(self, chosen_implementation):
        self.dictionary = chosen_implementation()
        self.check_split()
        self.check_find_dict()
        self.check_add_word()
        self.check_create_dict()
        self.check_sort()      

    def test_list_impl(self):
        self.check_implementation(freq_dict.FreqDictList)

    def test_dict_impl(self):
        self.check_implementation(freq_dict.FreqDictDict)

if __name__ == '__main__':
    unittest.main()
