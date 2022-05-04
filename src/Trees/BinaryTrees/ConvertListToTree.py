"""
Leetcode 108 Convert Sorted Array to Binary Tree

Technique:
- Recurrsive
- set the middle point of the array as the node and recursively set the left side as the left side of the array before the middle and the right side as the opposite.

"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums):
        def recurrsiveHelper(l,r):
            if l > r:
                return None
            m = (l + r) // 2
            
            root = TreeNode(nums[m])
            
            root.left = recurrsiveHelper(l,m-1)
            root.right = recurrsiveHelper(m+1,r)
            
            return root
        return recurrsiveHelper(0, len(nums)-1)