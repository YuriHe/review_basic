# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        SOLUTION1: divide and conquer
        STEP: each time divide half into small sublist; recursively merge pairs of linkedlist
        TIME: (nlogk) SPACE: (logk) H
        """
        def merge(l1, l2):
            # base case
            if not l1 and not l2: return None
            if l1 and not l2: return l1
            if l2 and not l1: return l2

            # compare val and create head of linkedlist 
            dummy = ListNode(-1)
            cur = dummy
            while l1 and l2:
                if l1.val < l2.val:
                    cur.next = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next
                cur = cur.next
            if l1:
                cur.next = l1
            if l2:
                cur.next = l2

            return dummy.next

        def divide(nested):
            # base case
            if len(nested) == 0: return None
            if len(nested) == 1: return nested[0]
            # recursive divide
            mid = len(nested) // 2
            left = divide(nested[:mid])
            right = divide(nested[mid:])
            # merge
            return merge(left, right)

        # divide nested list
        return divide(lists)
        