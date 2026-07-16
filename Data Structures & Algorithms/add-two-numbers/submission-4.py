# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        res = None
        result = None
        carry = 0
        while l1 and l2:
            if not res:
                res = ListNode((l1.val+l2.val+carry) % 10)
                result = res
            else:
                res.next = ListNode((l1.val+l2.val+carry) % 10)
                res = res.next
            carry = (l1.val+l2.val+carry) // 10
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            res.next = ListNode((l1.val + carry) % 10)
            carry = (l1.val + carry) // 10
            res = res.next
            l1 = l1.next
        
        while l2:
            res.next = ListNode((l2.val + carry) % 10)
            carry = (l2.val + carry) // 10
            res = res.next
            l2 = l2.next
        
        if carry:
            res.next = ListNode(carry)
            carry = carry // 10

        return result

            