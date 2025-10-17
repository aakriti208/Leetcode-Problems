# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def insertIntoBST(self, root, val: int):
        if root is None: 
            return TreeNode(val)
        original_root = root
        while root is not None:
            if root.val <= val:
                if root.right is not None:
                    root = root.right
                else:
                    root.right = TreeNode(val)
                    return original_root
            else:
                if root.left is not None:
                    root = root.left
                else:
                    root.left = TreeNode(val)
                    return original_root
        return original_root
        
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

solution = Solution()
result = solution.insertIntoBST(root, 5)

