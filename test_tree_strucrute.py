#!/usr/bin/env python3

import tree_structure as ts 
import unittest

class TestTreeStruct(unittest.TestCase):
    word1 = 'b'
    word2 = 'c'
    empty_tree = ts.Tree()
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
    node2.right = node4
    result_tree = root

    def test_find_parent(self):
        res = self.empty_tree.find_parent(self.word1)
        self.assertTrue(res == None, 'test find parent: [false], was {}, should None'.format(res))
        list_of_exp_parent = [self.node2, self.node2]
        list_of_res = [self.tree.find_parent(self.word2), self.tree.find_parent(self.word1)]
        for r,e in zip(list_of_exp_parent, list_of_res): 
            self.assertTrue(r == e, '''test find parent: [false],
                was: res({}, {},'''.format(r.word, r.cnt) + ' {}, {}), '.format( r.left, r.right) + '''
                should: exp_tree({}, {},'''.format(e.word, e.cnt) + '{}, {})'.format(e.left, e.right))
        print ('find_parent error')

    def test_add_node(self):
        e = ts.Tree()
        e.root = self.node2
        list_of_exp_tree = [e, self.result_tree]
        list_of_res = [self.empty_tree.add_node(self.word1), self.tree.add_node(self.word2)]
        for r,e in zip(list_of_exp_tree, list_of_res): 
            print('add_note error')
            self.assertTrue(r == e, '''test find parent: [false],
                was: res({}, {},'''.format(r.word, r.cnt) + ' {}, {}), '.format( r.left, r.right) + '''
                should: exp_tree({}, {},'''.format(e.root.word, e.root.cnt) + '{}, {})'.format(e.left, e.right))
    
if __name__ == '__main__':
    unittest.main()
