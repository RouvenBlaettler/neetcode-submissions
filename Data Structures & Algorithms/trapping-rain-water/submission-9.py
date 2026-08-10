class Solution:
    def trap(self, height: List[int]) -> int:
        def check_l(i):
            return max(height[:i + 1])

        def check_r(i):
            return max(height[i:])

        res = 0

        for i, h in enumerate(height):
            w_capacity = min(check_l(i),check_r(i)) - h
            if w_capacity > 0:
                res += w_capacity

        return res


        