#!/usr/bin/env python3
"""Unittest for tree_structure. """

import tree_structure as ts
import unittest
import copy

class TestTreeStruct(unittest.TestCase):
    """Class of unittest. """

    word1 = 'b'
    word2 = 'c'
    word3 = 'e'

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
        self.assertTrue(res == None,
                        'test find parent in empty tree: [false],'\
                        ' was {}, should None'.format(str(res)))
        tree = ts.Tree()
        tree.root = ts.Node('d', 1)
        tree.root.left = ts.Node('b', 2)
        tree.root.right = ts.Node('e', 1)
        tree.root.left.left = ts.Node('a', 1)

        exp_node = ts.Node('b', 2)
        exp_node.left = ts.Node('a', 1)
        res = tree.find_parent(self.word2)
        message = 'test find parent: [false], was: res({}, {},'.format(
            res.word, res.cnt)
        message += ' {}, {}), '.format(res.left, res.right)
        message += 'should: exp_tree({}, {},'.format(exp_node.word,
                                                     exp_node.cnt)
        message += ' {}, {})'.format(exp_node.left, exp_node.right)

        assert res == exp_node, message

    def test_add_node(self):
        """ Method makes test of method add_node in tree_structure. """
        empty_tree = ts.Tree()
        exp = ts.Tree()
        exp.root = ts.Node('b', 1)
        res = empty_tree.add_node(self.word1)
        message = 'test add node in empty tree: [false], was: res('
        message += '{}, {},'.format(res.root.word, res.root.cnt)
        message += ' {}, {}), '.format(res.root.left, res.root.right)
        message += 'should: exp({}, {},'.format(exp.root.word, exp.root.cnt)
        message += '{}, {})'.format(exp.root.left, exp.root.right)

        assert res == exp, message

        tree = ts.Tree()
        tree.root = ts.Node('d', 1)
        tree.root.left = ts.Node('b', 2)
        tree.root.right = ts.Node('e', 1)
        tree.root.left.left = ts.Node('a', 1)
        exp_tree = ts.Tree()
        exp_tree.root = ts.Node('d', 1)
        exp_tree.root.left = ts.Node('b', 2)
        exp_tree.root.right = ts.Node('e', 1)
        exp_tree.root.left.left = ts.Node('a', 1)
        exp_tree.root.left.right = ts.Node('c', 1)
        res = tree.add_node(self.word2)
        message = 'test add node: [false], was: res('
        message += ' {}, {},'.format(res.root.word, res.root.cnt)
        message += ' {}, {}), '.format(res.root.left, res.root.right)
        message += 'should: exp({}, {},'.format(exp_tree.root.word,
                                                exp_tree.root.cnt)
        message += '{}, {})'.format(exp_tree.root.left, exp_tree.root.right)

        assert res == exp_tree, message

        exp_tree.root.right = ts.Node('e', 2)
        res = tree.add_node(self.word3)
        message = 'test add node: [false], was: res('
        message += ' {}, {},'.format(res.root.word, res.root.cnt)
        message += ' {}, {}), '.format(res.root.left, res.root.right)
        message += 'should: exp({}, {},'.format(exp_tree.root.word,
                                                exp_tree.root.cnt)
        message += '{}, {})'.format(exp_tree.root.left, exp_tree.root.right)

        assert res == exp_tree, message

    def test_find_node(self):
        """ Method makes test of method find_node in tree_structure. """
        node = ts.Node('e', 1)
        tree = ts.Tree()
        tree.root = ts.Node('d', 1)
        tree.root.left = ts.Node('b', 2)
        tree.root.right = ts.Node('e', 1)
        tree.root.left.left = ts.Node('a', 1)
        exp_node = tree.root.right
        res = tree.find_node(node)
        message = 'test find existing node in not empty tree: [false],'
        message += 'was: res({}, {}, '.format(res.word, res.cnt)
        message += '{}, {}), '.format(res.left, res.right)
        message += 'should: exp_node({}, {}, '.format(exp_node.word,
                                                      exp_node.cnt)
        message += '{}, {})'.format(exp_node.left, exp_node.right)

        assert res == exp_node, message

        node = ts.Node('b', 2, ts.Node('a', 1))
        exp_node = tree.root.left
        res = tree.find_node(node)
        message = 'test find existing node in not empty tree: [false],'
        message += 'was: res({}, {}, '.format(res.word, res.cnt)
        message += '{}, {}), '.format(res.left, res.right)
        message += 'should: exp_node({}, {}, '.format(exp_node.word,
                                                      exp_node.cnt)
        message += '{}, {})'.format(exp_node.left, exp_node.right)

        assert res == exp_node, message

        empty_tree = ts.Tree()
        res = empty_tree.find_node(node)
        message = 'test find existing node in empty tree: [false],'
        message += 'was: res({}, {}, {}, {}), should: None'.format(
            None if not res else res.word,
            None if not res else res.cnt,
            None if not res else res.left,
            None if not res else res.right
            )

        assert res is None, message

        node = ts.Node('s', 3)
        res = tree.find_node(node)
        message = 'test find not existing node in not empty tree: [false],'
        message += 'was: res({}, {}, {}, {}), should: None'.format(
            None if not res else res.word,
            None if not res else res.cnt,
            None if not res else res.left,
            None if not res else res.right
            )

        assert res is None, message

    def test_split_to_word(self):
        text = ['aa bb', 'aa - bb', 'aa,- bb', 'aa bb cc ']
        list_of_words = [['aa','bb'], ['aa','bb'],
                         ['aa','bb'], ['aa','bb','cc']]
        for (t,l) in zip(text, list_of_words):
            res = ts.FreqDictImpl.split_to_words(t)
            assert res == l, 'split to words test: [false]'

    def test_create_tree(self):
        list_of_words = ['d', 'b', 'e', 'a', 'b', 'c']
        tree = ts.Tree()
        tree.root = ts.Node('d', 1)
        tree.root.left = ts.Node('b', 2)
        tree.root.right = ts.Node('e', 1)
        tree.root.left.left = ts.Node('a', 1)
        tree.root.left.right = ts.Node('c', 1)
        res = ts.FreqDictImpl.create_tree(list_of_words)
        exp_res = tree
        message = 'test create tree: [false], '
        message += 'was: res({}, {}, {}, {})'.format(
            res.root.word, res.root.cnt, res.root.left, res.root.right
            )
        message += 'should: exp_res({}, {}, {}, {})'.format(
            exp_res.root.word, exp_res.root.cnt,
            exp_res.root.left, exp_res.root.right
            )

        assert res == exp_res, message

    def test_convert_tree_to_list(self):
        tree = ts.Tree()
        tree.root = ts.Node('d', 1)
        tree.root.left = ts.Node('b', 2)
        tree.root.right = ts.Node('e', 1)
        tree.root.left.left = ts.Node('a', 1)
        tree.root.left.right = ts.Node('c', 1)
        FDI_obj = ts.FreqDictImpl()
        FDI_obj.tree = tree
        res = FDI_obj.convert_tree_to_list()
        exp_res = [['a', 1], ['c', 1], ['b', 1], ['e', 1], ['d', 1]]
        message = 'test create freq dict 1: [false],'
        message =+ 'was: {}, should: {}'.format(res, exp_res)

        assert res == exp_res, message

if __name__ == '__main__':
    unittest.main()
