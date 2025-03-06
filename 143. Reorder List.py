# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        """
        SOLUTION1: brute force, use extra space
        STEP: put the node in the list, and use two pointer of left and right
        """
        if not head:
            return

        nodes = []
        # put nodes into list
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next

        i, j = 0, len(nodes)-1
        while i < j:
            nodes[i].next = nodes[j]
            i += 1
            if i >= j: # no need to iterate rest
                break
            nodes[j].next = nodes[i]
            j-=1
        # tail point to None
        nodes[i].next = None
        """
        SOLUTION2: swap no extra space
        STEP1: split two parts, find middle use fast and slow pointer
        STEP2: reverse second half use prev lead linkedlist
        STEP3: merge two linkedlist
        """
        if not head or not head.next:
            return

        # find middle(even use first)
        fast, slow = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        # now fast is end, slow is middle node

        # reverse second half
        second = slow.next
        slow.next = None # cut
        prev = None # reversed second half's head
         
        while second:
            # save second.next before relink
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        # merge two linedlist
        first, second = head, prev
        # second longer
        while first and second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2




        


