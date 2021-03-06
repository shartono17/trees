'''
This file implements the AVL Tree data structure.
The functions in this file are considerably harder than the functions in the BinaryTree and BST files.
'''

from Trees.BinaryTree import BinaryTree, Node
from Trees.BST import BST

class AVLTree(BST):
    '''
    FIXME:
    AVLTree is currently not a subclass of BST.
    You should make the necessary changes in the class declaration line above 
    and in the constructor below.
    '''

    def __init__(self, xs=None):
        super().__init__()
        self.root = None
        if xs:
            self.insert_list(xs)
        
        '''
        FIXME:
        Implement this function.
        '''


    def balance_factor(self):
        '''
        Returns the balance factor of a tree.
        '''
        return AVLTree._balance_factor(self.root)

    @staticmethod
    def _balance_factor(node):
        '''
        Returns the balance factor of a node.
        '''
        if node is None:
            return 0
        return BinaryTree._height(node.left) - BinaryTree._height(node.right)


    def is_avl_satisfied(self):
        '''
        Returns True if the avl tree satisfies that all nodes have a balance factor in [-1,0,1].
        '''
        return AVLTree._is_avl_satisfied(self.root)

    @staticmethod
    def _is_avl_satisfied(node):
        if node is None:
            return True
        return AVLTree._balance_factor(node) in [-1,0,1] and AVLTree._is_avl_satisfied(node.right) and AVLTree._is_avl_satisfied(node.left)

        '''
        FIXME:
        Implement this function.
        '''


    @staticmethod
    def _left_rotate(node):
        if node is None or node.right is None:
            return node

        newroot = Node(node.right.value)
        newroot.right = node.right.right

        new_left = Node(node.value)
        new_left.left = node.left
        new_left.right = node.right.left

        newroot.left = new_left

        return newroot
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of tree rotations,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree code is fairly different from our class hierarchy,
        however, so you will have to adapt their code.
        '''


    @staticmethod
    def _right_rotate(node):
        if node is None or node.left is None:
            return node

        newroot = Node(node.left.value)
        newroot.left = node.left.left

        new_right = Node(node.value)
        new_right.right = node.right
        new_right.left = node.left.right

        newroot.right = new_right

        return newroot

        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of tree rotations,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree code is fairly different from our class hierarchy,
        however, so you will have to adapt their code.
        '''


    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else: 
            self.root = AVLTree._insert(value, self.root)


    def insert_list(self, xs):
        for x in xs:
            self.insert(x)

            print(x, self.root)

    
    @staticmethod
    def _insert(value, node):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                AVLTree._insert(value, node.left)
            
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                AVLTree._insert(value, node.right)
        
        if AVLTree._is_avl_satisfied(node) == False:
            node.left = AVLTree._rebalance(node.left)
            node.right = AVLTree._rebalance(node.right)
            return AVLTree._rebalance(node)
        
        else:
            return node

        
    @staticmethod
    def _rebalance(node):

        while AVLTree._balance_factor(node) < -1 or AVLTree._balance_factor(node) > 1:
            
            if AVLTree._balance_factor(node) > 1:
                if AVLTree._balance_factor(node.left) < 0:
                    node.left = AVLTree._left_rotate(node.left)
                    return AVLTree._right_rotate(node)
                else: return AVLTree._right_rotate(node)
                
            elif AVLTree._balance_factor(node) < -1:
                if AVLTree._balance_factor(node.right) > 0:
                    node.right = AVLTree._right_rotate(node.right)
                    return AVLTree._left_rotate(node)
                else: return AVLTree._left_rotate(node)

            else:
                return node
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of how to insert into an AVL tree,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree code is fairly different from our class hierarchy,
        however, so you will have to adapt their code.

        HINT:
        It is okay to add @staticmethod helper functions for this code.
        The code should look very similar to the code for your insert function for the BST,
        but it will also call the left and right rebalancing functions.
        '''
