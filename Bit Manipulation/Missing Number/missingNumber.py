# xor approach - xor of 2 same numbers is 0
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numRange = 0
        arrRange = 0

        for i in range(1, len(nums)+1):
            numRange = numRange ^ i
        
        for num in nums:
            arrRange = arrRange ^ num

        return numRange ^ arrRange 
