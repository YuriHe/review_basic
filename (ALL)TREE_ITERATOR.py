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
                