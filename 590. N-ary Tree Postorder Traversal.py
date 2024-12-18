def postorder(self, root: 'Node') -> List[int]:
        if not root: return []
        res = []
        stack = []
        stack.append(root)
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            for c in cur.children:
                stack.append(c)
        return res[::-1]

def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Postorder
        if not root: return []
        stack = []
        res = []
        stack.append(root)
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        return res[::-1]