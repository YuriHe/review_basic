# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Question:convert sorted array to BST
    Topic:
    build BST(inorder)(left.val<=cur.val<=right.val)
    height-balanced means diff between left subtree height and right subtree height <= 1 ---> middle of nums is root
    """
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # MUST HAVE it 
        if nums is None or len(nums) == 0: return None
        # find root
        root_idx = len(nums)//2
        root_val = nums[root_idx]
        # build tree starting from root
        node = TreeNode(root_val)
        # recursion 
        node.left = self.sortedArrayToBST(nums[:root_idx])
        node.right = self.sortedArrayToBST(nums[root_idx+1:])
        return node


