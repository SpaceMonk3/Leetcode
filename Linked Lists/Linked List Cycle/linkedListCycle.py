# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 2 pointer approach. the rabit and tortoise method, 1 pointer goes fast, the other goes slow - if they meetup at some point then cycle exists 
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slowPointer = head
        fastPointer = head

        while(fastPointer is not None):
            slowPointer = slowPointer.next

            if fastPointer.next is None or fastPointer.next.next is None:
                return False
            fastPointer = fastPointer.next.next

            if slowPointer == fastPointer:
                return True
        
        return False

#hashmap approach