#!usr/bin/env python3 

class Node:
    def __init__(self, word, cnt, left = None, right = None):
        self.word = word
        self.cnt = cnt
        self.left = left
        self.right = right

class Tree:
    def __init__(self):
        self.root = None
        
    def addNode(self, word, root_node, direct):
        new_node = Node(None, None, None, None)
        new_node.word = word
        new_node.cnt = 1
        if root_node == None:
            return new_node
        else:
            if direct == 0:
                root_node.left = new_node
                return new_node
            else:
                root_node.right = new_node
                return new_node

if __name__ == '__main__':
    pass        
