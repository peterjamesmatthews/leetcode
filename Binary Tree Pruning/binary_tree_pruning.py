"""
Given the root of a binary tree, return the same tree where every subtree (of the given
tree) not containing a 1 has been removed.

A subtree of a node node is node plus every node that is a descendant of node.

Constraints:

    The number of nodes in the tree is in the range [1, 200].
    Node.val is either 0 or 1.
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return root
