# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    Question: sort linkedlist use merge sort O(nlogn)
    1.find the middle, split two ll
    2.merge two ll
    create getMid func, think1,2,3,4 
    """
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # base case
        if not head or not head.next:
            return head
        
        first = head
        second = self.getMid(head)
        # save it before cut from middle, split two lists
        tmp = second.next
        second.next = None
        second = tmp
        # recursive call
        first = self.sortList(first)
        second = self.sortList(second)
        # merge two lists (create new linkedlist as result)
        return self.merge(first, second)

    def getMid(self, head):
        fast, slow = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, l1, l2):
        # create res list
        dummy = ListNode()
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



        


