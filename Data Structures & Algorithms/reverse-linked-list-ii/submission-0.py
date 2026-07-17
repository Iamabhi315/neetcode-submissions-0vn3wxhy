# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if(not head or not head.next or left == right):
            return head
        
        dummy = ListNode(-1)
        dummy.next = head
        i = left
        p = dummy
        q = None
        while i:
            q = p
            p = p.next
            i -= 1
        prev = None
        tail = None
        for i in range(right - left + 1):
            if not prev:
                tail = p
            nxt = p.next
            p.next = prev
            prev = p
            p = nxt
        
        q.next = prev
        tail.next = p
        return dummy.next

        
        