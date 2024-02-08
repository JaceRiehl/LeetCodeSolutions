# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# recursive
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        def bfs(root, ret):
            if not root:
                return ret
            ret.append(root.val)
            ret = bfs(root.left,ret)
            ret = bfs(root.right,ret)
            return ret
        return bfs(root,ret)
        
        
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# iterative
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        stack = []
        current = root

        while current or stack:
            if current:
                ret.append(current.val)
                stack.append(current.right)
                current = current.left
            else:
                current = stack.pop()
        return ret