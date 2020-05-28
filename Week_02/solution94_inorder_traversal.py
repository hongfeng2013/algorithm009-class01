
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def helper(node):
            if not node:
                return []
            return helper(node.left) + [node.val] + helper(node.right)

        return helper(root)

    def inorderTraversal2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        stack, res = [], []
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            top = stack.pop()
            res.append(top.val)
            cur = top.right
        return res
