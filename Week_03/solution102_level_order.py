
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        from collections import deque
        queue = deque()
        res = []
        queue.append(root)
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level)
        return res

    #dfs
    def levelOrder2(self, root: TreeNode) -> List[List[int]]:
        res = []

        def _dfs(root, level, res):
            if not root:
                return
            if len(res) == level:
                res.append([])
            res[level].append(root.val)
            if root.left:
                _dfs(root.left, level+1, res)
            if root.right:
                _dfs(root.right, level+1, res)

        _dfs(root, 0, res)
        return res


