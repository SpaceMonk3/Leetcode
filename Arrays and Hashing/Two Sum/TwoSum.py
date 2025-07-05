'''
brute force approach:
- loop thru array and subtract each element with target
- then loop thru the list again to find the result of the subtraction
- if value doesn't exist then handle return accordingly (not needed for leetcode problem due to existing contraints)
- return list of both elements indices if match found
Big O - O(n^2) due to 2 loops

hashmap approach:
- loop thru array and subtract each element with target 
- check if result is in the hashmap - if so then return indices
- else add element in hashmap (if it doesn't exist) along with it's index
- return default list if loop ends without finding a numbeer pair 
Big O - O(n)
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair = []
        hmap = dict()

        for i in range(len(nums)):
            if (target - nums[i]) in hmap:
                pair = [hmap[target - nums[i]], i]
                break
            if nums[i] not in hmap:
                hmap[nums[i]] = i

        return pair

        