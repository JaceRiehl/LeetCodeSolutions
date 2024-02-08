# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        def dfs(root, ret):
            if root:
                ret = dfs(root.left,ret)
                ret = dfs(root.right,ret)
                ret.append(root.val)
            return ret
        return dfs(root, ret)