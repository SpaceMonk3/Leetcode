'''
Approach: Greedy

KEY IDEA: work backwards from the last index, updating the goal index
whenever we find a position that can reach it.

1. set goalIndex to the last index (the target we want to reach)
2. iterate backwards through the array
3. at each index, check if we can reach the current goalIndex from here:
       nums[i] >= (goalIndex - i) 
       i.e. the jump length at i is >= the distance to the goal
4. if we can reach it, update goalIndex to i (this position becomes the new goal)
5. if goalIndex reaches 0 by the end, we can reach the end from the start

Time Complexity: O(N) — single pass backwards through the array
Space Complexity: O(1) — only a single goalIndex variable used
'''
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goalIndex = len(nums) - 1
        for i in range(len(nums)-1, -1, -1):
            if nums[i] >= (goalIndex-i):
                goalIndex = i
        
        return goalIndex is 0
            

# Explore all other options on how to solve this problem