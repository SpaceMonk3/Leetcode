# look at version 1 for cleaner code
class Solution:

    def encode(self, strs: List[str]) -> str:
        temp = []
        for s in strs:
            temp.append(str(len(s)) + "!" + s)

        return "".join(temp)
        
    def decode(self, s: str) -> List[str]:
        result = []
        lengthStr = []
        lengthInt = -1
        word = []
        for c in s:
            if c != "!" and lengthInt == -1:
                lengthStr.append(c)
            elif lengthInt == -1 and c == "!":
                lengthInt = int("".join(lengthStr))
                lengthStr = []
                if lengthInt == 0:
                    result.append("")
                    lengthInt = -1
            else:
                word.append(c)
                lengthInt -= 1
                if lengthInt == 0:
                    result.append("".join(word))
                    lengthInt = -1
                    word = []
        
        return result
    

# version 1 code
class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = []
        for s in strs:
            enc += str(len(s)) + "!" + s
        return "".join(enc)
    
    def decode(self, s: str) -> List[str]:
        dec = []
        length = []
        c = 0
        while c < len(s):
            if s[c] != '!':
                length.append(s[c])
                c += 1
            else:
                size = int("".join(length))
                dec.append(s[c+1 : c+1+size])
                c = c + 1 + size
                length = []
            
        return dec
    

'''
Best concise solution. 

Note: In Python, the index() method is used to find the first occurrence of a specified substring within a string.
Syntax:
stringName.index(substring, start, end)
'''
class Solution:
    def encode(self, strs: List[str]) -> str:
        result = []
        for s in strs:
            result.append(str(len(s)) + "!" + s)
        return "".join(result)
        
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            # find the delimiter
            j = s.index("!", i)
            
            # extract the length
            length = int(s[i:j])
            
            # extract the word and add to result
            word = s[j+1 : j+1+length]
            result.append(word)
            
            # move i to the start of the next encoded string
            i = j + 1 + length
        return result

        
