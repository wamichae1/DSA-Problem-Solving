# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(0, head)
        current = dummy.next
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            current = current.next
        return dummy.next

        