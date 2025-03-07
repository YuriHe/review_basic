# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Validate BST(unique num)
    SOLUTION1: inorder traversal to generate list and compare with sort list O(nlogn) and also need to check counter
    """
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: return False

        # must unique , use inorder traversal save order of node's val, and check if unique and sorted
        ls = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            ls.append(node.val)
            inorder(node.right)
        
        inorder(root)

        return len(ls) == len(set(ls)) and ls == sorted(ls)
    
        """
        SOLUTION2: BFS
        (-inf, leftV, curV). (curV, rightV, inf)
        TIME SPACE O(h) O(n)
        """
        if not root: return False
        q = deque([(root, float('-inf'), float('inf'))])
        
        while q:
            node, leftBound, rightBound = q.popleft()
            if not (leftBound < node.val < rightBound):
                return False
            if node.left:
                q.append((node.left, leftBound, node.val))
            if node.right:
                q.append((node.right, node.val, rightBound))
        return True


    """
    SOLUTION3: use dfs recursion
    """
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = float('-inf')

        def dfs(node) -> bool:
            nonlocal prev

            if not node:
                return True
            # iterate left
            if not dfs(node.left):
                return False
            # computing
            if prev >= node.val:
                return False
            # update prev to cur node
            prev = node.val
            # iterate right
            if not dfs(node.right):
                return False
            # DONE consider all egdes
            return True
        
        return dfs(root)

    """
    SOLUTION4: use iterative function by using stack  (hard to think)
    """
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
            # create stack list store node
            stack = []
            # traverse tree
            cur = root
            # set ancestor 
            prev = float('-inf')

            while cur or stack:
                # go leftmost nodes
                while cur:
                    stack.append(cur)
                    cur = cur.left
                # go to first smallest node
                cur = stack.pop()
                if prev >= cur.val:
                    return False
                # update prev
                prev = cur.val

                # move to right subtree
                cur = cur.right
            
            return True
