# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if root.val == key:
            return root
        
        dummy = TreeNode(root.val)
        while root is not None:
            if root.val > key and root.left.val != key:
                root = root.right
                if root.right == key:
                    del root.right
                    root = root.left.right
            elif root.val < key:
                root = root.left
                if root.left == key:
                    del root.left
                    root = root.right.left
        return root
   
        