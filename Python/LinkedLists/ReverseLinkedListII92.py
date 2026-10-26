# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        dummy = ListNode(0, head)

        left_prev = dummy
        current = head
        for i in range(left - 1):
            left_prev = current
            current = current.next

        prev = None

        for i in range(right - left + 1):
            newpointer = current.next
            current.next = prev
            prev = current
            current = newpointer

        left_prev.next.next = current # point 2 (from 1) to 5
        left_prev.next = prev # point 1 to 4

        return dummy.next
