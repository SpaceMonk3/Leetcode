# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# iterative approach
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return list1
        elif not list1:
            return list2
        elif not list2:
            return list1

        curr1 = list1
        curr2 = list2
        if curr1.val <= curr2.val:
            sorted = curr1
            resultHead = sorted
            curr1 = curr1.next
        else:
            sorted = curr2
            resultHead = sorted
            curr2 = curr2.next

        while(curr1 is not None and curr2 is not None):
            if curr1.val <= curr2.val:
                sorted.next = curr1
                sorted = sorted.next
                curr1 = curr1.next
            else:
                sorted.next = curr2
                sorted = sorted.next
                curr2 = curr2.next

        if curr1 is None:
            sorted.next = curr2
        elif curr2 is None:
            sorted.next = curr1

        return resultHead
    

#recursive approach