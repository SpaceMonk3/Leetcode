# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# In order traversal, recursive approach, with a shared variable in recursive memory
# In order traversal of a BST will give you the 'ordered sorted values' in a BST 
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        
        def helper(root: Optional[TreeNode]) -> int:
            if not root:
                return -1
            
            # left node 
            left = helper(root.left)
            if left != -1:
                return left
            
            # parent/root node + base case
            self.k -= 1
            if self.k == 0:
                return root.val
            
            # right node
            right = helper(root.right)
            if right != -1:
                return right
            
            return -1

        return helper(root)