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
        temp = head
        dit = {}
        shallow_copy = None
        prev = None

        while temp:
            if not prev:
                prev = Node(temp.val)
                shallow_copy = prev
            else:
                prev.next = Node(temp.val)
                prev = prev.next
            dit[temp] = prev
            temp = temp.next

        deep_copy = shallow_copy
        while head and shallow_copy:
            if head.random == None:
                shallow_copy.random = None
            else:
                shallow_copy.random = dit[head.random]
            head = head.next
            shallow_copy = shallow_copy.next

        return deep_copy


