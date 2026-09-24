# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        placeholder = ListNode()
        current = placeholder
        while l1 != None or l2 != None:
            if l1:
                x = l1.val
            else:
                x = 0
            if l2:
                y = l2.val
            else:
                y = 0
            lsum = x + y + carry
            digit = (lsum) % 10
            carry = (lsum) // 10

            current.next = ListNode(digit)
            current = current.next
            if l1:
                l1 = l1.next
            else:
                l1 = None
            if l2:
                l2 = l2.next
            else:
                l2 = None
        if carry:
            current.next = ListNode(carry)
        return placeholder.next