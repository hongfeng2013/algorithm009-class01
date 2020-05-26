

# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        # 递归
        if not root:
            return []
        res = []

        def helper(node):
            if not node:
                return
            res.append(node.val)
            for cur in node.children:
                helper(cur)
        help(root)
        return res

    def preorder2(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        # 迭代
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            root = stack.pop()
            res.append(root.val)

            stack.extend(root.children[::-1])

        return res

