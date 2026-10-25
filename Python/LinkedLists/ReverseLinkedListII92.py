# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        dummy = ListNode()
        dummy.next = head
        prev = None
        current = head
        NodeNum = 1
        while NodeNum != left:
            if NodeNum + 1 == left:
                prev = current
            NodeNum += 1
            current = current.next

        while NodeNum != right:
            newpointer = current.next
            current.next = prev

            prev = current
            current = newpointer
            NodeNum += 1
        
