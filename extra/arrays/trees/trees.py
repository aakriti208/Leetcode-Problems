# Node structure

class TreeNode:
    def __init__(self):
        self.val = val
        self.left = left
        self.right = right
        

# Traversals

    # Inorder : left -> root -> right
    # Gives sorted order for BST
    
    def inorder(root):
        if not root:
            return []
        return inorder(root.left) + (root.val) + inorder(root.right)
    
    
    # Preorder : root -> left -> right
    # useful for copying or serializing tree
    
    def preorder(root):
        if not root:
            return []
        return (root.val) + preorder(root.left) + preorder(root.right)
    
    
    # Postorder : left-> right -> root
    # useful for deletion, evaluating expressions
    
    def postorder(root):
        if not root:
            return []
        return postorder(root.left) + postorder(root.left) + (root.val)
    
    
