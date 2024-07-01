"""
226. Invert Binary Tree
Given the root of a binary tree, invert the tree, and return its root.

Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:
Input: root = [2,1,3]
Output: [2,3,1]
Example 3:

Input: root = []
Output: []
 
Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


    def insert_left(self,value):
        if self.left == None:
            self.left = TreeNode(value)
        else:
            new_node = TreeNode(self.value)
            new_node.left_child = self.left_child
            self.left_child = new_node

    def insert_right(self,value):
        if self.right == None:
            self.right = TreeNode(value)
        else:
           new_node = TreeNode(self.value)
           new_node.right = self.right
           self.right = new_node


root = TreeNode(val=4)
root.insert_left(val=2)
root.insert_right(val=7)
root.left.insert_left(val=1)
root.right.insert_right(val=3)
root.left.insert_left(val=6)
root.right.insert_right(val=9)

# root = [4,2,7,1,3,6,9]

"""
start at the root
check if there a left child, if yes, 
get value check if there is a right child, get value if yes
swap the right and left children

recursive solution

base case - node.left and node.right == None

when an example of the base case occurs, start over/return 

recursive case - 
use a temp variable name to complete the swap of right and left children 

invertTree(right)
invertTree(left)

return root
"""
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
