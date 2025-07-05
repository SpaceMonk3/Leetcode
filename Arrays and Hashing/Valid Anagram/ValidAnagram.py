"""
Brute force: 
- loop thru the string comparing each letter in t with s. 
- once a letter is found in both arrays, go to the next letter to compare. 
- keep track of letter count using a counter variable
- if a repeating letter is noticed in t then go into a loop of s to see if equal   
- if, for repeating letters, the count in both string are not equal, then return False
- if a letter is not found in either string then return False
- return True after loop ends

hashmap approach
- edge case: if length is not equal then immediate return false
- loop thru s and add it into a hashmap while adding a counter as value and letter as key
- loop thru t and check if letter is in hashmap
- if letter not in hashmap then return false
- if in hashmap then subtract count value 
- if count value of a letter in hashmap is 0, then delete the letter key-value pair
- at the end if hashmap size is 0 then return true, else false

    O(n) time complexity
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hmap = dict()
        for i in s:
            if i in hmap:
                hmap[i] += 1
            else:
                hmap[i] = 1
        
        for x in t:
            if x not in hmap:
                return False
            hmap[x] -= 1

            if hmap[x] == 0:
                del hmap[x]
        
        if len(hmap) != 0:
            return False
        
        return True
        
# try problem with ascii approach, Counter approach, one loop approach 
# (add both strings into 2 hashmap separately in one loop and then simply compare with ==), and any others