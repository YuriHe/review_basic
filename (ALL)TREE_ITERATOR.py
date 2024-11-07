"""
94. Binary Tree Inorder Traversal
Inorder -> iterative method by using stack
"""
def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    if not root: return []

    res = []
    stack = []
    cur = root
    # store leftnodes into stack
    while cur:
        stack.append(cur)
        cur = cur.left
    
    while len(stack) > 0:
        last = stack.pop()
        res.append(last.val)

        # check righ side
        if last.right:
            cur = last.right
            while cur:
                stack.append(cur)
                # keep store left node of sub-righttree
                cur = cur.left
    return res
                

"""
144. Binary Tree Preorder Traversal
Use stack
push root, right, then left
"""
def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    stack = [root]
    res = []
    while len(stack) > 0:
        cur = stack.pop()
        res.append(cur.val)
        if cur.right:
            stack.append(cur.right)
        if cur.left:
            stack.append(cur.left)
    return res
        