#!usr/bin/env python3

class Node:
    def __init__(self, word=None, cnt=None, left=None, right=None):
        self.word = word
        self.cnt = cnt
        self.left = left
        self.right = right

    def __repr__(self):
        return 'node: {} {}, l={}, r={}'.format(self.word, self.cnt,
                                                None if not self.left else self.left.word,
                                                None if not self.right else self.right.word)

    def __eq__(self, other):
        if not other:
            print('false')
            return False
        print('true')
        return (self.word == other.word
                and self.cnt == other.cnt
                and self.left == other.left
                and self.right == other.right)

class Tree:
    node = Node()

    def __init__(self):
        self.root = None

    def find_parent(self, word):
        print('self.root == ', self)
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

    def __eq__(self, other):
        if not other:
            return False
        return (self.root == other.root)

    def add_node(self, word):
        parent = self.find_parent(word)
        if parent == None:
            new_node = Node(None, None, None, None)
            new_node.word = word
            new_node.cnt = 1
            self.root = new_node
            return self
        list_nodes = [self.root]
        if word == parent.word:
            parent.cnt += 1
            return self
        new_node = Node(None, None, None, None)
        new_node.word = word
        new_node.cnt = 1
        if parent.word > word:
            parent.left = new_node
            return self
        parent = new_node
        return self
