class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        temp = ListNode()
        current = temp
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                current.next = ListNode(list1.val)
                current = current.next
                list1 = list1.next
            else:
                current.next = ListNode(list2.val)
                current = current.next
                list2 = list2.next
        while list1 != None:
            current.next = ListNode(list1.val)
            current = current.next
            list1 = list1.next
        while list2 != None:
            current.next = ListNode(list2.val)
            current = current.next
            list2 = list2.next
            
        return temp.next