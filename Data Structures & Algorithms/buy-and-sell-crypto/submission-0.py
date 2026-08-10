class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        for i1, p1 in enumerate(prices):
            for i2, p2 in enumerate(prices):
                if i1 < i2:
                    if maxP < (p2 - p1):
                        maxP = p2 - p1
        return maxP