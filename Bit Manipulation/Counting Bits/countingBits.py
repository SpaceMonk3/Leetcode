class Solution:
    def countBits(self, n: int) -> List[int]:
        def countOnes(i) -> int:
            count = 0

            while(i > 0):
                count += (i & 1)
                i = i >> 1
            return count
        
        res = [0] * (n+1)

        for i in range(0, n+1):
            res[i] = countOnes(i)

        return res