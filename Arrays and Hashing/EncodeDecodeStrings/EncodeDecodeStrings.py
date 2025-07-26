'''
brute force:
- encode -loop thru & choose a non ascii/ utf-8 character as an identifier and add it at the end of each string
- !4neet!4code!3you!2we
- 4neet44ode
- decode -loop thru & remove strings before the non ascii character identifier and add them all to a single string and return
- 

'''
class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = ""
        for s in strs:
            enc += str(len(s)) + "!" + s  
            print(enc) # testing
        
        return enc
    
    def decode(self, s: str) -> List[str]:
        dec = []
        length = ""
        c = 0
        while c < len(s):
            string = ""
            if s[c] != '!':
                length += s[c]
                c += 1
            else:
                size = int(length)
                c += 1
                while(size != 0):
                    string += s[c]    
                    c += 1
                    size -= 1
                
                length = ""
                dec.append(string)
            
        return dec