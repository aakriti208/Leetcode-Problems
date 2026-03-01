# Complete Guide to Trees for LeetCode and Coding Interviews

## Table of Contents
1. [Core Concepts and Terminology](#core-concepts)
2. [Types of Trees](#types-of-trees)
3. [Tree Traversal Methods](#tree-traversals)
4. [Common Tree Patterns](#common-patterns)
5. [Key Algorithms](#key-algorithms)
6. [Time and Space Complexity](#complexity-analysis)
7. [LeetCode Problem Types](#leetcode-patterns)
8. [Example Problems by Pattern](#example-problems)
9. [Pattern Recognition Tips](#pattern-recognition)
10. [Practice Roadmap](#practice-roadmap)

---

## 1. Core Concepts and Terminology {#core-concepts}

### Basic Terminology

**Node**: The fundamental unit of a tree containing data and pointers to child nodes
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

**Edge**: Connection between two nodes (parent-child relationship)

**Root**: The topmost node with no parent

**Leaf**: A node with no children (both left and right are None)

**Parent**: A node that has one or more child nodes

**Child**: A node connected to a parent node

**Siblings**: Nodes that share the same parent

**Ancestor**: Any node on the path from root to a given node

**Descendant**: Any node reachable by following child pointers from a given node

**Subtree**: A tree formed by a node and all its descendants

**Height of a Node**: Length of longest path from that node to a leaf
- Height of leaf = 0
- Height of tree = height of root

**Depth of a Node**: Length of path from root to that node
- Depth of root = 0

**Level**: Set of all nodes at the same depth
- Root is at level 0

**Diameter**: Longest path between any two nodes (may or may not pass through root)

**Path**: Sequence of nodes connected by edges

---

## 2. Types of Trees {#types-of-trees}

### Binary Tree
- Each node has at most 2 children (left and right)
- No ordering constraint on values

**Properties:**
- Max nodes at level i: 2^i
- Max nodes in tree of height h: 2^(h+1) - 1
- Min height with n nodes: log2(n)

### Binary Search Tree (BST)
- Left subtree contains only nodes with values less than parent
- Right subtree contains only nodes with values greater than parent
- Both left and right subtrees must also be BSTs

**Properties:**
- Inorder traversal gives sorted sequence
- Average search/insert/delete: O(log n)
- Worst case (skewed): O(n)

### Complete Binary Tree
- All levels completely filled except possibly the last
- Last level filled from left to right
- Used in heap implementation

### Full Binary Tree
- Every node has either 0 or 2 children
- No node has exactly 1 child

### Perfect Binary Tree
- All internal nodes have 2 children
- All leaves at same level
- Total nodes = 2^(h+1) - 1

### Balanced Binary Tree
- Height of left and right subtrees differ by at most 1
- This property holds for all nodes in the tree

### AVL Tree
- Self-balancing BST
- Balance factor (height_left - height_right) is -1, 0, or 1
- Rotations maintain balance after insert/delete
- Guarantees O(log n) operations

### Red-Black Tree
- Self-balancing BST with color property
- Every node is red or black
- Root and leaves (NIL) are black
- Red nodes cannot have red children
- All paths from node to descendant leaves have same number of black nodes

### N-ary Tree
- Each node can have at most N children
- Stored as list of children

```python
class NaryNode:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children else []
```

### Trie (Prefix Tree)
- Tree used to store strings
- Each path represents a word
- Common prefix sharing saves space

```python
class TrieNode:
    def __init__(self):
        self.children = {}  # char -> TrieNode
        self.is_end_of_word = False
```

### Segment Tree
- Used for range queries and updates
- Each node stores aggregate info about a range
- Common for range sum, min, max queries

### Fenwick Tree (Binary Indexed Tree)
- Efficient structure for cumulative frequency tables
- Supports prefix sum queries and updates in O(log n)

---

## 3. Tree Traversal Methods {#tree-traversals}

### Depth First Search (DFS)

#### Inorder Traversal (Left-Root-Right)
**Use case**: Get sorted order from BST

**Recursive:**
```python
def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)
```

**Iterative:**
```python
def inorder_iterative(root):
    result, stack = [], []
    curr = root

    while curr or stack:
        # Go to leftmost node
        while curr:
            stack.append(curr)
            curr = curr.left

        # Process node
        curr = stack.pop()
        result.append(curr.val)

        # Move to right subtree
        curr = curr.right

    return result
```

**Time**: O(n) | **Space**: O(h) where h is height

#### Preorder Traversal (Root-Left-Right)
**Use case**: Copy tree, prefix expression, serialize tree

**Recursive:**
```python
def preorder(root):
    if not root:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)
```

**Iterative:**
```python
def preorder_iterative(root):
    if not root:
        return []

    result, stack = [], [root]

    while stack:
        node = stack.pop()
        result.append(node.val)

        # Push right first so left is processed first
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return result
```

**Time**: O(n) | **Space**: O(h)

#### Postorder Traversal (Left-Right-Root)
**Use case**: Delete tree, postfix expression, calculate tree properties

**Recursive:**
```python
def postorder(root):
    if not root:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]
```

**Iterative:**
```python
def postorder_iterative(root):
    if not root:
        return []

    result, stack = [], [root]

    while stack:
        node = stack.pop()
        result.append(node.val)

        # Push left first, then right
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    # Reverse to get postorder from modified preorder
    return result[::-1]
```

**Time**: O(n) | **Space**: O(h)

### Breadth First Search (BFS) / Level Order

**Use case**: Find shortest path, level-by-level processing, serialize tree

```python
from collections import deque

def level_order(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(current_level)

    return result
```

**Time**: O(n) | **Space**: O(w) where w is max width

### Morris Traversal (Threaded Binary Tree)
**Space-optimized traversal without stack/recursion**

```python
def morris_inorder(root):
    result = []
    curr = root

    while curr:
        if not curr.left:
            # No left child, visit and go right
            result.append(curr.val)
            curr = curr.right
        else:
            # Find inorder predecessor
            pred = curr.left
            while pred.right and pred.right != curr:
                pred = pred.right

            if not pred.right:
                # Establish thread
                pred.right = curr
                curr = curr.left
            else:
                # Thread exists, remove it
                pred.right = None
                result.append(curr.val)
                curr = curr.right

    return result
```

**Time**: O(n) | **Space**: O(1)

---

## 4. Common Tree Patterns {#common-patterns}

### Pattern 1: Tree DFS (Recursion)
**When to use**: Path finding, tree property calculation, validation

**Template:**
```python
def dfs(root):
    # Base case
    if not root:
        return base_value

    # Recursive case
    left_result = dfs(root.left)
    right_result = dfs(root.right)

    # Combine results
    return combine(root.val, left_result, right_result)
```

**Examples**: Max depth, min depth, diameter, path sum, validate BST

### Pattern 2: Tree BFS (Level Order)
**When to use**: Level-by-level processing, shortest path, zigzag traversal

**Template:**
```python
from collections import deque

def bfs(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(current_level)

    return result
```

**Examples**: Level order, zigzag, right side view, level averages

### Pattern 3: Top-Down DFS (Pass info down)
**When to use**: Path tracking, parent info needed, target sum

**Template:**
```python
def top_down(root, accumulated_value):
    if not root:
        return

    # Use accumulated value with current node
    new_value = update(accumulated_value, root.val)

    # Check condition at current node
    if is_leaf(root) and condition(new_value):
        # Found answer
        return True

    # Pass down to children
    return (top_down(root.left, new_value) or
            top_down(root.right, new_value))
```

**Examples**: Path sum, root to leaf paths, binary tree paths

### Pattern 4: Bottom-Up DFS (Return info up)
**When to use**: Calculate tree properties, subtree info needed

**Template:**
```python
def bottom_up(root):
    if not root:
        return base_case

    # Get info from children
    left_info = bottom_up(root.left)
    right_info = bottom_up(root.right)

    # Calculate current node's info
    current_info = calculate(root.val, left_info, right_info)

    # Update global answer if needed
    global answer
    answer = max(answer, current_info)

    # Return info to parent
    return current_info
```

**Examples**: Height, diameter, max path sum, balanced tree check

### Pattern 5: Binary Search on BST
**When to use**: BST search, insertion, deletion, kth element

**Template:**
```python
def search_bst(root, target):
    if not root or root.val == target:
        return root

    if target < root.val:
        return search_bst(root.left, target)
    else:
        return search_bst(root.right, target)
```

**Examples**: Search, insert, delete, LCA in BST, kth smallest

### Pattern 6: Two Pointers / Multiple Trees
**When to use**: Compare trees, merge trees, subtree checks

**Template:**
```python
def compare_trees(root1, root2):
    # Base cases
    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False

    # Compare current nodes and recurse
    return (root1.val == root2.val and
            compare_trees(root1.left, root2.left) and
            compare_trees(root1.right, root2.right))
```

**Examples**: Same tree, symmetric tree, merge trees, subtree check

### Pattern 7: Parent Pointer / HashMap for Parent Tracking
**When to use**: LCA, distance from nodes, ancestor queries

**Template:**
```python
def find_with_parent_map(root, target):
    # Build parent map using BFS
    parent = {root: None}
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node.left:
            parent[node.left] = node
            queue.append(node.left)
        if node.right:
            parent[node.right] = node
            queue.append(node.right)

    # Use parent map to solve problem
    # (e.g., find ancestors, LCA, etc.)
```

**Examples**: LCA, nodes at distance K, all ancestors

### Pattern 8: Serialization / Deserialization
**When to use**: Convert tree to/from string, save/load tree

**Template:**
```python
def serialize(root):
    if not root:
        return "null"

    left = serialize(root.left)
    right = serialize(root.right)
    return f"{root.val},{left},{right}"

def deserialize(data):
    def helper(vals):
        val = next(vals)
        if val == "null":
            return None

        node = TreeNode(int(val))
        node.left = helper(vals)
        node.right = helper(vals)
        return node

    return helper(iter(data.split(",")))
```

**Examples**: Serialize/deserialize, codec problems

### Pattern 9: Path Tracking with Backtracking
**When to use**: All paths, path with condition, path sum variations

**Template:**
```python
def find_paths(root):
    result = []

    def backtrack(node, path):
        if not node:
            return

        # Add current node
        path.append(node.val)

        # Check if leaf and condition met
        if not node.left and not node.right:
            if condition(path):
                result.append(path[:])  # Make copy

        # Recurse
        backtrack(node.left, path)
        backtrack(node.right, path)

        # Backtrack
        path.pop()

    backtrack(root, [])
    return result
```

**Examples**: All root-to-leaf paths, path sum II, binary tree paths

### Pattern 10: Construct Tree from Traversals
**When to use**: Build tree from inorder/preorder/postorder

**Template:**
```python
def build_tree(preorder, inorder):
    if not preorder or not inorder:
        return None

    # First element in preorder is root
    root_val = preorder[0]
    root = TreeNode(root_val)

    # Find root in inorder to split left/right
    mid = inorder.index(root_val)

    # Recursively build subtrees
    root.left = build_tree(preorder[1:mid+1], inorder[:mid])
    root.right = build_tree(preorder[mid+1:], inorder[mid+1:])

    return root
```

**Examples**: Construct from pre+in, post+in, level+in

---

## 5. Key Algorithms {#key-algorithms}

### BST Insertion

```python
def insert_bst(root, val):
    if not root:
        return TreeNode(val)

    if val < root.val:
        root.left = insert_bst(root.left, val)
    else:
        root.right = insert_bst(root.right, val)

    return root
```

**Time**: O(h) where h is height | **Space**: O(h) for recursion

### BST Deletion

```python
def delete_bst(root, key):
    if not root:
        return None

    if key < root.val:
        root.left = delete_bst(root.left, key)
    elif key > root.val:
        root.right = delete_bst(root.right, key)
    else:
        # Found node to delete

        # Case 1: Leaf or one child
        if not root.left:
            return root.right
        if not root.right:
            return root.left

        # Case 2: Two children
        # Find inorder successor (smallest in right subtree)
        min_node = root.right
        while min_node.left:
            min_node = min_node.left

        # Replace with successor
        root.val = min_node.val

        # Delete successor
        root.right = delete_bst(root.right, min_node.val)

    return root
```

**Time**: O(h) | **Space**: O(h)

### BST Search

```python
def search_bst(root, val):
    if not root or root.val == val:
        return root

    if val < root.val:
        return search_bst(root.left, val)
    return search_bst(root.right, val)
```

**Time**: O(h) | **Space**: O(h) recursive, O(1) iterative

### Lowest Common Ancestor (LCA)

**For any Binary Tree:**
```python
def lca(root, p, q):
    if not root or root == p or root == q:
        return root

    left = lca(root.left, p, q)
    right = lca(root.right, p, q)

    if left and right:
        return root  # Split case

    return left if left else right
```

**Time**: O(n) | **Space**: O(h)

**For BST (optimized):**
```python
def lca_bst(root, p, q):
    while root:
        if p.val < root.val and q.val < root.val:
            root = root.left
        elif p.val > root.val and q.val > root.val:
            root = root.right
        else:
            return root
```

**Time**: O(h) | **Space**: O(1)

### Tree Height

```python
def height(root):
    if not root:
        return 0

    return 1 + max(height(root.left), height(root.right))
```

**Time**: O(n) | **Space**: O(h)

### Check if Balanced

```python
def is_balanced(root):
    def check(node):
        if not node:
            return 0, True  # height, is_balanced

        left_h, left_bal = check(node.left)
        right_h, right_bal = check(node.right)

        balanced = (left_bal and right_bal and
                   abs(left_h - right_h) <= 1)
        height = 1 + max(left_h, right_h)

        return height, balanced

    return check(root)[1]
```

**Time**: O(n) | **Space**: O(h)

### Validate BST

```python
def is_valid_bst(root):
    def validate(node, min_val, max_val):
        if not node:
            return True

        if not (min_val < node.val < max_val):
            return False

        return (validate(node.left, min_val, node.val) and
                validate(node.right, node.val, max_val))

    return validate(root, float('-inf'), float('inf'))
```

**Time**: O(n) | **Space**: O(h)

### Kth Smallest in BST

```python
def kth_smallest(root, k):
    # Inorder traversal gives sorted order
    stack = []
    curr = root

    while True:
        while curr:
            stack.append(curr)
            curr = curr.left

        curr = stack.pop()
        k -= 1
        if k == 0:
            return curr.val

        curr = curr.right
```

**Time**: O(h + k) | **Space**: O(h)

### Mirror/Invert Tree

```python
def invert_tree(root):
    if not root:
        return None

    # Swap children
    root.left, root.right = root.right, root.left

    # Recurse
    invert_tree(root.left)
    invert_tree(root.right)

    return root
```

**Time**: O(n) | **Space**: O(h)

---

## 6. Time and Space Complexity Analysis {#complexity-analysis}

### Common Operations

| Operation | Average (Balanced) | Worst (Skewed) | Space |
|-----------|-------------------|----------------|-------|
| Search | O(log n) | O(n) | O(h) |
| Insert | O(log n) | O(n) | O(h) |
| Delete | O(log n) | O(n) | O(h) |
| Traversal | O(n) | O(n) | O(h) |

### Tree Types Comparison

| Tree Type | Search | Insert | Delete | Space | Notes |
|-----------|--------|--------|--------|-------|-------|
| Binary Tree | O(n) | O(1) | O(n) | O(n) | No ordering |
| BST | O(h) | O(h) | O(h) | O(n) | Can degrade to O(n) |
| AVL Tree | O(log n) | O(log n) | O(log n) | O(n) | Strict balancing |
| Red-Black | O(log n) | O(log n) | O(log n) | O(n) | Less strict than AVL |
| Complete BT | O(n) | O(log n) | O(log n) | O(n) | For heap operations |

### Traversal Complexity

| Traversal | Time | Space (Recursive) | Space (Iterative) | Space (Morris) |
|-----------|------|-------------------|-------------------|----------------|
| Inorder | O(n) | O(h) | O(h) | O(1) |
| Preorder | O(n) | O(h) | O(h) | O(1) |
| Postorder | O(n) | O(h) | O(h) | O(1) |
| Level Order | O(n) | O(w) | O(w) | N/A |

**Note**: h = height, w = max width, n = number of nodes

### Complexity Breakdown Examples

#### Example 1: Max Depth
```python
def max_depth(root):
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))
```

**Analysis:**
- Visits each node once: O(n) time
- Recursion stack depth: O(h) space
- Best case (balanced): O(log n) space
- Worst case (skewed): O(n) space

#### Example 2: Level Order with Result
```python
def level_order(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)

    return result
```

**Analysis:**
- Each node processed once: O(n) time
- Queue holds at most width w nodes: O(w) space
- Result array stores all n values: O(n) additional space
- Total space: O(w + n) which is O(n)

#### Example 3: Path Sum with All Paths
```python
def path_sum(root, target):
    result = []

    def dfs(node, path, remaining):
        if not node:
            return

        path.append(node.val)

        if not node.left and not node.right and remaining == node.val:
            result.append(path[:])

        dfs(node.left, path, remaining - node.val)
        dfs(node.right, path, remaining - node.val)

        path.pop()

    dfs(root, [], target)
    return result
```

**Analysis:**
- Visits all nodes: O(n) time
- For each leaf, might copy path of length h: O(h) per path
- Worst case k paths: O(k * h) for copying
- Total time: O(n + k * h) where k can be O(2^h) in worst case
- Space: O(h) for recursion + O(k * h) for result

---

## 7. LeetCode Problem Types and Approaches {#leetcode-patterns}

### 7.1 Tree Construction Problems

**Pattern**: Build tree from arrays or other structures

**Approach**:
- Use recursion with index tracking
- HashMap for quick lookups
- Identify root, split left/right recursively

**Common Problems**:
- Construct Binary Tree from Preorder and Inorder
- Construct Binary Tree from Postorder and Inorder
- Construct BST from Preorder
- Maximum Binary Tree

### 7.2 Tree Traversal Problems

**Pattern**: Visit nodes in specific order

**Approach**:
- Choose appropriate traversal (in/pre/post/level)
- Recursive or iterative based on space constraints
- Morris for O(1) space

**Common Problems**:
- Binary Tree Inorder Traversal
- Binary Tree Level Order Traversal
- Binary Tree Zigzag Level Order
- Vertical Order Traversal

### 7.3 Path Problems

**Pattern**: Find/count/sum paths in tree

**Approach**:
- Top-down: Pass accumulated value
- Bottom-up: Return value from subtrees
- Backtracking for all paths

**Common Problems**:
- Path Sum I, II, III
- Binary Tree Maximum Path Sum
- Sum Root to Leaf Numbers
- Longest Univalue Path

### 7.4 Tree Property Problems

**Pattern**: Calculate or verify tree properties

**Approach**:
- Bottom-up DFS to calculate from leaves
- Return multiple values (height, balance, etc.)
- Combine children's results

**Common Problems**:
- Maximum Depth
- Minimum Depth
- Balanced Binary Tree
- Diameter of Binary Tree

### 7.5 BST-Specific Problems

**Pattern**: Leverage BST ordering property

**Approach**:
- Binary search on tree structure
- Inorder for sorted processing
- Range checking

**Common Problems**:
- Validate Binary Search Tree
- Kth Smallest Element in BST
- Lowest Common Ancestor of BST
- Convert Sorted Array to BST

### 7.6 Tree Modification Problems

**Pattern**: Change tree structure or values

**Approach**:
- Recursion to modify subtrees
- Return modified subtree root
- Handle null cases carefully

**Common Problems**:
- Invert Binary Tree
- Flatten Binary Tree to Linked List
- Trim a Binary Search Tree
- Delete Node in BST

### 7.7 Tree Comparison Problems

**Pattern**: Compare two or more trees

**Approach**:
- Simultaneous traversal
- Check conditions at each step
- Handle null cases

**Common Problems**:
- Same Tree
- Symmetric Tree
- Subtree of Another Tree
- Merge Two Binary Trees

### 7.8 Ancestor/Descendant Problems

**Pattern**: Find relationships between nodes

**Approach**:
- Build parent map if needed
- DFS to find nodes
- Use LCA algorithm

**Common Problems**:
- Lowest Common Ancestor
- All Nodes Distance K
- Deepest Leaves Sum
- Find Distance in Binary Tree

### 7.9 Serialization Problems

**Pattern**: Convert tree to/from string representation

**Approach**:
- Choose traversal method
- Handle null markers
- Use delimiters

**Common Problems**:
- Serialize and Deserialize Binary Tree
- Serialize and Deserialize BST
- Verify Preorder Serialization

### 7.10 View/Boundary Problems

**Pattern**: Find visible nodes from certain perspective

**Approach**:
- Level order with tracking
- DFS with level/column tracking
- Boundary traversal logic

**Common Problems**:
- Binary Tree Right Side View
- Binary Tree Left Side View
- Boundary of Binary Tree
- Vertical Order Traversal

---

## 8. Example Problems by Pattern {#example-problems}

### Pattern 1: Tree DFS - Maximum Depth

**Problem**: Find the maximum depth of a binary tree.

**Approach**: Bottom-up DFS
- Depth of null = 0
- Depth of node = 1 + max(left_depth, right_depth)

```python
def max_depth(root):
    if not root:
        return 0

    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)

    return 1 + max(left_depth, right_depth)
```

**Complexity**:
- Time: O(n) - visit each node once
- Space: O(h) - recursion stack, h = height

---

### Pattern 2: Tree BFS - Binary Tree Right Side View

**Problem**: Return values of nodes you can see from right side.

**Approach**: Level order traversal, take last node of each level

```python
from collections import deque

def right_side_view(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)

        for i in range(level_size):
            node = queue.popleft()

            # Last node in this level
            if i == level_size - 1:
                result.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return result
```

**Complexity**:
- Time: O(n) - visit each node
- Space: O(w) - queue width, w = max width

**Alternative DFS approach**:
```python
def right_side_view_dfs(root):
    result = []

    def dfs(node, level):
        if not node:
            return

        # First node at this level from right
        if level == len(result):
            result.append(node.val)

        # Visit right first
        dfs(node.right, level + 1)
        dfs(node.left, level + 1)

    dfs(root, 0)
    return result
```

---

### Pattern 3: Path Sum - Has Path Sum

**Problem**: Check if tree has root-to-leaf path summing to target.

**Approach**: Top-down DFS with accumulated sum

```python
def has_path_sum(root, target_sum):
    if not root:
        return False

    # Leaf node check
    if not root.left and not root.right:
        return root.val == target_sum

    # Recurse with reduced target
    remaining = target_sum - root.val
    return (has_path_sum(root.left, remaining) or
            has_path_sum(root.right, remaining))
```

**Complexity**:
- Time: O(n) - worst case visit all nodes
- Space: O(h) - recursion stack

**Variation - Find All Paths**:
```python
def path_sum_all(root, target_sum):
    result = []

    def dfs(node, path, remaining):
        if not node:
            return

        # Add current node
        path.append(node.val)

        # Check if leaf with target sum
        if not node.left and not node.right and remaining == node.val:
            result.append(path[:])  # Copy path

        # Recurse
        dfs(node.left, path, remaining - node.val)
        dfs(node.right, path, remaining - node.val)

        # Backtrack
        path.pop()

    dfs(root, [], target_sum)
    return result
```

**Complexity**:
- Time: O(n * h) - visit n nodes, copy path of length h
- Space: O(h) for recursion + O(number_of_paths * h) for result

---

### Pattern 4: Diameter of Binary Tree

**Problem**: Find length of longest path between any two nodes.

**Approach**: Bottom-up DFS, update global max

```python
def diameter(root):
    diameter_max = 0

    def height(node):
        nonlocal diameter_max

        if not node:
            return 0

        # Get heights of subtrees
        left_h = height(node.left)
        right_h = height(node.right)

        # Update diameter (path through this node)
        diameter_max = max(diameter_max, left_h + right_h)

        # Return height to parent
        return 1 + max(left_h, right_h)

    height(root)
    return diameter_max
```

**Complexity**:
- Time: O(n) - visit each node once
- Space: O(h) - recursion stack

**Key insight**: For each node, diameter passing through it = left_height + right_height

---

### Pattern 5: Validate Binary Search Tree

**Problem**: Check if tree is valid BST.

**Approach**: DFS with min/max bounds

```python
def is_valid_bst(root):
    def validate(node, min_val, max_val):
        if not node:
            return True

        # Current value must be in range
        if not (min_val < node.val < max_val):
            return False

        # Left subtree: upper bound is current value
        # Right subtree: lower bound is current value
        return (validate(node.left, min_val, node.val) and
                validate(node.right, node.val, max_val))

    return validate(root, float('-inf'), float('inf'))
```

**Complexity**:
- Time: O(n) - check each node
- Space: O(h) - recursion stack

**Alternative - Inorder Traversal**:
```python
def is_valid_bst_inorder(root):
    prev = float('-inf')
    stack = []
    curr = root

    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left

        curr = stack.pop()

        # Inorder should be strictly increasing
        if curr.val <= prev:
            return False

        prev = curr.val
        curr = curr.right

    return True
```

---

### Pattern 6: Lowest Common Ancestor

**Problem**: Find LCA of two nodes in binary tree.

**Approach**: DFS, return node if found, check if both sides have results

```python
def lca(root, p, q):
    # Base case: empty or found target
    if not root or root == p or root == q:
        return root

    # Search in subtrees
    left = lca(root.left, p, q)
    right = lca(root.right, p, q)

    # Both sides found nodes - current is LCA
    if left and right:
        return root

    # Return whichever side found something
    return left if left else right
```

**Complexity**:
- Time: O(n) - might visit all nodes
- Space: O(h) - recursion stack

**Key insight**: Three cases:
1. Both nodes in different subtrees → current is LCA
2. One node is ancestor of other → that node is LCA
3. Both in same subtree → recurse deeper

---

### Pattern 7: Construct Tree from Traversals

**Problem**: Build tree from preorder and inorder arrays.

**Approach**: First element of preorder is root, find in inorder to split

```python
def build_tree(preorder, inorder):
    if not preorder or not inorder:
        return None

    # First of preorder is root
    root_val = preorder[0]
    root = TreeNode(root_val)

    # Find root in inorder to get left/right split
    mid = inorder.index(root_val)

    # Elements to left of mid are left subtree
    # Elements to right are right subtree
    root.left = build_tree(preorder[1:mid+1], inorder[:mid])
    root.right = build_tree(preorder[mid+1:], inorder[mid+1:])

    return root
```

**Complexity**:
- Time: O(n^2) - index() takes O(n), called n times
- Space: O(n) - recursion + slicing

**Optimized with HashMap**:
```python
def build_tree_optimized(preorder, inorder):
    # Build index map for O(1) lookup
    inorder_map = {val: i for i, val in enumerate(inorder)}

    def build(pre_start, pre_end, in_start, in_end):
        if pre_start > pre_end:
            return None

        root_val = preorder[pre_start]
        root = TreeNode(root_val)

        mid = inorder_map[root_val]
        left_size = mid - in_start

        root.left = build(pre_start + 1, pre_start + left_size,
                         in_start, mid - 1)
        root.right = build(pre_start + left_size + 1, pre_end,
                          mid + 1, in_end)

        return root

    return build(0, len(preorder) - 1, 0, len(inorder) - 1)
```

**Optimized Complexity**:
- Time: O(n) - each node created once
- Space: O(n) - hashmap + recursion

---

### Pattern 8: Serialize and Deserialize Binary Tree

**Problem**: Convert tree to string and back.

**Approach**: Use preorder with null markers

```python
def serialize(root):
    def encode(node):
        if not node:
            return "null"

        left = encode(node.left)
        right = encode(node.right)

        return f"{node.val},{left},{right}"

    return encode(root)

def deserialize(data):
    def decode(values):
        val = next(values)

        if val == "null":
            return None

        node = TreeNode(int(val))
        node.left = decode(values)
        node.right = decode(values)

        return node

    return decode(iter(data.split(",")))
```

**Complexity**:
- Time: O(n) - visit each node
- Space: O(n) - string storage + O(h) recursion

**Alternative - Level Order**:
```python
from collections import deque

def serialize_level_order(root):
    if not root:
        return ""

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()

        if node:
            result.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append("null")

    return ",".join(result)

def deserialize_level_order(data):
    if not data:
        return None

    values = data.split(",")
    root = TreeNode(int(values[0]))
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()

        # Left child
        if values[i] != "null":
            node.left = TreeNode(int(values[i]))
            queue.append(node.left)
        i += 1

        # Right child
        if i < len(values) and values[i] != "null":
            node.right = TreeNode(int(values[i]))
            queue.append(node.right)
        i += 1

    return root
```

---

### Pattern 9: Kth Smallest in BST

**Problem**: Find kth smallest element in BST.

**Approach**: Inorder traversal gives sorted order

```python
def kth_smallest(root, k):
    stack = []
    curr = root

    while True:
        # Go to leftmost
        while curr:
            stack.append(curr)
            curr = curr.left

        # Process node
        curr = stack.pop()
        k -= 1

        if k == 0:
            return curr.val

        # Move to right subtree
        curr = curr.right
```

**Complexity**:
- Time: O(h + k) - go to leftmost, then k nodes
- Space: O(h) - stack size

**Follow-up - Frequent Queries**:
If tree is frequently modified, augment each node with size of subtree:

```python
class TreeNodeWithSize:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.left_size = 0  # Number of nodes in left subtree

def kth_smallest_with_size(root, k):
    left_size = root.left_size

    if k <= left_size:
        # In left subtree
        return kth_smallest_with_size(root.left, k)
    elif k == left_size + 1:
        # Current node
        return root.val
    else:
        # In right subtree
        return kth_smallest_with_size(root.right, k - left_size - 1)
```

**With augmentation**:
- Time: O(h) - binary search
- Space: O(h) or O(1) if iterative

---

### Pattern 10: Binary Tree Maximum Path Sum

**Problem**: Find maximum path sum between any two nodes.

**Approach**: Bottom-up DFS, track global max

```python
def max_path_sum(root):
    max_sum = float('-inf')

    def max_gain(node):
        nonlocal max_sum

        if not node:
            return 0

        # Only take positive gains
        left_gain = max(max_gain(node.left), 0)
        right_gain = max(max_gain(node.right), 0)

        # Path through current node
        path_sum = node.val + left_gain + right_gain

        # Update global max
        max_sum = max(max_sum, path_sum)

        # Return max gain if going through this node
        # Can only take one branch (left or right)
        return node.val + max(left_gain, right_gain)

    max_gain(root)
    return max_sum
```

**Complexity**:
- Time: O(n) - visit each node once
- Space: O(h) - recursion stack

**Key insight**:
- For each node, calculate max path through it
- Can take both children for path, but only one when returning to parent

---

## 9. Pattern Recognition Tips {#pattern-recognition}

### How to Identify Which Pattern to Use

#### 1. Keywords in Problem Statement

| Keywords | Pattern | Example |
|----------|---------|---------|
| "level by level", "layer", "width" | BFS / Level Order | Level order, zigzag, right side view |
| "path from root to leaf" | Top-down DFS | Path sum, all paths |
| "height", "depth", "balanced" | Bottom-up DFS | Max depth, balanced tree |
| "binary search tree", "sorted", "kth" | BST properties | Validate BST, kth smallest |
| "two trees", "compare", "same" | Two pointer DFS | Same tree, merge trees |
| "build", "construct", "from array" | Construction | Build from traversals |
| "ancestors", "distance between nodes" | Parent tracking / LCA | LCA, distance K |
| "string representation" | Serialization | Serialize/deserialize |

#### 2. Input/Output Analysis

**Single tree, single value output** → DFS likely
- Max depth, diameter, sum of leaves

**Single tree, array/list output** → Traversal
- Level order, all paths, inorder

**Two trees** → Simultaneous traversal
- Compare, merge, check subtree

**Array to tree** → Construction
- Build from preorder+inorder

**Tree to array** → Serialization or traversal
- Serialize, flatten

#### 3. Decision Tree for Pattern Selection

```
Is it about levels/width?
├─ Yes → BFS
└─ No
    ├─ Do you need info from children?
    │   ├─ Yes → Bottom-up DFS
    │   └─ No → Top-down DFS
    │
    ├─ Is it a BST with search/order requirement?
    │   └─ Yes → BST properties / Binary search
    │
    ├─ Multiple trees involved?
    │   └─ Yes → Two-pointer traversal
    │
    ├─ Need all paths or combinations?
    │   └─ Yes → Backtracking DFS
    │
    └─ Convert to/from other format?
        └─ Yes → Serialization / Construction
```

#### 4. Common Problem Indicators

**Use BFS when**:
- Problem asks for level information
- Need shortest path (unweighted)
- Want to process nodes layer by layer
- Right/left side view
- Zigzag traversal

**Use DFS when**:
- Need to explore all paths
- Calculate tree properties
- Validate tree structure
- Path sum problems
- Most tree problems default to DFS

**Use Bottom-Up DFS when**:
- Need info from children to decide parent
- Calculate aggregate values (height, sum, count)
- Examples: height, diameter, balanced check

**Use Top-Down DFS when**:
- Pass information from parent to children
- Track accumulated values (path sum, depth)
- Examples: path sum, max depth with level tracking

**Use BST properties when**:
- Tree is explicitly BST
- Need sorted order
- Search/insert/delete operations
- Kth element problems

**Use Parent Map when**:
- Need to traverse upward
- Find ancestors
- LCA when tree doesn't have parent pointers
- Distance between arbitrary nodes

#### 5. Optimization Hints

**Space optimization needed?**
- Use Morris traversal instead of recursion
- Iterative instead of recursive
- Modify tree in-place if allowed

**Time optimization needed?**
- Use BST properties for binary search
- Cache results (memoization)
- Augment tree with extra info (size, height)

**Multiple queries on same tree?**
- Preprocess tree (parent map, size augmentation)
- Build auxiliary structures

---

## 10. Practice Roadmap {#practice-roadmap}

### Week 1-2: Fundamentals

**Goal**: Master basic traversals and tree properties

#### Day 1-2: Traversals
1. Binary Tree Inorder Traversal (LC 94) - Easy
2. Binary Tree Preorder Traversal (LC 144) - Easy
3. Binary Tree Postorder Traversal (LC 145) - Easy
4. Binary Tree Level Order Traversal (LC 102) - Medium

#### Day 3-4: Basic Properties
5. Maximum Depth of Binary Tree (LC 104) - Easy
6. Minimum Depth of Binary Tree (LC 111) - Easy
7. Balanced Binary Tree (LC 110) - Easy
8. Symmetric Tree (LC 101) - Easy

#### Day 5-7: Path Problems Intro
9. Path Sum (LC 112) - Easy
10. Sum of Left Leaves (LC 404) - Easy
11. Path Sum II (LC 113) - Medium
12. Binary Tree Paths (LC 257) - Easy

**Practice**: Do all traversals recursively AND iteratively

---

### Week 3-4: BST and Tree Modification

**Goal**: Understand BST properties and tree transformations

#### Day 8-10: BST Basics
13. Search in BST (LC 700) - Easy
14. Insert into BST (LC 701) - Medium
15. Validate Binary Search Tree (LC 98) - Medium
16. Kth Smallest Element in BST (LC 230) - Medium

#### Day 11-13: Tree Modification
17. Invert Binary Tree (LC 226) - Easy
18. Merge Two Binary Trees (LC 617) - Easy
19. Trim a BST (LC 669) - Medium
20. Delete Node in BST (LC 450) - Medium

#### Day 14: Mixed Practice
21. Convert Sorted Array to BST (LC 108) - Easy
22. Increasing Order Search Tree (LC 897) - Easy

**Practice**: For each BST problem, think about the ordering property

---

### Week 5-6: Advanced DFS Patterns

**Goal**: Master bottom-up and top-down patterns

#### Day 15-17: Bottom-Up DFS
23. Diameter of Binary Tree (LC 543) - Easy
24. Lowest Common Ancestor (LC 236) - Medium
25. Binary Tree Maximum Path Sum (LC 124) - Hard
26. Longest Univalue Path (LC 687) - Medium

#### Day 18-20: Construction
27. Construct from Preorder and Inorder (LC 105) - Medium
28. Construct from Postorder and Inorder (LC 106) - Medium
29. Construct BST from Preorder (LC 1008) - Medium
30. Maximum Binary Tree (LC 654) - Medium

#### Day 21: Review
- Redo 3 hardest problems from weeks 5-6

**Practice**: Draw out recursion tree for construction problems

---

### Week 7-8: BFS and Level-Order Patterns

**Goal**: Master BFS variations

#### Day 22-24: Level Order Variations
31. Binary Tree Level Order Traversal II (LC 107) - Medium
32. Binary Tree Zigzag Level Order (LC 103) - Medium
33. Average of Levels (LC 637) - Easy
34. Binary Tree Right Side View (LC 199) - Medium

#### Day 25-27: BFS Applications
35. Populating Next Right Pointers (LC 116) - Medium
36. Populating Next Right Pointers II (LC 117) - Medium
37. All Nodes Distance K (LC 863) - Medium
38. Vertical Order Traversal (LC 987) - Hard

#### Day 28: Mixed Practice
39. Minimum Depth (revisit with BFS approach)
40. Cousins in Binary Tree (LC 993) - Easy

**Practice**: Solve level order problems with both BFS and DFS

---

### Week 9-10: Advanced Topics

**Goal**: Handle complex scenarios

#### Day 29-31: Serialization
41. Serialize and Deserialize Binary Tree (LC 297) - Hard
42. Serialize and Deserialize BST (LC 449) - Medium
43. Verify Preorder Serialization (LC 331) - Medium

#### Day 32-34: Path Sum Variations
44. Path Sum III (LC 437) - Medium
45. Sum Root to Leaf Numbers (LC 129) - Medium
46. Insufficient Nodes in Root to Leaf Paths (LC 1080) - Medium

#### Day 35-36: Tree DP / Complex Problems
47. House Robber III (LC 337) - Medium
48. Binary Tree Cameras (LC 968) - Hard
49. Distribute Coins in Binary Tree (LC 979) - Medium

#### Day 37-38: Miscellaneous
50. Flatten Binary Tree to Linked List (LC 114) - Medium
51. Count Good Nodes in Binary Tree (LC 1448) - Medium
52. Maximum Width of Binary Tree (LC 662) - Medium

**Practice**: For hard problems, spend 30 min before looking at hints

---

### Week 11-12: Advanced BST and Special Trees

**Goal**: Master advanced tree structures

#### Day 39-41: BST Advanced
53. Lowest Common Ancestor of BST (LC 235) - Medium
54. Convert BST to Greater Tree (LC 538) - Medium
55. Recover Binary Search Tree (LC 99) - Medium
56. Unique Binary Search Trees (LC 96) - Medium

#### Day 42-44: Trie
57. Implement Trie (LC 208) - Medium
58. Add and Search Word (LC 211) - Medium
59. Word Search II (LC 212) - Hard

#### Day 45-47: N-ary Trees
60. N-ary Tree Preorder (LC 589) - Easy
61. N-ary Tree Level Order (LC 429) - Medium
62. Maximum Depth of N-ary Tree (LC 559) - Easy

**Practice**: Implement trie from scratch without looking

---

### Week 13-14: Hard Problems and Mock Interviews

**Goal**: Prepare for actual interviews

#### Day 48-52: Hard Problems Focus
63. Binary Tree Postorder (Morris, LC 145) - Medium
64. Count Complete Tree Nodes (LC 222) - Medium
65. Longest Zigzag Path (LC 1372) - Medium
66. Maximum Sum BST in Binary Tree (LC 1373) - Hard
67. Binary Tree Coloring Game (LC 1145) - Medium

#### Day 53-56: Mock Interview Sets

**Set 1** (45 min):
- Path Sum III
- Lowest Common Ancestor
- Validate BST

**Set 2** (45 min):
- Serialize and Deserialize
- Right Side View
- Diameter of Binary Tree

**Set 3** (45 min):
- Construct from Preorder and Inorder
- Binary Tree Maximum Path Sum
- Kth Smallest in BST

**Set 4** (45 min):
- Vertical Order Traversal
- All Nodes Distance K
- Recover Binary Search Tree

#### Day 57-58: Review and Weak Areas
- List all problems you struggled with
- Redo them without hints
- Write explanations in own words

**Practice**: Time yourself, explain solution out loud

---

### Difficulty Progression Guide

#### Easy (Build Confidence)
Start here to understand basic concepts:
- Traversals (inorder, preorder, postorder)
- Max/min depth
- Same tree, symmetric tree
- Path sum
- Invert tree

#### Medium (Core Interview Problems)
Majority of interview questions:
- Level order variations
- BST operations
- Tree construction
- LCA
- Path sum variations
- Diameter, balanced check

#### Hard (Stretch Goals)
For top-tier companies:
- Binary tree maximum path sum
- Serialize/deserialize
- Vertical order traversal
- Word search II (Trie)
- Advanced DP on trees

---

### Topic Mastery Checklist

Mark off when you can solve without hints:

**Traversals**
- [ ] Recursive inorder, preorder, postorder
- [ ] Iterative inorder, preorder, postorder
- [ ] Level order BFS
- [ ] Morris traversal
- [ ] Zigzag level order

**Properties**
- [ ] Height/depth calculation
- [ ] Balanced tree check
- [ ] Diameter calculation
- [ ] Symmetric tree check
- [ ] Same tree comparison

**BST Operations**
- [ ] Search in BST
- [ ] Insert into BST
- [ ] Delete from BST
- [ ] Validate BST
- [ ] Kth smallest/largest
- [ ] LCA in BST
- [ ] Convert sorted array to BST

**Path Problems**
- [ ] Has path sum
- [ ] Find all paths with sum
- [ ] Path sum III (any path)
- [ ] Maximum path sum
- [ ] Sum root to leaf
- [ ] Binary tree paths

**Construction**
- [ ] From preorder + inorder
- [ ] From postorder + inorder
- [ ] From preorder (BST)
- [ ] From level order + inorder
- [ ] Maximum binary tree

**Modification**
- [ ] Invert/mirror tree
- [ ] Merge two trees
- [ ] Flatten to linked list
- [ ] Trim BST
- [ ] Prune tree

**Advanced**
- [ ] Serialize/deserialize
- [ ] All nodes distance K
- [ ] Vertical order traversal
- [ ] Trie implementation
- [ ] Morris traversal

---

## Additional Resources

### Key Patterns Summary

1. **Top-Down DFS**: Pass info from parent to children
2. **Bottom-Up DFS**: Collect info from children to parent
3. **Level Order BFS**: Process tree level by level
4. **BST Binary Search**: Leverage ordering for O(log n)
5. **Parent Tracking**: Build map for upward traversal
6. **Backtracking**: Find all possible paths/combinations
7. **Two Trees**: Simultaneous traversal of multiple trees
8. **Construction**: Build tree from arrays/traversals
9. **Serialization**: Convert between tree and string

### Debugging Tips

1. **Draw the tree**: Visualize small examples
2. **Trace recursion**: Follow execution step by step
3. **Check base cases**: null, single node, two nodes
4. **Edge cases**:
   - Empty tree
   - Single node
   - All left/right (skewed)
   - Complete binary tree
   - Perfect binary tree

### Interview Tips

1. **Clarify**: Ask about null nodes, duplicate values, balance
2. **Start simple**: Explain brute force first
3. **Think out loud**: Explain your thought process
4. **Code iteratively**: Start with structure, then fill logic
5. **Test**: Walk through example, consider edge cases
6. **Optimize**: Discuss time/space tradeoffs
7. **Practice explaining**: Complexity analysis is crucial

### Time Complexity Quick Reference

- Single traversal: O(n)
- Search in BST (balanced): O(log n)
- Search in BST (skewed): O(n)
- Level order: O(n) time, O(w) space
- DFS: O(n) time, O(h) space
- Copying paths: O(number_of_paths * path_length)

### Space Complexity Quick Reference

- Recursion stack: O(h) where h = height
- Queue for BFS: O(w) where w = max width
- Morris traversal: O(1)
- Parent map: O(n)
- Result storage: O(output_size)

---

## Final Tips for Success

1. **Consistency**: Do 2-3 problems daily rather than 20 once a week
2. **Understand, don't memorize**: Focus on why, not just how
3. **Redo problems**: Solve again after 1 week, then 1 month
4. **Explain out loud**: Teach concepts to reinforce learning
5. **Time yourself**: Practice under interview conditions
6. **Review patterns**: Before interview, review pattern templates
7. **Draw it out**: Visual understanding is crucial for trees
8. **Code from scratch**: Don't just read solutions
9. **Analyze complexity**: Always explain time and space
10. **Stay organized**: Track which problems you've mastered

Good luck with your tree problem practice! Focus on understanding patterns, and you'll be able to tackle any tree problem in interviews.
