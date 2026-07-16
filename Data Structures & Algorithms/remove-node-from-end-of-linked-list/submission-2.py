# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        head = self.reverse(head)

        p = head
        q = None

        for i in range(n-1):
            q = p
            p = p.next

        if not q:
            q = p.next
            return self.reverse(q)
        else:
            q.next = p.next
            return self.reverse(head)

    def reverse(self,head):
        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev