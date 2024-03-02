# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """
    Question: check if linkedlist list cycle
    Topic: fast-slow pointer
    when fast come to meet slow
    """
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None: return False
        fast = head
        slow = head 
        while fast and fast.next: # use fast because fast will go forward 2 more steps
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False
