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


class Solution:
    """
    21. Merge Two Sorted Lists
    Question: merge two sorted list and create linkedlist
    1.Create dummy linkedlist, dummy= ListNode(-1), cur =dummy, head will be cur.next
    2.iterate list1, list2 their own node, no need to define new node
    """
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 and not list2: return list1
        if list2 and not list1: return list2
        if not list1 and not list2: return None

        dummy = ListNode(-1)
        cur = dummy
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1 # assign list1node to res
                list1 = list1.next
            else:
                cur.next = list2 # assign list2node to res, not need to =ListNode(list2.val)
                list2 = list2.next
            cur = cur.next
        
        while list1:
            cur.next = list1
            cur = cur.next
            list1 = list1.next
        
        while list2:
            cur.next = list2
            cur = cur.next
            list2 = list2.next
        
        return dummy.next # return head of linkedlist, not running point:cur