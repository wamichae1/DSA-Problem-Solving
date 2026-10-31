# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:

        slow = head
        fast = head
        #find Middle of the list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        #flip the pointers for the second half
        while slow != None:
            newpointer = slow.next
            slow.next = prev

            prev = slow
            slow = newpointer
        
        #check from both ends to see if its pallindrome
        left = head
        right = prev
        while right != None:
            if left.val != right.val:
                return False
            
            left = left.next
            right = right.next
        return True
