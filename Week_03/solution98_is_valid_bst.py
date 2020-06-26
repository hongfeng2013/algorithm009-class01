
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def helper(root, min, max):
            if not root:
                return True
            if not min:
                if root.val <= min.val:
                    return False
            if not max:
                if root.val >= max.val:
                    return False

            return helper(root.left, min, root) and helper(root.right, root, max)

        return helper(root, None, None)







