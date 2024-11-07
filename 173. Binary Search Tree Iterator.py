# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    """
    Question: traverse BST by using inorder
    same as implementation of inorder
    contructor:create stack array store all left children of root
    next:finally return next Node's val.at beginning, next is leftmost, then next points will all the way to right
    hasNext:see if can go to right,see if stack isEmpty
    """
    def __init__(self, root: Optional[TreeNode]):
        # store leftnode of tree
        self.stack = []
        cur = root
        while cur:
            self.stack.append(cur)
            cur = cur.left

    def next(self) -> int:
        # return smallest element from rest of tree, pop from stack
        if len(self.stack) > 0:
            first = self.stack.pop()
            if first.right:
                cur = first.right
                while cur:
                    self.stack.append(cur)
                    cur = cur.left
            return first.val
        else:
            return -1


    def hasNext(self) -> bool:
        return len(self.stack) != 0
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()