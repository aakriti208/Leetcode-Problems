class Solution(object):
    def maxDepth(self, root):
        if root is None:
            return 0
        stack = [(root, 1)]
        maxDepth = 0
        while stack:
            depth = 0
            node, depth = stack.pop()
            maxDepth = max(maxDepth, depth)
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))
        return maxDepth