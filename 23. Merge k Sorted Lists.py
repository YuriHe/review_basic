# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return None
        
        def merge(ls1, ls2):
            if not ls1 and not ls2: return None
            if ls1 and not ls2: return ls1
            if ls2 and not ls1: return ls2
            # both ls exits, compare
            # create linkedlist
            dummy = ListNode(-1)
            cur = dummy 
            while ls1 and ls2:
                if ls1.val < ls2.val:
                    cur.next = ls1
                    ls1 = ls1.next
                else:
                    cur.next = ls2
                    ls2 = ls2.next
                cur = cur.next
            # handle extra list, iterate one node by node 
            cur.next = ls1 if ls1 else ls2
            return dummy.next


        # divide recursively
        def divide(nest_ls):
            # base case
            if len(nest_ls) <= 0: return None
            if len(nest_ls) == 1: return nest_ls[0]
            # find mid
            mid = len(nest_ls) // 2
            # divide recurisively until base case
            left = divide(nest_ls[:mid])
            right = divide(nest_ls[mid:])
            # conquer base case
            # merge base case and return back to previous recursive call as input
            return merge(left, right)

        return divide(lists)




        