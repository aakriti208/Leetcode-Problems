class TreeNode:
    # Constructor to initialize the node with a
    # value and set left and right pointers to None
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # This function searches for a node with
    # a specified value in a Binary Search Tree (BST).
    def searchBST(self, root, val):
        # Loop until either the tree is
        # exhausted (None) or the value is found.
        while root is not None and root.val != val:
            # Check if the target value is
            # less than the current node's value.
            # If so, move to the left subtree
            # (values smaller than the current node).
            # Otherwise, move to the right subtree
            # (values larger than the current node).
            root = root.left if val < root.val else root.right
        # Return the node containing the target value,
        # if found; otherwise, return None.
        return root

# Function to perform an in-order traversal
# of a binary tree and print its nodes
def printInOrder(root):
    # Check if the current node
    # is None (base case for recursion)
    if root is None:
        # If None, return and
        # terminate the function
        return

    # Recursively call printInOrder
    # for the left subtree
    printInOrder(root.left)

    # Print the value of the current node
    print(root.val, end=" ")

    # Recursively call printInOrder
    # for the right subtree
    printInOrder(root.right)

# Creating a BST
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(8)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(10)

print("Binary Search Tree:")
printInOrder(root)
print()

solution = Solution()

# Searching for a value in the BST
target = 6
result = solution.searchBST(root, target)

# Displaying the search result
if result is not None:
    print(f"Value {target} found in the BST!")
else:
    print(f"Value {target} not found in the BST.")