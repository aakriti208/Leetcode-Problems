# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def floorCeilOfBST(self, root, key):
        ceil, floor = -1, -1
        while root is not None:
            if root.data == key:
                return [key, key]
        if root.data < key:
            floor = root.data
            root = root.right
        else:
            ceil = root.data
            root = root.left
        return [floor, ceil]