# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 237. Delete Node in a Linked List
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        """
        1.Solution: singly linkedlist
        Idea: corner case if node is first one or last one
        """
        # move next of cur node's value to cur node, then let node next pointer to next next one
        node.val = node.next.val
        node.next = node.next.next

        