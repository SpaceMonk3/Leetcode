# bit wise operations approach:
# 1. use xor & and operators (^, &)
# 2. do the partial sum using xor operator
# 3. calculate the carries using and operator
# 4. combine them both until the carries is equal to 0
class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF

        if b == 0:
            # If the 31st bit is set, it means the number is negative in 2's complement
            if a > 0x7FFFFFFF:
                return ~(a ^ mask) 
            else:
                return a

        partial = (a ^ b) & mask
        carry = ((a & b) << 1) & mask
        a = partial
        b = carry
        
        return self.getSum(a, b)