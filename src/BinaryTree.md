# BinaryTreeModule

BinaryTreeModule is a Python module that provides efficient functions for working with Binary Trees.

## Initialise

Initialise a node of linked list:
```python
node = TreeNode(0, TreeNode(1), TreeNode(2)) # Creates a node with value 0, with 1 and 2 as left and right nodes respectively
```

## Functions

1. `nodePrint(lst)`
   - Prints the values of Binary Tree nodes in the list.
   - Time Complexity: O(n)
   - Space Complexity: O(n)

2. `maxDepth(self)`
   - Returns the maximum depth of the binary tree.
   - Time Complexity: O(n)
   - Space Complexity: O(h) where h is the height of the binary tree.

3. `inorderTraversal(self)`
   - Returns a list containing all the nodes of the binary tree in the order of inorder traversal.
   - Time Complexity: O(n)
   - Space Complexity: O(n)

4. `preorderTraversal(self)`
   - Returns a list containing all the nodes of the binary tree in the order of preorder traversal.
   - Time Complexity: O(n)
   - Space Complexity: O(n)

5. `postorderTraversal(self)`
   - Returns a list containing all the nodes of the binary tree in the order of postorder traversal.
   - Time Complexity: O(n)
   - Space Complexity: O(n)

6. `bfsTraversal(root: TreeNode)`
   - Returns a list containing all the nodes of the binary tree in level order traversal (BFS).
   - Time Complexity: O(n)
   - Space Complexity: O(n)

7. `bfsToTreeNode(bfs: list[str])`
   - Returns the root of the tree constructed from the values in the BFS (level order traversal) array.
   - Time Complexity: O(n)
   - Space Complexity: O(n)

8. `isSameTree(root1: TreeNode, root2: TreeNode)`
   - Returns True if both the passed Binary trees are congruent (even if node addresses are not the same), otherwise returns False.
   - Time Complexity: O(n)
   - Space Complexity: O(h) where h is the height of the binary tree.

## Example

```python
from BinaryTreeModule import *

# Example Binary Tree
#       1
#      / \
#     2   3
#    / \
#   4   5
bt = TreeNode(1)
bt.left = TreeNode(2)
bt.right = TreeNode(3)
bt.left.left = TreeNode(4)
bt.left.right = TreeNode(5)



# Print Binary Tree nodes' values
nodePrint(bt)  # Output: [1, 2, 3, 4, 5]

# Get the maximum depth of the binary tree
depth = maxDepth(bt)
print(depth)  # Output: 3

# Get the nodes of the binary tree in inorder traversal
inorder = bt.inorderTraversal()
nodePrint(inorder)  # Output: [4, 2, 5, 1, 3]

# Get the nodes of the binary tree in preorder traversal
preorder = bt.preorderTraversal()
nodePrint(preorder)  # Output: [1, 2, 4, 5, 3]

# Get the nodes of the binary tree in postorder traversal
postorder = bt.postorderTraversal()
nodePrint(postorder)  # Output: [4, 5, 2, 3, 1]

# Get the nodes of the binary tree in level order traversal (BFS)
bfs = bfsTraversal(bt)
nodePrint(bfs)  # Output: [1, 2, 3, 4, 5]

# Convert a BFS array back to a Binary Tree
bfs = [1, 2, 3, 4, None, None, 5]
root = bfsToTreeNode(bfs)

# Check if two Binary Trees are congruent
congruent = isSameTree(bt, root)
print(congruent)  # Output: False