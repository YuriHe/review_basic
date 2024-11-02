### Recursion
Return is returning cur node situation
100. Same Tree
101. Symmetric Tree
112. Path Sum
222. Count Complete Tree Nodes


### Swap Treenode
226. Invert Binary Tree


### Build Tree
105. Construct Binary Tree from Preorder and Inorder Traversal
106. Construct Binary Tree from Inorder and Postorder Traversal


### Update Node
129.Sum Root to Leaf Numbers


### BFS
637. Average of Levels in Binary Tree
102. Binary Tree Level Order Traversal


### Irerate Tree
#### BFS
530. Minimum Absolute Difference in BST


### Concept
#### Complete Tree
Every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible.





### BT
#### DFS
104.Maximum Depth of Binary Tree
110.Balanced Binary Tree
257.Binary Tree Paths

#### BFS(deque)

111.Minimum Depth of Binary Tree

938.Range Sum of BST

#### Recursion
108.Convert Sorted Array to Binary Search Tree


### Prefix tree
208. Implement Trie (Prefix Tree)
1233. Remove Sub-Folders from the Filesystem


### Traversal
inorder
preorder
postorder
DFS 
BFS


### Feature
#### height-balanced
A height-balanced binary tree is defined as a binary tree in which the height of the left and the right subtree of any node differ by not more than 1. AVL tree, red-black tree are examples of height-balanced trees. 


#### BST
##### Concept
at most two childs
left.val<=cur.val<=right.val


### SOLUTION
#### Solution1: Recursion
base case: if not root: return ..
rec base: return self.func(xx.left)
if build tree: return node