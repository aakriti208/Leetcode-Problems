from collections import deque

class Solution(object):
    def invertTree(self, root):
        if not root: return []
        q = deque([root])
        result = []
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                node.left, node.right = node.right, node.left
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
        return result
        