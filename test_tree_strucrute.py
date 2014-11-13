#!/usr/bin/env python3

import pdb
import tree_structure as ts 
import unittest
import copy

class TestTreeStruct(unittest.TestCase):
    word1 = 'b'
    word2 = 'c'
    root = ts.Node('d', 1, None, None)
    node1 = ts.Node('a', 1, None, None)
    node2 = ts.Node('b', 2, None, None)
    node3 = ts.Node('e', 1, None, None)
    root.left = node2
    root.right = node3
    root.left.left = node1
    tree = ts.Tree()
    tree.root = root
    node4 = ts.Node('c', 1, None, None)
    exp_tree = ts.Tree()
    root2 = ts.Node('d', 1, None, None)
    root2.left = node2
    root2.right = node3
    root2.left.left = node1
    exp_tree.root = root2
    exp_tree.root.left.right = node4

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
        self.assertTrue(res == None, 'test find parent: [false], was {}, should None'.format(str(res)))
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
        message += '{}, {})'.format(exp_node.left, exp_node.right)

        assert res == exp_node, message

    def test_add_node(self):
        empty_tree = ts.Tree()
        self.tree.root = self.root
        e = ts.Tree()
        e.root = self.node2
        list_of_exp_tree = [e, self.exp_tree]
        list_of_res = [empty_tree.add_node(self.word1), self.tree.add_node(self.word2)]
        for e,r in zip(list_of_exp_tree, list_of_res): 
            self.assertTrue(r == e, '''test add node: [false],
                was: res({}, {},'''.format(r.root.word, r.root.cnt) + ' {}, {}), '.format( r.root.left, r.root.right) + '''
                should: exp_tree({}, {},'''.format(e.root.word, e.root.cnt) + '{}, {})'.format(e.root.left, e.root.right))
    

if __name__ == '__main__':
    unittest.main()
