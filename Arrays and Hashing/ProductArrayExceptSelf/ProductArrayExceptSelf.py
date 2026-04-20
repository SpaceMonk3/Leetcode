# Prefix Sums Concept Used - IMPORTANT CONCEPT TO REVIEW
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        
        # left pass: result[i] stores the product of all elements to the left of i
        # result[0] stays 1 since there are no elements to the left of index 0
        for i in range(1, len(nums)):
            result[i] = nums[i-1] * result[i-1]
        
        # right pass: multiply each result[i] by the product of all elements to the right of i
        # start rightProduct at the last element since there are no elements to the right of it
        rightProduct = nums[len(nums)-1]
        for i in range(len(nums)-2, -1, -1):
            result[i] = result[i] * rightProduct
            rightProduct = nums[i] * rightProduct
        
        return result