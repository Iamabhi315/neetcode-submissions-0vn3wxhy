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
        if not head:
            return head
        
        curr = head
        while curr:
            temp = curr
            curr = curr.next
            temp.next = Node(temp.val)
            temp.next.next = curr

        curr = head
        while curr:
            if not curr.random:
                curr.next.random = None
            else:
                curr.next.random = curr.random.next
            curr = curr.next.next
        
        curr = head
        copyHead = head.next

        while curr:
            copy = curr.next

            curr.next = copy.next        # restore original

            if copy.next:
                copy.next = copy.next.next   # connect copied list

            curr = curr.next
        return copyHead



