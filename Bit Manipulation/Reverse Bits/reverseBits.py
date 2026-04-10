#two pointer approach
class Solution:
    def reverseBits(self, n: int) -> int:
        count = 0
        left = 1 << 31
        right = 1
        
        while(count < 16):
            rightBit = n & right
            leftBit = n & left

            n = n & ~(right)
            n = n | (leftBit >> 31-(2*count) ) # distance btwn L & R is (31-count) - (0+count)

            n = n & ~(left)
            n = n | (rightBit << 31-(2*count) )

            count += 1
            left = left >> 1
            right = right << 1

        return n


# creating a new integer approach
