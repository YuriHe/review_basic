# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        1.Solution: create res linkedlist and compare neighbor if duplicate
        """
        # Remove duplicates -> create
        dummy = ListNode(-1)
        dummy.next = head
        cur = dummy.next
        while cur:
            if cur.next and cur.next.val == cur.val: 
                # duplicate
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next

