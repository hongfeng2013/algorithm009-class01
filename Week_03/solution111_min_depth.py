
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if root.left is None and root.right is None:
            return 1
        min_deeep = float('inf')
        if root.left:
            min_deeep = min(self.minDepth(root.left), min_deeep)
        if root.right:
            min_deeep = min(self.minDepth(root.right), min_deeep)
        return min_deeep + 1