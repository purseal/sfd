#!/usr/bin/env python3

import freq_dict2
import unittest

text = ['Иван Анна', 'Иван - Анна', 'Иван,- Анна', 'Иван Анна дом ']
list_of_words = [['иван','анна'], ['иван','анна'], ['иван','анна'], ['иван','анна','дом']]

class TestFreqDict(unittest.TestCase):

    def setUp(self):
        pass

    def test_split(self):
        for (t,l) in zip(text, list_of_words):
           self.assertTrue(freq_dict2.split_to_words(t) == l, 'split to words test: wrong split')

if __name__ == '__main__':
    unittest.main()
