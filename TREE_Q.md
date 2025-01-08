### Recursion(DFS)
Return is returning cur node situation
100. Same Tree
101. Symmetric Tree
104. Maximum Depth of Binary Tree
110. Balanced Binary Tree
111. Minimum Depth of Binary Tree
112. Path Sum
124. Binary Tree Maximum Path Sum
222. Count Complete Tree Nodes
236. Lowest Common Ancestor of a Binary Tree
257. Binary Tree Paths
297. Serialize and Deserialize Binary Tree
404. Sum of Left Leaves
543. Diameter of Binary Tree
872. Leaf-Similar Trees
1372. Longest ZigZag Path in a Binary Tree
1448. Count Good Nodes in Binary Tree


### Iterative traverse
589. N-ary Tree Preorder Traversal


### BFS
102. Binary Tree Level Order Traversal
103. Binary Tree Zigzag Level Order Traversal
117. Populating Next Right Pointers in Each Node II
199. Binary Tree Right Side View
637. Average of Levels in Binary Tree
1161. Maximum Level Sum of a Binary Tree
2415. Reverse Odd Levels of Binary Tree
2471. Minimum Number of Operations to Sort a Binary Tree by Level
2583. Kth Largest Sum in a Binary Tree  &Minheap


### Swap Treenode
226. Invert Binary Tree


### Build Tree
105. Construct Binary Tree from Preorder and Inorder Traversal
106. Construct Binary Tree from Inorder and Postorder Traversal
108. Convert Sorted Array to Binary Search Tree
427. Construct Quad Tree


### Update Node
114. Flatten Binary Tree to Linked List
129. Sum Root to Leaf Numbers


### Backtrack
437. Path Sum III (prefixsum + backtracking)


### BST
use inorder traversal methood
98. Validate Binary Search Tree
173. Binary Search Tree Iterator
230. Kth Smallest Element in a BST
235. Lowest Common Ancestor of a Binary Search Tree
450. Delete Node in a BST
530. Minimum Absolute Difference in BST 
783. Minimum Distance Between BST Nodes
938. Range Sum of BST


### Prefix tree(dictionary tree)
208. Implement Trie (Prefix Tree)
211. Design Add and Search Words Data Structure
1233. Remove Sub-Folders from the Filesystem
1268. Search Suggestions System


### Concept
#### Complete Tree
Every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible.
#### height-balanced
A height-balanced binary tree is defined as a binary tree in which the height of the left and the right subtree of any node differ by not more than 1. AVL tree, red-black tree are examples of height-balanced trees. 
#### BFS
1.at most two childs 2.left.val<=cur.val<=right.val 3.use inorder to traverse bfs which keep increasing/decresing order


### SOLUTION
All tree solution, must handle if not root, return None/ []

#### Solution1
base case: if not root: return ..
rec base: self.func(xx.left)
no return

#### Solution2
base case: if not root: return None
update varaible(mutable var, nonlocal)
recursion: node1 = self.func(node.left)
return node  or node1 | node2











