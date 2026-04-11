#recursive approach - time exceeded on leetcode, not the right solution
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n < 0:
#             return 0
#         if n == 0:
#             return 1

#         res1 = self.climbStairs(n-1) 
#         res2 = self.climbStairs(n-2) 

#         return res1 + res2


# Dynamic Programming/ space optimized approach
# 0. draw the binary tree for this problem
# 1. identify overlapping/recurrent problems patterns in the binary tree
# 2. decide whether to use a bottom-up or top-down approach 
# 3. visualize the bottom-up approach in 1 dimension - usually array or single variables
# 4. create a storage/ cache to store the result of recurrent problems
class Solution:
    def climbStairs(self, n: int) -> int:
        left = 1
        right = 1
        n -= 2

        while(n > -1):
            temp = left
            left = left + right
            right = temp
            n -= 1

        return left



        