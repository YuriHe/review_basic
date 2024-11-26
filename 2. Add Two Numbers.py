# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    Question: 2.Add Two Numbers from two linkedlists
    create res linkedlist
    SOLUTION1: native
    SOLUTION2: optimize
    """
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # SOLUTION1: native
        # corner case
        if not l1 and not l2: return None
        if not l1: return l2
        if not l2: return l1

        dummy = ListNode(-1)
        cur = dummy # track res
        zero = False

        while l1 and l2:
            v1 = l1.val
            v2 = l2.val
            
            v = v1 + v2
            if zero:
                v += 1
            if v >= 10:
                v = v % 10
                zero = True
            else:
                zero = False
            cur.next = ListNode(v)
            l1 = l1.next
            l2 = l2.next
            cur = cur.next
        

        while l1:
            v = l1.val
            if zero:
                v += 1
            if v >= 10:
                v = v % 10
            else:
                zero = False
            cur.next = ListNode(v)
            cur = cur.next
            l1 = l1.next

        while l2:
            v = l2.val
            if zero:
                v += 1
            if v >= 10:
                v = v % 10
            else:
                zero = False
            cur.next = ListNode(v)
            cur = cur.next
            l2 = l2.next

        if zero:
            cur.next = ListNode(1)

        return dummy.next


    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # SOLUTION2: optimize
        # corner case
        if not l1 and not l2: return None
        if not l1: return l2
        if not l2: return l1

        dummy = ListNode(-1)
        cur = dummy # track res
        carry = 0

        while l1 or l2:
            num = carry
            if l1:
                num += l1.val
                l1 = l1.next
            if l2:
                num += l2.val
                l2 = l2.next
            cur.next = ListNode(num % 10)
            carry = num // 10
            cur = cur.next

        if carry != 0:
            cur.next = ListNode(carry)

        return dummy.next