# brute force approach
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for first in range(len(prices)):
            newArr = prices[first + 1: len(prices)]
            for second in range(len(newArr)):
                if prices[first] < newArr[second]:
                    if (newArr[second] - prices[first]) > profit:
                        profit = newArr[second] - prices[first]

        return profit