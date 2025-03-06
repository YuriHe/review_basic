# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        1.Solution: traverse linkedlist and create new rest linkedlist Two pass
        Idea: give length of linkedlist, find pos of nth node, no need to extra handle remove head(head=head.next)
        """
        if not head: return None
        # get length
        keepLen = self.getLength(head)
        # create new linkedlist
        dummy = ListNode(-1)
        # make all nodes deleteable include head,let dummy points to head, set node for new list
        dummy.next = head
        # start from dummy, not head since need to remove head, prev is for traverse for new list
        prev = dummy

        for _ in range(keepLen-n):
            prev = prev.next
        # skip nth
        prev.next = prev.next.next
        return dummy.next
    

    def getLength(self, head):
        if not head: return 0
        res = 0
        cur = head 
        while cur:
            res += 1
            cur = cur.next
        return res
    

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        2.Solution: two pointer and create new rest linkedlist One pass
        Idea: fast first walk n+1 steps, then fast and slow walk same time until fast reach end Dummy help handle deleteable
        """
        if not head: return None

        # Delete last nth node
        dummy = ListNode(-1)
        dummy.next = head
        fast = dummy
        slow = dummy

        for _ in range(n):
            # if n greater than length of list, no node to be removed
            if not fast.next:
                return head 
            fast = fast.next

        # move both fast and slow until fast reaches the end
        while fast.next: # not fast because handle n = len
            fast = fast.next
            slow = slow.next
        
        # move nth node from end
        slow.next = slow.next.next
        return dummy.next
