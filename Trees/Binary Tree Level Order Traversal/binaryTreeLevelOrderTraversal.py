# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# breadth first search using a queue/ deque in python, while keeping track of each level
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        bfsQueue = deque([root])
        result = []

        while(bfsQueue):
            temp = []
            size = len(bfsQueue)

            while(size > 0 ):
                node = bfsQueue.popleft()
                if node.left:
                    bfsQueue.append(node.left)
                if node.right:
                    bfsQueue.append(node.right)
                
                size -= 1
                temp.append(node.val)

            result.append(temp)
        
        return result


# dfs approach