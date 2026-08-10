class Solution:
    def maxArea(self, heights: List[int]) -> int:
        index1 = -1
        amounts = []
        for h1 in heights:
            index1 += 1
            index2 = -1
            for h2 in heights:
                index2 += 1
                amount = abs(index1-index2) * min(h1, h2)
                amounts.append(amount)
        return max(amounts)
                



