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