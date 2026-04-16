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


# one pass solution: use two pointer and a sliding window approach
# use a dummy node to cover edge cases such as "n = 1"
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy

        count = 0
        while(count < n):
            if fast.next:
                fast = fast.next
                count += 1
            else:
                break
        
        while(fast.next):
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        
        return dummy.next
            
