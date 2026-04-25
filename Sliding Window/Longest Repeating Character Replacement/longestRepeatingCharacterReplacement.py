'''
Optimal: O(N) time complexity. Sliding Window + Hashmap approach
KEY IDEA: find what makes a sliding window invalid in the problem: 
    ----- valid if: window size - most frequent character count <= k ------
APPROACH:    
1. loop thru the string with the right pointer, while counting the character frequencies in a hashmap
2. have a maxFreq variable to keep track of the most frequent character count in the string
3. if sliding window is not valid with the condition mentioned above, decrement the character freq at left pointer in the hashmap by -1. 
4. Then move left pointer by +1
5. Have a window length variable which keeps track of the longest window size and returns it at the end.  
'''
from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        maxFreq = 0
        windowSize = 0
        freq = defaultdict(int)

        for r in range(len(s)):
            freq[s[r]] += 1
            maxFreq = max(maxFreq, freq[s[r]])
            if (r-l+1) - maxFreq > k:
                freq[s[l]] -= 1
                l += 1
            windowSize = max(windowSize, r-l+1)

        return windowSize
