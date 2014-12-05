#!/usr/bin/env python3

import freq_dict
import unittest


class TestFreqDict(unittest.TestCase):

    def setUp(self):
        pass

    def check_split(self, chosen_implementation):
        text = ['aa bb', 'aa - bb', 'aa,- bb', 'aa bb cc ']
        list_of_words = [['aa','bb'], ['aa','bb'],
                         ['aa','bb'], ['aa','bb','cc']]
        for (t,l) in zip(text, list_of_words):
            self.assertTrue(chosen_implementation.split_to_words(t) == l, 'split to words test: [false]')

    def check_find_dict(self, chosen_implementation):
        word = 'dd'
        list_fd1 = [['aa', 2], ['dd', 1], ['d', 4]]
        list_fd2 = [['aa', 2], ['cc', 1], ['d', 4]]
        dict_fd1 = {'aa': 2, 'dd': 1, 'd': 4}
        dict_fd2 = {'aa': 2, 'cc': 1, 'd': 4}
        dic = chosen_implementation()
        if isinstance(dic, freq_dict.FreqDictList):
            dic.fd = list_fd1
            self.assertTrue(dic.find_in_dict(word) == 1, 'find word in freq dict test1 list: [false]')
            dic.fd = list_fd2
            self.assertTrue(dic.find_in_dict(word) is None, 'find word in freq dict test2 list: [false]')
        else:
            dic.fd = dict_fd1
            self.assertTrue(dic.find_in_dict(word) == -1, 'find word in freq dict test1 dict: [false]')
            dic.fd = dict_fd2
            self.assertTrue(dic.find_in_dict(word) is None, 'find word in freq dict test2 dict: [false]')

    def check_add_word(self, chosen_implementation):
        word = 'dd'
        list_fd = [[['aa', 1], ['dd', 2]], [['aa', 1], ['bb', 3]]]
        list_new_fd = [[['aa', 1], ['dd', 3]], [['aa', 1], ['bb', 3], ['dd', 1]]]
        dict_fd = [{'aa': 1, 'dd': 2}, {'aa': 1, 'bb': 3}]
        new_fd = [{'aa': 1, 'dd': 3}, {'aa': 1, 'bb': 3, 'dd': 1}]
        dic = chosen_implementation()
        if isinstance(dic, freq_dict.FreqDictList):
            for (f,n) in zip(list_fd, list_new_fd):
                dic.fd = f
                self.assertTrue(dic.add_word(word) == n, 'add word in freq dict test1 list: [false]')
        else:
            for (f,n) in zip(dict_fd, new_fd):
                dic.fd = f
                res = dic.add_word(word)
                self.assertTrue(res == n, 'add word in freq dict test1 dict: [false] {} {}'.format(res, n))

    def check_create_dict(self, chosen_implementation):
        words = ['aa', 'bb', 'cc', 'aa', 'bb', 'bb']
        list_fd = [['aa', 2], ['bb', 3], ['cc', 1]]
        dict_fd = {'aa': 2, 'bb': 3, 'cc': 1}
        dic = chosen_implementation()
        # TODO: when there is more than 2 implementations - error here))
        expected_out = list_fd if isinstance(dic, freq_dict.FreqDictList) else dict_fd
        res = dic.create_dict(words)
        self.assertTrue(res == expected_out, 'create dict test: [false] implementation:{}, was:{} should:{} '.format(type(dic), res, expected_out))

    def check_sort(self, chosen_implementation):
        list_fd = [['aa', 2], ['bb', 3], ['cc', 1]]
        dict_fd = {'aa': 2, 'bb': 3, 'cc': 1}
        sort_fd = [['bb', 3], ['aa', 2], ['cc', 1]]
        dic = chosen_implementation()
        if isinstance(dic, freq_dict.FreqDictList):
            dic.fd = list_fd
            res = dic.sort()
            self.assertTrue(res == sort_fd, 'sort test: [false] was: {} should:{}'.format(res, sort_fd))
        else:
            dic.fd = dict_fd
            res = dic.sort()
            self.assertTrue(res == sort_fd, 'sort test: [false] was:{} should:{}'.format(res, sort_fd))

    def check_implementation(self, chosen_implementation):
        self.check_split(chosen_implementation)
        self.check_find_dict(chosen_implementation)
        self.check_add_word(chosen_implementation)
        self.check_create_dict(chosen_implementation)
        self.check_sort(chosen_implementation)

    def test_list_impl(self):
        self.check_implementation(freq_dict.FreqDictList)

    def test_dict_impl(self):
        self.check_implementation(freq_dict.FreqDictDict)

if __name__ == '__main__':
    unittest.main()
