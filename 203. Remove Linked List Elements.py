# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        """
        1.Solution: create linkedlist and conn
        Idea:create new linkedlist, check which node
        """
        # 1STEP:create dummy list, set dummy.next is head
        dummy = ListNode(-1)
        dummy.next = head
        # 2STEP:use cur to traverse dummy 
        cur = dummy
        while cur.next:
            if cur.next.val == val:
                # found the node need deleted, point to next
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next
