'''
Approach: Greedy (Kadane's Algorithm)

KEY IDEA: at each index, decide whether to extend the current subarray
or start a new one from scratch:
      if adding nums[i] to the current subarray is worse than just 
      starting fresh at nums[i], start fresh.

1. initialize currMax and maxRes to nums[0] to handle all-negative arrays
2. iterate through the array starting from index 1
3. at each index, extend the current subarray or start fresh:
       currMax = max(currMax + nums[i], nums[i])
       i.e. if currMax is negative, it only drags us down — start fresh
4. update maxRes if currMax is the largest subarray sum seen so far
5. return maxRes at the end

Time Complexity: O(N) — single pass through the array
Space Complexity: O(1) — only currMax and maxRes variables used
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currMax = nums[0]
        maxRes = nums[0]

        for i in range(1, len(nums)):
            currMax = currMax + nums[i]
            currMax = max(currMax, nums[i])
            maxRes = max(currMax, maxRes)
        
        return maxRes
    

# Explore all other options on how to solve this problem