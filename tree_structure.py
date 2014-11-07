#!usr/bin/env python3 

class Node:
    def __init__(self, word=None, cnt=None, left=None, right=None):
        self.word = word
        self.cnt = cnt
        self.left = left
        self.right = right

class Tree:
    node = Node()

    def __init__(self):
        self.root = None

    def find_parent(self, word):
        if self.root == None:
            return self.root
        parent = self.root
        i = 0
        while ((parent.left != None) and (parent.right != None) and (i<6)):
            print(i)
            print(parent.word)
            print(parent.left)
            print(parent.right)
            if parent.word > word:
                parent = parent.left
            elif parent.word < word:
                parent = parent.right
            i += 1
        return parent
        
    def add_node(self, word):
        parent = self.find_parent(word)
        if parent == None:
            new_node = Node(None, None, None, None)
            new_node.word = word
            new_node.cnt = 1
            return new_node
        if word == parent.word:
            parent.cnt += 1
            return parent
        new_node = Node(None, None, None, None)
        new_node.word = word
        new_node.cnt = 1
        if parent.word > word:
            parent.left = new_node
            return new_node
        root_node.right = new_node
        return new_node

if __name__ == '__main__':
    pass        
