class Solution:
    import math
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r

        while l <= r:
            amount = 0
            m = (l+r)//2
            for p in piles:
                amount += math.ceil(p/m)
            if amount <= h:
                res = min(res, m)
                r = m-1
            else:
                l = m + 1
        return res




