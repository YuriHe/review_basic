# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        1.Solution: traverse node and find middle(pick second) of linkedlist from helper getLen
        2.Solution: two pointers
        Idea: if two middle node, pick second one
        """
        # 1Solution: use helper
        if not head: return None
        full = self.getLength(head)
        cur = head
        for _ in range(full//2):
            cur = cur.next
        return cur

        # 2Solution: use fast and slow pointer
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

        # if two middle nodes, pick first
        fast = head
        slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow


    def getLength(self, head):
        if not head: return 0
        res = 0
        cur = head # traverse as cur pointer
        while cur:
            res += 1
            cur = cur.next
        return res