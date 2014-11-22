#!usr/bin/env python3
'''Program creates a tree stucture with possibility of adding new node in it'''

class Node:
    '''Class, which contains main properties of node.'''

    def __init__(self, word=None, cnt=None, left=None, right=None):
        self.word = word
        self.cnt = cnt
        self.left = left
        self.right = right

    def __eq__(self, other):
        if not other:
            return False
        if (self.word == other.word
            and self.cnt == other.cnt
            and self.left == other.left
            and self.right == other.right):
            return True

    def __repr__(self):
        message = 'node: {} {},'.format(self.word, self.cnt)
        message += ' l={}, r={}'.format(
            None if not self.left else self.left.word,
            None if not self.right else self.right.word
            )

        return message
class Tree:
    '''Class, which contains all methods and propeties of tree.'''

    node = Node()

    def __init__(self):
        self.root = None

    def __eq__(self, other):
        if not other:
            return False
        if (self.root.word == other.root.word
            and self.root.cnt == other.root.cnt
            and self.root.left == other.root.left
            and self.root.right == other.root.right):
            return True
        return False

    def find_parent(self, word):
        '''Method finds a parent of new word in tree.'''
        if self.root == None:
            return None
        parent = self.root
        while parent.left != None or parent.right != None:
            if parent.word > word:
                if parent.left is None:
                    return parent
                else:
                    parent = parent.left
            elif parent.word < word:
                if parent.right is None:
                    return parent
                else:
                    parent = parent.right
            else:
                return parent
        return parent

    def add_node(self, word):
        '''Method adds new word in tree.'''
        parent = self.find_parent(word)
        if parent == None:
            new_node = Node(None, None, None, None)
            new_node.word = word
            new_node.cnt = 1
            self.root = new_node
            return self
        if word == parent.word:
            parent.cnt += 1
            return self
        new_node = Node(None, None, None, None)
        new_node.word = word
        new_node.cnt = 1
        if parent.word > word:
            parent.left = new_node
            return self
        if parent.word < word:
            parent.right = new_node
            return self

    def find_node(self, node):
        comp_node = self.root
        while comp_node is not None:
            if comp_node.word > node.word:
                if comp_node.left is not None:
                    comp_node = comp_node.left
                else:
                    return None
            elif comp_node.word < node.word:
                if comp_node.right is not None:
                    comp_node = comp_node.right
                else:
                    return None
            else:
                return comp_node
        return None
