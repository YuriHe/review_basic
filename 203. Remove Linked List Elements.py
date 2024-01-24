# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        """
        Question: remove val from linkedlist T:O(1), return head of linkedlist
        Topic: single linkedlist - delete and create linkedlist and one pointer
        """
        start from headnode None/not
        if head is None: return head
        # create new linkedlist to deal with first node
        dummy = ListNode(-1)
        dummy.next = head
        cur = dummy # like prev
        # iterate until pointing to null
        while cur.next is not None:
            if cur.next.val == val:
                    cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next 




        