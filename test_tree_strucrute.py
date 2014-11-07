#!/usr/bin/env python3

import tree_structure as ts 
import unittest

class TestTreeStruct(unittest.TestCase):

    def setUp(self):
        pass
    
    def test_addNode(self):
        t = ts.Tree()
        word = 'a'
        exp_tree = ts.Node (word, 1, None, None)
        res = t.addNode(word, None, None)
        print(type(res), type (exp_tree))
        print('res(' + res.word + ', ' + str(res.cnt) + ', ' + str(res.left) + ', ' + str(res.right) + ')')
        print ('exp_tree(' + exp_tree.word + ', ' + str(exp_tree.cnt) + ', ' + str(exp_tree.left) + ', ' + str(exp_tree.right) + ')')
        self.assertTrue(res == exp_tree, 'test add node in an empty tree: [false]')
    
    
if __name__ == '__main__':
    unittest.main()
