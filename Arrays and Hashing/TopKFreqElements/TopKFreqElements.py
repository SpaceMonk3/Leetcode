'''
brute force:
- loop thru the list/array and use a hashmap to count frequencies
- once out of loop, sort the hashmap's frequency values.
- loop thru sorted list and return the first k elements 

Big O - O(N log n + K) -> O(N log n) 
_________________________________________________________________________
Optimized solution:
- use a priority queue/ heap and a hashmap?
- loop thru the list/array and add frequencies into a heap/priority queue directly
- loop thru the list/array and build a frequency hashmap 
- then build the heap from the hashmap entries
- pop the top k elements and return them 

Big O - O(n + k log n) -> not really super optimal
__________________________________________________________________________
Bucket Sort approach:
- use a hashmap to count the frequencies initially
- use an temp array to map the frequencies from hashmap to the temp array indices
- since there are no bounds array "nums" cannot use indices as the numbers & array contents/elements as frequencies. 
- Instead use indices as frequencies, and the elements as the numbers, make each index element a list to accommodate for the numbers that have the same frequencies.
- after looping thru all numbers, loop thru the temp array from the end to beginning until we get the k most frequent elements.

Big O - O(n)
'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict()
        freq_buckets = [[] for _ in range(len(nums) + 1)] # loop to populate the list with empty [] x amount of times. _ is a throw away loop variable; basically an "i".
        
        for i in nums:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1
            # count[i] += 1 + count.get(i, 0) - simpler way
        
        for keyNum, valueFreq in count.items():
            freq_buckets[valueFreq].append(keyNum)

        results = []
        for i in range(len(freq_buckets)-1, 0, -1):
            if len(freq_buckets[i]) != 0:
                for n in freq_buckets[i]:
                    results.append(n)
                    if len(results) == k:
                        return results
        

# hashmap & sorting approach from 4/12/2026. O(n log(n)) time complexity
from collections import defaultdict 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for i in nums:
            freq[i] += 1
        
        #sorting dict in descending order by the 'values'
        temp = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))

        #converting to list for easy traversal
        res = list(temp.keys())
        result = []
        for i in range(0, k):
            result.append(res[i])

        return result



# bucket sort approach from 4/12/2026. O(n) time complexity
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for i in nums:
            freq[i] += 1
        
        temp = [[] for _ in range(len(nums)+1)]
        for key, value in freq.items():
            temp[value].append(key)
        
        res = []
        for r in range(len(temp)-1, -1, -1):
            for c in range(0, len(temp[r])):
                if len(res) < k:
                    res.append(temp[r][c])
                else: 
                    return res

        return res


        



        