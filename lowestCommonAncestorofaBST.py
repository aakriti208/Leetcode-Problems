class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if not root: return 
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root
            
            
    # case where p or q is not in the tree or the nodes are empty:
    
    def lowestCommonAncestor(self, root, p, q):
        def exists(node, target):
            while node:
                if target.val < node.val:
                    node.left
                elif target.val > node.val:
                    node.right
                else:
                    return True
            return False
        
        if not exists(root, p) or not exists(root, q):
            return 
        
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root    
    
                