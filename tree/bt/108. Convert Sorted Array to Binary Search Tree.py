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
    height-balanced means diff between left subtree height and right subtree height <= 1 ---> 
    root of subtree always in the middle
    """
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # recursion itself function must have base case
        if len(nums) == 0:
            return None
        # find root which in the middle 
        mid = len(nums) // 2
        root_v = nums[mid]
        node = TreeNode(val=root_v)
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right =self.sortedArrayToBST(nums[mid+1:])
        # building tree return node
        return node
        

