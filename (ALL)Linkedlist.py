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
    142. Linked List Cycle II
    Check if there is cycle two pointer
    1. finding cycle:
    slow:a
    fast:a+b+c
    meet: confirm this is loop
    If intersection is one node
    fast run a+(b+c)+b
    slow run a+b 
    fast_distance=2*slow_distance
    a=c
    2.after meet, fast and slow at same speed until meet again
    """
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:return head
        fast=head
        slow=head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow: # meet first time, confirm this loop
                # restart from head, and run
                fast = head
                while fast != slow:
                    fast = fast.next
                    slow = slow.next
                return slow
        return None


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
        
        cur.next = list1 if list1 else list2
        
        return dummy.next # return head of linkedlist, not running point:cur




class Solution:
    """
    328. Odd Even Linked List
    All odd + All even
    link from back to front(assign)
    """
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        odd = head
        even = head.next
        even_head = even
        while even and even.next:
            # odd link to even.next(which is next odd)
            odd.next = even.next
            # assign next odd(above) to odd
            odd = odd.next

            # even link to odd.next(which is next even)
            even.next = odd.next
            # assign next even(above) to even
            even = even.next
        odd.next = even_head
        return head


class Solution:
    """
    206. Reverse Linked List
    For an input list 1 -> 2 -> 3 -> None, after each iteration:
First iteration: 1 <- 2 -> 3 -> None (prev is 1)
Second iteration: 1 <- 2 <- 3 -> None (prev is 2)
Third iteration: 1 <- 2 <- 3 (prev is 3 and cur is None)
    """
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        prev = None
        cur = head
        while cur:
            # save cur.next before break link
            tmp = cur.next
            # cur next pointer to prev
            cur.next = prev
            # prev assign by cur
            prev = cur
            # move on, update cur
            cur = tmp
        return prev


class Solution:
    """
    2130. Maximum Twin Sum of a Linked List
    Question: find maximum sum from two node, twin index is n-1-i and i
    """
    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head:
            return head

        # store array with value, index
        ls = []
        cur = head
        while cur:
            ls.append(cur.val)
            cur = cur.next
        
        res = 0
        for i in range(len(ls)//2):
            res = max(res, ls[i] + ls[len(ls) - 1 - i])
        return res