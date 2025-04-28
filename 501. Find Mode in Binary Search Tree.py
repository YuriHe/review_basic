# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    QUESTION: find all the most frequently occur elements from the BST
    """
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        """
        SOLUTION1: use hashmap store {val:freq}
        """
        ctn = defaultdict(int)
        res = []
        def traverse(node):
            if not node: return
            traverse(node.left)
            ctn[node.val] += 1
            traverse(node.right)
        traverse(root)
        max_freq = max(ctn.values())
        for k, v in ctn.items():
            if v == max_freq:
                res.append(k)
        return res
        """
        SOLUTION2: no extra space
        Since BST, so duplicate should be nearest
        """
        # return most frequently node
        self.res = []
        self.max_count,self.cur_val,self.cur_count = 0, None, 0
        def inorder(node):
            if not node:return 
            inorder(node.left)
            if self.cur_val == node.val:
                self.cur_count += 1
            else:
                self.cur_val=node.val
                self.cur_count = 1
            if self.cur_count > self.max_count:
                self.max_count = self.cur_count
                self.res = [self.cur_val]
            elif self.cur_count == self.max_count:
                self.res.append(self.cur_val)
            inorder(node.right)

        inorder(root)
        return self.res

          


        