'''
brute force: 
1. loop thru string list, sort each string element, 
2. check to see if its in a hashmap (if not, add the sorted string as key and the actual og string as value)
3. if sorted string exists, add the og string as it's value. 
4. once the looping of the array is done, return a list of all the values in the hashmap.
Big O - O(N * Klogk)



optimal approach:
1. instead of sorted keys use an array (converted to tuple) as the hashmap key
2. the array will be 26 in size (to represent a-z). each letter will map to an index in the array. (a -> index 0, c-> index 2, etc)
3. the arrays elements/ values will be how many times a letter appears in the string
4. this array wil then be converted to a tuple and added into the hashmap as key (since lists in python cannot be hashmap keys)
Big O - O(N * K) would've been O(N^2) but size of individual strs is K, so N*K
'''
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)

        for s in strs:
            temp = [0] * 26
            for i in range(0, len(s)):
                temp[ord(s[i]) - ord('a')] += 1
            
            map[tuple(temp)].append(s)
        
        return list(map.values())