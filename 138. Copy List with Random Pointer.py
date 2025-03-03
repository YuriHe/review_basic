"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        Question:Deep copy whole linkedlist with random Node
        Two pass instead of one pass because random node may not create
        1.create node and traverse old linkedlist, use hashmap{oldnode:newnode}
        2.set next pointer and random pointer
        """
        if not head:
            return None
            
        # create hashmap store mapping of old node to new node
        old_to_new = {}
        # first pass create new node with val and store mapping
        cur = head
        while cur:
            new_node = Node(cur.val)
            old_to_new[cur] = new_node
            cur = cur.next
        # second pass set next pointer and random pointer
        cur = head
        while cur:
            found_new_node = old_to_new[cur]
            if cur.next:
                found_new_node.next = old_to_new[cur.next]
            if cur.random:
                found_new_node.random = old_to_new[cur.random]
            cur = cur.next

        # return new head
        return old_to_new[head]