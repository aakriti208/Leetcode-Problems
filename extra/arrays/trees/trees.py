from collections import deque

# Node structure

class TreeNode:
    def __init__(self):
        self.val = val
        self.left = left
        self.right = right
        

# DFS Traversals (Recursive)

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
    
    

# DFS Traversals (Iterative)

    # Inorder iterative ---> important for BST problems
    # "Go as far left as possible, saving breadcrumbs (stack).
    # When you hit a dead end, backtrack (pop), visit, then try right.
    # Repeat."
    
    def inorder_itr(root):
        stack, result = [], []
        curr = root
        while curr or stack:
            while curr:
                # go as far left as possible and keep on pushing elements to the stack
                stack.append(curr)
                curr = curr.left
            # after the inner loop ends and all the left nodes are visited, the current value is the topmost of the stack
            curr = stack.pop()
            result = curr.val
            # then go and see the right sides
            curr = curr.right
        return result
    
    # Preorder iterative ---> Copy tree, prefix expression, serialize tree
    # Pop a node → visit it → push right then left.
    # Left always processes first because it's on top of stack."
    
    def preorder_itr(root):
        if not root:
            return []
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            result.append(node.val)
            # Push right first, because stack if LIFO and left sits on top of stack
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result
    
    
    # Postorder iterative ---> Delete tree, postfix expression, calculate tree properties
    
    def postorder_itr(root):
        if not root:
            return []
        result, stack = [], [root]
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        # reverse to get postorder from modified preorder
        return result[::-1]
    
    
    # time complexity : O(n), space complexity : O(h)
    
    
    # BFS ---> Level order (Queue)
    # Find shortest path, level-by-level processing, serialize tree, minimum depth
    
    
    def level_order(root):
        if not root: return []
        q = deque([root])
        result = []
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(level)
        return result
        


    