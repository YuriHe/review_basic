### BST
#### Concept
at most two childs
left.val<=cur.val<=right.val

#### List
938. Range Sum of BST

### BT
#### DFS
100. Same Tree
101. Symmetric Tree
104. Maximum Depth of Binary Tree
110. Balanced Binary Tree
#### BFS(deque)
102. Binary Tree Level Order Traversal
111. Minimum Depth of Binary Tree





108. Convert Sorted Array to Binary Search Tree

112. Path Sum
257. Binary Tree Paths



### Traversal
inorder
preorder
postorder
DFS 
BFS

### Feature
#### height-balanced
A height-balanced binary tree is defined as a binary tree in which the height of the left and the right subtree of any node differ by not more than 1. AVL tree, red-black tree are examples of height-balanced trees.


### SOLUTION
#### Solution1: Recursion
base case: if not root: return ..
rec base: return self.func(xx.left)