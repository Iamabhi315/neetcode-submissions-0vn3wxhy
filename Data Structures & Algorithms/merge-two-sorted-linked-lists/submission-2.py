# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        head = None
        tail = None

        head1 = list1
        head2 = list2

        while head1 and head2:

            if head1.val <= head2.val:
                temp = ListNode(head1.val)
                head1 = head1.next
            else:
                temp = ListNode(head2.val)
                head2 = head2.next

            if head is None:
                head = temp
                tail = temp
            else:
                tail.next = temp
                tail = tail.next

        while head1:
            temp = ListNode(head1.val)

            if head is None:
                head = temp
                tail = temp
            else:
                tail.next = temp
                tail = tail.next

            head1 = head1.next

        while head2:
            temp = ListNode(head2.val)

            if head is None:
                head = temp
                tail = temp
            else:
                tail.next = temp
                tail = tail.next

            head2 = head2.next

        return head