# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        1.Solution: Two pass use helper + update linkedlist
        """
        if not head or not head.next: return None
        full = self.getLength(head)
        cur = head
        for _ in range(full//2-1):
            cur = cur.next
        if cur.next:
            cur.next = cur.next.next
        return head
        
    def getLength(self, head):
        if not head: return 0
        res = 0
        cur = head # traverse as cur pointer
        while cur:
            res += 1
            cur = cur.next
        return res
    
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        2.Solution: One pass + update linkedlist, remove middles node (second if two)
        """
        if not head or not head.next: return None
        slow, fast, prev = head, head, None
        while fast and fast.next:
            prev = slow
            fast = fast.next.next
            slow = slow.next
        if prev:
            prev.next = prev.next.next
        return head
