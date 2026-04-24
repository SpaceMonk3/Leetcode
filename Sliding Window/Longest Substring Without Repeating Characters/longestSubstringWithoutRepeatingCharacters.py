'''
Approach: Sliding window with hashmap/dicts. 
1. loop thru string and add each new character (key) to hashmap with it's index (value)
2. Increment right pointer until a repeating letter is found in the hashmap
3. move the left pointer to the index next to the existing duplicate letter (duplicate letter index + 1)
4. calculate the length of substring thru right-left pointers each time every iteration and use max() to always store the max length 
'''

# O(n) time complexity
from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subString = defaultdict(int)
        l = 0
        longest = 0

        for r in range(0, len(s)):
            if s[r] in subString:
                l = max(subString[s[r]] + 1, l)
            
            subString[s[r]] = r
            longest = max(r - l + 1, longest)
        
        return longest
            



# Amortized O(n) solution but not clean code/ fully optimal:
# from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subString = defaultdict(int)
        l,r = 0, 0
        longest = 0

        while r < len(s):
            if s[r] not in subString:             
                subString[s[r]]  = r
                r += 1
            else:
                while l <= subString[s[r]]:
                    del subString[s[l]]
                    l += 1
                subString[s[r]] = r
                r += 1

            longest = max(r - l, longest)

        return longest
        

        

        
        

        