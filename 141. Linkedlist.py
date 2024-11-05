# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """
    141. Linked List Cycle
    Question: check if linkedlist list cycle
    Topic: fast-slow pointer
    when fast come to meet slow
    eg. 5 unit in loop, 1&2,2&4,3&6,4&8,5&10,  10 is 2times of 5. and meet at [0]
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
