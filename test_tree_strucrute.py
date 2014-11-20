#!/usr/bin/env python3

import pdb
import tree_structure as ts 
import unittest
import copy

class TestTreeStruct(unittest.TestCase):
    word1 = 'b'
    word2 = 'c'

    def test_node_eq(self):
        n1 = ts.Node('a', 2)
        assert n1 == copy.copy(n1)
        assert n1 != ts.Node('b', 2)
        assert n1 != ts.Node('a', 3)
        assert n1 != ts.Node('a', 2, ts.Node('a', 1))
        assert ts.Node('a', 2, ts.Node('a', 1)) != n1
        n1.left = ts.Node('a', 1)
        assert ts.Node('a', 2, ts.Node('a', 1)) == n1
        assert not n1 != n1

    def test_find_parent(self):
        empty_tree = ts.Tree()
        res = empty_tree.find_parent(self.word1)
        self.assertTrue(res == None, 'test find parent in empty tree: [false], was {}, should None'.format(str(res)))
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
        message += 'should: exp_tree({}, {},'.format(exp_node.word, exp_node.cnt) 
        message += ' {}, {})'.format(exp_node.left, exp_node.right)

        assert res == exp_node, message

    def test_add_node(self):
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
        message += 'should: exp({}, {},'.format(exp_tree.root.word, exp_tree.root.cnt)
        message += '{}, {})'.format(exp_tree.root.left, exp_tree.root.right)

        assert res == exp_tree, message

     #  list_of_exp_tree = [e, exp_tree]
      #  list_of_res = [empty_tree.add_node(self.word1), tree.add_node(self.word2)]
       # for e,r in zip(list_of_exp_tree, list_of_res): 
        #    self.assertTrue(r == e, '''test add node: [false],
         #       was: res({}, {},'''.format(r.root.word, r.root.cnt) + ' {}, {}), '.format( r.root.left, r.root.right) + '''
          #      should: exp_tree({}, {},'''.format(e.root.word, e.root.cnt) + '{}, {})'.format(e.root.left, e.root.right))
    

if __name__ == '__main__':
    unittest.main()
