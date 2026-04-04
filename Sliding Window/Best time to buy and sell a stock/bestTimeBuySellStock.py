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


#optimal solution approach - sliding window approach
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buyIndex = 0
        sellIndex = -1

        for index in range(len(prices)):
            if prices[index] < prices[buyIndex]:
                buyIndex = index
            if prices[index] > prices[buyIndex]:
                    sellIndex = index
                    if profit < prices[sellIndex] - prices[buyIndex]:
                        profit = prices[sellIndex] - prices[buyIndex]

        return profit