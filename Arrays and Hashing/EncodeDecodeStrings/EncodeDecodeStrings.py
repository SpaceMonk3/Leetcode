'''
brute force:
- encode - loop thru each string and count length AND choose a character as an identifier and add both at the start of each string (length first then identifier)
- 4!neet4!code3!you2!we - example
- decode - loop thru string and get words based off the length and identifier & add them to a list and return

-Notes of why other approaches didn't work:
1) Just an identifier is not enough to encode/decode the string as there could be similar characters in the strings. Ex: ["name","na!e"] -> !name!na!e -> which would result in "na" instead of "na!e"
2) Length of string is not enough to encode/decode the string as there could be lengths w double digits. Ex: is the length in "10namesnames" 1 or 10? How would we know? We add an identifier AFTER the length to solve this.
3) Adding identifier before length (!4name) will not work as this brings us back to problem 2.

Big O: O(n) for both encode and decode as long as string aren't being concatenated. (They are immutable in python & Java)
'''
class Solution:

    def encode(self, strs: List[str]) -> str:
        # enc = ""
        # for s in strs:
        #     enc += str(len(s)) + "!" + s  
        #     print(enc) # testing
        # return enc
        '''Strings are immutable O(n^2) so we need to use a list to store the encoded strings for O(n)'''
        enc = []
        for s in strs:
            enc += str(len(s)) + "!" + s
        return "".join(enc)
    
    def decode(self, s: str) -> List[str]:
        dec = []
        length = []
        c = 0
        while c < len(s):
            # string = ""
            if s[c] != '!':
                '''Strings are immutable O(n^2) so we need to use a list to store the encoded strings for O(n)'''
                # length += s[c]
                # c += 1
                length.append(s[c])
                c += 1
            else:
                size = int("".join(length))
                '''Strings are immutable O(n^2) so using a direct .append approach for O(n)'''
                # c += 1
                # while(size != 0):
                #     string += s[c]    
                #     c += 1
                #     size -= 1
                
                dec.append(s[c+1 : c+1+size])
                c = c + 1 + size
                length = []
            
        return dec
    
'''Code needs to be written more concisely'''