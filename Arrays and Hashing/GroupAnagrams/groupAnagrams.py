'''
brute force:
- create a results hashamp dict of lists, and a store list to store dicts which contain patters of words (number of letters in each word)
- loop thru each word in strs and create a temp dict with key as letters and values as the number of times they appear
- check if temp dict exists in store list, if doesnt exist then append to list
- If exists make the index of the dict in the store list the key of results dict, and the values being the actual final list groupings of the word anagrams
- return only the group of lists at the end 

Big O - O(N * Klogk)
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = dict()
        store = []

        for s in strs:
            tempDict = dict()
            for c in s:
                if c not in tempDict:
                    tempDict[c] = 1
                else:
                    tempDict[c] += 1

            tempDict = sorted(tempDict.items())
            tempTuple = tuple(tempDict)
            
            index = 0
            if tempTuple in store:
                index = store.index(tempTuple)
            else:
                store.append(tempTuple)
                index = len(store) - 1

            if index in results:
                results[index].append(s)
            else:
                results[index] = [s]
        
        return list(results.values())


'''
Optimized solution:
- use an array "temp" (that acts like a hashmap) that stores characters a-z (in the form of indices) and each character frequency (array elements)
- create a results hashmap dict where key is a pattern of "temp" array and values are grouped anagrams
- loop thru the words lists and update character frequency of the word in temp
- after a word is mapped to temp, check for it in results (after being coverted to a tuple) and add the word into the grouped list 
- return final group of anagram lists 

Big O - O(M * N)
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = defaultdict(list)

        for s in strs:
            temp = [0] * 26 #array of 26 elements all initialized to 0s
            
            for c in s:
                temp[ord(c) - ord("a")] += 1
            
            # No need to check if using a default dict, but doing it just cus 
            if tuple(temp) not in results:
                results[tuple(temp)] = [s]
            else:
                results[tuple(temp)].append(s)

        return list(results.values())





         


        