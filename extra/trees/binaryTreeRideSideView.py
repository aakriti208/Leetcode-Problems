# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution(object):
    def rightSideView(self, root):
        if not root: return []
        result = []
        q = deque([root])
        while q:
            rightside = None
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    rightside = node
                    q.append(node.left)
                    q.append(node.right)
            if rightside:
                result.append(rightside.val)
        return result        