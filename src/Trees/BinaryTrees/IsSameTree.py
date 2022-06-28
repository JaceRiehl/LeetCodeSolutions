class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    if not q and not p:
        return True
    if (p and not q) or (q and not p) or (p.val != q.val):
        return False
    
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

print(isSameTree(TreeNode(2, TreeNode(3), TreeNode(3)), TreeNode(2, TreeNode(3))))
print(isSameTree(TreeNode(2, TreeNode(3))))