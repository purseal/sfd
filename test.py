#!/usr/bin/env python3

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

    def test_split_to_word(self):
        text = ['aa bb', 'aa - bb', 'aa,- bb', 'aa bb cc ']
        list_of_words = [['aa','bb'], ['aa','bb'],
                         ['aa','bb'], ['aa','bb','cc']]
        for (t,l) in zip(text, list_of_words):
            res = freq_dict.FreqDictTree.split_to_words(t)
            assert res == l, self.message.format(res, l)

    def test_create_tree(self):
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


class TestFreqDict(unittest.TestCase):

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


    def check_sort(self, chosen_implementation):
        sort_fd = [['bb', 3], ['aa', 2], ['cc', 1]]
        dic = chosen_implementation()
        dic.add_word('aa')
        dic.add_word('aa')
        dic.add_word('bb')
        dic.add_word('bb')
        dic.add_word('bb')
        dic.add_word('cc')
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
