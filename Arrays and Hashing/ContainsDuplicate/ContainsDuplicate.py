class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #brute force
        #loop thru the entire array n times where n is the length of array
        #for each element check if repeats itself
        #Big O would be O(n^2) cause of 2 loops - one for outer loop, 
        #one for inner loop where each element is checked. Space would be O(n)?

        #hashmap approach
        #loop thru the array adding each element into a hashmap 
        #simultaneously check hashmap for existing letters 
        #if an element/ number exists in hashmap -> return true 
        #else return false
        #Big O would be O(n)? space is O(n^2)?

        hmap = dict()
        
        for i in range(len(nums)):
            if nums[i] in hmap:
                return True
            else:
                hmap[nums[i]] = 1
        
        return False

        #need to check other approaches such as sorting, hashset (python set), and their time and space complexity