#o(n) space 
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = {}
        pos = 0
        current = head
        while current:
            if current not in seen:
                seen[current] = pos
            else:
                return current
            current = current.next
            pos += 1
        return current
            

        