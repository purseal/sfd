#!/usr/bin/env python3

import freq_dict2
import unittest

class TestFreqDict(unittest.TestCase):

    def setUp(self):
        pass

    def test_split(self):
        text = ['Иван Анна', 'Иван - Анна', 'Иван,- Анна', 'Иван Анна дом ']
        list_of_words = [['иван','анна'], ['иван','анна'], ['иван','анна'], ['иван','анна','дом']]
        for (t,l) in zip(text, list_of_words):
            self.assertTrue(freq_dict2.split_to_words(t) == l, 'split to words test: [false]')

    def test_find_dict(self):
        word = 'dd'
        fd1 = [['aa', 2], ['dd', 1], ['d', 4]]
        fd2 = [['aa', 2], ['cc', 1], ['d', 4]]
        self.assertTrue(freq_dict2.find_in_dict(word, fd1) == 1, 'find word in freq dict test1: [false]')
        self.assertTrue(freq_dict2.find_in_dict(word, fd2) == None, 'find word in freq dict test2: [false]')

    def test_add_word(self):
        word = 'dd'
        fd1 = [['aa', 1], ['dd', 2]]
        new_fd1 = [['aa', 1], ['dd', 3]]
        fd2 = [['aa', 1], ['bb', 3]]
        new_fd2 = [['aa', 1], ['bb', 3], ['dd', 1]]
        self.assertTrue(freq_dict2.add_word(word, fd1) == new_fd1, 'add word in freq dict test1: [false]')
        self.assertTrue(freq_dict2.add_word(word, fd2) == new_fd2, 'add word in freq dict test2: [false]')

if __name__ == '__main__':
    unittest.main()
