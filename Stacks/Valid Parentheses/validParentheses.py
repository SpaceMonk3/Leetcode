from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        tempStack = deque()

        for char in s:
            if char in '([{':
                tempStack.append(char)
            elif char == ')': 
                if not tempStack or tempStack[-1] != '(':
                    return False
                tempStack.pop()
            elif char == ']':  
                if not tempStack or tempStack[-1] != '[':
                    return False
                tempStack.pop()
            elif char == '}': 
                if not tempStack or tempStack[-1] != '{':
                    return False
                tempStack.pop()
    
        if not tempStack:
            return True
        else:
            return False