'''
Brute Force: sort the array first using sort() - O(n log n), then traverse thru array and check if consecutive sequence exists and if so, find the longest one

Optimal O(n): 
1. convert input array to a set (which is implemented using a hashtable) to remove
duplicates and acheive O(1) lookup times 
2. loop thru the set and check if number is the start of a sequence by checking if 
'element - 1' doesn't exist in the set. (If it does that means it's not the start)
3. enter the count loop if the start of the sequence is found and keep traversing the set 
while 'element + 1' exists, while incrementing the length count variable.

'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longest = 0

        for num in numsSet:
            if not (num-1 in numsSet):
                count = 1
                i = num
                while (i+1) in numsSet: 
                    i += 1                   
                    count += 1
                
                longest = max(longest, count)
                               
        return longest 

                    




        