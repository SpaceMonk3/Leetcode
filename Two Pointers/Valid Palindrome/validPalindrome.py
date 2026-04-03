class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) <= 1:
            return True

        lowerStr = s.lower()
        
        start = 0
        end = len(lowerStr) - 1        
        while start < end:
            while(lowerStr[start].isalnum() is False and start < end):
                start += 1
            
            while(lowerStr[end].isalnum() is False and start < end):
                end -= 1
            
            print("start: " + lowerStr[start] + ", end: " + lowerStr[end])

            if lowerStr[start] is not lowerStr[end]:
                return False
            else:
                start += 1
                end -= 1
        
        return True