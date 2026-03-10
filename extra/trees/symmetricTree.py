class Solution(object):
    def isSymmetric(self, root):
        if root is None: return True
        return self.isMirror(root.left, root.right)
        def isMirror(self, node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2 or node1.val != node2.val:
                return False
            return self.isMirror(node1.left, node2.right) and self.isMirror(node2.left, node1.right)

                
        
class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return True
        return self.isMirror(root.left, root.right)
    def isMirror(self, node1, node2):
        if not node1 and not node2:
            return True
        if not node1 or not node2 or node1.val != node2.val:
            return False
        
        # 3. The "Mirror" Recursion:
        # Compare Outer (node1.left and node2.right) 
        # AND Inner (node1.right and node2.left)
        return self.isMirror(node1.left, node2.right) and 
               self.isMirror(node1.right, node2.left)