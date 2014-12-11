#!/usr/bin/env python3
''' Test of freq_dict.py with 3 reliasations: list, dictionary, tree structure.
'''

import freq_dict
import unittest
import tree_structure as ts
import copy

class TestTreeStruct(unittest.TestCase):
    """Class of unittest. """

    word1 = 'b'
    word2 = 'c'
    word3 = 'e'
    message = 'was:res({}), should: exp_res({})'

    def test_node_eq(self):
        """ Method makes test of method eq on class Node in tree_structure.
        """
        node1 = ts.Node('a', 2)
        assert node1 == copy.copy(node1)
        assert node1 != ts.Node('b', 2)
        assert node1 != ts.Node('a', 3)
        assert node1 != ts.Node('a', 2, ts.Node('a', 1))
        assert ts.Node('a', 2, ts.Node('a', 1)) != node1
        node1.left = ts.Node('a', 1)
        assert ts.Node('a', 2, ts.Node('a', 1)) == node1
        assert not node1 != node1

    def test_tree_eq(self):
        """ Method makes test of method eq in class Tree in tree_structure.
        """
        tree = ts.Tree()
        tree.root = ts.Node('a', 2)
        assert tree == copy.copy(tree)
        tree2 = ts.Tree()
        tree2.root = ts.Node('b', 2)
        assert tree != tree2
        tree2.root = ts.Node('a', 1)
        assert tree != tree2
        tree2.root = ts.Node('a', 2, ts.Node('a', 1))
        assert tree != tree2
        tree.root.left = ts.Node('a', 1)
        assert tree == tree2
        tree2.root.left = ts.Node('b', 1)
        assert tree != tree2
        tree2.root.left = ts.Node('a', 2)
        assert tree != tree2
        tree2.root.right = ts.Node('a', 1)
        assert tree != tree2

    def test_find_parent(self):
        """ Methode makes test of method find_parent in tree_structure. """
        empty_tree = ts.Tree()
        res = empty_tree.find_parent(self.word1)
        assert res == None, self.message.format(res, None)

        tree = ts.Tree()
        tree.root = ts.Node('d', 1)
        tree.root.left = ts.Node('b', 2)
        tree.root.right = ts.Node('e', 1)
        tree.root.left.left = ts.Node('a', 1)
        exp_res = ts.Node('b', 2)
        exp_res.left = ts.Node('a', 1)
        res = tree.find_parent(self.word2)
        assert res == exp_res, self.message.format(res, exp_res)

    def test_add_node(self):
        """ Method makes test of method add_node in tree_structure. """
        tree = ts.Tree()
        exp_res = ts.Tree()
        tree.add_node('d')
        res = tree
        exp_res.root = ts.Node('d', 1)
        assert res == exp_res, self.message.format(res.root, exp_res.root)

        tree.add_node('b')
        res = tree
        exp_res.root.left = ts.Node('b', 1)
        assert res == exp_res, self.message.format(res.root, exp_res.root)

        tree.add_node('b')
        res = tree
        exp_res.root.left.cnt = 2
        assert res == exp_res, self.message.format(res.root, exp_res.root)

    def test_find_node(self):
        """ Method makes test of method find_node in tree_structure. """
        node = ts.Node('e', 1)
        tree = ts.Tree()
        res = tree.find_node(node)
        assert res is None, self.message.format(res, None)

        tree.add_node('d')
        tree.add_node('b')
        tree.add_node('e')
        tree.add_node('a')
        exp_res = tree.root.right
        res = tree.find_node(node)
        assert res == exp_res, self.message.format(res, exp_res)

        node = ts.Node('b', 2, ts.Node('a', 1))
        exp_res = tree.root.left
        res = tree.find_node(node)
        assert res == exp_res, self.message.format(res, exp_res)

        node = ts.Node('s', 3)
        res = tree.find_node(node)
        assert res is None, self.message.format(res, exp_res)

    def test_create_tree(self):
        ''' This method makes test of method create_tree in freq_dict.py. '''
        list_of_words = ['d', 'b', 'e', 'a', 'b', 'c']
        tree = ts.Tree()
        tree.add_node('d')
        tree.add_node('b')
        tree.add_node('b')
        tree.add_node('e')
        tree.add_node('a')
        tree.add_node('c')
        fdi_obj = freq_dict.FreqDictTree()
        res = fdi_obj.create_tree(list_of_words)
        exp_res = tree
        assert res == exp_res, self.message.format(res, exp_res)

    def test_convert_tree_to_list(self):
        ''' This method maes test of method convert_tree_to_list in
            freq_dict.py.
        '''
        tree = ts.Tree()
        tree.root = ts.Node('d', 1)
        tree.add_node('b')
        tree.add_node('e')
        tree.add_node('a')
        tree.add_node('c')
        tree.add_node('b')
        freq_dict_tree = freq_dict.FreqDictTree()
        freq_dict_tree.tree = tree
        res = freq_dict_tree.sort()
        exp_res = [['b', 2], ['a', 1], ['c', 1], ['e', 1], ['d', 1]]
        assert res == exp_res, self.message.format(res, exp_res)

class ImplBaseTest(unittest.TestCase):
    ''' Class contains test's methods, which differs only in the values of used
        variables.
    '''

    create_dict_exp = None
    chosen_implementation = None
    message = 'was: ({}), should: ({})'
    fd1 = None
    fd2 = None
    find_dict_right_index = None
    add_word_fd = None
    add_word_new_fd = None

    def check_create_dict(self):
        ''' Method makes test of method create_dict in freq_dict.py. '''
        words = ['aa', 'bb', 'cc', 'aa', 'bb', 'bb']
        dic = self.chosen_implementation()
        exp_res = self.create_dict_exp
        res = dic.create_dict(words)
        assert res == exp_res, self.message.format(res, exp_res)

    def check_find_dict(self):
        ''' Method makes test of find_dict method in freq_dict.py. '''
        word = 'dd'
        dic = self.chosen_implementation()
        dic.f_dict = self.fd1
        res = dic.find_in_dict(word)
        exp_res = self.find_dict_right_index
        assert res == exp_res, self.message.format(res, exp_res)

        dic.f_dict = self.fd2
        res = dic.find_in_dict(word)
        assert res is None, self.message.format(res, None)

    def check_add_word(self):
        ''' Method makes test of method add_word in freq_dict.py. '''
        word = 'dd'
        dic = self.chosen_implementation()
        for (word_fd, word_new_fd) in zip(self.add_word_fd,
                                          self.add_word_new_fd):
            dic.f_dict = word_fd
            res = dic.add_word(word)
            assert res == word_new_fd, self.message.format(res, word_new_fd)

    def run_all_checks(self):
    ''' Method runs all check methods. '''
        self.check_create_dict()
        self.check_find_dict()
        self.check_add_word()


class TestFreqDictListImpl(ImplBaseTest):
    ''' Class contains all variables for test of freq_dict in list
        implementation, which calls in ImplBaseTest's mehods.
    '''

    create_dict_exp = [['aa', 2], ['bb', 3], ['cc', 1]]
    chosen_implementation = freq_dict.FreqDictList
    fd1 = [['aa', 2], ['dd', 1], ['d', 4]]
    fd2 = [['aa', 2], ['cc', 1], ['d', 4]]
    find_dict_right_index = 1
    add_word_fd = [[['aa', 1], ['dd', 2]], [['aa', 1], ['bb', 3]]]
    add_word_new_fd = [[['aa', 1], ['dd', 3]],
                       [['aa', 1], ['bb', 3], ['dd', 1]]]

    def test_impl(self):
        ''' Method runs all check methods higher. '''
        self.run_all_checks()


class TestFreqDictDictImpl(ImplBaseTest):
    ''' Class contains all variables for test of freq_dict in dict
        implementation, which calls in ImplBaseTest's mehods.
    '''

    create_dict_exp = {'aa': 2, 'bb': 3, 'cc': 1}
    chosen_implementation = freq_dict.FreqDictDict
    fd1 = {'aa': 2, 'dd': 1, 'd': 4}
    fd2 = {'aa': 2, 'cc': 1, 'd': 4}
    find_dict_right_index = -1
    add_word_fd = [{'aa': 1, 'dd': 2}, {'aa': 1, 'bb': 3}]
    add_word_new_fd = [{'aa': 1, 'dd': 3}, {'aa': 1, 'bb': 3, 'dd': 1}]
    message = 'was: ({}), should: ({})'

    def test_impl(self):
        ''' Method runs all check methods higher. '''
        self.run_all_checks()

class TestFreqDict(unittest.TestCase):
    ''' Class contains tests for similar methods in all realisations
        in freq_dict.py
    '''

    message = 'was: ({}), should: ({})'

    def check_split(self, chosen_implementation):
        ''' Method makes test for split_to_words method in freq_dict.py. '''
        text_list = ['aa bb', 'aa - bb', 'aa,- bb', 'aa bb cc ']
        list_of_words_list = [['aa', 'bb'], ['aa', 'bb'],
                              ['aa', 'bb'], ['aa', 'bb', 'cc']]
        for (text, list_of_words) in zip(text_list, list_of_words_list):
            res = chosen_implementation.split_to_words(text)
            assert res == list_of_words, self.message.format(res,
                                                             list_of_words)

    def check_sort(self, chosen_implementation):
        ''' Method makes test est of sort method in freq_dict.py. '''
        sort_fd = [['bb', 3], ['aa', 2], ['cc', 1]]
        dic = chosen_implementation()
        dic.add_word('aa')
        dic.add_word('aa')
        dic.add_word('bb')
        dic.add_word('bb')
        dic.add_word('bb')
        dic.add_word('cc')
        res = dic.sort()
        assert res == sort_fd, self.message.format(res, sort_fd)

    def check_implementation(self, chosen_implementation):
        ''' Method runs check method for choosen implementation'''
        self.check_split(chosen_implementation)
        self.check_sort(chosen_implementation)

    def test_list_impl(self):
        ''' Method runs check_implementation for List implementation. '''
        self.check_implementation(freq_dict.FreqDictList)

    def test_dict_impl(self):
        ''' Method runs check_implementation for Dict implementation. '''
        self.check_implementation(freq_dict.FreqDictDict)

    def test_tree_impl(self):
        ''' Method runs check_implementation for Tree implementation. '''
        self.check_implementation(freq_dict.FreqDictTree)

if __name__ == '__main__':
    unittest.main()
