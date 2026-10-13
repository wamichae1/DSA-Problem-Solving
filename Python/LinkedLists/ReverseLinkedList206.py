# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution: # Solution Iterative approach
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev = None
        current = head

        while current:
            newpointer = current.next
            current.next = prev

            prev = current
            current = newpointer
        
        return prev
        