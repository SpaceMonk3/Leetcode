# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: 
            return True
        if not root:
            return False
        
        if self.isSame(root, subRoot):
            return True
        resultLeft = self.isSubtree(root.left, subRoot)
        resultRight = self.isSubtree(root.right, subRoot)

        return resultLeft or resultRight
            
    def isSame(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p and q:
            return False
        elif p and not q:
            return False
        elif p.val != q.val:
            return False

        left = self.isSame(p.left, q.left)
        right = self.isSame(p.right, q.right)

        return left and right

        