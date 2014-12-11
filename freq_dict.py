#!/usr/bin/env python3
''' This file create a freq dict of text. '''

import re
import sys
import operator
from tree_structure import Tree

class FrequencyDict:
    ''' Class contains methods to create a frequency dictionary (freq dict)
        from text. It has three implementations: List, Dict, Tree.
    '''

    @staticmethod
    def split_to_words(text):
        ''' Method splits a text to list of words. '''
        text = text.lower()
        text = text.strip()
        text = re.sub(r'\d', '', text)
        words = re.split(r'\W*', text)
        return words

    def find_in_dict(self, word):
        ''' Method checks if there is a given word in freq dict. '''
        raise NotImplementedError

    def add_word(self, word):
        ''' Method adds word in freq dict. '''
        raise NotImplementedError

    def create_dict(self, words):
        ''' Method creates frequency unsorted dictionary. '''
        raise NotImplementedError

    def sort(self):
        ''' Method sorts freq dict. '''
        raise NotImplementedError

class FreqDictList(FrequencyDict):
    ''' Implementation of frequency dictionary's creating with lists. '''

    def __init__(self):
        self.f_dict = []

    def create_dict(self, words):
        ''' Method creates frequency unsorted dictionary. '''
        for word in words:
            self.add_word(word)
        return self.f_dict

    def find_in_dict(self, word):
        ''' Method checks if there is a given word in freq dict.
            If not - it returns None, if yes - it returns its number in list.
        '''
        for i in range(len(self.f_dict)):
            if word == self.f_dict[i][0]:
                return i
        return None

    def add_word(self, word):
        ''' Method adds word in freq dict. '''
        i = self.find_in_dict(word)
        if i is None:
            self.f_dict.append([word, 1])
        else:
            self.f_dict[i][1] += 1
        return self.f_dict

    def sort(self):
        ''' Method sorts freq dict. '''
        self.f_dict = sorted(
            self.f_dict, key=lambda dict: dict[1], reverse=True
            )
        return self.f_dict


class FreqDictDict(FrequencyDict):
    ''' Implementation of frequency dictionary's creating with dictionaries. '''

    def __init__(self):
        self.f_dict = {}

    def create_dict(self, words):
        ''' Method creates frequency unsorted dictionary. '''
        for word in words:
            self.add_word(word)
        return self.f_dict

    def find_in_dict(self, word):
        ''' Method checks if there is a given word in freq dict.
            If not - it returns None, if yes - it returns -1.
        '''
        if word in self.f_dict:
            return -1
        return None

    def add_word(self, word):
        ''' Method adds word in freq dict. '''
        if self.find_in_dict(word) is None:
            self.f_dict[word] = 1
        else:
            self.f_dict[word] += 1
        return self.f_dict

    def sort(self):
        ''' Method sorts freq dict. '''
        sort_list_of_tuples = sorted(
            self.f_dict.items(), key=operator.itemgetter(1), reverse=True
            )
        return [[key, item] for key, item in sort_list_of_tuples]


class FreqDictTree(Tree):
    ''' Class contains methods, which create freq dict
        from text by tree structure.
    '''
    def __init__(self):
        self.tree = Tree()

    @staticmethod
    def split_to_words(text):
        ''' Method splits a text to list of words. '''
        text = text.lower()
        text = text.strip()
        text = re.sub(r'\d', '', text)
        words = re.split(r'\W*', text)
        return words

    def create_tree(self, words):
        ''' Method creates a frequency tree from lost of words. '''
        for word in words:
            self.tree = self.tree.add_node(word)
        return self.tree

    def add_word(self, word):
        ''' Method adds new word in tree. '''
        self.tree.add_node(word)

    def sort(self):
        ''' Method converts tree to list of lists and sorts it. '''
        current_node = self.tree.root
        list_of_nodes = []
        while 1:
            if current_node.left and not current_node.left.checked:
                current_node = current_node.left
                continue
            elif current_node.right and not current_node.right.checked:
                current_node = current_node.right
                continue
            else:
                current_node.checked = True
                list_of_nodes.append(current_node)
                if not current_node.parent:
                    break
                current_node = current_node.parent
        for cur_node in list_of_nodes:
            cur_node.checked = False
        freq_dict_list = [
            [cur_node.word, cur_node.cnt] for cur_node in list_of_nodes
            ]
        freq_dict_list = sorted(freq_dict_list, key=lambda dict: dict[1],
                                reverse=True)
        return freq_dict_list


if __name__ == '__main__':
    SFD = FreqDictList()
    INPUT_FILE_NAME = sys.argv[1]
    OUTPUT_FILE_NAME = sys.argv[2]
    with open(INPUT_FILE_NAME) as text_file:
        STRING_OF_TEXT = text_file.read()
        LIST_OF_WORDS = SFD.split_to_words(STRING_OF_TEXT)
        FD = SFD.create_dict(LIST_OF_WORDS)
        FD = SFD.sort()
    with open(OUTPUT_FILE_NAME, 'w+') as fd_file:
        for count, a_word in FD:
            output = '{} {}\n'.format(a_word, count)
            fd_file.write(output)
