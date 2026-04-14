# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Two pass approach
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        last = 1
        while(curr.next):
            curr = curr.next
            last += 1
        
        start = last - (n - 1)
        curr = head
        while(start > 0):
            if start == 1:
                head = head.next
                break
            elif start == 2:
                curr.next = curr.next.next
                break
            else:
                curr = curr.next
                start -= 1

        return head